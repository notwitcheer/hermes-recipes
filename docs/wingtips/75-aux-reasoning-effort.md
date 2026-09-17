# Hermes Wingtips #75: reasoning_effort for side tasks, how hard each background call thinks

posted 2026-09-17. original: [https://x.com/witcheer/status/2100460797239415168](https://x.com/witcheer/status/2100460797239415168)

besides your chat, Hermes Agent makes small model calls of its own: the summary written when a long conversation is compacted, the name it gives a session, reading an image you paste, the check on whether a command needs your approval.

those calls run on your main model unless you gave them another one, at the provider's default thinking level.

but a session title does not need deep thinking.

each side task has its own `reasoning_effort`. set it to `low` or `none` for that task and the call comes back sooner and costs less, while your chat keeps the level you set for it.

```yaml
# in ~/.hermes/config.yaml  (or: hermes config set auxiliary.<task>.reasoning_effort low)
auxiliary:
  compression:
    reasoning_effort: low
  title_generation:
    reasoning_effort: none
  vision:
    reasoning_effort: none
```

levels: `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, `max`, `ultra`. not set by default (the provider's default level). same knob on approval, curator, triage_specifier, kanban_decomposer, goal_judge and the other side tasks; your chat keeps its own `agent.reasoning_effort`. MoA slots set depth in the preset, and a background review that stays on your main model ignores this key.

docs: https://hermes-agent.nousresearch.com/docs/user-guide/configuration#the-universal-config-pattern
