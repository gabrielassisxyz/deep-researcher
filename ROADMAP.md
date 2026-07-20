# Roadmap

## What exists today

- The deep-research workflow itself (`opencode/prompts/deep-research.md`, the single canonical prompt): search-first discovery, a search ledger that logs every query including the empty ones, a gap loop with only terminal states (`resolved` / `blocked`), claim typing with confidence ceilings, and a depth budget the run must report when exhausted.
- Harness adapters for OpenCode, Claude Code, Codex, pi, and Antigravity (`scripts/deep-research-*`) — thin wrappers over the one canonical prompt, never reimplementations of it.
- Two external checks: a second opinion (one model re-researches blind, attacking omission) and a review panel (N models critique the dossier, attacking error), with consensus computed by `scripts/consensus.py` rather than asked for.
- First-run configuration: `scripts/setup` detects installed agent CLIs and LiteLLM models, offers a self-hosted Firecrawl (`infra/firecrawl/`), and records choices in `.deep-research.conf`; `scripts/detect-reviewers` reports the reviewer catalogue.
- A dossier template (`research/_template/`), golden test prompts (`prompts/examples/`), and worked example dossiers including one where the panel caught the run's own wrong headline.
- Deterministic gates: gitleaks, shellcheck, and the consensus test suite, runnable locally via `bin/ci` and in CI (`.github/workflows/ci.yml`).

## Missing / natural next steps

- Automated tests cover only `scripts/consensus.py`; the bash pipeline (`review-panel`, `setup`, `detect-reviewers`) is linted but not behaviour-tested.
- The golden prompts exist to repeat the same research across harnesses, but comparing the resulting dossiers is manual — no automated cross-harness conformance check.
- The minimum-expected-files check for a finished dossier (`docs/agent-clis.md`) is a manual `find`; it could be a script that validates a dossier's shape.

## Deliberately out of scope

- Documentation ingestion (turning a docs site into an MCP server) — extracted into its own tool, [docs-to-mcp](https://github.com/gabrielassisxyz/docs-to-mcp).
- Hardcoded model or reviewer lists — the catalogue is always detected from the machine the tool runs on; what exists is a fact about the installation, not about this repository.
- Committed credentials or per-machine configuration — API keys come from environment variables, and choices live in the untracked `.deep-research.conf`.
- Resolving "fit" questions from web evidence — the workflow deliberately caps them at `low` confidence and answers with the local evaluation that would settle them.
