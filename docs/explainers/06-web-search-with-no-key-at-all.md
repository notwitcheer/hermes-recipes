# release explainer #6: web search with no key at all

posted 2026-09-07. original: [https://x.com/witcheer/status/2096902241777004650](https://x.com/witcheer/status/2096902241777004650)

a fresh install of Hermes Agent can search the web before you have added a single API key. 

here is what is happening behind that, and what your options are:

(1) the keyless tier

with no web credentials configured, web_search and web_extract rotate across the public free tiers of four search vendors: Exa, Parallel, Firecrawl and Keenable. if one of them throttles the request, Hermes retries on the next one in the ring.

(2) it is the last resort, not the default winner

any backend you configure or any API key you add takes over immediately. the keyless ring only answers when nothing else can.

(3) you can turn it off

`web.keyless_fallback: false` in config[.]yaml and Hermes never touches the anonymous endpoints.

(4) if you want guaranteed, unthrottled service, pick a door

with a Nous Portal subscription, web search and extract run through the Tool Gateway with managed Firecrawl, no key to manage (`hermes setup --portal` on a new install, or switch web on in `hermes tools` on an existing one). 
or add your own key for any vendor and pin it in `hermes tools`, where Exa, Parallel and Keenable each show a Free (keyless) and a Paid (API key) row.

https://hermes-agent.nousresearch.com/docs/user-guide/features/web-search
