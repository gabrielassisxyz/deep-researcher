---
type: source
source_type: official
title: "How AI assistance impacts the formation of coding skills"
publisher: "Anthropic"
url: "https://www.anthropic.com/research/AI-assistance-coding-skills"
author: "Judy Hanwen Shen, Alex Tamkin"
published: 2026-01-29
accessed: 2026-07-12
confidence: medium
used_for: [comprehension, non-speed-effects, experience-level, rct]
independence: vendor
---

# Anthropic Skill-Formation RCT

Vendor-authored (Anthropic) but a genuine RCT with a pre-registered design. Directly
addresses the comprehension / non-speed axis.

## Setup

- 52 (mostly junior) software engineers, Python 1+ yr.
- Task: implement two features using **Trio**, a Python async library they were
  *unfamiliar with*.
- Randomized: AI assistant in sidebar vs no AI.
- Outcomes: completion time + a quiz on debugging, code reading, code writing, conceptual.

## Key results

- **AI group scored 17% lower on the quiz** (50% vs 67%; Cohen's d=0.738, p=0.01) — nearly
  two letter grades. Largest gap on **debugging**.
- **Completion time: AI group slightly faster (~2 min) but NOT statistically significant.**
- Interaction pattern mattered: high-scorers used AI to *build comprehension* (conceptual
  questions, explanations); low-scorers delegated code generation/debugging ("cognitive
  offloading").

## Why this matters for the dossier

- This is *novel-logic / unfamiliar-library* work — exactly the task type the user asked
  about. AI did NOT produce a statistically significant speedup here, and it measurably
  *reduced* comprehension.
- Vendor source, so the comprehension finding is unusually honest for a vendor to publish.
- Anthropic's own framing: AI may "accelerate productivity on well-developed skills and
  hinder the acquisition of new ones."

## Claim typing

- Fact (RCT run): high.
- Performance (AI reduces comprehension of novel material, no sig. speedup on novel task):
  medium — vendor but RCT, small n=52, short-term quiz only.
- Fit: LOW — novel-library learning task, not the user's familiar-codebase daily work.