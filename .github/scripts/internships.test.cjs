const assert = require('node:assert/strict');
const { test } = require('node:test');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { execFileSync } = require('node:child_process');
const { validate, finalize } = require('./internships.cjs');

const url = id => `https://apply.careers.microsoft.com/careers/job/${id}`;
const item = (href, title = 'Software Engineer Internship') => `<li>\n    <a href="${href}">${title}</a>\n</li>`;
const page = items => `<header>Unchanged</header><ul class="internship-link-list">\n${items.join('\n')}\n</ul><footer>Unchanged</footer>`;
const first = '1970393557000001';
const stale = '1970393557000002';
const added = '1970393557000003';
const keep = item('https://aka.ms/existing');
const unknown = item('https://aka.ms/unresolved');
const before = page([keep, item(url(stale)), unknown]);
const after = page([keep, unknown, item(url(added))]);
const jobs = [first, added].map(id => ({ id, name: 'Software Engineer Intern', url: url(id) }));
const links = `https://aka.ms/existing\t${first}\n${url(stale)}\t${stale}\nhttps://aka.ms/unresolved\tunknown\n`;

test('accepts exact additions/removals and preserves open and unknown links', () => {
    const result = validate(before, after, jobs, links);
    assert.deepEqual(result.added.map(job => job.id), [added]);
    assert.deepEqual(result.removed.map(job => job.id), [stale]);
});

for (const [name, href] of [['aliased', url(first)], ['identical', 'https://aka.ms/existing']]) {
    test(`keeps the first existing link when ${name} job links are duplicated`, () => {
        const result = validate(page([keep, item(href)]), page([keep]), jobs.slice(0, 1),
            `https://aka.ms/existing\t${first}\n${href}\t${first}\n`);
        assert.equal(result.removed.length, 1);
    });
}

test('can populate an initially empty list', () => {
    assert.equal(validate(page([]), page([item(url(first))]), jobs.slice(0, 1), '').added.length, 1);
});

for (const [name, invalid] of [
    ['outside-list changes', after.replace('<header>Unchanged', '<header>Changed')],
    ['scripts', after.replace('</ul>', '<script>alert(1)</script></ul>')],
    ['extra attributes', after.replace('<a href=', '<a onclick="alert(1)" href=')],
    ['missing jobs', page([keep, unknown])],
    ['duplicate jobs', page([keep, unknown, item(url(added)), item(url(added))])],
    ['retained stale jobs', page([keep, item(url(stale)), unknown, item(url(added))])],
    ['changed existing links', page([item(url(first)), unknown, item(url(added))])],
    ['dropped unknown links', page([keep, item(url(added))])],
    ['unapproved destinations', page([keep, unknown, item('https://example.com/job')])],
    ['unescaped ampersands', page([keep, unknown, item(url(added), 'Data & Analytics Internship')])]
]) {
    test(`rejects ${name}`, () => assert.throws(() => validate(before, invalid, jobs, links)));
}

test('rejects missing or malformed source data', () => {
    assert.throws(() => validate(before, after, [], links));
    assert.throws(() => validate(before, after, jobs, links.replace('\tunknown', '')));
    assert.throws(() => validate(before, after, jobs, links + `https://aka.ms/existing\t${stale}\n`), /Conflicting/);
});

function fixture() {
    const calls = [];
    const review = { base: 'base-sha', tree: 'reviewed-tree', added: [{}], removed: [{}] };
    const context = { repo: { owner: 'segunak', repo: 'stem-education' }, sha: review.base, serverUrl: 'https://github.com', runId: 123 };
    const pr = {
        user: { login: 'github-actions[bot]' }, draft: false, state: 'open', merged: false,
        head: { sha: 'reviewed-head', ref: 'internships/update-123', repo: { full_name: 'segunak/stem-education' } },
        base: { ref: 'master', sha: review.base }
    };
    const commit = { tree: { sha: review.tree } };
    const github = { rest: {
        pulls: {
            get: async () => ({ data: pr }),
            merge: async args => { calls.push(['merge', args]); return { data: { merged: true } }; }
        },
        git: { getCommit: async () => ({ data: commit }) },
        actions: { createWorkflowDispatch: async args => calls.push(['deploy', args]) },
        issues: { createComment: async args => calls.push(['notify', args]) }
    } };
    return { github, context, review, pr, commit, calls };
}

