# Hermes Wingtips #29: local models context floor

posted 2026-07-24. original: [https://x.com/witcheer/status/2080682763594899763](https://x.com/witcheer/status/2080682763594899763)

Hermes Wingtips #29: local models context floor

you point Hermes Agent at Ollama, the first few turns are fine, then the agent starts forgetting instructions or repeating work. 

the usual cause is that Ollama's default context depends on your VRAM, and under 24 GB it is 4,096 tokens. Hermes needs at least 64,000 for agent work, because the system prompt and tool schemas alone take 4k to 8k, and most servers drop your oldest messages once the window fills.

here is what to do server-side:

(1) Ollama: `OLLAMA_CONTEXT_LENGTH=64000 ollama serve`, then check the CONTEXT column in ollama ps

(2) vLLM: `--max-model-len 64000`

(3) llama.cpp: `llama-server -m model.gguf -c 64000`

LM Studio users can skip this since Hermes asks it to load the model at 64K by default.
