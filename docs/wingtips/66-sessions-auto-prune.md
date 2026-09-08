# Hermes Wingtips #66: sessions.auto_prune

posted 2026-09-08. original: [https://x.com/witcheer/status/2097201422844436642](https://x.com/witcheer/status/2097201422844436642)

Hermes Wingtips #66: sessions.auto_prune

every conversation you have with Hermes Agent is kept, so you can resume it or search it later. over time, a busy gateway or cron setup collects a lot of ended sessions that nobody will open again.

so what happens to them?

Hermes now tidies up for you: sessions that have ended and sat untouched for a long while are removed when Hermes starts, and the database gives the space back when there is enough to reclaim. anything open, pinned or mid-conversation stays put, and your recent history stays searchable.

if you would rather keep every session forever, it is one command:

`hermes config set sessions.auto_prune false`

and if you like the cleanup but want a wider window, `sessions.retention_days`.
