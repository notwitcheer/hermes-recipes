# Hermes Wingtips #30: back up your agent before you need to

posted 2026-07-25. original: [https://x.com/witcheer/status/2081051573254549904](https://x.com/witcheer/status/2081051573254549904)

Hermes Wingtips #30: back up your agent before you need to

(1) `hermes backup` 

it writes `~/hermes-backup-<timestamp>.zip` with config.yaml, .env, auth, memories, skills, sessions, cron and profiles. it copies the databases through SQLite's own backup API, so you can run it while Hermes is live.

(2) `hermes import ~/hermes-backup-<timestamp>.zip` puts it all back.

for a fast one, you can use `hermes backup --quick`, which targets critical state only: config.yaml, state.db, .env, auth and cron jobs.

`hermes backup` is super useful if you are moving to a new box, if you want to duplicate your agent or before doing any experiment!
