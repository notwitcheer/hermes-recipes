# 24/7 Hermes Agent on a Mac Mini: crons, approvals, and a gateway that stays up

I run Hermes Agent around the clock on a Mac Mini M4. it executes scheduled jobs day and night, messages me on Telegram when something needs me, and nothing it drafts ever goes public without my explicit approval. this recipe is everything I learned making that reliable, including a launchd gotcha that can silently downgrade your gateway supervision, and the two-line fix.

everything below ran on my own hardware: a Mac Mini M4 on macOS 15, running Hermes Agent v0.16.0 (the Surface Release). if a step is not in here, I have not tested it.

## what you get

- Hermes Agent gateway running 24/7 under launchd, with a watchdog so a crash or reboot can't take your jobs down without you knowing
- scheduled jobs (crons) that write to a git-synced workspace and message you on Telegram, with a clean pattern for "only message me when it matters"
- a human-in-the-loop setup: the agent drafts, you approve, nothing posts itself

## prerequisites

- a Mac that stays on (mine is a Mac Mini M4, any Apple silicon Mac works)
- Hermes Agent installed and the Telegram gateway configured: follow the official docs at https://hermes-agent.nousresearch.com, this recipe starts where the installer ends
- Homebrew, and `gh` if your jobs touch GitHub (`brew install gh`)

## part 1: keep the gateway alive

the gateway is the process that runs your crons and connects your messaging platforms. if it dies, your jobs stop and nothing tells you. three layers fix that.

### the launchd gotcha

on macOS (seen on macOS 15 with Hermes v0.16.0), `hermes gateway start` can fail to register the launchd service and fall back to an unsupervised background process. when it happens you see this:

```
Bootstrap failed: 5: Input/output error
⚠ launchd cannot manage the gateway on this macOS version (launchctl exit 5)
✓ Started gateway as a background process instead
  It will NOT auto-start at login or auto-restart on crash.
```

the trap: if you had a working launchd job before running the command, it got unloaded. the cli's fallback works until the first crash or reboot, then your agent is gone and nothing tells you.

### the fix: bootstrap it yourself

raw launchctl works fine where the cli fails, including over ssh:

```bash
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/ai.hermes.gateway.plist
```

verify it took:

```bash
launchctl print gui/$(id -u)/ai.hermes.gateway | grep state
# state = running
```

### the watchdog: cover crashes and reboots

the generated plist starts the gateway at login but does not restart it on crash. a cron watchdog closes both gaps (cron itself runs at boot, no login needed):

```bash
mkdir -p ~/scripts && cat > ~/scripts/gateway-watchdog.sh <<'EOF'
#!/usr/bin/env bash
# restart the hermes gateway if it has died. runs from cron every 5 min.
set -u
HERMES_PY="$HOME/.hermes/hermes-agent/venv/bin/python"
LOG="$HOME/.hermes/logs/gateway-watchdog.log"

pgrep -f "hermes_cli.main gateway run" >/dev/null && exit 0

echo "$(date -u +%FT%TZ) gateway down, restarting" >> "$LOG"
launchctl bootout "gui/$(id -u)/ai.hermes.gateway" 2>/dev/null
if launchctl bootstrap "gui/$(id -u)" "$HOME/Library/LaunchAgents/ai.hermes.gateway.plist" 2>>"$LOG"; then
  echo "$(date -u +%FT%TZ) restarted via launchd" >> "$LOG"
else
  nohup "$HERMES_PY" -m hermes_cli.main gateway run --replace >> "$HOME/.hermes/logs/gateway.log" 2>&1 &
  echo "$(date -u +%FT%TZ) restarted as background process (launchd refused)" >> "$LOG"
fi
EOF
chmod +x ~/scripts/gateway-watchdog.sh

# install: every 5 minutes
(crontab -l 2>/dev/null; echo '*/5 * * * * $HOME/scripts/gateway-watchdog.sh >/dev/null 2>&1') | crontab -
```

I have watched this sequence recover a downgraded gateway on my own machine. the same script ships in this folder as `gateway-watchdog.sh`.

## part 2: cron jobs that behave

Hermes has a built-in scheduler, no system crontab needed for agent work:

```bash
hermes cron create "30 7 * * *" "read the new notes in my workspace from the last 24 hours and send me a 5-line morning brief: counts, top 3 items with links, suggested priority." --name morning-brief --deliver telegram:<your-chat-id> --workdir ~/workspace
```

four things I learned the hard way:

- **schedule syntax**: `"30m"` means once, in 30 minutes. recurring jobs need cron expressions (`"*/30 * * * *"`).
- **quiet jobs**: the gateway delivers a job's final response to its target. if the agent replies exactly `[SILENT]`, the gateway skips delivery. the pattern for "only message me when it matters": tell the job to respond with its alert text when there is something, and `[SILENT]` when there is not. do not rely on the agent calling a messaging tool mid-run; in my testing, cron agents ignore that instruction, the final-response route is the reliable one.
- **`--workdir` matters**: it injects the CLAUDE.md / AGENTS.md from that directory as project context, so jobs inherit your workspace rules.
- **prompt files beat inline prompts**: register the job as "read crons/<job>.md in this directory and execute it exactly", keep the actual prompt in your git-synced workspace. fixing a misbehaving job becomes a git push instead of re-registering, and your prompts are versioned.

scripts on a schedule (no llm involved) use `--script` with `--no-agent`. Hermes refuses symlinks that point outside `~/.hermes/scripts/`, so use a two-line wrapper that execs the real script from your workspace.

## part 3: a git-synced workspace

my agent reads and writes a plain markdown folder that is also a private git repo. the Mini commits and pushes on a schedule; my laptop pulls. two rules keep it conflict-free:

- the agent machine writes only to one folder (its inbox); the human writes everywhere else
- offset the sync from the jobs: jobs run at :00 and :30, sync runs at :15 and :45, so the sync never commits a half-finished write

the `git-sync.sh` in this folder does pull-rebase-commit-push with an identity guard. for credentials, use a repo-scoped deploy key on the Mini rather than your account credentials: if the machine is ever compromised, the blast radius is one repo.

```bash
ssh-keygen -t ed25519 -f ~/.ssh/my-workspace-deploy -N "" -C "mini-deploy"
# add the .pub as a deploy key with write access in the repo settings, then:
cd ~/workspace && git config core.sshCommand "ssh -i ~/.ssh/my-workspace-deploy -o IdentitiesOnly=yes"
```

## part 4: the approval rule

the one architectural rule I never break: the agent has no path to post publicly. drafts land in a queue file in the workspace, Telegram is where I approve or reject, and publishing is something only I do. if you automate one thing about this setup, do not automate that.

## verify your setup

1. `hermes cron list`: every job shows its schedule and last run status
2. kill the gateway process, wait 5 minutes, confirm the watchdog restarted it (`grep restarted ~/.hermes/logs/gateway-watchdog.log`)
3. force one test job: `hermes cron create "1m" "respond with exactly: test ping, please ignore" --deliver telegram:<your-chat-id>`, confirm it arrives
4. reboot the Mini, confirm the gateway is back within 5 minutes without logging in

## what breaks first (and the fix)

- gateway down after a macOS update: the watchdog brings it back; check the log if pings stop
- a job goes noisy: tighten its prompt file, push, the next run picks it up
- git push rejected: concurrent edits, the sync script's rebase handles it; check the sync log if it loops
- `hermes gateway start` ran and supervision downgraded: re-bootstrap with the launchctl command above

## cost

one Mac Mini you already own, the agent's model subscription, zero additional services. the workspace repo is a free private GitHub repo.
