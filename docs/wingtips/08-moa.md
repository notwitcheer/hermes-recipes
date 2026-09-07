# Hermes Wingtips #8: MoA

posted 2026-06-27. original: [https://x.com/witcheer/status/2070888011508674819](https://x.com/witcheer/status/2070888011508674819)

Hermes Wingtips #8: MoA

the new Mixture of Agents virtual model fans every turn out to four reference models plus an aggregator. 

I put it on a fresh Hermes box: gpt-5.5, deepseek-v4-pro and sonnet-4.6 as references, opus-4.8 as the aggregator.

measured on the box: 

- a single opus call ran 27.9k tokens for ~$0.14
- the full MoA turn ran 28.6k tokens for ~$0.15, the same within a cent

the system prompt and tool schemas dominate that number, and the references run on stripped context, so the four extra calls stay cheap. 
for one question, you get the whole ensemble for barely more than a single model.

and the quality is the point: Nous's HermesBench puts an opus + gpt-5.5 MoA at 0.8202 vs 0.7607 / 0.7412 for those models alone. 

it is 5 calls a turn, so it scales with task length, which is exactly why Nous frames it for "genuinely difficult problems" and on that ground it's one of the better-value things they've shipped.
