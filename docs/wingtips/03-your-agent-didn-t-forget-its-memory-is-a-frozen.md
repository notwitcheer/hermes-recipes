# Hermes Wingtips #3: your agent didn't forget, its memory is a frozen snapshot

posted 2026-06-22. original: [https://x.com/witcheer/status/2069020659829608570](https://x.com/witcheer/status/2069020659829608570)

Hermes Wingtips #3: your agent didn't forget, its memory is a frozen snapshot.

tell it something, it saves to MEMORY.md, the write hits disk right away. 
but the curated memory block in the system prompt loads once at session start and stays fixed for the whole session.

this is on purpose, to keep the prefix cache warm.

so mid-session it can act like it "forgot" what it just saved. 
it didn't: tool calls still read the live on-disk value, only the injected block is frozen. it refreshes next session.

if you need it acting on a fresh memory right now, start a new session. the save already landed, it just shows up next time.
