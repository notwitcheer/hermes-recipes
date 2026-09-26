# Hermes Wingtips #84: mcp.discovery_concurrency, how many MCP servers connect at once

posted 2026-09-26. original: [https://x.com/witcheer/status/2103850251220042077](https://x.com/witcheer/status/2103850251220042077)

new in Hermes Agent: a cap on how many MCP servers connect at the same time.

the servers in your config connect when your Hermes Agent starts, and each local one runs as its own process.

raise it to bring a long list of servers up sooner, or lower it on a small machine.

docs: [https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp#discovery-time](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp#discovery-time)
