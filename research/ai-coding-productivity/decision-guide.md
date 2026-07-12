---
type: decision-guide
slug: ai-coding-productivity
created: 2026-07-12
updated: 2026-07-12
confidence: medium
---

# Decision Guide: Under what conditions is the AI productivity gain supported?

## The decision frame (from intake.md)

Decide how far to commit to an AI-agent-centric workflow — and whether to recommend it —
based on the conditions under which **measured** evidence (not self-report) shows a
productivity gain for experienced developers on familiar codebases, weighted by non-speed
effects and by where measured vs. self-reported speedup diverge.

## Condition matrix

| Condition | Measured speed effect | Non-speed effects | Evidence strength | Recommendation |
|---|---|---|---|---|
| **Junior / new dev, greenfield, well-specified** | **Large positive** (−55.8% time, pooled treatment group, vendor lab; junior subgroup gained more, magnitude unquantified) | Skill-formation risk (comprehension ↓) | Medium (vendor lab, corroborated direction) | **Use it** — but pair with deliberate comprehension practice |
| **Junior / new dev, existing codebase** | **Positive** (+21–40% throughput, junior subgroup) | Build-success may drop; quality depends on review | Medium (field RCT subgroup, underpowered) | **Use it** with strong review |
| **Experienced dev, unfamiliar codebase** | **Unknown — no measured evidence.** The nearest RCT (Anthropic, novel library) found no significant speedup and −17% comprehension. METR lists this as "not tested here." | Comprehension deficit on novel material (Anthropic) | Low | **Use for exploration, not for learning the codebase.** Expect no measured speedup; budget time to understand the output. |
| **Experienced dev, familiar codebase (the user's condition)** | **Early-2025: +19% (slower, retired). Late-2025: −18% (faster point-estimate, uninterpretable). Current state: unmeasured.** | Delivery stability ↓ (DORA); maintainability metrics ↓ (Horikawa); more clones (GitClear); long-term costs undercounted (BNY Mellon) | **Low for current speed; medium for non-speed downsides** | **Don't assume it helps. Measure it. (See below.)** |
| **Agentic tools (Claude Code/Codex), experienced dev, late-2025/2026** | Unknown — only RCT broken by selection; qualitative "faster" from interviews | Comprehension/skill-formation risk higher for agentic (Anthropic note) | **Low** | **Treat as unproven; measure before committing** |

## The honest recommendation for the user

For Gabriel's specific condition — experienced developer, daily AI-agent use, familiar
codebases — **the measured evidence does NOT currently support a confident claim either
way about speed.** The only clean RCT on this condition (METR early-2025, Cursor +
Claude 3.5/3.7 chat/autocomplete) found a slowdown, but its authors have retired that
number and their late-2025 agentic-tool follow-up — which point-estimates a speedup — is
uninterpretable due to selection. The current state for experienced devs on familiar
codebases is genuinely unmeasured. What the evidence *does* support, robustly:

1. **The popular claim ("AI makes developers X% faster") is not supported by the evidence
   for the user's population.** It is supported for juniors and for greenfield/boilerplate
   work, where the measured effects are largest. The widely-cited 55.8% is a vendor lab
   figure on a mixed-experience pooled sample doing a single greenfield task — never
   repeat it as if it applies to experienced devs on real work.
2. **The user's own perception that AI helps him is exactly the perception the evidence
   warns against.** METR's experienced devs *believed* they were 20% faster while being
   19% slower. The self-reported-vs-measured divergence is the most robust cross-study
   finding in the dossier. The user should treat his own self-report with suspicion.
3. **The non-speed effects skew negative and are better-evidenced than the speed effects.**
   Maintainability metrics, delivery stability, code comprehension, and long-term skill
   formation all show concerning signals across independent sources (DORA, GitClear,
   Horikawa, Anthropic, BNY Mellon, Gao review).
4. **Committing further to an AI-centric workflow before measuring is a decision on
   self-report, not evidence.** That may be fine — but it should be named as such.
5. **Recommending the workflow to other experienced developers as a *speed win* is not
   supported by measured evidence.** It is supported for less-experienced developers.

## The experiment you must run (the only thing that can answer the fit question)

The web cannot answer "does this make *me* faster." Only a local self-experiment can.
Concretely — adapted from METR's design, runnable by one developer:

1. **Pick 30 real tasks** from your actual codebase over the next 2–4 weeks.
   Stratify by type: ~10 boilerplate/well-specified, ~10 novel logic, ~10
   ambiguous/refactor. Exclude trivial fixes.
2. **Randomize each task** to AI-allowed vs AI-disallowed (within-person, coin flip).
   Commit to the assignment — do not drop "hard" AI-disallowed tasks (this is what
   broke METR's late-2025 study).
3. **Record per task**, before and after:
   - Wall-clock implementation time.
   - Lines changed; files touched.
   - **Forecast** expected speedup before; **estimate** perceived speedup after
     (this measures *your* perception gap).
   - Defects found in your own review; defects found in review by a peer if available.
   - Defects found in production within 30 days (track separately).
   - Subjective difficulty (1–5).
4. **Run two sessions**, one with autocomplete tools (Copilot/Cursor tab), one with
   agentic tools (Claude Code), if you want to compare tool classes.
5. **Minimum n=20 tasks per condition** for a usable directional signal; 30 is better.
   Fewer than 15 and you're reading noise.
6. **Primary outcome**: measured AI-allowed / AI-disallowed time ratio, per task type.
   **Secondary**: defect rate ratio, perception gap (forecast − measured).
7. **Honesty checks**: don't peek at AI on disallowed tasks; don't cherry-pick easy
   tasks for the AI-allowed arm; pre-register the task list before randomizing.

If your measured ratio is >1.0 (AI slower) or near 1.0, the honest conclusion is that
AI does not make *you* faster on *your* codebase, regardless of how it feels. If it is
substantially <1.0, you have personal measured evidence and can commit and recommend
with confidence.

**Why this matters more than any source in the dossier**: METR's whole finding is that
self-report is unreliable *even for experienced developers who just finished the task*.
The only defense against your own misperception is a measurement you ran on yourself.

## Escalation / review rules

- For **greenfield, boilerplate, well-specified** work: use AI freely; it's the
  best-supported case.
- For **novel logic, ambiguous, or unfamiliar** code: use AI for exploration and
  drafting, but expect no speedup and budget time to *understand* the output (per
  Anthropic: comprehension is the cost).
- For **existing, familiar codebase with quality standards**: this is the
  least-supported case for speed and the most-supported case for non-speed downsides.
  Prefer smaller AI-assisted changes; require the same review rigor; watch for cloned
  code and declining refactor ratios (GitClear signal).
- For **safety-critical / high-stakes** code: do not let AI-generated code ship
  without human review you would have done anyway. The 39% of devs who distrust
  AI-generated code (DORA) are not being irrational.
- **Track your own delivery metrics** (DORA four: lead time, deploy frequency, change
  failure rate, MTTR) before and after deepening AI adoption. If change-failure rate
  rises, that's the DORA signal that local speed is buying system instability.

## What to tell others

- **To less-experienced developers**: "The evidence supports that AI helps you, on
  greenfield and boilerplate work. Beware it may reduce your comprehension of new
  material — use it to learn, not only to produce."
- **To other experienced developers**: "The only clean RCT on our condition (experienced,
  familiar codebase) found AI made us slower in early 2025; its authors retired that
  number, and their late-2025 follow-up is uninterpretable. The current state is
  unmeasured. The non-speed effects (maintainability, stability, comprehension) skew
  negative. Don't take my word for it or the vendors' — run a 30-task self-experiment
  and measure."
- **To no one**: repeat the 55.8% number without its context. It is the most cited and
  least applicable figure in the literature.