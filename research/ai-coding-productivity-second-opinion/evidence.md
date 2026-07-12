---
type: evidence-ledger
slug: ai-coding-productivity-second-opinion
status: complete
created: 2026-07-12
updated: 2026-07-12
confidence: medium
tags: [ai-coding, productivity, evidence]
---

# Evidence Ledger

| Claim | Claim Type | Source | Source Type | Confidence | Caveat | Used In |
| --- | --- | --- | --- | --- | --- | --- |
| The strongest direct study of experienced developers working in familiar repositories found AI-allowed tasks took 19% longer. | Performance | [[sources/metr-early-2025-rct]] | Independent nonprofit preprint/RCT | High for the studied setting; medium for generalization | Small sample and early-2025 tool mix. | [[synthesis]] |
| In that METR RCT, developers predicted a 24% speedup and afterward estimated a 20% speedup despite measured slowdown. | Performance / self-report gap | [[sources/metr-early-2025-rct]] | Independent nonprofit preprint/RCT | High | Timing was task-level and self-reported, but randomized and screen recorded. | [[synthesis]] |
| METR's later 2025 experiment produced possible speedup signals but METR says selection effects make the estimate unreliable. | Performance / currentness | [[sources/metr-late-2025-uplift-update]] | Independent nonprofit update | Medium | Not a clean final estimate; likely biased by AI-positive participant/task selection. | [[synthesis]], [[open-questions]] |
| The classic GitHub Copilot controlled experiment found a 55.8% faster completion time on a JavaScript HTTP-server task. | Performance | [[sources/peng-github-copilot-controlled-experiment]] | Vendor-affiliated preprint | Medium | Greenfield, short task; not familiar-codebase work. | [[synthesis]], [[decision-guide]] |
| Three workplace Copilot RCTs estimated 26.08% more completed tasks among users, but gains were larger for less-experienced developers and not significant for longer-tenure/senior Microsoft developers. | Performance | [[sources/cui-high-skilled-work-field-experiments]] | Working paper / field RCTs with company data | Medium | Noisy experiments, imperfect compliance, output metric rather than matched task time. | [[synthesis]], [[decision-guide]] |
| Earlier two-company field results suggested PR throughput gains but were imprecise and significant only under some weighting. | Performance | [[sources/cui-copilot-field-experiment]] | Field experiment preview | Medium-low | Superseded/refined by later three-company draft. | [[methodology]] |
| DORA reports AI adoption improves individual productivity/flow/job satisfaction but is associated with lower delivery throughput and stability. | Performance / organizational outcome | [[sources/dora-2024-ai-impact]] | Industry survey/report | Medium | Survey/association, not causal task-level evidence. | [[synthesis]] |
| Uplevel found no significant change in cycle time, PR throughput, or always-on time, and reported 41% more bugs among Copilot users. | Performance / quality | [[sources/uplevel-copilot-quantitative-study]] | Vendor-authored analytics report | Medium-low | Vendor-authored and not peer-reviewed; methodology public detail limited. | [[synthesis]] |
| GitClear reports increased duplication/copy-paste and warns activity metrics can hide maintainability costs. | Quality / maintenance | [[sources/gitclear-code-quality-2025]] | Vendor-authored code metrics report | Medium-low | AI attribution is partly inferential. | [[synthesis]], [[decision-guide]] |
| BNY Mellon mixed-method research finds developer perceptions of AI usefulness conflict and long-term factors include expertise and ownership. | Self-report / measurement | [[sources/chen-bny-productivity-perspectives]] | arXiv mixed-method preprint | Medium | Not measured speed evidence. | [[synthesis]] |
| Anthropic's RCT found AI users scored 17% lower on a follow-up coding-skill quiz, while speedup was slight and not statistically significant. | Non-speed outcome | [[sources/anthropic-skill-formation-rct]] | Vendor-authored RCT | Medium | Learning unfamiliar library, not familiar codebase; vendor-authored. | [[synthesis]] |
| An OSS observational study found AI-associated productivity gains driven by less-experienced developers, while core developers reviewed 6.5% more code and had 19% lower original-code productivity. | Performance / maintenance burden | [[sources/xu-maintenance-burden-2025]] | arXiv observational preprint | Medium | Observational and potentially confounded. | [[synthesis]], [[decision-guide]] |
| A collaborative OSS Copilot study found contribution increases but also an 8% increase in coordination time. | Performance / coordination | [[sources/song-copilot-collaborative-oss]] | arXiv observational preprint | Medium | Not direct task-time evidence. | [[synthesis]] |
| A NAV longitudinal case study found no statistically significant commit-activity change after Copilot adoption and negligible correlation between perceived productivity and commit metrics. | Self-report gap / measured activity | [[sources/stray-nav-copilot-longitudinal]] | arXiv case study | Medium | Commit metrics are imperfect and sample is modest. | [[synthesis]] |
| An agent-generated-code maintenance study found AI-generated files received less frequent maintenance than human-authored files. | Quality / maintenance | [[sources/sawada-agent-maintenance-2026]] | arXiv empirical preprint | Medium-low | Could reflect age, selection, or usage differences; not speed evidence. | [[synthesis]] |
