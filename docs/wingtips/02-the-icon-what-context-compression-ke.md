# Hermes Wingtips #2: the 🗜️ icon, what context compression keeps and what it drops

posted 2026-06-19. original: [https://x.com/witcheer/status/2068027535955468533](https://x.com/witcheer/status/2068027535955468533)

Hermes Wingtips #2

the 🗜️ icon, what context compression keeps and what it drops

this little emojy is the compression count: how many times Hermes auto-summarised the session to stay under the context limit, which kicks in around 50% full. 

when compression occurs, it keeps your first 3 turns and your last 20, and summarises everything in between. 
a detail from the middle of a long session can then drop out, and the agent repeats work it already did, even though the opening goal and the recent turns are intact.

~~~
three levers when it bites, all in config.yaml, hot-reloading on a running gateway: 

- protect_last_n keeps more recent turns uncompressed 

- auxiliary.compression.model points the summariser at a cheap fast model so it does not burn main-model tokens

- model.context_length raises the ceiling so it fires later.

https://hermes-agent.nousresearch.com/docs/developer-guide/context-compression-and-caching
