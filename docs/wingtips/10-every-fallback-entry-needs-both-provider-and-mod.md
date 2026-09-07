# Hermes Wingtips #10: every fallback entry needs both provider and model

posted 2026-07-01. original: [https://x.com/witcheer/status/2072321716626366479](https://x.com/witcheer/status/2072321716626366479)

Hermes Wingtips #10: every fallback entry needs both provider and model

your fallback_providers list in ~/.hermes/config.yaml counts an entry as a real fallback only when it carries a provider field and a model field. 

two things worth setting:

(1) write provider and model on every entry in the chain, top to bottom.

(2) put a local model last as your floor for a cloud outage, pointing provider: custom at your own llama.cpp or vLLM endpoint.
