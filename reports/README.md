# Reports

This directory stores durable maintenance notes for the awesome list.

Use `scripts/collect_starred_candidates.py` to scan a GitHub user's starred
repositories and generate `.maintenance/starred-candidates.md`.

The collector also writes `.maintenance/starred-candidates.json` for automated
Codex review.

Candidate reports are ignored cache files. Final entries still need manual or agent
curation against `CONTRIBUTING.md` before changing `README.md` and
`README.zh-CN.md`.

## Weekly Codex Automation

Run the full weekly workflow manually from `main` with:

```bash
scripts/daily_starred_codex_update.sh
```

The workflow:

1. Refuses to run unless the git worktree is clean.
2. Requires working GitHub CLI authentication for the `scortt` account.
3. Regenerates ignored candidate reports under `.maintenance/`.
4. Audits listed GitHub repositories for unavailable, archived, disabled, or
   renamed projects.
5. Runs `codex exec` to curate strong candidates into `README.md` and
   `README.zh-CN.md`.
6. Verifies allowed file changes, bilingual URL/order parity, duplicate URLs,
   Markdown entry structure, and `git diff --check`.
7. Creates a local commit only when there are accepted changes.

Install the Sunday 20:30 cron entry with:

```bash
scripts/install_daily_starred_codex_cron.sh
```

Cron logs go to `reports/daily-starred-codex.log`, which is ignored by git.
The automation never pushes commits. Push or review local commits separately.
