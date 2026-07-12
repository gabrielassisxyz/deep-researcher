---
type: methodology
slug: cheap-default-agent-model-2026
topic: "Cheap default model for a coding-agent harness"
created: 2026-07-12
updated: 2026-07-12
---

# Methodology

## Search strategy

Discovery used Firecrawl `search` (the only search tool available in this harness — `mcp_firecrawl_firecrawl_search`) before any scrape. 21 queries issued across two rounds; every query logged in `log.md` including the fruitless ones. No source entered the dossier without a logged query or a citation trail from another source.

Query phrasings were deliberately varied from the user's words to surface models the user did not name. The candidate set was **discovered**, not assumed: the prompt names zero models, and the final shortlist is drawn from SWE-bench Verified and Aider-Polyglot leaderboards (llm-stats), Aider's official board, and practitioner commentary (dev.to, evolink).

## Source tiers

1. **Official vendor docs/pages** — primary for facts (existence, id, price, context, tool-calling support). Ceiling `high` for facts; **cap `medium` for any performance claim** because a vendor is not a neutral witness about its own quality.
2. **Independent benchmarks** — Aider Polyglot (independent methodology, small N). Medium confidence.
3. **Aggregators** — llm-stats.com (collates self-reported scores), OpenRouter (real provider pricing + tool-call error rates). Medium, used for discovery and cross-check.
4. **Practitioner commentary** — dev.to, evolink. Medium for real-world agent behavior and routing patterns; low for any specific performance number.
5. **Social (Reddit)** — cited only as leads inside the dev.to source; never used as high-confidence evidence.

## Benchmark interpretation

- **SWE-bench Verified**: 500 human-verified GitHub issues, patches to Python repos. The most-cited coding-agent benchmark, but: (a) scores are mostly vendor-self-reported (llm-stats marks 0 verified); (b) contamination is a known issue — OpenAI stopped reporting it early 2026 (per dev.to); (c) it tests Python repo patching, not the user's multi-language, multi-file repo work. Treat as a **weak ordering signal**, not a quality verdict.
- **Aider Polyglot**: 225 Exercism exercises across 6 languages, two attempts with feedback. Independent and closer to agent editing behavior, but small N and the two-attempt protocol inflates pass rates. DeepSeek V4-Flash not yet on this board; V3.2-Exp proxies it.
- **Terminal-Bench 2.0/2.1**: the long-horizon terminal-agent benchmark most relevant to the user's "long, multi-file work" axis. Vendor-reported numbers only (GLM-5.2, Claude Opus 4.8). The dev.to claim that "the same model swings 30–50pp by harness" is the key caveat: on this benchmark, **the harness matters as much as the model**.

## Claim typing applied

- **Facts** (DeepSeek V4-Flash price $0.14/$0.28, 1M context, tool calling ✓) — `high`, from official docs.
- **Performance** (DeepSeek V4-Flash ~79% SWE-bench; MiniMax M3 0.805; tool-call reliability "Good — improving") — `medium`, from aggregator + commentary; vendor performance claims capped at medium.
- **Fit** ("is V4-Flash the right default for this user?") — `low` ceiling; named as unanswerable, with a proposed local evaluation in `decision-guide.md`.

## Cost model approach

The user's daily volume is unknown; the cost model in `decision-guide.md` is **parametric** (a table over daily input/output token volumes). The frontier baseline is pinned to Claude Sonnet 5 at $3/$15 (the "workhorse frontier" price point the user would plausibly use frontier-only). Cache-hit and batch discounts are noted but not assumed; DeepSeek's cache-hit price ($0.0028/M) is shown as a best-case.

## What was not done

- No local inference viability analysis beyond noting the RX 580 cannot run a 284B+ MoE model (the cheapest credible hosted candidate is itself a 284B/13B-active MoE — far beyond an RX 580's ~8GB VRAM). Local inference is not viable for any candidate in the shortlist.
- No second opinion, no Gemini review (non-interactive run, per user).