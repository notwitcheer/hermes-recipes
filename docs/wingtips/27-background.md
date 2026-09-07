# Hermes Wingtips #27: /background

posted 2026-07-22. original: [https://x.com/witcheer/status/2079951218101891530](https://x.com/witcheer/status/2079951218101891530)

Hermes Wingtips #27: /background

you do not have to wait while your agent grinds through a long task. 

`/background <prompt>` spawns a completely separate agent session that runs in parallel: your chat stays fully interactive, and the result comes back as a panel in your terminal when it finishes.  

(1) as an example: `/background analyse the logs in /var/log and summarise today's errors`. 

you can run several at once, and the status bar shows how many are in flight.  

(2) one thing to know: the background agent starts clean, with no knowledge of your conversation. 

it only gets the prompt you give it, so write it self-contained.  it inherits your model, provider and toolsets, so no setup needed.
