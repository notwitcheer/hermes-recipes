# Hermes Wingtips #26: every web page your agent reads costs a main-model call

posted 2026-07-21. original: [https://x.com/witcheer/status/2079595063534145708](https://x.com/witcheer/status/2079595063534145708)

Hermes Wingtips #26: every web page your agent reads costs a main-model call 

web_extract is the tool Hermes agent uses to read web pages. by default the summariser that processes long pages reuses your main chat model. 

it means that on every docs page, article, thread... the agent opens burns a full-price call to whatever model you're chatting with. 

(1) route the summariser to a cheap model:

```
auxiliary:
  web_extract:
    provider: nous
    model: google/gemini-3-flash-preview
```
or pick it interactively: hermes model → configure auxiliary models → web_extract.  

(2) if you need raw unsummarised content later, use browser_navigate & browser_snapshot instead. 

the browser tool returns a live page without auxiliary-model rewriting.
