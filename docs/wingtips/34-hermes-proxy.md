# Hermes Wingtips #34: hermes proxy

posted 2026-07-29. original: [https://x.com/witcheer/status/2082613966774350301](https://x.com/witcheer/status/2082613966774350301)

Hermes Wingtips #34: hermes proxy  

your Nous Portal subscription can serve any other app that speaks the OpenAI API.  

`hermes proxy start` runs a small local pass-through server. point the app at the address it prints, give it any placeholder API key and a model from your plan, and it will works. 

in order to double check that the Portal login is ready, type `hermes proxy status`.  

it serves the raw model, not your agent: if you want the whole agent (tools, memory, skills) behind an API, that is `hermes serve`.  

this tips is for people using Open WebUI, Karakeep, or anything self-hosted that asks for an OpenAI key you did not want to buy!
