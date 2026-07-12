---
type: research
slug: cheap-default-agent-model-2026
topic: "A cheap default model for a coding-agent harness (opencode/pi/Claude Code/Codex via LiteLLM)"
status: final
created: 2026-07-12
updated: 2026-07-12
freshness_requirement: "Model and price landscape moves monthly; re-verify prices against vendor docs before configuring the proxy. Re-run the local evaluation quarterly."
confidence: medium
source_count: 8
tags: [llm, coding-agent, model-routing, cost, fit]
---

# A Cheap Default Model for My Agent Harness

## What this is

A source-backed research dossier answering: **which cheap hosted LLM should be the default executor for a coding-agent harness (opencode, pi, Claude Code, Codex via LiteLLM), and at what point is escalating to a frontier model paying for itself?** It also names, explicitly, what web research **cannot** answer.

## TL;DR (read [[synthesis]] and [[decision-guide]] for the sourced version)

- **Discovered default:** `deepseek-v4-flash` — $0.14/$0.28 per M (in/out), 1M context, native tool calling, Anthropic-format endpoint for Claude Code. ~30× cheaper than Claude Sonnet 5 for the same task shape.
- **Fallback / cheap secondary:** `minimax-m3` (SWE-bench 0.805, explicit OpenCode/Claude-Code/Codex support, different provider family).
- **Escalation:** → `claude-sonnet-5` ($3/$15) → `claude-opus-4.8`/`gpt-5.5` for the hard 20%. Rule: static heuristic (touches >8 files or red test), or 3 retries failed, or architecturally ambiguous.
- **Cost:** at 10M in / 1M out per day, an 80% V4-Flash / 20% Sonnet 5 blend costs ~$10/day vs ~$45/day frontier-only — a ~$1,040/month saving.
- **What the web can't settle:** whether V4-Flash is the right default **for your repos**. That is a fit question. The experiment to settle it is in [[decision-guide]].

## How to audit this dossier

- **Search ledger:** [[log]] — 21 queries, including the fruitless ones. The candidate set was **discovered**, not assumed (the prompt names zero models).
- **Evidence:** [[evidence]] — claim-level, with claim type (Fact/Performance/Fit) and confidence ceiling.
- **Gaps:** [[open-questions]] — every high-impact gap is `resolved` or `blocked`; none `partially resolved`.
- **Method:** [[methodology]] — source tiers, claim typing, benchmark interpretation.
- **Sources:** `sources/` — 8 source notes, each with frontmatter and confidence.
- **Candidate notes:** `models/` — DeepSeek V4-Flash, MiniMax M3, GLM-5.2, and the **rejected candidates** with reasons (the user asked to see what didn't make the cut).

## Key caveats

1. **All SWE-bench / Terminal-Bench numbers are vendor-self-reported or aggregator-collated**; none independently reproduced for the cheap candidates. Performance confidence is `medium`, not `high`. No vendor source carries a performance claim at `high`.
2. **The harness matters as much as the model.** On Terminal-Bench 2.0, the same model swings 30–50pp by harness (dev.to). Your results in opencode/pi/Claude Code/Codex will differ from benchmark ordering.
3. **DeepSeek V4-Flash availability is the main non-price risk** (rated "High — variable availability"). Mitigate with the LiteLLM fallback chain.
4. **MiniMax M3 pricing is aggregator-sourced** — confirm on `platform.minimaxi.com` before committing.
5. **Local inference is not viable** on an RX 580 for any credible candidate.
6. Non-interactive run: **no second opinion, no Gemini review** (per user).

## How the research terminated

`Done` — 2 rounds, 21 queries, 8 sources kept. All four high-impact gaps `blocked`: three because the evidence doesn't exist in searchable sources, one (the fit question) because it is inherently unanswerable by web research and is resolved by the proposed local evaluation. The last round surfaced no new high-impact gap. See [[log]].