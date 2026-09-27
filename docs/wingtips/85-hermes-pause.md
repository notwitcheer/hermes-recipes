# Hermes Wingtips #85: hermes pause, stop your agent starting new work

posted 2026-09-27. original: [https://x.com/witcheer/status/2104227606614757460](https://x.com/witcheer/status/2104227606614757460)

one command stops your Hermes Agent from starting new work. while it is on:

- no cron job fires
- no kanban task is dispatched
- your gateway bots start no new turns

`hermes resume` lifts it.

useful when a scheduled job does something you did not expect, or before you change a skill your cron jobs use!

docs: [https://hermes-agent.nousresearch.com/docs/user-guide/features/cron#pausing-everything-hermes-pause](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron#pausing-everything-hermes-pause)
