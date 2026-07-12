# Codex Deep Research Dossier Prompt

Read `opencode/prompts/deep-research.md` in full and follow it as the controlling workflow.

Use the user's request as the research topic and requirements. If the request does not specify an output directory, derive one under `research/<topic-slug>/`.

The primary output must be files in the repository, not a chat-only answer.

Before any intake question or live research, ask whether the user wants an external Gemini review loop through `agy`. If yes, ask for the maximum number of loops. In non-interactive runs, default to no Gemini review unless the request explicitly enables it and provides a maximum loop count.

Before live research, perform the research intake step from the workflow. If the objective, target decisions, use cases, comparison axes, or confidence threshold are missing, ask a short mini interview before searching. If this is a non-interactive run, write explicit assumptions in `intake.md` and keep conclusions conservative.

After intake and before searching, write `research-contract.md` from the workflow. Use it as the source of truth for the research plan and final audit.

Use optional domain folders only when they fit the research topic. Do not create `benchmarks/`, `models/`, or other domain folders unless they improve auditability.

If Gemini review is enabled, use `agy/prompts/deep-research-review.md` for review reports and apply the Gate 8.5 review loop from the canonical workflow. If `agy` cannot be invoked from the current environment, save the review prompt under `review/` and mark the external review as blocked instead of claiming it happened.

Before finishing, verify that the research directory contains:

- `README.md`
- `intake.md`
- `research-contract.md`
- `synthesis.md`
- `methodology.md`
- `evidence.md`
- `open-questions.md`
- `log.md`
- `sources/`

Also verify that optional directories are not empty, decision-critical notes are not shallow stubs presented as complete notes, and confidence levels distinguish source confidence, claim confidence, and recommendation confidence.
