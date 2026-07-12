---
type: open-questions
slug: cheap-default-agent-model-2026
topic: "Cheap default model for a coding-agent harness"
created: 2026-07-12
updated: 2026-07-12
---

# Open Questions (Gap Analysis)

Every high-impact gap is resolved or blocked. No gap is left in "partially resolved."

## High-impact gaps

| # | Gap | Impact | Status | Resolution / block |
| --- | --- | --- | --- | --- |
| H1 | DeepSeek V4-Flash SWE-bench score independently reproduced (not vendor self-report) | high | **blocked** | Only aggregator (llm-stats, self-reported) and a dev.to blog citing "~79% vendor single-attempt." No independent reproduction found. Targeted searches ("SWE-bench Verified independent reproduction", "DeepSeek V4 Flash... review") returned only the vendor homepage or junk (SWE = Society of Women Engineers). OpenAI's own withdrawal from SWE-bench (per dev.to) makes the gap worse for *all* models, not just DeepSeek. Block is: absence of independent reproduction in searchable sources, not a tool failure. Settled by the local evaluation in `decision-guide.md`. |
| H2 | DeepSeek V4-Flash tool-calling reliability in real agent loops at volume | high | **blocked** | No controlled, independent tool-call reliability measurement for V4-Flash exists in searchable sources. evolink rates it "Good — improving" (medium, vendor-blog). OpenRouter's tool-call error rate (3.3–11.75% across providers) is measured on V3, not V4. Targeted queries returned only the DeepSeek homepage. Block is: absence of measured V4-Flash tool-call data; only proxy (V3) and practitioner ratings. Settled by the local eval. |
| H3 | MiniMax M3 official pricing (not aggregator) | high | **blocked** | Pricing lives on `platform.minimaxi.com/subscribe/token-plan` (a login-gated subscription page); the public model page does not list per-token prices. Only the llm-stats aggregator ($0.30/$1.20) was found. Block is: login-gated pricing page, not reachable by scrape. **Action for user:** log in to platform.minimaxi.com and confirm before committing. |
| H4 | Which model is right **for this user's** repos/task mix/harnesses | high | **blocked (inherently unanswerable by web research)** | This is the fit question. The web cannot settle it. Named explicitly in synthesis and decision-guide; the local evaluation is the only resolution. |

## Medium-impact gaps

| # | Gap | Impact | Status |
| --- | --- | --- | --- |
| M1 | DeepSeek V4-Flash-Max price discrepancy ($0.10/$0.20 on llm-stats vs $0.14/$0.28 official) | medium | **blocked** — llm-stats may list a promo or a different sub-variant ("Flash-Max" vs "Flash"). Official DeepSeek docs are the source of truth; treat $0.14/$0.28 as the confirmed price. |
| M2 | GLM-5.2 API pricing | medium | **blocked** — not on the openlm page; GLM-5 proxy is $1.00/$3.20. |
| M3 | Terminal-Bench 2.1 independent leaderboard (full, not vendor claims) | medium | **blocked** — searches for "Terminal-Bench 2.1 leaderboard" returned only Windows Terminal / generic results; tbench.ai was referenced by dev.to but not scraped. Vendor numbers (GLM-5.2 81.0) used with medium cap. |
| M4 | MiniMax M3 independent agent-loop validation (not vendor demos) | medium | **blocked** — only vendor demos (ICLR reproduction, CUDA optimization) found; no independent report. |

## Low-impact gaps

| # | Gap | Impact | Status |
| --- | --- | --- | --- |
| L1 | Whether DeepSeek's Anthropic-format endpoint works cleanly with Claude Code via LiteLLM | low | **blocked** — documented as existing on official docs; no independent verification of Claude Code compatibility found. |
| L2 | Exact RX 580 VRAM (8GB vs other) | low | **blocked** — assumed 8GB; user can correct. Doesn't change the conclusion (no candidate fits). |

## What this means for synthesis

The dossier can recommend a default executor **at medium confidence** (facts high, performance medium, fit blocked). The recommendation is contingent on the local evaluation in `decision-guide.md`. No claim is made that the web settles the fit question.