---
type: index
status: active
updated: 2026-07-04
---

# Research Directory

This directory stores focused research dossiers. Each dossier should live under its own topic slug, for example `research/llm-models/`.

Use `research/_template/` as the expected structure for new deep research outputs.

## Expected Dossier Shape

```text
research/<topic-slug>/
  README.md
  intake.md
  research-contract.md
  synthesis.md
  methodology.md
  evidence.md
  open-questions.md
  log.md
  sources/
```

Add domain folders only when useful for the topic, such as `models/`, `products/`, `vendors/`, `papers/`, `entities/`, `concepts/`, `datasets/`, or `benchmarks/`. Create `raw/` only when raw captures materially improve auditability.

If Gemini review is enabled, add `review/` with the prompt, review report, and fix report for each completed review loop.
