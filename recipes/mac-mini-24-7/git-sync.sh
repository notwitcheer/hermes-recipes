#!/usr/bin/env bash
# git-sync.sh: two-way sync for a git-backed agent workspace.
# pulls with rebase (autostash), commits local changes if any, pushes.
# run every 30 min on the agent machine, offset from your cron jobs
# (jobs at :00/:30, sync at :15/:45) so half-finished writes never commit.
#
# env vars:
#   WORKSPACE_DIR  workspace path (default: $HOME/workspace)
#   GIT_IDENTITY   expected git user.name; refuses to commit as anyone else (optional)
# usage: git-sync.sh [--dry-run]

set -euo pipefail

WORKSPACE_DIR="${WORKSPACE_DIR:-$HOME/workspace}"
DRY_RUN=0
[[ "${1:-}" == "--dry-run" ]] && DRY_RUN=1

cd "$WORKSPACE_DIR"

if [[ -n "${GIT_IDENTITY:-}" && "$(git config user.name)" != "$GIT_IDENTITY" ]]; then
  echo "git user.name is not $GIT_IDENTITY; refusing to commit. fix with: git config user.name $GIT_IDENTITY" >&2
  exit 1
fi

if [[ $DRY_RUN -eq 1 ]]; then
  echo "[dry-run] workspace: $WORKSPACE_DIR"
  echo "[dry-run] would run: git pull --rebase --autostash"
  echo "[dry-run] local changes that would be committed and pushed:"
  git status --short
  exit 0
fi

git pull --rebase --autostash

git add -A
if ! git diff --cached --quiet; then
  git commit -m "agent sync $(date +%F-%H%M)"
fi

git push
