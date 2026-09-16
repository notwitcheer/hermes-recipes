# Hermes Wingtips #74: provider_routing, pick which host serves your model on OpenRouter

posted 2026-09-16. original: [https://x.com/witcheer/status/2100156876209963106](https://x.com/witcheer/status/2100156876209963106)

on OpenRouter, one model name is served by several hosts, and OpenRouter picks the host for each request.

but what if one of those hosts is rate-limiting you today?

`provider_routing` in config.yaml lets you choose.

list a host under `ignore` and your requests for that model stop going there, even when it is the cheapest one. the other hosts keep serving as before.

on Nous Portal you can skip this step: the Portal picks the host for every model on your behalf, so there is nothing to set.

```yaml
# in ~/.hermes/config.yaml (OpenRouter setups)
provider_routing:
  ignore:
    - "<provider slug>"   # the lowercase slug OpenRouter shows for that host
```

same key, other lists: `only:` (allow these hosts) and `order:` (try these first). read at startup, so restart hermes or the gateway after the edit. list values: edit config.yaml directly, not `hermes config set`. one model only? put the same lists under `models:` for that model id.

docs: [provider routing](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing)
