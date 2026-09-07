# Hermes Wingtips #19: it remembered, it just can't see it yet

posted 2026-07-13. original: [https://x.com/witcheer/status/2076670836891689174](https://x.com/witcheer/status/2076670836891689174)

Hermes Wingtips #19: it remembered, it just can't see it yet.

we snapshot MEMORY.md and USER.md once at session start so the LLM prefix cache stays warm. 

a mid-session save hits disk immediately, and only lands in the system prompt on the next session.

you need the new fact in play now?

(1) start a fresh session
(2) or hermes -c on the next turn

tool responses already show the live write.
