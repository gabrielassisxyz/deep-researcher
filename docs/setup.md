# OpenCode Setup

This repository provides two OpenCode agents:

- `deep-research`: current, source-backed research using Firecrawl and Context7.

The same deep research workflow is also available for Claude Code, Codex, and Antigravity. See `docs/agent-clis.md`.

## Environment

Copy the variables from `.env.example` into your shell or local environment manager.

`FIRECRAWL_API_KEY` is recommended for full Firecrawl MCP access. `CONTEXT7_API_KEY` is optional but improves Context7 limits.

## MCPs

The root `opencode.jsonc` configures:

- `firecrawl` as a local MCP launched through `npx -y firecrawl-mcp`, pointing at whatever `FIRECRAWL_API_URL` names — your own instance (`scripts/install-firecrawl`) or the hosted API at firecrawl.dev. `scripts/setup` asks which you want and writes it down.
- `context7` as a remote MCP at `https://mcp.context7.com/mcp`.

Both MCPs are disabled globally through tool globs and enabled only for the two custom agents.

## Usage

Run deep research:

```sh
opencode run --agent deep-research "Research the latest public LLM benchmark results for frontier coding models. Save the dossier in research/llm-models."
```

Run the golden LLM model research test:

```sh
opencode run --agent deep-research "$(cat prompts/examples/llm-models-golden.md)"
```

The `deep-research` agent is intentionally slow. Its prompt requires a research brief, discovery pass, evidence extraction, gap analysis, targeted follow-up, synthesis, adversarial audit, and optional Gemini review loop before the final answer. Its primary output is a Markdown dossier under `research/<topic-slug>/`, not a chat-only answer.

At the start of an interactive run, the workflow asks whether to add an external Gemini review loop through `agy`. Use one review loop for normal research and two loops for higher-stakes research. The loop stops early when Gemini finds no actionable issues.

Expected research output:

```text
research/<topic-slug>/
  README.md
  intake.md
  research-contract.md
  synthesis.md
  methodology.md
  evidence.md
  open-questions.md
  log.md
  sources/
```

Domain-specific research may add focused folders such as `models/`, `benchmarks/`, `entities/`, or `concepts/`. See `research/_template/` for the canonical shape.

Domain folders are optional. The required core is the dossier root files plus `sources/`; add folders such as `models/`, `products/`, `vendors/`, `papers/`, `datasets/`, or `benchmarks/` only when they make the research easier to audit.

If Gemini review is enabled, review reports are saved under:

```text
research/<topic-slug>/review/
  agy-review-prompt-round-1.md
  agy-review-round-1.md
  agy-review-fixes-round-1.md
```

Use the phrase `quick mode` in the user request only when a short web-research answer is enough and a dossier is not needed.

Check configured MCPs:

```sh
opencode mcp list
```

Inspect a completed research dossier:

```sh
find research/llm-models -maxdepth 2 -type f | sort
```
