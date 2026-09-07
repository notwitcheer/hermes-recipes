# Hermes Wingtips #39: the missing provider prefix

posted 2026-08-06. original: [https://x.com/witcheer/status/2085293767506931833](https://x.com/witcheer/status/2085293767506931833)

Hermes Wingtips #39: the missing provider prefix

if a model id ever answers you with a 404 error, check the id before you check your keys. 

providers know their models as `vendor/model`, and an id that lost its prefix (`nemotron-3-ultra-550b-a55b` instead of `nvidia/nemotron-3-ultra-550b-a55b`) returns a 404, so it reads like an outage.

a fix just merged for the next release: the error now names the model and suggests the prefixed id. 

until then, the habit to keep in mind: `vendor/model`, always, and `hermes model` picks it correctly for you.
