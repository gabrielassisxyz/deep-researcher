---
type: source
source_type: paper
title: "The Impact of AI on Developer Productivity: Evidence from GitHub Copilot"
publisher: "arXiv (GitHub/Microsoft Research)"
url: "https://arxiv.org/abs/2302.06590"
author: "Sida Peng, Eirini Kalliamvakou, Peter Cihon, Mert Demirer"
published: 2023-02-13
accessed: 2026-07-12
confidence: medium
used_for: [measured-speedup, task-type-greenfield, experience-level, vendor-study]
independence: vendor
---

# GitHub/Microsoft Copilot 55.8% Study

Vendor-authored (GitHub/Microsoft Research). The most-cited "AI makes devs faster" number.

## Setup

- Recruited developers (not employees; mix of experience).
- Task: implement an HTTP server in JavaScript "as quickly as possible."
- Between-subjects: Copilot access vs. no access.
- Lab-style, single self-contained task, greenfield, well-specified.

## Key result

- Treatment (Copilot) completed 55.8% faster.
- Heterogeneous: less-experienced developers benefited more; "promise for AI pair
  programmers to help people transition into software development careers."

## Why this number overstates the general effect (per its own authors and later work)

- Single greenfield task, not real work in a real codebase.
- Lab setting, not day-to-day workflow.
- Copilot autocomplete only, not agentic tools.
- The MIT field-experiment follow-up by the same authors ([[sources/cui-demirer-mit-copilot-field-experiments]])
  found a 26.08% effect in real work — and explicitly notes the lab effect is "substantially
  smaller" in the field.
- Vendor source → performance claim capped at medium (Gate 4.5).

## Claim typing

- Fact (study exists): high.
- Performance (Copilot helps on this kind of task, esp. for juniors): medium — vendor,
  lab setting, corroborated direction by independent field work.
- Fit (generalizes to experienced devs on familiar codebases): LOW — wrong population,
  wrong task type.