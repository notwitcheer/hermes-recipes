#!/bin/bash
# drain/restore: borrow the whole GPU from your agent for a heavy job
# (training run, big benchmark), and GUARANTEE the agent comes back.
#
# the pattern that matters is the trap: the restore runs on EVERY exit path —
# success, failure, ctrl-C, timeout, kill. an unattended job that stops your
# model server and then dies must not leave the agent dead until you notice.
#
# usage: ./drain-restore.sh <command...>
# example: ./drain-restore.sh python train.py --epochs 1
#
# requires the scoped sudoers rule (see sudoers-llama-server) so the
# start/stop needs no password from cron or a non-interactive shell.
# NOTE: set -u, deliberately NOT set -e. under set -e a failing command exits
# the script BEFORE your $? bookkeeping runs, and subtle interactions with
# trap have produced restore failures in the wild. keep the error handling
# explicit.
set -u

if [ $# -eq 0 ]; then
  echo "usage: $0 <command...>" >&2
  exit 2
fi

LOG="${DRAIN_LOG:-$HOME/drain-restore.log}"

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
