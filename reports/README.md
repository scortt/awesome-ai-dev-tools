# Reports

This directory stores generated review reports for maintaining the awesome list.

Use `scripts/collect_starred_candidates.py` to scan a GitHub user's starred
repositories and generate `reports/starred-candidates.md`.

The collector also writes `reports/starred-candidates.json` for automated
Codex review.

The report is a candidate list only. Final entries still need manual or agent
curation against `CONTRIBUTING.md` before changing `README.md` and
`README.zh-CN.md`.

## Daily Codex Automation

Run the full nightly workflow manually with:

```bash
scripts/daily_starred_codex_update.sh
```

The workflow:

1. Refuses to run unless the git worktree is clean.
2. Requires working GitHub CLI authentication for the `scortt` account.
3. Regenerates `starred-candidates.md` and `starred-candidates.json`.
4. Runs `codex exec` to curate strong candidates into `README.md` and
   `README.zh-CN.md`.
5. Verifies allowed file changes, duplicate GitHub URLs within each README,
   basic Markdown entry structure, and `git diff --check`.
6. Creates a local commit only when there are accepted changes.

Install the 20:30 daily cron entry with:

```bash
scripts/install_daily_starred_codex_cron.sh
```

Cron logs go to `reports/daily-starred-codex.log`, which is ignored by git.
The automation never pushes commits. Push or review local commits separately.
