---
type: synthesis
slug: ai-coding-productivity-second-opinion
topic: "Do AI coding agents make experienced developers measurably faster?"
status: complete
created: 2026-07-12
updated: 2026-07-12
freshness_requirement: "Current through July 12, 2026; prioritize controlled or measured evidence over surveys."
confidence: medium
source_count: 14
tags: [ai-coding, productivity, second-opinion]
---

# Synthesis

## Bottom Line

The evidence does **not** support a general claim that AI coding agents make experienced developers measurably faster on real work in codebases they already know.

The honest answer is conditional:

- **Supported**: AI coding tools can speed up constrained, well-specified, implementation-heavy work, especially boilerplate or short greenfield tasks. The classic Copilot experiment found 55.8% faster completion on a JavaScript HTTP-server task (Source: [[sources/peng-github-copilot-controlled-experiment]]).
- **Supported with caveats**: In workplace field experiments, Copilot access increased measured task completion overall, but the strongest gains were for less-experienced or more junior developers, not senior/long-tenure developers (Source: [[sources/cui-high-skilled-work-field-experiments]]).
- **Contradicted in the strict target setting**: The best direct RCT for experienced developers working in familiar mature repositories found AI made them 19% slower, while they believed it made them faster (Source: [[sources/metr-early-2025-rct]]).
- **Unsettled for current 2026 agents**: METR says later tools likely changed the effect, but its later task-level data is not reliable enough to estimate the size of current gains (Source: [[sources/metr-late-2025-uplift-update]]).

The most important finding is the **divergence between felt speed and measured speed**. METR found developers expected a 24% speedup, later believed they got a 20% speedup, but measured task time was 19% slower (Source: [[sources/metr-early-2025-rct]]). A NAV case study found perceived productivity had negligible correlation with commit metrics (Source: [[sources/stray-nav-copilot-longitudinal]]).

## Evidence By Method

| Evidence family | What it says | Source type | Confidence |
| --- | --- | --- | --- |
| Experienced familiar-codebase RCT | 16 experienced OSS developers, 246 tasks, familiar repositories; AI-allowed tasks took 19% longer. | Independent nonprofit preprint/RCT | High for studied setting, medium for generalization: [[sources/metr-early-2025-rct]] |
| Currentness update | Late-2025 tools may speed developers up, but selection effects and agent concurrency make the estimate unreliable. | Independent nonprofit update | Medium: [[sources/metr-late-2025-uplift-update]] |
| Short controlled task | Copilot users completed a JavaScript HTTP server task 55.8% faster. | Vendor-affiliated preprint | Medium: [[sources/peng-github-copilot-controlled-experiment]] |
| Workplace RCTs | Three company experiments estimate 26.08% more completed tasks among Copilot users; less-experienced developers benefit more. | Working paper with company data | Medium: [[sources/cui-high-skilled-work-field-experiments]] |
| Earlier field experiment preview | Microsoft and Accenture PR gains were suggestive but imprecise. | Field-experiment preview | Medium-low: [[sources/cui-copilot-field-experiment]] |
| Organizational report | AI adoption correlates with higher individual productivity but lower delivery throughput and stability. | DORA/Google industry report | Medium: [[sources/dora-2024-ai-impact]] |
| Engineering analytics | No significant efficiency gain; 41% more bugs reported. | Vendor-authored analytics report | Medium-low: [[sources/uplevel-copilot-quantitative-study]] |
| Code-quality metrics | More copy/paste and duplication; activity metrics may hide maintenance costs. | Vendor-authored report | Medium-low: [[sources/gitclear-code-quality-2025]] |
| Real organization case study | No significant commit-activity change; perceived productivity diverges from metrics. | arXiv case study | Medium: [[sources/stray-nav-copilot-longitudinal]] |

## Task Type

AI speed gains are best supported for **well-specified, implementation-heavy work**: autocomplete, boilerplate, syntax, simple transformations, tests or docs scaffolding, and short tasks where correctness is easy to check (Sources: [[sources/peng-github-copilot-controlled-experiment]], [[sources/cui-high-skilled-work-field-experiments]], [[sources/stray-nav-copilot-longitudinal]]).

The evidence is weaker or negative for **ambiguous, high-context, mature-codebase work**. METR's RCT used mature repositories and real issues selected by experienced contributors; AI slowed task completion. METR's own reconciliation suggests benchmarks, anecdotes, and RCTs may be measuring different slices of the task distribution (Source: [[sources/metr-early-2025-rct]]).

