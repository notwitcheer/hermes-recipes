# Hermes Wingtips #79: agent.disabled_toolsets, one list that turns a toolset off on every platform

posted 2026-09-21. original: [https://x.com/witcheer/status/2101910495888392672](https://x.com/witcheer/status/2101910495888392672)

Hermes Agent picks its tools per platform: the CLI, Telegram, Discord and the rest each keep their own list of toolsets, set in `hermes tools`.

this key is one list above all of them. a toolset named here is removed everywhere at once, on the CLI and on every gateway platform. it is applied after the per-platform lists.

```yaml
agent:
  disabled_toolsets:
    - web
    - memory
```

`web` takes web_search and web_extract out of every session.
`memory` removes the memory tools and also drops the memory guidance from the prompt.

docs: [https://hermes-agent.nousresearch.com/docs/user-guide/configuration#global-toolset-disable](https://hermes-agent.nousresearch.com/docs/user-guide/configuration#global-toolset-disable)
