# Hermes Wingtips #56: switching models from anywhere

posted 2026-08-27. original: [https://x.com/witcheer/status/2092941623961190832](https://x.com/witcheer/status/2092941623961190832)

Hermes Wingtips #56: switching models from anywhere

`hermes model` opens an interactive picker, so it refuses to run through a pipe, a script, or another agent's terminal tool.

the fix is that you never needed the picker. in any chat, on any platform:

/model grok-4 --provider x-ai --global

`--global` persists it to config.yaml and switches the running session in the same move.

`--once` is the sibling: it switches for a single turn and restores the previous model afterward, even on an error.
