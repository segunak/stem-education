---
description: Weekly sync of the Microsoft internship link list on the AI resources page with currently open undergraduate internships.

on:
  schedule:
    - cron: "0 19 * * 0" # Sundays 3 PM EDT (2 PM EST in winter, cron is UTC only)
  workflow_dispatch:

permissions:
  contents: read
  copilot-requests: write

engine: copilot

network:
  allowed:
    - defaults

tools:
  edit:

# Deterministic data gathering happens here so the agent only has to edit HTML.
steps:
  - name: Fetch open Microsoft internships and resolve current links
    run: |
      set -euo pipefail
      mkdir -p /tmp/gh-aw/agent
      out=/tmp/gh-aw/agent
      api='https://apply.careers.microsoft.com/api/pcsx/search?domain=microsoft.com&query=intern&location=United%20States&filter_include_remote=1&filter_employment_type=internship'

      # The careers API returns 10 results per page and rate limits fast callers.
      : > "$out/pages.jsonl"
      for start in $(seq 0 10 190); do
        page=$(curl -fsS --retry 6 --retry-delay 20 -H 'Accept: application/json' "$api&start=$start")
        n=$(echo "$page" | jq '.data.positions | length')
        [ "$n" -eq 0 ] && break
        echo "$page" | jq -c '.data.positions[] | {id, name, department}' >> "$out/pages.jsonl"
        sleep 2
      done

      # The API already filters to internships. Keep undergraduate roles only: drop PhD, MBA, Masters, research and CTJ.
      jq -s '[ .[]
        | select(.name | test("PhD|MBA|Master|Research|CTJ"; "i") | not)
        | {id: (.id | tostring), name, url: ("https://apply.careers.microsoft.com/careers/job/" + (.id | tostring))}
      ] | unique_by(.id)' "$out/pages.jsonl" > "$out/open-internships.json"

      # Refuse to continue on an empty result so a flaky API can never wipe the list.
      [ "$(jq length "$out/open-internships.json")" -gt 0 ] || { echo "No internships returned"; exit 1; }

      # Resolve every link in the current list to a job id (aka.ms links are redirects).
      : > "$out/current-links.tsv"
      sed -n '/<ul class="internship-link-list">/,/<\/ul>/p' ai-resources/index.html \
        | grep -oE 'href="[^"]+"' | sed -E 's/^href="|"$//g' | while read -r href; do
          target=$(curl -sS -o /dev/null -w '%{redirect_url}' "$href" || true)
          id=$(echo "${target:-$href}" | grep -oE '[0-9]{12,}' | head -n1 || true)
          printf '%s\t%s\n' "$href" "${id:-unknown}" >> "$out/current-links.tsv"
        done

safe-outputs:
  # gh-aw opens GitHub issues for failed runs by default. Turn off every path so failures only show in the Actions tab.
  report-failure-as-issue: false
  missing-tool:
    create-issue: false
  missing-data:
    create-issue: false
  report-incomplete:
    create-issue: false
  noop:
    report-as-issue: false
  create-pull-request:
    title-prefix: "[internships] "
    labels: [automation]
    draft: false
    reviewers: [copilot]
    allowed-files: [ai-resources/index.html]
    fallback-as-issue: false
---

# Update Microsoft Internship List

Keep the `<ul class="internship-link-list">` in `ai-resources/index.html` in sync with the internships Microsoft currently has open.

Inputs, already prepared for you:

- `/tmp/gh-aw/agent/open-internships.json`: currently open undergraduate internships (`id`, `name`, `url`). PhD, MBA, research, and non-intern roles are already filtered out. Treat this as the full truth for "open".
- `/tmp/gh-aw/agent/current-links.tsv`: each link currently in the list (`href`, then the job `id` it resolves to).

Do this:

1. **Remove stale items.** Delete the `<li>` for any link whose id is not in `open-internships.json`. If an id is `unknown`, leave that item alone.
2. **Add missing items.** For every open internship whose id is not already in the list, append a new `<li>` that links to its `url`. Skip duplicates: one `<li>` per job id.
3. **Name new items in the existing style.** Look at the current titles and match them: `Role, Focus Internship`, `&` written as `&amp;`, no location, no "Opportunities for University Students" filler. Example: "Software Engineer: Data Platform/Analytics Intern Opportunities for University Students, Redmond" becomes `Software Engineer, Data Platform &amp; Analytics Internship`.
4. **Keep existing items as they are** (href and text) when their job is still open, including `aka.ms` links.

Only edit the `<ul class="internship-link-list">` block. Do not touch anything else in the file, and keep the existing indentation and `<li>` / `<a>` markup.

If nothing needs to change, call `noop` and do not open a pull request. Otherwise open a pull request titled `Update Microsoft internship list` whose body lists what was removed and what was added.
