---
type: source
source_type: benchmark
title: "Aider LLM Leaderboards (Polyglot)"
publisher: "Aider (Paul Gauthier)"
url: "https://aider.chat/docs/leaderboards/"
author: "Paul Gauthier"
published: null
accessed: 2026-07-12
confidence: medium
used_for: [independent-coding-benchmark, model-pass-rates, cost-per-run]
---

# Aider LLM Leaderboards

Scraped 2026-07-12. Aider's own polyglot benchmark — 225 Exercism exercises across C++, Go, Java, JS, Python, Rust; two attempts each with test-error feedback. Independent of vendors (Aider runs the evals). Page "last updated November 20, 2025" but includes runs dated through 2025-10-03.

## Methodology notes (caveats)

- Tests **code editing** in a real agent loop (Aider), not just generation — closer to agent behavior than HumanEval.
- 225 tasks is small; differences of a few percent are within noise.
- Two attempts with feedback inflates pass rates vs single-attempt.
- Each run reports total cost — useful for cost-per-benchmark-run comparisons.

## Key rows (cheap candidates + frontier reference)

| Model | Pass rate 2 | Total cost | Well-formed % | Date |
| --- | --- | --- | --- | --- |
| gpt-5 (high) | 88.0% | $29.08 | 91.6% | 2025-08-23 |
| gemini-2.5-pro-preview-06-05 (32k) | 83.1% | $49.88 | 99.6% | 2025-06-06 |
| **DeepSeek-V3.2-Exp (Reasoner)** | **74.2%** | **$1.30** | 97.3% | 2025-10-03 |
| DeepSeek R1 (0528) | 71.4% | $4.80 | 94.6% | 2025-06-06 |
| **DeepSeek-V3.2-Exp (Chat)** | **70.2%** | **$0.88** | 98.2% | 2025-10-03 |
| claude-sonnet-4-20250514 (32k think) | 61.3% | $26.58 | 97.3% | 2025-05-24 |
| Kimi K2 | 59.1% | $1.24 | 92.9% | 2025-07-17 |
| Qwen3 235B A22B (no think) | 59.6% | — | 92.9% | 2025-05-09 |
| gemini-2.5-flash-preview-05-20 (24k) | 55.1% | $8.56 | 95.6% | 2025-05-25 |
| DeepSeek V3 (0324) | 55.1% | $1.12 | 99.6% | 2025-03-24 |
| gpt-4.1-mini | 32.4% | $1.99 | 92.4% | 2025-04-14 |
| gpt-4.1-nano | 8.9% | $0.43 | 94.2% | 2025-04-14 |

Note: DeepSeek-V4-Flash was not yet on this Aider board at scrape time (newest run 2025-10-03 is V3.2-Exp). The V3.2-Exp Chat result at 70.2% for $0.88 is the closest proxy for the cheap-DeepSeek default; V4-Flash is reported (by llm-stats and dev.to) to be a further step up.

## Confidence

Medium: independent methodology, but small task count, two-attempt protocol, and the V4-Flash row is absent (proxied by V3.2-Exp).