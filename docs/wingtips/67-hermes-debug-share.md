# Hermes Wingtips #67: hermes debug share

posted 2026-09-09. original: [https://x.com/witcheer/status/2097565476435992883](https://x.com/witcheer/status/2097565476435992883)

Hermes Wingtips #67: hermes debug share

you want to ask about something Hermes Agent did, in Discord or in an issue. the first questions back are always the same: which version, which model, which provider, what do the logs say.

Hermes has one command that builds the whole report: version and OS, model and provider, the recent lines of the agent, gateway and desktop logs, and which API keys are set. the key values never appear, the report only says set or not set, and the logs are redacted before anything is uploaded.

`hermes debug share`

add --local to print it in your terminal and read it first, nothing leaves your machine. the plain command uploads to a paste service and hands you a link that expires on its own. 

Nous support asks for a bundle? --nous sends the same report to private storage only the team can see.
