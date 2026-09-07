# Hermes Wingtips #5: /learn

posted 2026-06-24. original: [https://x.com/witcheer/status/2069828190197973337](https://x.com/witcheer/status/2069828190197973337)

Hermes Wingtips #5: /learn 

it turns a source into a reusable skill in one command. 

four ways to feed it: a local code/docs folder, a doc url, a workflow you just ran, or pasted notes. reach for it once you've done something non-trivial and don't want to re-explain it next time.

the skill lands in ~/.hermes/skills/ and auto-loads only when a task calls for it, so it's procedural memory that doesn't bloat every prompt. 

I used it today and it drafted a genuinely good skill, even pulling in a real adjacent feature I hadn't mentioned.

~~~
what you need to know: it currently ignores its own <=60-char description rule (mine came out 123 and 202 chars). 

since a skill's description loads every session, a 200-char one is dead weight. open the SKILL.md, tighten it, fix the author, before you rely on it or share it.
