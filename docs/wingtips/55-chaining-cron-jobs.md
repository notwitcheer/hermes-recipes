# Hermes Wingtips #55: chaining cron jobs

posted 2026-08-26. original: [https://x.com/witcheer/status/2092527968140632114](https://x.com/witcheer/status/2092527968140632114)

Hermes Wingtips #55: chaining cron jobs

every cron job wakes up in a fresh session. a two-step pipeline, collect then summarize, can't see what step one produced.

`context_from` wires the connection. when you create the second job, point it at the first job's id, and the first job's latest output is prepended to the second job's prompt at fire time.

a job can also point at itself. `continuity` injects the job's own previous output. 

you set all of this by asking your Hermes Agent in plain language, it manages its own cron table.
