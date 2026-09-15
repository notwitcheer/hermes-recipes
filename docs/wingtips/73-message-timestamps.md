# Hermes Wingtips #73: gateway.message_timestamps, show the model when you wrote

posted 2026-09-15. original: [https://x.com/witcheer/status/2099784645529276481](https://x.com/witcheer/status/2099784645529276481)

your agent reads your messages through Telegram or Discord, but it does not see when you sent them.

`message_timestamps` under `gateway` in config.yaml changes that.

with `enabled: true`, every message you send carries its send time in front, for the model only. the chat you read does not change and the transcripts on disk stay clean. the agent can tell this morning from last week, notice a long gap, and answer with the right day in mind.

your messages only. the agent's replies and the system prompt are untouched.

```yaml
gateway:
  message_timestamps:
    enabled: true
```

or from the terminal: `hermes config set gateway.message_timestamps.enabled true`

docs: [https://hermes-agent.nousresearch.com/docs/user-guide/messaging#message-timestamps-in-model-context](https://hermes-agent.nousresearch.com/docs/user-guide/messaging#message-timestamps-in-model-context)
