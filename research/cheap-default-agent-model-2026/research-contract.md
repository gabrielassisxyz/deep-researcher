---
type: research-contract
slug: cheap-default-agent-model-2026
topic: "A cheap default model for a coding-agent harness"
status: active
created: 2026-07-12
updated: 2026-07-12
depth_budget_rounds: 6
depth_budget_sources: 40
tags: [llm, coding-agent, model-routing, cost, fit]
---

# Research Contract

## Research objective

Determine which cheap hosted LLM should be the **default executor** for a coding-agent
harness (opencode/pi/Claude Code/Codex via LiteLLM), and define the **escalation rule** at
which switching to a frontier model pays for itself. Produce a cost model at the user's
volume and an explicit statement of what web research cannot settle.

## Decision frame

Choose the cheapest model that is sufficient as a default executor for the bulk of agent
work; reserve frontier models for cases where evidence shows they materially improve
outcomes; define the escalation threshold by task difficulty, not habit.

## Target decisions / judgments

1. Default executor model + identifier.
2. Escalation rule (when to call a frontier model).
3. Cost model vs. frontier-only baseline, parametric in the user's daily token volume.

## Audience and intended use

Single developer running coding agents through opencode, pi, Claude Code, Codex against a
LiteLLM proxy. Output is read by that developer to configure the proxy's default route.

## Scope

- IN: hosted LLM APIs suitable as a coding-agent default (cheap tier), priced in USD per
  million tokens, with tool-calling support and context windows adequate for multi-file
  repo work. Aggregators/benchmarks that compare such models on coding/tool-calling/agent
  tasks. Open-weight models available via hosted APIs.
- OUT: local inference unless genuinely viable on a single RX 580 (expected: not viable).
  Pure vision/audio/specialty models. Enterprise/private deployments not reachable via a
  proxy. Detailed vendor sales motion.

## Key research questions

1. Which cheap hosted models are credible coding-agent defaults as of mid-2026 (the
   candidate set — must be **discovered**, not assumed)?
2. What are their exact identifiers, prices (input/output/cache), context windows, and
   tool-calling support?
3. What does independent evidence say about their performance on **multi-file repo work**
   and **agent/tool-calling loops** — not just one-shot benchmarks?
4. What independent benchmarks/leaderboards/evals cover coding-agent behavior (SWE-bench
   family, terminal-bench, agentic harness evals, Aider leaderboard, etc.)?
5. Which candidates get **rejected** and why (tool-calling gaps, context too small,
  unstable, too expensive for the default slot, etc.)?
6. What is a sensible **escalation rule** from cheap default to frontier, grounded in
  evidence about where cheap models fail?
7. What does the default cost per day at the user's volume vs. a frontier-only baseline?
8. What is the **fit question the web cannot answer**, and what local experiment would
   settle it?

## Comparison axes / evaluation criteria

- Price per million tokens (input, output, cache) — dominant.
- Long multi-file repo work quality (independent evidence preferred).
- Tool-calling reliability.
- Instruction adherence.
- Context window.
- Open weights (bonus).
- Availability through a standard OpenAI-compatible API (for LiteLLM).

## Evidence requirements and source priority

1. **Vendor official pages/docs** — primary for facts: existence, model IDs, pricing,
   context, tool-calling support. Ceiling `high` for facts; **cap `medium` for any
   performance/quality claim** (vendor is not a neutral witness about its own quality).
2. **Independent benchmarks/leaderboards** (SWE-bench Verified, Aider leaderboard,
   terminal-bench, agentic evals, Artificial Analysis, etc.) — primary for performance.
   Ceiling `medium` unless methodology is transparent and reproducible.
3. **Papers/repositories** — supporting.
4. **Aggregators/commentary** — context only, ceiling `medium`.
5. **Social/forum** — leads only, not high-confidence evidence.

**Fit claims** ("right for this user's repos/task mix") — ceiling `low` from web evidence
alone. Must be named as unanswerable with the local evaluation proposed.

## Coverage plan (decision-critical units of analysis — to be discovered)

- Each candidate model: identifier, vendor, price table, context, tool-calling, open
  weights, independent coding/agent evidence, caveats, practical implication,
  claim-level confidence.
- Each relevant benchmark family: what it measures, methodology transparency, recency,
  coverage of cheap models.
- The candidate set and the rejected set, with reasons.

Minimum coverage per candidate: identifier, price (input/output), context window,
tool-calling support, at least one independent coding/agent signal, and a stated
rejection-or-keep reason.

## Expected artifacts

- `README.md`, `intake.md`, `research-contract.md`, `methodology.md`, `evidence.md`,
  `open-questions.md`, `log.md`.
- `synthesis.md` with facts/estimates/inferences/unknowns separated.
- `decision-guide.md` with decision matrix, sufficient-cheaper-option analysis,
  frontier-required analysis, escalation rules, and the **required local evaluation**.
- `sources/*.md` per major source.
- `models/*.md` for candidates that warrant a standalone note; others in a comparison
  table.

## Success criteria

- Discovered candidate set includes models the user did **not** name (the prompt names
  none, so any model is discovered — but the set must come from search, not memory).
- Search ledger in `log.md` non-empty, with fruitless queries logged.
- Every high-impact gap reaches `resolved` or `blocked`; no `partially resolved`.
- No vendor source carrying a performance claim at `high` confidence.
- Fit question named as unanswerable, with a concrete proposed local evaluation.
- Cost model is parametric and names its frontier baseline.
- Decision guide gives a default executor + escalation rule with stated confidence.

## Assumptions

- See `intake.md` Assumptions: ~5–15M tokens/day heavy individual developer; frontier
  baseline ~$3–15/M input, ~$15–75/M output; USD per-million-token pricing; date
  2026-07-12; cache/batch discounts noted but not assumed by default.

## Risks, ambiguities, terms needing definition

- "Cheap" is relative. Operationalize as: a model whose per-day cost at the user's volume
  is a small fraction (e.g. <10–20%) of a frontier-only baseline.
- "Frontier model" must be pinned to a specific reference for the cost model.
- Benchmark numbers do not equal multi-file repo performance — treat as weak signal.
- Model naming is volatile; capture exact identifiers and dates.
- "Tool calling" support exists on a spectrum (native vs. prompted vs. unreliable) —
  capture independent reports, not just vendor claims.

## External review settings

- Second opinion: **disabled**.
- Gemini review: **disabled**.

## Output directory

`research/cheap-default-agent-model-2026/`