# Hermes Wingtips #4: which file is your agent's brain

posted 2026-06-23. original: [https://x.com/witcheer/status/2069385776756895880](https://x.com/witcheer/status/2069385776756895880)

Hermes Wingtips #4: which file is your agent's brain

~ SOUL.md is who the agent is: slot #1 in the system prompt, it replaces the default identity. 

~ USER.md is who you are. 

~ MEMORY.md is the facts it keeps about your work. 

~ AGENTS.md is your project's rules, found by walking the directory.

~~~
what you need to understand is that project rule files are first-match-wins. 
Hermes loads only one of .hermes.md, AGENTS.md, CLAUDE.md, .cursorrules, in that order. 

a .hermes.md in the repo shadows your AGENTS.md with no warning, and the rules you wrote never load.

SOUL.md is exempt, it always loads on its own from ~/.hermes/SOUL.md. 

if Hermes is ignoring your project instructions, check for a higher-priority file next to them. and it caps every one of these at 20,000 characters, then truncates the rest.
