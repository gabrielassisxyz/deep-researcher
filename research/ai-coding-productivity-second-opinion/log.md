---
type: research-log
slug: ai-coding-productivity-second-opinion
status: complete
created: 2026-07-12
updated: 2026-07-12
confidence: medium
tags: [ai-coding, productivity, search-ledger]
---

# Research Log

## Run Settings

- Role: independent Gate 8.4 second opinion.
- Primary dossier isolation: did not read `research/ai-coding-productivity/`.
- Firecrawl search: required and available.
- Review panel: disabled for this second-opinion run.
- Depth budget: 6 rounds or 40 kept sources.

## Search Ledger

| Round | Query | Purpose | Result |
| --- | --- | --- | --- |
| Discovery | Firecrawl: `AI coding assistant productivity randomized controlled trial experienced developers measured time completion` with research category | Find controlled studies | No usable results returned. Feedback attempt failed with Firecrawl 404. |
| Discovery | Firecrawl: `AI coding assistant productivity randomized controlled trial experienced developers measured time completion` | Find controlled studies | Found METR arXiv page plus irrelevant generic AI sites. |
| Discovery | Firecrawl: `GitHub Copilot 55 percent faster study controlled experiment developers task completion time` | Find classic Copilot controlled experiment | Poor results: mostly generic GitHub pages. |
| Discovery | Firecrawl: `GitHub Copilot experiment 55% faster developers JavaScript HTTP server paper Peng Kalliamvakou Cihon Demirer` | Find classic Copilot controlled experiment by authors/task | Poor results: mostly generic GitHub pages. |
| Discovery | Firecrawl: `"The Impact of AI on Developer Productivity" "GitHub Copilot" experiment` | Exact title search | Poor results: dictionary and generic pages. |
| Discovery | Firecrawl: `copilot productivity 55 percent arxiv 2023 developer productivity experiment` | Find Copilot RCT without exact title | Poor results: mostly Microsoft Copilot product pages. |
| Discovery | Firecrawl: `METR early 2025 AI experienced open source developer productivity study measured slowdown self reported speedup` | Find direct contradictory evidence | Found METR pages but not the specific study in top result set. |
| Discovery | Firecrawl: `self reported productivity measured productivity AI coding assistants developers study` | Find perception/measurement divergence | Poor results: dictionary and unrelated "Self" pages. |
| Discovery | Firecrawl: `perceived productivity objective productivity GitHub Copilot developers measured study` | Find perception/metric divergence | Poor results: dictionary pages. |
| Discovery | Firecrawl: `AI code generation code quality maintainability defects review burden empirical study Copilot developers` | Find non-speed costs | Poor results: generic AI sites. |
| Discovery | Firecrawl: `AI assistant coding productivity field experiment professional developers pull request metrics cycle time` | Find professional field experiments | Poor results: generic AI sites. |
| Discovery | Web: `arXiv measuring impact early 2025 AI experienced open-source developer productivity` | Find direct experienced-developer RCT | Found [[sources/metr-early-2025-rct]]. |
| Discovery | Web: `The Impact of AI on Developer Productivity Evidence from GitHub Copilot study 55 percent faster` | Find classic Copilot RCT | Found [[sources/peng-github-copilot-controlled-experiment]]. |
| Discovery | Web: `AI coding assistants self-reported productivity measured productivity study developers` | Find self-report divergence | Found [[sources/stray-nav-copilot-longitudinal]] and [[sources/chen-bny-productivity-perspectives]]. |
| Discovery | Web: `GitHub Copilot field experiment professional developers productivity pull request cycle time` | Find field experiments | Found [[sources/cui-copilot-field-experiment]] and later [[sources/cui-high-skilled-work-field-experiments]]. |
| Discovery | Web: `DORA 2024 report AI adoption software delivery performance throughput stability generative AI` | Find organizational non-speed outcomes | Found [[sources/dora-2024-ai-impact]]. |
| Discovery | Web: `Uplevel GitHub Copilot productivity study no improvement bugs vulnerabilities 2024` | Find contradictory analytics evidence | Found [[sources/uplevel-copilot-quantitative-study]]. |
| Discovery | Web: `GitClear AI code quality 2025 code churn copy pasted code maintainability study` | Find maintainability evidence | Found [[sources/gitclear-code-quality-2025]]. |
| Discovery | Web: `BNY Mellon Developer Perspectives on Productivity with AI Coding Assistants arxiv 2602.03593` | Find enterprise perception/measurement research | Found [[sources/chen-bny-productivity-perspectives]]. |
| Discovery | Web: `Anthropic randomized controlled trial AI coding assistant developers comprehension follow-up test Python library 17% lower` | Find comprehension/skill RCT | Found [[sources/anthropic-skill-formation-rct]]. |
| Discovery | Web: `AI coding assistants randomized controlled trial comprehension maintenance code review burden developers` | Find non-speed RCTs and maintenance evidence | Found [[sources/anthropic-skill-formation-rct]], [[sources/xu-maintenance-burden-2025]], and [[sources/sawada-agent-maintenance-2026]]. |
| Discovery | Web: `Harvard 187,000 developers GitHub Copilot collaboration coding time project management study` | Find large-scale OSS collaboration studies | Found [[sources/song-copilot-collaborative-oss]] and related MIT Sloan commentary. |
| Discovery | Web: `GitHub Copilot collaboration open source 187000 developers study 2026` | Find Copilot OSS collaboration evidence | Found [[sources/song-copilot-collaborative-oss]]. |
| Follow-up 1 | Firecrawl: `peer reviewed experienced developers familiar codebase AI coding assistant productivity randomized controlled trial` | Check for peer-reviewed exact-setting RCT | Found METR and arXiv records; no peer-reviewed exact-setting controlled trial found. |
| Follow-up 1 | Web: `AI coding assistants effect by developer experience senior junior measured productivity study` | Check experience-level split | Found the MIT Economics high-skilled-work field-experiment draft and experience-level findings. |
| Follow-up 1 | Web: `GitHub Copilot productivity effect developer experience novice experienced larger gains study` | Check junior/senior heterogeneity | Found [[sources/cui-high-skilled-work-field-experiments]] and supporting summaries. |
| Follow-up 1 | Web: `experienced developers AI coding assistant productivity existing codebase familiar repository study` | Check familiar-codebase evidence coverage | Found METR and related commentary; no additional exact-setting controlled study found. |

