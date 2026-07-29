#!/usr/bin/env bash
set -euo pipefail

ROOT="/Users/scortt/project/awesome-ai-dev-tools"
SCRIPT_MARKER="scripts/daily_starred_codex_update.sh"
CRON_LINE="30 20 * * 0 cd ${ROOT} && /bin/bash scripts/daily_starred_codex_update.sh >> reports/daily-starred-codex.log 2>&1"

tmp="$(mktemp)"
trap 'rm -f "$tmp"' EXIT

if crontab -l >"$tmp" 2>/dev/null; then
  grep -Fv "$SCRIPT_MARKER" "$tmp" >"${tmp}.next" || true
  mv "${tmp}.next" "$tmp"
else
  : >"$tmp"
fi

printf '\n%s\n' "$CRON_LINE" >>"$tmp"
crontab "$tmp"
echo "installed weekly starred Codex cron:"
echo "$CRON_LINE"
