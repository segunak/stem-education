const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');

const page = 'ai-resources/index.html';
const jobUrl = 'https://apply.careers.microsoft.com/careers/job/';

function parseList(html) {
    const lists = [...html.matchAll(/<ul class="internship-link-list">([\s\S]*?)<\/ul>/g)];
    assert.equal(lists.length, 1, 'Expected exactly one internship list');
    const itemPattern = /<li>\s*<a href="([^"<>\s]+)">([^<>]+)<\/a>\s*<\/li>/g;
    const items = [...lists[0][1].matchAll(itemPattern)].map(match => ({
        markup: match[0], href: match[1], title: match[2]
    }));
    assert.equal(lists[0][1].replace(itemPattern, '').trim(), '', 'Unexpected markup in internship list');
    return { surrounding: html.replace(lists[0][0], ''), items };
}

function validate(before, after, internships, links) {
    const oldList = parseList(before);
    const newList = parseList(after);
    assert.equal(newList.surrounding, oldList.surrounding, 'Changes outside the internship list');
    assert.ok(Array.isArray(internships) && internships.length > 0, 'Missing open internship data');
    const open = new Map();
    for (const job of internships) {
        assert.match(job.id, /^\d{12,}$/, 'Invalid job id');
        assert.equal(job.url, jobUrl + job.id, 'Unexpected job URL');
        assert.ok(typeof job.name === 'string' && job.name.trim(), 'Missing original job name');
        assert.ok(!open.has(job.id), 'Duplicate source job id');
        open.set(job.id, job);
    }
    const resolved = new Map();
    for (const line of links.trim().split(/\r?\n/).filter(Boolean)) {
        const fields = line.split('\t');
        assert.equal(fields.length, 2, 'Malformed resolved-link data');
        assert.match(fields[1], /^(unknown|\d{12,})$/, 'Invalid resolved job id');
        assert.ok(!resolved.has(fields[0]) || resolved.get(fields[0]) === fields[1], 'Conflicting resolved job ids');
        resolved.set(fields[0], fields[1]);
    }
    assert.equal(resolved.size, new Set(oldList.items.map(item => item.href)).size, 'Incomplete resolved-link data');
    const seen = new Set();
    const retained = [];
    const removed = [];
    for (const item of oldList.items) {
        assert.ok(resolved.has(item.href), 'Unresolved source href is missing');
        const id = resolved.get(item.href);
        if (id === 'unknown' || (open.has(id) && !seen.has(id))) {
            retained.push(item);
            if (id !== 'unknown') seen.add(id);
        } else {
            removed.push({ id, title: item.title });
        }
    }
    assert.deepEqual(
        newList.items.slice(0, retained.length), retained,
        'Existing open or unknown entries must retain their markup and order'
    );
    const added = newList.items.slice(retained.length).map(item => {
        assert.ok(item.href.startsWith(jobUrl), 'New links must use the Microsoft job URL');
        const id = item.href.slice(jobUrl.length);
        assert.ok(open.has(id) && !seen.has(id), 'Unexpected or duplicate added job');
        assert.match(item.title, /\S Internship$/, 'New titles must end with Internship');
        assert.doesNotMatch(item.title, /&(?!amp;)|[\r\n]/, 'Invalid title escaping or line break');
        seen.add(id);
        return { id, name: open.get(id).name, title: item.title };
    });
    assert.equal(seen.size, open.size, 'Open internships are missing');
    return { added, removed };
}

