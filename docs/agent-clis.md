# Agent CLI Workflows

This project supports the same deep research dossier workflow from OpenCode, Claude Code, Codex, and Antigravity.

The canonical workflow lives in `opencode/prompts/deep-research.md`. Agent-specific wrappers should point to that file instead of reimplementing the research contract.

Interactive runs ask at the very beginning whether to add an external Gemini review loop through `agy`, and if yes, how many loops to allow. A normal deep-research run should usually use 1 loop; high-stakes research can use 2. The configured hard cap is 3 loops unless explicitly overridden.

## Golden Test Prompt

Use `prompts/examples/llm-models-golden.md` to repeat the LLM model research test across agents.

## OpenCode

```sh
opencode run --agent deep-research "$(cat prompts/examples/llm-models-golden.md)"
```

## Claude Code

Claude Code can use the project slash command:

```text
/deep-research Research the latest public LLM benchmark results. Save the dossier in research/llm-models-claude.
```

Or run through the helper script:

```sh
scripts/deep-research-claude "$(cat prompts/examples/llm-models-golden.md)"
```

Claude Code reads project-scoped MCP servers from `.mcp.json`. The Firecrawl server reads
`FIRECRAWL_API_URL` from the environment — self-hosted or hosted, whichever `scripts/setup`
recorded.

## Codex

Codex does not have project-local named agents in the same way OpenCode does. In this repository, `deep-research` is exposed to Codex as a prompt/skill-style workflow plus a helper script, not as `codex --agent deep-research`. If your Codex build lists `deep-research` as a skill, that is expected; it is the workflow instruction surface, while MCP access and execution permissions still come from Codex configuration and CLI flags.

Run through the helper script:

```sh
scripts/deep-research-codex "$(cat prompts/examples/llm-models-golden.md)"
```

Codex MCP configuration is user-level. If Firecrawl is not already configured, add it once:

```sh
codex mcp add firecrawl \
  --env FIRECRAWL_API_URL=http://localhost:3002 \
  --env FIRECRAWL_API_KEY="${FIRECRAWL_API_KEY:-}" \
  -- npx -y firecrawl-mcp
```

Check:

```sh
codex mcp list
```

## Antigravity

Antigravity discovers project-local skills under `.agents/skills/`. The deep research skill is available at `.agents/skills/deep-research/SKILL.md`.

Natural-language invocation:

```text
Use the deep-research skill. Research the latest public LLM benchmark results. Save the dossier in research/llm-models-agy.
```

CLI helper:

```sh
scripts/deep-research-agy "$(cat prompts/examples/llm-models-golden.md)"
```

Review an existing dossier with Antigravity:

```sh
scripts/deep-research-agy-review research/llm-models-agy 1
```

Project-scoped Firecrawl MCP configuration is in `.gemini/settings.json`.

## Output Check

After any run, inspect the dossier:

```sh
find research/llm-models-v2 -maxdepth 2 -type f | sort
```

Minimum expected files:

- `README.md`
- `intake.md`
- `research-contract.md`
- `synthesis.md`
- `methodology.md`
- `evidence.md`
- `open-questions.md`
- `log.md`
- `sources/`

Domain folders such as `models/`, `benchmarks/`, `vendors/`, or `papers/` are optional and should be created only when useful for the topic.

If Gemini review is enabled, expect a `review/` folder with the prompt, review report, and fix report for each completed loop.
