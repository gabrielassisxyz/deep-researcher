# Deep Researcher Agent Instructions

This repository defines OpenCode setups for two workflows:

- Deep research on current, source-backed topics.
- Documentation ingestion that turns a docs site into a focused MCP server.

The deep research workflow also has adapters for Claude Code, Codex, and Antigravity.

All generated files, comments, identifiers, prompts, and documentation in this repository must be written in English.

## Operating Rules

- Use `reference-repos/` only as local reference material. It is intentionally ignored by git.
- Prefer narrow, task-specific MCP access. Enable only the tools needed by the selected agent.
- Treat live data as time-sensitive. Verify current facts before reporting them.
- Keep research outputs source-backed. Every non-obvious claim should point to a source URL or a local captured artifact.
- Deep research output should be a focused Markdown dossier under `research/<topic-slug>/`, using local source notes, wikilinks, frontmatter, `evidence.md`, `open-questions.md`, and `log.md`.
- Do not store API keys in committed files. Use environment variables.

## Agent Selection

- Use `deep-research` for broad, current, multi-source research.
- Use `docs-to-mcp` for crawling a documentation site, normalizing the pages, and building a small MCP interface over the captured docs.
- Use `docs/agent-clis.md` when running the deep research workflow from Claude Code, Codex, or Antigravity.