function prepareReview(inputs, detection) {
    const read = name => fs.readFileSync(path.join(inputs, name), 'utf8');
    const patches = fs.readdirSync(detection).filter(name => /^aw(?:-.*)?\.patch$/.test(name));
    assert.equal(patches.length, 1, 'Expected one reviewable patch');
    const patch = path.join(detection, patches[0]);
    const git = (...args) => execFileSync('git', args, { encoding: 'utf8' });
    assert.match(git('apply', '--numstat', '-z', patch), /^\d+\t\d+\tai-resources\/index\.html\0$/, 'Patch must modify only the allowed file');
    const before = git('show', `HEAD:${page}`);
    git('update-index', '--refresh');
    git('apply', '--index', '--whitespace=error-all', patch);
    assert.equal(git('diff', '--cached', '--name-status').trim(), `M\t${page}`, 'Only a regular file modification is allowed');
    assert.equal(git('diff', '--cached', '--summary'), '', 'File modes must not change');
    const result = validate(
        before, fs.readFileSync(path.join('ai-resources', 'index.html'), 'utf8'),
        JSON.parse(read('open-internships.json')), read('current-links.tsv')
    );
    const review = { base: git('rev-parse', 'HEAD').trim(), tree: git('write-tree').trim(), ...result };
    fs.writeFileSync(path.join(detection, 'internship-review.json'), JSON.stringify(review, null, 2));
    console.log(`Validated ${result.added.length} additions and ${result.removed.length} removals.`);
}

async function finalize(github, context, number, review) {
    assert.ok(Number.isSafeInteger(number) && number > 0, 'Missing created PR number');
    assert.equal(review.base, context.sha, 'Review is from another workflow revision');
    const repo = context.repo;
    const { data: pr } = await github.rest.pulls.get({ ...repo, pull_number: number });
    assert.equal(pr.user.login, 'github-actions[bot]', 'Unexpected PR author');
    assert.equal(pr.head.repo.full_name, `${repo.owner}/${repo.repo}`, 'Unexpected source repository');
    assert.equal(pr.base.ref, 'master', 'Unexpected target branch');
    assert.ok(pr.head.ref.startsWith('internships/'), 'Unexpected source branch');
    assert.equal(pr.draft, false, 'Draft PRs must not merge');
    const { data: commit } = await github.rest.git.getCommit({ ...repo, commit_sha: pr.head.sha });
    assert.equal(commit.tree.sha, review.tree, 'PR contents differ from the reviewed tree');
    if (!pr.merged) {
        assert.equal(pr.state, 'open', 'PR is no longer open');
        assert.equal(pr.base.sha, review.base, 'Target branch advanced; rerun against current master');
        const { data: merge } = await github.rest.pulls.merge({
            ...repo, pull_number: number, sha: pr.head.sha, merge_method: 'squash'
        });
        assert.equal(merge.merged, true, `Merge refused: ${merge.message}`);
    }
    const ref = { ...repo, ref: `heads/${pr.head.ref}` };
    const readBranch = async () => {
        try {
            return (await github.rest.git.getRef(ref)).data;
        } catch (error) {
            if (error.status !== 404) throw error;
            console.log('PR branch is already deleted.');
            return null;
        }
    };
    const branch = await readBranch();
    if (branch && branch.object.sha !== pr.head.sha) {
        console.warn('Retaining the PR branch because it advanced after review.');
    } else if (branch) {
        try {
            await github.rest.git.deleteRef(ref);
            console.log(`Deleted merged PR branch ${pr.head.ref}.`);
        } catch (error) {
            // Native cleanup can delete the branch between our lookup and deletion.
            if (![404, 422].includes(error.status) || await readBranch()) throw error;
        }
    }
    await github.rest.actions.createWorkflowDispatch({ ...repo, workflow_id: 'pages.yml', ref: 'master' });
    await github.rest.issues.createComment({
        ...repo, issue_number: number,
        body: `@segunak The internship update passed strict validation and independent AI review and has been merged.\n\n` +
            `Added ${review.added.length} internship(s); removed ${review.removed.length} stale or duplicate entry/entries. ` +
            `See this PR's description and diff for details. Pages deployment has been requested.\n\n` +
            `[Workflow run](${context.serverUrl}/${repo.owner}/${repo.repo}/actions/runs/${context.runId})`
    });
}

module.exports = { validate, finalize };
if (require.main === module) prepareReview(process.argv[2], process.argv[3]);
