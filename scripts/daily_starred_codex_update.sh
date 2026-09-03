#!/usr/bin/env bash
set -euo pipefail

export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"

ROOT="/Users/scortt/project/awesome-ai-dev-tools"
EXPECTED_BRANCH="${AWESOME_EXPECTED_BRANCH:-main}"
CACHE_DIR="$ROOT/.maintenance"
LOCK_DIR="${TMPDIR:-/tmp}/awesome-ai-dev-tools-update.lock"
LOG_PREFIX="[weekly-starred-codex]"

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

require_expected_branch() {
  local branch
  branch="$(git branch --show-current)"
  [[ "$branch" == "$EXPECTED_BRANCH" ]] ||
    fail "expected branch $EXPECTED_BRANCH, found $branch"
}

require_not_behind_origin() {
  local behind
  git fetch --quiet origin "$EXPECTED_BRANCH"
  behind="$(git rev-list --count HEAD.."origin/$EXPECTED_BRANCH")"
  [[ "$behind" == "0" ]] ||
    fail "$EXPECTED_BRANCH is behind origin/$EXPECTED_BRANCH by $behind commit(s)"
}

acquire_lock() {
  if ! mkdir "$LOCK_DIR" 2>/dev/null; then
    fail "another update appears to be running: $LOCK_DIR"
  fi
  trap 'rmdir "$LOCK_DIR" 2>/dev/null || true' EXIT
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
allowed = ("README.md", "README.zh-CN.md", "docs/*.md")
paths = [line.strip() for line in sys.stdin if line.strip()]
disallowed = [path for path in paths if not any(fnmatch.fnmatchcase(path, pattern) for pattern in allowed)]
if disallowed:
    print("Disallowed changed files:", file=sys.stderr)
    print("\n".join(disallowed), file=sys.stderr)
    sys.exit(1)'
}

commit_if_changed() {
  if [[ -z "$(changed_files)" ]]; then
    log "no changes after Codex analysis"
    return
  fi

  check_allowed_files
  python3 scripts/verify_awesome_update.py
  git diff --check

  git add README.md README.zh-CN.md docs
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

acquire_lock
require_expected_branch
require_clean_worktree

mkdir -p "$CACHE_DIR"

log "checking GitHub starred API access"
if ! gh api "/users/scortt/starred?per_page=1" --jq ".[0].full_name" >/dev/null; then
  fail "GitHub CLI cannot read scortt starred repositories; run gh auth login before enabling this automation"
fi
require_not_behind_origin

log "collecting starred repository candidates"
python3 scripts/collect_starred_candidates.py \
  --user scortt \
  --output .maintenance/starred-candidates.md \
  --json-output .maintenance/starred-candidates.json

log "auditing listed GitHub repositories"
python3 scripts/audit_listed_repositories.py \
  --output .maintenance/listed-repository-health.json

log "running Codex curation"
codex -a never exec \
  -C "$ROOT" \
  -s workspace-write \
  "$(cat <<'PROMPT'
You are maintaining the Awesome AI Dev Tools curated list.

Read AGENTS.md and CONTRIBUTING.md first. Use
.maintenance/starred-candidates.json and .maintenance/starred-candidates.md as
candidate input. Also read .maintenance/listed-repository-health.json for
existing entries that may be unavailable, archived, disabled, renamed, or
stale.

Task:
- Add only strong, directly relevant open source AI developer-tool entries.
- Update README.md and README.zh-CN.md consistently.
- Keep each entry one sentence, factual, and workflow-oriented.
- Preserve the existing category structure unless a clearly necessary category already exists.
- Do not include star counts, popularity claims, hype words, or ranking language.
- Reject generic apps, generic libraries, prompt dumps, courses, and projects that do not improve AI-assisted development workflows.
- Keep the English and Chinese lists in the same order with the same GitHub URLs.
- Treat repository health findings as review signals; do not remove a project solely because it has not pushed recently.

Do not run git commit, git push, or destructive git commands. Leave final
changes in the working tree for the wrapper script to verify and commit.
PROMPT
)"

commit_if_changed
log "done"