For **collaborative OSS work**, AI can increase contribution volume while increasing coordination time. One study found 5.9% higher project-level contributions but 8% higher coordination time (Source: [[sources/song-copilot-collaborative-oss]]).

## Experience And Familiarity

Evidence repeatedly suggests lower-experience developers benefit more from coding assistants:

- The workplace RCT paper found greater gains and adoption among less-experienced developers; at Microsoft, task completion rose for recent hires and junior positions, not for longer-tenure or more senior developers (Source: [[sources/cui-high-skilled-work-field-experiments]]).
- The classic Copilot experiment's abstract says heterogeneous effects showed promise for helping people transition into software-development careers (Source: [[sources/peng-github-copilot-controlled-experiment]]).
- An OSS maintenance-burden study found aggregate gains were driven by peripheral developers, while core developers carried more review/rework burden and lost original-code productivity (Source: [[sources/xu-maintenance-burden-2025]]).

Familiarity cuts both ways. It may help experienced developers identify bad AI suggestions, but that review itself costs time. In METR's familiar-codebase RCT, expertise did not translate into measured speedup; it may have increased scrutiny and integration cost (Source: [[sources/metr-early-2025-rct]]).

## Why Evidence Conflicts

The studies conflict because they measure different things:

- **Task distribution**: greenfield HTTP server versus mature OSS issues versus company PRs.
- **Outcome metric**: elapsed task time, PR count, completed tasks, commits, build counts, perceived productivity, or code-quality proxies.
- **Population**: recruited developers, junior/recent hires, senior/long-tenure developers, OSS core maintainers, or mixed enterprise populations.
- **Tool generation**: Copilot autocomplete in 2022-2023, Cursor/Claude in early 2025, and more agentic Claude Code/Codex-style tools by late 2025/2026.
- **Selection effects**: people and tasks with the largest expected AI gains may opt out of no-AI conditions, making later RCTs harder to interpret (Source: [[sources/metr-late-2025-uplift-update]]).
- **Perception mismatch**: developers may feel faster because flow improves, drudgery drops, or first drafts appear sooner, while total delivery time, review, and rework do not improve (Sources: [[sources/metr-early-2025-rct]], [[sources/stray-nav-copilot-longitudinal]], [[sources/chen-bny-productivity-perspectives]]).

## Non-Speed Outcomes

The non-speed evidence is mixed but important:

- **Defects**: Uplevel reports 41% more bugs with Copilot access and no significant efficiency improvement (Source: [[sources/uplevel-copilot-quantitative-study]]).
- **Delivery stability**: DORA reports AI adoption correlates with lower throughput and lower stability despite higher individual productivity and flow (Source: [[sources/dora-2024-ai-impact]]).
- **Maintenance burden**: GitClear reports more copy/paste and duplication; Xu et al. report experienced core developers reviewed more code and had lower original-code productivity after AI adoption (Sources: [[sources/gitclear-code-quality-2025]], [[sources/xu-maintenance-burden-2025]]).
- **Coordination burden**: Song et al. report higher coordination time in collaborative OSS (Source: [[sources/song-copilot-collaborative-oss]]).
- **Comprehension and skill**: Anthropic's RCT found AI users scored 17% lower on a follow-up coding-skill quiz, while speedup was not statistically significant (Source: [[sources/anthropic-skill-formation-rct]]).
- **Counterpoint**: Sawada et al. found agent-generated files received less frequent maintenance than human-authored files, so "AI always increases maintenance burden" is not settled (Source: [[sources/sawada-agent-maintenance-2026]]).

## Evidence Looked For But Not Found

I did not find a peer-reviewed controlled trial that cleanly answers: experienced professional developers, familiar production codebase, current 2026 agentic coding tools, randomized AI access, measured elapsed time, defects, review burden, and follow-up maintenance.

I also did not find a stable current estimate for autonomous agents such as Claude Code or Codex on this exact setting. METR's late-2025 update is the closest, but it explicitly says selection and timing issues make the result unreliable (Source: [[sources/metr-late-2025-uplift-update]]).

## What The Web Cannot Settle

The web cannot settle whether AI will make **a specific experienced developer or team** faster in **its own familiar codebase**. That is a fit claim. The local evaluation in [[open-questions]] is the concrete way to answer it.

## Final Judgment

Measured speedup is real in some conditions, but the popular broad claim is too strong. For experienced developers in familiar codebases, the evidence is best summarized as:

**Possible gains, not generally established; likely task-dependent; self-reports are unreliable; review, defects, coordination, and maintenance can erase or reverse apparent speedups.**
