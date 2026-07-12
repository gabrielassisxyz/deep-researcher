# Deep Researcher Agent Instructions

This repository defines a deep-research workflow: source-backed research on current
topics, producing an auditable Markdown dossier. It runs under OpenCode, and has adapters
for Claude Code, Codex, pi, and Antigravity.

(Documentation ingestion — turning a docs site into an MCP server — used to live here and
is now its own tool: https://github.com/gabrielassisxyz/docs-to-mcp)

All generated files, comments, identifiers, prompts, and documentation in this repository must be written in English.

## Operating Rules

- Prefer narrow, task-specific MCP access. Enable only the tools needed by the selected agent.
- Treat live data as time-sensitive. Verify current facts before reporting them.
- Keep research outputs source-backed. Every non-obvious claim should point to a source URL or a local captured artifact.
- Deep research output should be a focused Markdown dossier under `research/<topic-slug>/`, using local source notes, wikilinks, frontmatter, `evidence.md`, `open-questions.md`, and `log.md`.
- Do not store API keys in committed files. Use environment variables.

## Agent Selection

- Use `deep-research` for broad, current, multi-source research.
- Use `docs/agent-clis.md` when running the deep research workflow from Claude Code, Codex, or Antigravity.
