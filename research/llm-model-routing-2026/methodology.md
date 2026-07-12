---
type: methodology
status: complete
updated: 2026-07-04
confidence: medium
sources:
  - "[[sources/artificial-analysis-methodology]]"
  - "[[sources/livebench]]"
  - "[[sources/benchlm]]"
  - "[[sources/openrouter-models-api]]"
---

# Methodology

## Research Brief

- Intake summary: route AI coding and research tasks to the cheapest model tier that is sufficiently reliable, escalating to frontier models only where evidence supports a material quality gain.
- Scope: public model availability, official docs, model cards, benchmark leaderboards, methodology pages, pricing pages, context windows, latency and throughput data, task-specific routing evidence, and model-name verification.
- Success criteria: the dossier must support practical routing decisions, identify cheaper sufficient cases, identify frontier-justified cases, and clearly mark unknown or unverifiable models.
- Freshness requirement: current public sources as of 2026-07-04; model availability, pricing, and benchmark ranks are time-sensitive and require direct verification.
- Source targets: official vendor pages, API docs, model cards, pricing pages, release notes, LiveBench, Artificial Analysis, BenchLM, OpenRouter, SWE-bench, LM Arena, relevant benchmark repositories, and credible model papers.
- Minimum evidence: at least one source note for every source cited in `synthesis.md`, `decision-guide.md`, or `evidence.md`; at least one targeted follow-up for every high-impact gap.
- Output directory: `research/llm-model-routing-2026/`.

## Search Plan

| Subquestion | Best source type | Expected evidence |
| --- | --- | --- |
| Which listed model identifiers are publicly verifiable? | Official vendor docs, OpenRouter, benchmark leaderboards | Exact model IDs, vendor, release status, aliases, availability |
| What do official sources say about context, modalities, tool use, pricing, and intended use? | Official docs, model cards, pricing pages | Context windows, input/output price, modalities, API behavior, safety or system cards |
| What do independent benchmarks show for coding, reasoning, and long-context tasks? | LiveBench, Artificial Analysis, SWE-bench, LM Arena, BenchLM, methodology pages | Scores, ranks, model identifiers, dates, benchmark caveats |
| Which cheaper models show enough coding strength for implementation from a clear spec? | Coding benchmark pages, model cards, repositories, credible third-party evaluations | Coding scores, agentic coding scores, open-weight availability, cost/performance evidence |
| Which frontier models show material advantage for ambiguous planning, architecture, or final review? | Reasoning benchmarks, agentic coding benchmarks, system cards, independent evals | Evidence of stronger reasoning, tool use, long-horizon or multimodal performance |
| How should routing change for long context or documentation work? | API docs, long-context benchmarks, context window data, model cards | Context length, retrieval behavior, benchmark caveats, latency/cost consequences |
| How should routing change for multimodal tasks? | Official modality docs, benchmark pages, model cards | Supported modalities and quality evidence |
| What are the cost-performance trade-offs? | Pricing pages, Artificial Analysis, OpenRouter, provider docs | Price per token, latency, throughput, availability, caveats |
| What are the unresolved gaps? | Targeted follow-up searches | Gap status: resolved, partially resolved, or blocked |

## Source Tiers

| Tier | Source type | Confidence rule |
| --- | --- | --- |
| 1 | Primary official sources | High when directly supporting exact availability, pricing, context, modality, or release claims |
| 2 | Independent benchmarks, papers, repositories | High or medium depending on methodology clarity, freshness, and exact model identifiers |
| 3 | Aggregators | Medium unless corroborated by primary or multiple independent sources |
| 4 | Commentary and social sources | Low; use only as leads or context |

## Interpretation Rules

- Preserve exact model identifiers as written by the source.
- Do not infer that an unverified requested model exists because an adjacent family model exists.
- Do not compare benchmark scores across unrelated benchmark methodologies as if they are a single normalized score.
- Treat latency, throughput, pricing, and availability as volatile.
- Treat routing recommendations as evidence-backed decision rules, not universal model rankings.
