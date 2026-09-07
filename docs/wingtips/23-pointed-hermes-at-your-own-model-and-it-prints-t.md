# Hermes Wingtips #23: pointed Hermes at your own model and it prints the tool call instead of running it?

posted 2026-07-17. original: [https://x.com/witcheer/status/2078094918740758606](https://x.com/witcheer/status/2078094918740758606)

Hermes Wingtips #23: pointed Hermes at your own model and it prints the tool call instead of running it?

if the reply comes back as raw json like {"name": "web_search", ...}, your inference server handed the tool call over as text and Hermes never got to run it.

tool calling has to be switched on at the server, and it is off until you set it:

(1) vLLM: add --enable-auto-tool-choice --tool-call-parser hermes

(2) SGLang: add --tool-call-parser qwen (or your model's parser)

(3) llama.cpp: add --jinja
