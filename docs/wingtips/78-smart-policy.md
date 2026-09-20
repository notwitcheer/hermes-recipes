# Hermes Wingtips #78: approvals.smart_policy, your own rules for the command reviewer

posted 2026-09-20. original: [https://x.com/witcheer/status/2101606053800456228](https://x.com/witcheer/status/2101606053800456228)

when Hermes Agent wants to run a terminal command that looks risky, a second model reviews it first. it reads the command and answers with one word: approve, deny, or escalate, which means ask you.

this key lets you add your own rules to that reviewer's instructions.

"always escalate anything that modifies /etc."
"approve docker compose restarts in ~/deploys, they are routine here."

your rules are read as instructions from you, never as part of the command it is judging.

```yaml
approvals:
  smart_policy: |
    Always ESCALATE commands that modify anything under /etc.
```

empty by default. the reviewer itself is on by default (`approvals.mode: smart`).

docs: [https://hermes-agent.nousresearch.com/docs/user-guide/configuration#smart-approvals](https://hermes-agent.nousresearch.com/docs/user-guide/configuration#smart-approvals)
