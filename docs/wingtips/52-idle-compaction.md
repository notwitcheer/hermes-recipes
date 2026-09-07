# Hermes Wingtips #52: idle compaction

posted 2026-08-23. original: [https://x.com/witcheer/status/2091520019318423801](https://x.com/witcheer/status/2091520019318423801)

Hermes Wingtips #52: idle compaction

a long-lived thread carries its whole history back into context every time you come back to it, and you pay for that stale backlog on every turn.

your Hermes Agent has a time-based trigger for exactly this:

`hermes config set compression.idle_compact_after_seconds 1800`

the size-based threshold waits for the context to grow big. this one fires on the time gap since your last message. set it in seconds, 1800 = 30 minutes.

super useful if you keep one long Telegram or Discord thread with your agent, or park a session overnight and pick it up in the morning!
