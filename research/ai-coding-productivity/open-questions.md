---
type: open-questions
slug: ai-coding-productivity
created: 2026-07-12
updated: 2026-07-12
---

# Open Questions & Gap Analysis

## Gate 5 — Gap analysis after Round 1

### High-impact gaps

1. **G-H1: No clean RCT of late-2025/2026 AGENTIC tools (Claude Code, Codex) on
   experienced developers.** → **Status: BLOCKED.** Round 2 searched
   `Claude Code Cursor agentic coding productivity study measured 2026 experienced
   developer` and the METR late-2025 update is the only direct attempt. METR themselves
   declared the design broken by selection effects
   ([[sources/metr-late-2025-uplift-update]]). No other team is running this exact
   experiment publicly. The Horikawa MSR '26 study ([[sources/horikawa-readability-2026]])
   provides agentic-era *quality* evidence but not productivity/speed evidence on
   experienced devs. Blocking reason: the evidence does not exist in accessible form;
   producing it requires a new RCT.

2. **G-H2: Maintainability / defect-rate causal evidence is correlational only.** →
   **Status: BLOCKED (direction strongly corroborated; causality unresolved).** Round 3
   added Horikawa et al. (MSR '26) and Gao et al. (systematic review of bugs in
   AI-generated code). Horikawa finds Maintainability Index *decreased* in 56.1% and
   Cyclomatic Complexity *increased* in 42.7% of AI-agent refactoring commits; Gao
   consolidates the broader literature confirming patterned bugs/defects in AI-generated
   code. These strengthen the *directional* evidence (AI-era code has more duplication,
   worse maintainability metrics, documented bug patterns) but are still
   observational/commit-mined/survey-of-surveys, not an RCT measuring long-run defect or
   maintenance cost. No RCT of long-run maintenance cost exists. Blocking reason: no
   causal longitudinal defect study exists; would require a multi-month RCT. The
   terminal state is `blocked` — "partially mitigated" is not a terminal state and is
   not used as one.

3. **G-H3: Codebase-familiarity as an isolated variable.** → **Status: BLOCKED.** Round
   2 confirmed: no study cleanly varies familiarity while holding developer skill
   constant. METR is the only study on experienced devs *familiar* with the codebase
   (avg 5 yrs); all others are greenfield (Peng) or mixed-tenure enterprise (Cui/Demirer,
   NAV IT). Blocking reason: the cross-study comparison is the best available evidence;
   no single study isolates familiarity.

4. **G-H4: Review burden.** → **Status: BLOCKED.** The review-burden search
   (`"code review" AI generated code reviewer effort time increase study arxiv` —
   query #14 in `log.md`) returned only generic hijacked results; no primary measured
   study surfaced. Only DORA's self-reported +3.1% review speed exists. The BNY Mellon
   "Beyond the Commit" study (Round 3) touches long-term review/ownership factors but
   does not measure reviewer effort/time. Blocking reason: no measured study of AI's
   effect on reviewer effort/time found via accessible search; may exist behind paywalls
   or under non-obvious terms, but not discoverable.

### Medium-impact gaps

5. **G-M1: Long-term skill-formation effect.** Anthropic's RCT measured a quiz minutes
   after the task. Does the comprehension deficit persist? Does it compound over months?
   No longitudinal follow-up. → Likely `blocked`.

6. **G-M2: Effect on senior devs specifically.** Cui/Demirer show a small, ns senior
   effect; METR shows negative for experienced. More data on seniors would sharpen the
   decision guide. → Target in Round 2.

### Low-impact gaps

7. **G-L1: Vendor surveys (GitHub 2,000-dev, Stack Overflow).** Captured as context only;
   not decision-critical.
8. **G-L2: Non-coding effects (planning, design, testing time).** Out of scope per
   contract.

## Not answerable from the web (Gate 4.5 / Gate 7)

These are **fit** questions — "does this make *me* faster" — and by construction the web
cannot settle them. They go in the synthesis's mandatory "what the web cannot settle"
section and in the decision guide.

- **N1: Does AI make Gabriel faster on his specific codebase?** The user's codebase,
  task distribution, and AI fluency are unique. METR's experienced-dev result is the
  closest proxy but is (a) a different population, (b) early-2025 tools, (c) now
  superseded. No web source can answer this for the user.
- **N2: Does AI make Gabriel's *system* faster (delivery, defects)?** DORA shows org-level
  instability; whether that applies to a solo / small-team workflow is unknown.
- **N3: Will the current positive trajectory (METR late-2025 qualitative) continue?**
  Extrapolation, not measurement.

### Local evaluation that would settle N1–N3

A concrete self-experiment (put in decision-guide.md and synthesis):
1. Pick 20–30 real tasks from the user's actual codebase, stratified by type (boilerplate
   / novel logic / ambiguous / refactor).
2. Randomize each task to AI-allowed vs AI-disallowed (within-person, like METR).
3. Record: wall-clock time, lines changed, defects found in review, defects found in
   production within 30 days, subjective difficulty.
4. Before each task, forecast expected speedup; after, estimate perceived speedup (to
   measure the perception gap on *your own* work).
5. Run 2 sessions: one with autocomplete tools, one with agentic tools (Claude Code).
6. Minimum n=20 tasks per condition for a usable signal; 30 better.
7. Primary outcome: measured time ratio. Secondary: defect rate, perception gap.
8. This is the *only* way to answer "does this make *me* faster" with any confidence.