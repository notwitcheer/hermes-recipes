# Hermes Wingtips #21: credential pools

posted 2026-07-15. original: [https://x.com/witcheer/status/2077409888045510954](https://x.com/witcheer/status/2077409888045510954)

Hermes Wingtips #21: credential pools

a credential pool is several keys or logins for one provider. Hermes picks a healthy key, and when that key is rate-limited or out of quota it rotates to the next one. 

(this is different from fallback providers. a fallback jumps to a different provider, and only after every key in the pool is exhausted).

(1) add a second key (OpenRouter example): 

`hermes auth add openrouter --api-key sk-or-...-key`

(2) check the pool: `hermes auth list`

when Hermes does rotate, the new key has no cached prefix for your chat, so the next request re-reads the full history.  

lastly, if you are on Nous Portal with a single OAuth login, you usually do not need a pool. this tip is for multi-key API setups.
