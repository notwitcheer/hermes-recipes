#!/bin/bash
# drain/restore: borrow the whole GPU from your agent for a heavy job
# (training run, big benchmark), and GUARANTEE the agent comes back.
#
# the pattern that matters is the trap: the restore runs on EVERY exit path —
# success, failure, ctrl-C, timeout, kill. an unattended job that stops your
# model server and then dies must not leave the agent dead until you notice.
#
# usage: ./drain-restore.sh [--dry-run] <command...>
# example: ./drain-restore.sh python train.py --epochs 1
#
# --dry-run prints the exact steps (stop, job, restore, log) without
# executing any of them: no sudo calls, no service stop, no log write.
# use it to sanity-check a cron line before trusting it overnight.
#
# requires the scoped sudoers rule (see sudoers-llama-server) so the
# start/stop needs no password from cron or a non-interactive shell.
# NOTE: set -u, deliberately NOT set -e. under set -e a failing command exits
# the script BEFORE your $? bookkeeping runs, and subtle interactions with
# trap have produced restore failures in the wild. keep the error handling
# explicit.
set -u

DRY_RUN=0
if [ "${1:-}" = "--dry-run" ]; then
  DRY_RUN=1
  shift
fi

if [ $# -eq 0 ]; then
  echo "usage: $0 [--dry-run] <command...>" >&2
  exit 2
fi

LOG="${DRAIN_LOG:-$HOME/drain-restore.log}"

if [ "$DRY_RUN" -eq 1 ]; then
  # print the plan and exit BEFORE the trap is installed, so a dry run
  # can never touch the service or the log.
  echo "[dry-run] would stop:    sudo -n systemctl stop llama-server.service"
  echo "[dry-run] would wait:    sleep 5"
  echo "[dry-run] would run:     $*"
  echo "[dry-run] would restore: sudo -n systemctl start llama-server.service (via trap, on every exit path)"
  echo "[dry-run] would log to:  $LOG"
  exit 0
fi

restore() {
  sudo -n systemctl start llama-server.service
  echo "[drain] restore attempted at $(date)" >> "$LOG"
}
trap restore EXIT

echo "[drain] stopping llama-server for: $* ($(date))" >> "$LOG"
sudo -n systemctl stop llama-server.service
sleep 5

"$@"
RC=$?
echo "[drain] job exited rc=$RC at $(date)" >> "$LOG"
exit $RC
