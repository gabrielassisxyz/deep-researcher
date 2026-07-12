---
type: decision-guide
slug: cheap-default-agent-model-2026
topic: "Cheap default model for a coding-agent harness"
status: final
created: 2026-07-12
updated: 2026-07-12
confidence: medium
tags: [llm, coding-agent, model-routing, cost, fit]
---

# Decision Guide

## Decision frame

From [[intake]]: choose the **cheapest model that is sufficient as a default executor** for the bulk of agent work; reserve frontier models for cases where evidence shows they materially improve outcomes; define the escalation threshold by task difficulty, not habit.

## Recommendation (medium confidence on facts/performance; low on fit)

> **Default executor: `deepseek-v4-flash`** (DeepSeek's own API, `api.deepseek.com`, with the Anthropic-format endpoint `api.deepseek.com/anthropic` for Claude-Code-style harnesses through LiteLLM).
>
> **Escalation target: `claude-sonnet-5` ($3/$15)** as the workhorse frontier, with `claude-opus-4.8` ($5/$25) or `gpt-5.5` (~$5/$30) for the genuinely hard 5%.
>
> **Fallback chain (in LiteLLM):** `deepseek-v4-flash` → `minimax-m3` (cheap secondary, different family/provider) → `claude-sonnet-5` (frontier).
>
> **In-family reasoning escalation:** `deepseek-v4-flash` → `deepseek-v4-pro` ($0.435/$0.87 promo, then $1.74/$3.48) when a task needs DeepSeek-style reasoning but not a frontier model.

**Why DeepSeek V4-Flash over MiniMax M3 as the *default*:** V4-Flash is ~3× cheaper on input and ~4× cheaper on output at confirmed official pricing, has a native Anthropic-format endpoint (good for Claude Code), and the Aider proxy (V3.2-Exp) gives it independent coding-editing evidence. **Why keep MiniMax M3 as the cheap fallback:** it has a higher SWE-bench score (0.805 vs 0.790), explicit OpenCode/Claude-Code/Codex integration, and a different provider family — so a DeepSeek outage or rate limit doesn't take down the cheap tier. (Sources: [[sources/deepseek-api-pricing]], [[sources/minimax-m3-page]], [[sources/llm-stats-leaderboards]])

**Confidence:** facts `high`; performance `medium`; the *fit* of this default for the user's repos is `low` and **must be validated by the local evaluation below before it hardens into habit.**

## Task taxonomy and decision matrix

| Task class | Model | Why |
| --- | --- | --- |
| Routine edits, boilerplate, read-heavy repo navigation, single-file changes | `deepseek-v4-flash` | Price dominates; ~79% SWE-bench is plenty; 1M context handles repo reads. |
| Multi-file refactors, cross-module changes, new features in known territory | `deepseek-v4-flash` first; escalate on failure/heuristic | Cheap enough to retry 3–5× and still beat one Sonnet run. |
| Genuinely hard: ambiguous spec, architectural decision, debugging a subtle concurrency bug, security-sensitive changes | Escalate to `claude-sonnet-5` (or `opus-4.8`/`gpt-5.5`) | Frontier quality materially improves outcomes here; this is where the 20–40% goes. |
| Big-context / whole-repo analysis (>200K input) | `gemini-3.1-pro` or `glm-5.2` | 1M context; but watch Gemini's tiered pricing above 200K. |
| Long-horizon autonomous runs (hours, thousands of tool calls) | `minimax-m3` or `glm-5.2` (long-horizon positioning) | Vendor demos (M3: 12h ICLR reproduction; GLM-5.2: T-Bench 2.1 81.0) suggest these are tuned for stamina. Medium confidence. |

## Sufficient-cheaper-option analysis

A model that is "3% better and 10× the price is a bad default" (user). Concretely, for a **multi-file refactor (100K input, 20K output)**:

| Model | Cost | SWE-bench Verified |
| --- | --- | --- |
| Claude Sonnet 5 | $0.60 | 0.852 |
| Claude Opus 4.8 | $0.60 → $0.80 | 0.886 |
| GPT-5.5 | ~$0.80 (at $5/$30) | 0.887 |
| **DeepSeek V4-Flash** | **$0.020** | ~0.79 |
| MiniMax M3 | ~$0.027 | 0.805 |

V4-Flash is **~30× cheaper** than Sonnet 5 for this task shape. Even if it fails and retries **5×**, total cost ($0.10) is still **6× cheaper** than a single Sonnet run. The "sufficient cheaper option" bar is comfortably cleared *on benchmark ordering*. The open question is whether it is sufficient **on the user's actual tasks** — see the local evaluation.

## Frontier-required analysis

When is escalating to a frontier model actually paying for itself? Evidence-backed triggers:

1. **Ambiguity / spec-formation.** The task is "design X" not "implement X." Frontier models (Opus 4.8, GPT-5.5) are materially better at judgment under ambiguity. (Source: [[sources/devto-agentic-coding-2026]])
2. **Subtle bugs.** Concurrency, memory model, distributed-systems correctness. Practitioners escalate here (dev.to: "payment settlement logic and idempotency guards" → Opus).
3. **The cheap model has already failed.** Retry budget exhausted (suggested: 3 retries on the cheap default), or the cheap model produced a diff that fails tests it can't diagnose.
4. **Static heuristic fires.** Task touches >N files (try N=8 as a starting point) OR involves a currently-red test. This beats model self-assessment of difficulty (dev.to commenter). (Source: [[sources/devto-agentic-coding-2026]])
5. **Safety/compliance-sensitive.** Anything where a confident-but-wrong change is expensive. Frontier models have better calibration (dev.to: "right 95% and knows when it's unsure > right 98% and confidently ships the other 2%").

**When escalation is NOT paying for itself:** routine CRUD, boilerplate, doc generation, single-file edits, read-heavy exploration. These are the bulk of the volume; keeping them on V4-Flash is where the savings come from.

## Escalation rule (concrete)

```
For each task:
  1. Start on deepseek-v4-flash.
  2. If static heuristic fires (touches >8 files OR red test involved) → skip to claude-sonnet-5.
  3. If V4-Flash fails 3 retries (failed tool calls, tests still red, malformed diffs) → claude-sonnet-5.
  4. If Sonnet 5 fails 2 retries OR task is architecturally ambiguous → claude-opus-4.8 (or gpt-5.5).
  5. DeepSeek outage/rate-limit → LiteLLM falls back to minimax-m3 → claude-sonnet-5.
```

Tune the `>8 files` threshold and retry counts from the local evaluation's results.

## Cost model (parametric — plug in your real volume)

The user's daily volume is unknown. Below: daily cost = (input_tokens/1M × in_price) + (output_tokens/1M × out_price), assuming a heavy individual developer. Adjust the input/output split to your real telemetry. Frontier baseline = Claude Sonnet 5 ($3/$15).

### Scenario: 10M input / 1M output per day

| Model | In cost | Out cost | Daily | Monthly (30d) |
| --- | --- | --- | --- | --- |
| Claude Sonnet 5 (frontier-only baseline) | $30.00 | $15.00 | $45.00 | $1,350 |
| Claude Opus 4.8 (frontier ceiling) | $50.00 | $25.00 | $75.00 | $2,250 |
| **DeepSeek V4-Flash (cheap default, 100%)** | $1.40 | $0.28 | **$1.68** | **$50.40** |
| MiniMax M3 (100%) | $3.00 | $1.20 | $4.20 | $126.00 |
| **Blend: 80% V4-Flash + 20% Sonnet 5** | — | — | **$10.34** | **$310.20** |

The blend (80% cheap / 20% frontier) costs **~23% of the frontier-only baseline** at this volume — a ~$1,040/month saving — while preserving frontier quality for the hard 20%.

### Scenario: 5M input / 0.5M output per day

| Model | Daily | Monthly |
| --- | --- | --- |
| Sonnet 5 baseline | $22.50 | $675 |
| V4-Flash 100% | $0.84 | $25.20 |
| 80/20 blend | $5.17 | $155.10 |

### Cache-hit upside (best case)

DeepSeek V4-Flash cache-hit input is **$0.0028/M** (vs $0.14 miss). In a coding-agent loop with heavy repo re-reads, cache hit rate can be 60–80% (per OpenRouter's note on effective pricing). At 70% cache hit on 10M input: input cost drops from $1.40 to ~$0.43, daily total ~$0.71. **Treat this as a best-case upside, not the plan.**

### What the cost model does NOT include

- Retry overhead (a 10% failure rate adds ~10% to effective cost).
- Reasoning/thinking tokens (DeepSeek thinking mode emits extra tokens; count them in output).
- Provider markup through OpenRouter/aggregators (use DeepSeek's direct API for cheapest).
- Developer wait time on a stall — the real cost of a bad default is often latency, not tokens.

## The local evaluation you need to run (the fit question, answered)

> **The web cannot tell you which model is best for your repos.** This is the experiment that can. Run it before you trust any recommendation here, including this one.

### Task set

Pull **30–40 real tasks** from your own recent work, stratified:
- 15 routine edits (single-file, boilerplate, CRUD).
- 10 multi-file refactors in repos you know.
- 5 ambiguous / architectural tasks (the kind you'd currently reach for Opus on).
- 5–10 long-horizon runs (multi-hour, many tool calls).

Use **your actual harnesses** (opencode, pi, Claude Code, Codex) and **your actual repos**. Do not use synthetic tasks.

### Scoring

For each task, record:
1. **Success** (did the change pass tests / achieve the goal) — binary, with a reviewer (you) judging.
2. **First-attempt success** vs **success within retry budget** (3 retries).
3. **Total tokens** (input, output, reasoning).
4. **Total cost** (tokens × price).
5. **Tool-call failure count** (malformed calls, wrong tool, stalls).
6. **Wall-clock time** and **number of stalls requiring intervention**.

### Models to compare

Run each task on **at least 3 models**, blind to which is which if possible:
- `deepseek-v4-flash` (cheap default candidate)
- `minimax-m3` (cheap alternative)
- `claude-sonnet-5` (frontier baseline)
- (optional) `deepseek-v4-pro` (in-family escalation)

### How many runs for it to mean anything

- **Minimum: 3 runs per model per task** (to get a variance estimate). 30 tasks × 3 models × 3 runs = **270 runs**.
- Better: 5 runs per cell = 450 runs. At V4-Flash prices, 450 runs of a 100K-in/20K-out task ≈ $9; the frontier arm dominates cost (~$270 for the Sonnet cells).
- Report **mean success rate ± standard error** per model per task class. A difference of <5 percentage points on 30 tasks is likely noise; >10 points is real.
- **The decision rule:** if V4-Flash's success-within-3-retries on routine + multi-file tasks is within ~5 points of Sonnet 5's, switch the default to V4-Flash. If it's >15 points worse on multi-file refactors, keep Sonnet 5 as the default for that class and use V4-Flash only for routine work. **Re-run quarterly** — the model that wins your loop in Q4 probably hasn't been released yet (dev.to).

### What this experiment settles that the web cannot

- Whether V4-Flash's tool calling holds up **in your harness** (the 30–50pp harness swing on Terminal-Bench means this is not predictable from benchmarks).
- Whether the 80/20 blend's quality loss is acceptable **on your task mix**.
- The right value of the `>N files` escalation heuristic for **your repos**.

## Final caveat

This guide recommends a default and an escalation rule at **medium confidence**. The single most important deliverable in this dossier is the local evaluation above. A dossier that ends in "here is the experiment you need to run, and here is why the web cannot substitute for it" is, per the user's own framing, a **success**.