## Candidate Sources Rejected

| Source | Reason |
| --- | --- |
| Reddit and Hacker News discussion threads | Useful for finding what practitioners were debating, but not used as evidence for measured productivity. |
| SoftwareSeni, Cerbos, Medium, LinkedIn summaries | Commentary summarizing primary studies; not kept because primary sources were available. |
| Generic Microsoft/GitHub/OpenAI product pages | Marketing or product information; not evidence for measured speed. |
| ResearchGate mirrors | Duplicative or lower-audit copies of arXiv/preprint sources. |
| News articles about AI-generated "slop" | Current and relevant context, but not controlled or measured evidence for the target question. |
| Statistics/SEO pages listing Copilot adoption or speed claims | Aggregated claims with weak provenance; rejected where primary study was available. |

## Round Notes

### Round 0: Setup

- Created intake and research contract before live web research.
- No primary-run files read.

### Round 1: Broad Discovery

- Issued more than five Firecrawl discovery queries before extracting source notes.
- Firecrawl search quality was poor for several queries; fallback web search was used and logged.
- Kept 13 source notes from RCTs, field experiments, observational studies, and reports.
- High-impact gaps after Round 1:
  - Exact experienced/familiar-codebase controlled evidence: candidate resolved by METR, but currentness unclear.
  - Self-report versus measured-speed divergence: candidate resolved by METR and NAV.
  - Non-speed costs: candidate resolved by DORA, Uplevel, GitClear, Anthropic, Xu, Song, and Sawada.

### Round 2: Targeted Follow-Up

- Searched for peer-reviewed exact-setting RCTs and experience-level heterogeneity.
- Added [[sources/cui-high-skilled-work-field-experiments]] because it materially improves the workplace RCT evidence and developer-experience split.
- Determined that no peer-reviewed controlled trial exactly matching current agentic tools plus experienced developers plus familiar codebases was found.
- Marked current 2026 exact-setting speedup as blocked because METR's later experiment is explicitly unreliable.

## Termination

Status: Done.

Reason: All high-impact gaps are either resolved or blocked in [[open-questions]]. The exact current-2026 agentic-tool effect for experienced developers in familiar codebases remains blocked because no clean measured study was found and METR's latest task-level update says the available data is unreliable.

Depth reached: 2 rounds, 29 logged queries, 14 kept sources, 6 rejected source families.
