# Hermes Wingtips #28: cron jobs & workdir

posted 2026-07-23. original: [https://x.com/witcheer/status/2080346485745676561](https://x.com/witcheer/status/2080346485745676561)

Hermes Wingtips #28: cron jobs & workdir

a cron job runs in a completely fresh session, detached from any repo: no AGENTS.md is loaded, and the terminal and file tools start from wherever the gateway happens to be running.

the fix is one flag:

(1) `hermes cron create "every 1d at 09:00" "audit open PRs, summarise CI health" --workdir /home/me/projects/acme`

(2) or from the chat directly, just tell Hermes which directory the job should run in (the cronjob tool takes workdir= the same way)

with workdir set, the job loads AGENTS.md from that directory and every file tool runs inside it. the path must be absolute and exist, or the create is rejected.
