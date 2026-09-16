# Hermes Autopilot #5: write the AGENTS.md for this repo

posted 2026-09-16. original: [https://x.com/witcheer/status/2100223649026314532](https://x.com/witcheer/status/2100223649026314532)

your Hermes Agent can brief itself on your project before every session. this prompt writes the file that does it. paste it into a chat opened in the repo: it reads the README, the build files and the recent commits, asks you what the repo could not tell it, and drafts the AGENTS.md that Hermes loads at the start of every session in that folder. you see the whole file before it is saved, and Hermes asks once more before it writes an AGENTS.md, that file is protected by default.

paste this into a Hermes Agent chat opened in the repository:

```
<role>
You are my Hermes Agent. Write the AGENTS.md for the repository we are in, so that every future session starts knowing how this project works. Ask, do not assume.
</role>

<principles>
<principle name="Read before you write">
Read the README, the build and test files, the folder layout and the recent commits before you draft a line. If the repo does not answer a question, ask me instead of guessing.
</principle>
<principle name="Under sixty lines">
The file stays under sixty lines: what the project is, how to run and test it, the conventions you found, and what must never be touched. Plain sentences, one level of headings.
</principle>
<principle name="Show before you save">
Show me the whole draft and wait. Save AGENTS.md only after I say yes. If you cannot get my answer, end your turn and save nothing.
</principle>
</principles>

<instructions>
1. List the files you read, one line each, with the one thing each file taught you.
2. Ask me the questions the repo could not answer, three at most.
3. Draft AGENTS.md from what you read and what I answered. Show me the whole file. Then stop and wait for my yes.
4. After my yes, save it at the root of the repository.
</instructions>

<task>
Start with step one now.
</task>
```
