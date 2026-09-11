# Hermes Wingtips #69: tool_loop_guardrails

posted 2026-09-11. original: [https://x.com/witcheer/status/2098290534758408306](https://x.com/witcheer/status/2098290534758408306)

Hermes Wingtips #69: `tool_loop.guardrails`

your agent opens a file, reads it, decides to start over, and reads the same file again.

Hermes Agent keeps count of that inside one turn. it watches for three patterns: the same call failing twice in a row, the same tool failing on new arguments, and a call that comes back with the same result while nothing has changed. when a count is reached it writes a warning into the tool result itself, so the model reads it on the next step and changes course.

in the CLI, the TUI and the Desktop app that is where it ends, because you are there to step in. gateway and cron runs go one step further and stop the turn, since nobody is watching. a stop ends the turn, not the session, and the agent tells you which pattern fired.

`hermes config set tool_loop_guardrails.hard_stop_enabled true`

docs: https://hermes-agent.nousresearch.com/docs/user-guide/configuration#tool-loop-guardrails
