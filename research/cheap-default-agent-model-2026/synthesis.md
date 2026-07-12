---
type: synthesis
slug: cheap-default-agent-model-2026
topic: "Cheap default model for a coding-agent harness"
status: final
created: 2026-07-12
updated: 2026-07-12
confidence: medium
tags: [llm, coding-agent, model-routing, cost, fit]
---

# Synthesis

## The headline

The web can identify a strong **cheap default executor** and a sensible **escalation rule**, and can model the **cost** — all at **medium confidence** on performance. What the web **cannot** do is tell you whether that default is the right one *for your repos and task mix*. That is a fit question, and it is the headline limitation of this dossier, not a footnote. The experiment that would settle it is in `decision-guide.md`.

## Facts (high confidence)

- **DeepSeek V4-Flash** (`deepseek-v4-flash`) is the cheapest credible hosted coding-agent default as of mid-2026: **$0.14/M input (cache miss), $0.28/M output**, 1M context, 384K max output, native tool calling, JSON, and an **Anthropic-format endpoint** (`api.deepseek.com/anthropic`) that fits Claude-Code-style harnesses through LiteLLM. (Source: [[sources/deepseek-api-pricing]])
- The frontier workhorse baseline is **Claude Sonnet 5 at $3/$15** (SWE-bench Verified 0.852); the ceiling is Claude Opus 4.8 at $5/$25 (0.886) or GPT-5.5 at ~$5/$30 (0.887). (Sources: [[sources/llm-stats-leaderboards]], [[sources/devto-agentic-coding-2026]])
- DeepSeek V4-Flash is therefore **~21× cheaper on input and ~54× cheaper on output** than the Sonnet 5 baseline. (Source: [[sources/deepseek-api-pricing]])
- **MiniMax M3** (`MiniMax-M3`) is the strongest price-for-performance alternative: SWE-bench Verified **0.805** at ~$0.30/$1.20, with explicit OpenCode / Claude Code / Codex CLI integration. (Sources: [[sources/minimax-m3-page]], [[sources/llm-stats-leaderboards]]) — pricing medium-confidence (aggregator, confirm on platform.minimaxi.com).
- **GLM-5.2** is the open-weight long-horizon option: 1M context, MIT license, vendor-reported Terminal-Bench 2.1 81.0 (vs Claude Opus 4.8 85.0). Price unconfirmed; likely too expensive for the *cheap* slot. (Source: [[sources/openlm-glm-5.2]])
- Local inference is not viable: every credible candidate is a 284B–1.6T MoE; an RX 580 cannot host any of them. (Source: [[sources/openrouter-deepseek]])

## Performance estimates (medium confidence — vendor/aggregator/practitioner)

- DeepSeek V4-Flash sits around **~79% SWE-bench Verified** (vendor single-attempt, dev.to) / **0.790** (Flash-Max, llm-stats self-reported). Its Aider Polyglot proxy (V3.2-Exp Chat) is **70.2% for $0.88** across the full 225-task run — strong and cheap. (Sources: [[sources/devto-agentic-coding-2026]], [[sources/llm-stats-leaderboards]], [[sources/aider-leaderboard]])
- On the axis the user cares most about — **long, multi-file work in a real repository** — no public benchmark is a clean measurement. SWE-bench Verified is Python-only, mostly vendor-self-reported, and contamination-ridden enough that OpenAI stopped reporting it (per dev.to). Terminal-Bench 2.0 shows the **same model swinging 30–50 percentage points depending on the harness** (dev.to). Translation: benchmark ordering is a weak filter, and the harness (opencode/pi/Claude Code/Codex) will materially change the result. (Sources: [[sources/devto-agentic-coding-2026]], [[sources/aider-leaderboard]])
- Tool-calling reliability for V4-Flash is rated "Good — improving" (evolink, medium). Through aggregators, DeepSeek V3 tool-call error rates ranged **3.3%–11.75% depending on provider** — the hosting provider matters, not just the model. (Sources: [[sources/evolink-coding-agents-guide]], [[sources/openrouter-deepseek]])

## Inferences (medium confidence)

- For a model that runs on nearly every task, **price dominates**. At ~50× lower output cost than the frontier workhorse, DeepSeek V4-Flash can fail or retry several times per task and still cost less than one clean Sonnet 5 run. The math favors a cheap default + escalation, not a frontier-only loop.
- The biggest **non-price risk** for V4-Flash as a default is **availability / rate limits** (rated "High — variable availability"; production readiness "Medium — check status"). For a default executor, this must be mitigated with a fallback chain in LiteLLM. (Source: [[sources/evolink-coding-agents-guide]])
- The dominant community routing pattern (dev.to, multiple commenters) is **60–80% cheap, 20–40% frontier**, with escalation decided by a **cheap static heuristic (touches >N files, or a red test) rather than model self-assessment**. This is the escalation rule the user asked for, sourced from practitioners. (Source: [[sources/devto-agentic-coding-2026]])

## Unknowns (low confidence — the web cannot settle)

- **Whether DeepSeek V4-Flash (or MiniMax M3) is the right default for *your* repos.** No public benchmark measures your codebase, your task mix, your harnesses, your retry policy. This is a fit claim, ceiling low. The only resolution is the local evaluation in `decision-guide.md`.
- **Independent reproduction of V4-Flash's SWE-bench score.** Not found. Vendor/aggregator only.
- **MiniMax M3 confirmed per-token pricing.** Behind a login wall.

## Caveats

- All SWE-bench / Terminal-Bench numbers are vendor-self-reported or aggregator-collated; none independently reproduced for the cheap candidates in this dossier.
- Model and price landscape moves fast; every price is captured with source and access date (2026-07-12). Re-verify before configuring the proxy.
- The DeepSeek V4-Flash-Max price on llm-stats ($0.10/$0.20) differs from the official DeepSeek docs ($0.14/$0.28); treat the official figure as truth.
- This is a non-interactive run with no second opinion and no Gemini review (per user).

## How the research terminated

`Done` — every high-impact gap reached `resolved` or `blocked` (see [[open-questions]]). Four high-impact gaps, all `blocked`: three because the evidence does not exist in searchable sources (independent V4-Flash SWE-bench reproduction, V4-Flash tool-call reliability at volume, M3 official pricing behind a login) and one — the fit question — because it is **inherently unanswerable by web research** and is resolved by the proposed local evaluation, not by more searching. Two follow-up rounds were run; the last round surfaced no new high-impact gap. Budget consumed: 2 rounds, 21 queries, 8 sources kept, ~7 sources rejected.