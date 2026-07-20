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
- Generated dossier files are hard-wrapped: the workflow breaks lines mid-sentence, so a one-word edit rewrites a whole paragraph and diffs between runs are unreadable. Dossiers are the tool's output and are meant to be read and revised, which makes this a correctness problem for the artifact rather than a formatting preference.
- There is no reading surface for a finished dossier — it is a directory of Markdown files read in whatever editor is at hand, which is a poor fit for a document built out of cross-referenced claims. A reading UI in the style of Andy Matuschak's notes (stacked, side-by-side panes that keep the source of a claim open next to the claim) would match the structure the workflow already produces.
- A dossier cannot be exported into an existing note system. There is no configuration for a destination vault, so the output stays inside this repo instead of landing where the reader's other notes live. An export target belongs in `.deep-research.conf` alongside the other per-installation choices.
- Paper-heavy research has no dedicated retrieval path: arXiv is reached through generic web search like any other source, so metadata (authors, versions, citations) that would sharpen the search ledger is discarded. Whether this is a first-class source adapter or an existing integration wired in is the open question.

## Deliberately out of scope

- Documentation ingestion (turning a docs site into an MCP server) — extracted into its own tool, [docs-to-mcp](https://github.com/gabrielassisxyz/docs-to-mcp).
- Hardcoded model or reviewer lists — the catalogue is always detected from the machine the tool runs on; what exists is a fact about the installation, not about this repository.
- Committed credentials or per-machine configuration — API keys come from environment variables, and choices live in the untracked `.deep-research.conf`.
- Resolving "fit" questions from web evidence — the workflow deliberately caps them at `low` confidence and answers with the local evaluation that would settle them.