test('merges only the reviewed head, then requests deployment and notifies', async () => {
    const f = fixture();
    await finalize(f.github, f.context, 5, f.review);
    assert.deepEqual(f.calls.map(call => call[0]), ['merge', 'deploy', 'notify']);
    assert.equal(f.calls[0][1].sha, f.pr.head.sha);
    assert.equal(f.calls[0][1].merge_method, 'squash');
    assert.equal(f.calls[1][1].workflow_id, 'pages.yml');
    assert.match(f.calls[2][1].body, /@segunak/);
});

for (const [name, mutate] of [
    ['different PR contents', f => { f.commit.tree.sha = 'unreviewed-tree'; }],
    ['advanced base branch', f => { f.pr.base.sha = 'new-base'; }],
    ['different review revision', f => { f.review.base = 'old-base'; }],
    ['foreign source repository', f => { f.pr.head.repo.full_name = 'someone/fork'; }],
    ['unexpected PR author', f => { f.pr.user.login = 'someone'; }],
    ['unexpected source branch', f => { f.pr.head.ref = 'unrelated'; }],
    ['different target branch', f => { f.pr.base.ref = 'other'; }],
    ['draft PR', f => { f.pr.draft = true; }]
]) {
    test(`refuses to publish ${name}`, async () => {
        const f = fixture();
        mutate(f);
        await assert.rejects(finalize(f.github, f.context, 5, f.review));
        assert.deepEqual(f.calls, []);
    });
}

test('does not deploy or notify when GitHub refuses the merge', async () => {
    const f = fixture();
    f.github.rest.pulls.merge = async () => ({ data: { merged: false, message: 'Required checks pending' } });
    await assert.rejects(finalize(f.github, f.context, 5, f.review), /Merge refused/);
    assert.deepEqual(f.calls, []);
});

test('can retry deployment after an already completed merge', async () => {
    const f = fixture();
    f.pr.merged = true;
    f.pr.state = 'closed';
    f.pr.base.sha = 'merge-sha';
    await finalize(f.github, f.context, 5, f.review);
    assert.deepEqual(f.calls.map(call => call[0]), ['deploy', 'notify']);
});

function patchFixture(t) {
    const directory = fs.mkdtempSync(path.join(os.tmpdir(), 'internship-gate-test-'));
    t.after(() => fs.rmSync(directory, { recursive: true, force: true }));
    const repo = path.join(directory, 'repo');
    const inputs = path.join(directory, 'inputs');
    const detection = path.join(directory, 'detection');
    for (const folder of [path.join(repo, 'ai-resources'), inputs, detection]) fs.mkdirSync(folder, { recursive: true });
    const git = (...args) => execFileSync('git', args, { cwd: repo, encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] });
    const target = path.join(repo, 'ai-resources', 'index.html');
    fs.writeFileSync(target, before);
    fs.writeFileSync(path.join(repo, 'unchanged.txt'), 'Unchanged\n');
    git('init');
    git('config', 'core.autocrlf', 'false');
    git('add', '.');
    git('-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '--no-gpg-sign',
        '-m', 'Test fixture\n\nCo-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>');
    fs.writeFileSync(target, after);
    fs.writeFileSync(path.join(detection, 'aw-test.patch'), git('diff'));
    fs.writeFileSync(target, before);
    fs.writeFileSync(path.join(inputs, 'open-internships.json'), JSON.stringify(jobs));
    fs.writeFileSync(path.join(inputs, 'current-links.tsv'), links);
    const run = () => execFileSync(process.execPath, [path.join(__dirname, 'internships.cjs'), inputs, detection],
        { cwd: repo, encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] });
    return { repo, inputs, detection, git, target, run };
}

test('validates a real patch and records the exact approved Git tree', t => {
    const f = patchFixture(t);
    assert.match(f.run(), /Validated 1 additions and 1 removals/);
    const review = JSON.parse(fs.readFileSync(path.join(f.detection, 'internship-review.json'), 'utf8'));
    assert.equal(review.tree, f.git('write-tree').trim());
    assert.equal(review.base, f.git('rev-parse', 'HEAD').trim());
    assert.equal(fs.readFileSync(f.target, 'utf8'), after);
});

