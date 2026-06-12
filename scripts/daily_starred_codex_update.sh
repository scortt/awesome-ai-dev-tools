#!/usr/bin/env bash
set -euo pipefail

ROOT="/Users/scortt/project/awesome-ai-dev-tools"
LOG_PREFIX="[daily-starred-codex]"

cd "$ROOT"

log() {
  printf '%s %s %s\n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" "$LOG_PREFIX" "$*"
}

fail() {
  log "error: $*"
  exit 1
}

require_command() {
  command -v "$1" >/dev/null 2>&1 || fail "$1 is required"
}

require_clean_worktree() {
  local status
  status="$(git status --porcelain)"
  if [[ -n "$status" ]]; then
    printf '%s\n' "$status" >&2
    fail "worktree is not clean; refusing to mix automation changes with existing work"
  fi
}

changed_files() {
  {
    git diff --name-only
    git diff --cached --name-only
    git ls-files --others --exclude-standard
  } | sort -u
}

check_allowed_files() {
  changed_files | python3 -c 'import fnmatch, sys
allowed = ("README.md", "README.zh-CN.md", "reports/*", "docs/*.md")
paths = [line.strip() for line in sys.stdin if line.strip()]
disallowed = [path for path in paths if not any(fnmatch.fnmatchcase(path, pattern) for pattern in allowed)]
if disallowed:
    print("Disallowed changed files:", file=sys.stderr)
    print("\n".join(disallowed), file=sys.stderr)
    sys.exit(1)'
}

check_duplicate_github_urls() {
  python3 - <<'PY'
from pathlib import Path
import re
import sys

paths = [Path("README.md"), Path("README.zh-CN.md")]
pattern = re.compile(r"https://github\.com/[^)\s]+")
duplicates: list[tuple[str, str, str]] = []

for path in paths:
    seen: dict[str, str] = {}
    for url in pattern.findall(path.read_text()):
        key = url.rstrip("/")
        location = str(path)
        if key in seen:
            duplicates.append((key, seen[key], location))
        else:
            seen[key] = location

if duplicates:
    for url, first, second in duplicates:
        print(f"duplicate GitHub URL: {url} ({first}, {second})", file=sys.stderr)
    sys.exit(1)
PY
}

check_markdown_entries() {
  python3 - <<'PY'
from pathlib import Path
import sys

errors: list[str] = []

for path in [Path("README.md"), Path("README.zh-CN.md")]:
    for lineno, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.startswith("- [") or "github.com/" not in line:
            continue
        if ") - " not in line:
            errors.append(f"{path}:{lineno}: entry is missing the markdown description separator")
        if line.count("`") % 2 != 0:
            errors.append(f"{path}:{lineno}: entry has unbalanced code spans")

if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
PY
}

commit_if_changed() {
  if [[ -z "$(changed_files)" ]]; then
    log "no changes after Codex analysis"
    return
  fi

  check_allowed_files
  check_duplicate_github_urls
  check_markdown_entries
  git diff --check

  git add README.md README.zh-CN.md reports docs
  if git diff --cached --quiet; then
    log "no staged changes"
    return
  fi

  git commit -m "chore: update awesome ai dev tools from stars"
  log "created local commit $(git rev-parse --short HEAD)"
}

require_command gh
require_command codex
require_command git
require_command python3

require_clean_worktree

log "checking GitHub starred API access"
if ! gh api "/users/scortt/starred?per_page=1" --jq ".[0].full_name" >/dev/null; then
  fail "GitHub CLI cannot read scortt starred repositories; run gh auth login before enabling this automation"
fi

log "collecting starred repository candidates"
python3 scripts/collect_starred_candidates.py \
  --user scortt \
  --output reports/starred-candidates.md \
  --json-output reports/starred-candidates.json

log "running Codex curation"
codex -a never exec \
  -C "$ROOT" \
  -s workspace-write \
  "$(cat <<'PROMPT'
You are maintaining the Awesome AI Dev Tools curated list.

Read AGENTS.md and CONTRIBUTING.md first. Use reports/starred-candidates.json
and reports/starred-candidates.md as candidate input.

Task:
- Add only strong, directly relevant open source AI developer-tool entries.
- Update README.md and README.zh-CN.md consistently.
- Keep each entry one sentence, factual, and workflow-oriented.
- Preserve the existing category structure unless a clearly necessary category already exists.
- Do not include star counts, popularity claims, hype words, or ranking language.
- Reject generic apps, generic libraries, prompt dumps, courses, and projects that do not improve AI-assisted development workflows.
- If useful, write a short analysis summary to reports/daily-starred-codex-analysis.md.

Do not run git commit, git push, or destructive git commands. Leave final
changes in the working tree for the wrapper script to verify and commit.
PROMPT
)"

commit_if_changed
log "done"
