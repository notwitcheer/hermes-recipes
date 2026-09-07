# Hermes Wingtips #14: switching models resets your prompt cache

posted 2026-07-06. original: [https://x.com/witcheer/status/2074153526222114974](https://x.com/witcheer/status/2074153526222114974)

Hermes Wingtips #14: switching models resets your prompt cache

switch models mid-conversation and the next turn re-reads the whole thing at full input price. the cache key includes the model, so a new model means a cold cache. occasional switches are fine, frequent ones in a long session multiply your cost.

- batch your switches instead of ping-ponging mid-thread

- on a long session, start a fresh one or delegate (subagents get their own context) rather than switching back and forth