test('blocks patches touching another file before publication', t => {
    const f = patchFixture(t);
    fs.writeFileSync(path.join(f.repo, 'unchanged.txt'), 'Changed\n');
    const patch = path.join(f.detection, 'aw-test.patch');
    fs.appendFileSync(patch, f.git('diff'));
    fs.writeFileSync(path.join(f.repo, 'unchanged.txt'), 'Unchanged\n');
    assert.throws(f.run, /Patch must modify only the allowed file/);
    assert.equal(fs.existsSync(path.join(f.detection, 'internship-review.json')), false);
});

test('blocks a PR with a missing patch', t => {
    const f = patchFixture(t);
    fs.unlinkSync(path.join(f.detection, 'aw-test.patch'));
    assert.throws(f.run, /Expected one reviewable patch/);
});

test('rejects file-mode changes', t => {
    const f = patchFixture(t);
    f.git('update-index', '--chmod=+x', 'ai-resources/index.html');
    fs.writeFileSync(path.join(f.detection, 'aw-test.patch'), f.git('diff', '--cached'));
    f.git('update-index', '--chmod=-x', 'ai-resources/index.html');
    assert.throws(f.run, /File modes must not change/);
});

test('accepts the mailbox patch format used by the workflow', t => {
    const f = patchFixture(t);
    fs.writeFileSync(f.target, after);
    f.git('add', 'ai-resources/index.html');
    const tree = f.git('write-tree').trim();
    const commit = f.git('-c', 'user.name=Test', '-c', 'user.email=test@example.invalid',
        'commit-tree', tree, '-p', 'HEAD', '-m',
        'Candidate\n\nCo-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>').trim();
    fs.writeFileSync(path.join(f.detection, 'aw-test.patch'), f.git('format-patch', '-1', '--stdout', commit));
    f.git('read-tree', 'HEAD');
    fs.writeFileSync(f.target, before);
    assert.match(f.run(), /Validated 1 additions and 1 removals/);
});

test('compiled workflow gates publication on successful independent review', () => {
    const lock = fs.readFileSync(path.join(__dirname, '..', 'workflows', 'update-internships.lock.yml'), 'utf8');
    const job = name => lock.match(new RegExp(`^  ${name}:\\n([\\s\\S]*?)(?=^  [a-z_]+:|$(?![\\s\\S]))`, 'm'))[1];
    const configs = [...lock.matchAll(/^\s+GH_AW_SAFE_OUTPUTS_(?:HANDLER_)?CONFIG: (.+)$/gm)];
    assert.equal(configs.length, 2);
    for (const [, encoded] of configs) {
        const config = JSON.parse(JSON.parse(encoded)).create_pull_request;
        assert.deepEqual(config.allowed_files, ['ai-resources/index.html']);
        assert.equal(config.patch_format, 'am');
        assert.equal(config.auto_merge, undefined);
        assert.equal(config.reviewers, undefined);
    }
    assert.match(job('safe_outputs'), /needs\.agent\.result == 'success'/);
    assert.match(job('safe_outputs'), /needs\.detection\.outputs\.detection_success == 'true'/);
    assert.match(job('detection'), /GH_AW_DETECTION_CONTINUE_ON_ERROR: "false"/);
    assert.match(job('detection'), /CUSTOM_PROMPT:.*internship-review/);
    assert.doesNotMatch(job('detection'), /\bthreat-detect --engine/);
    assert.equal((job('detection').match(/uses: actions\/checkout@/g) || []).length, 1);
    assert.match(job('detection'), /name: Validate the exact proposed patch\n\s+if: contains\(needs\.agent\.outputs\.output_types, 'create_pull_request'\)/);
    const dependencies = [...job('finalize').matchAll(/^      - (agent|safe_outputs|detection)$/gm)].map(match => match[1]);
    assert.deepEqual(dependencies.sort(), ['agent', 'detection', 'safe_outputs']);
    assert.doesNotMatch(job('agent').split('steps:')[0], /- finalize/);
});
