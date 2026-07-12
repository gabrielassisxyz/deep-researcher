---
type: synthesis
slug: ai-coding-productivity
status: draft
created: 2026-07-12
updated: 2026-07-12
confidence: medium
---

# Synthesis: Do AI coding agents make experienced developers faster?

## Bottom line (the honest, sourced answer — corrected for recency)

**Sign convention used throughout: "% change in completion time; positive = slower,
negative = faster."** (Reviewers found the dossier mixed conventions. This is now
consistent.)

**The honest answer is a trajectory, not a number.** The only clean RCT on the user's
exact condition — experienced developers on codebases they know well — found that
early-2025 AI tools (Cursor + Claude 3.5/3.7, chat/autocomplete) made them **19% slower**
(+19% completion time, CI +2% to +39%) (Source: [[sources/metr-early-2025-rct]]). **METR
has since retired that number**: their blog now says "these results are out of date," and
their late-2025 follow-up on the *same developers* using agentic tools point-estimates an
**18% speedup** (−18%, CI −38% to +9%) — but selection effects (developers refusing to
work without AI, withholding high-uplift tasks) make that estimate uninterpretable
(Source: [[sources/metr-late-2025-uplift-update]]). **The current state for the user's
condition is unmeasured.** What we have is: one retired negative result, one
uninterpretable positive-point-estimate, and a strong qualitative signal that the
direction may have flipped as tools became agentic.

**Three things survive the recency correction intact:**

1. **The popular claim is not supported for the user's population.** The widely-cited
   "55.8% faster" is a vendor lab study (Peng et al.) on a single greenfield JavaScript
   task with a *mixed-experience* population (Source:
   [[sources/github-copilot-55-percent-study]]) — wrong population, wrong task type, wrong
   setting. The field RCTs that do show positive effects (Cui/Demirer, +26% throughput)
   show them **concentrated in juniors and short-tenure developers**, with small,
   non-significant effects for seniors (Source:
   [[sources/cui-demirer-mit-copilot-field-experiments]]). No independent measured study
   shows a clear positive speed effect for experienced developers on familiar codebases.
2. **The divergence the user predicted as the most important finding is real and is the
   strongest cross-study result in the dossier**: self-reported speedup systematically
   exceeds measured speedup — by ~40 percentage points in METR's RCT — and the divergence
   flows through to the system level (individuals *feel* faster while organizational
   delivery metrics get *slightly worse*).
3. **The non-speed effects skew negative and are better-evidenced than the speed effects.**
   Maintainability metrics, delivery stability, code comprehension, and long-term skill
   formation all show concerning signals across independent sources.

**Therefore: the recommendation that survives is "measure it yourself," and it is
strengthened, not weakened, by the recency correction.** The decision guide specifies the
30-task self-experiment. (See §"What the web cannot settle.")

## Findings, by question

### Q1 — What controlled/measured evidence exists?

**Recency framing first** (the dossier's headline changed after the review panel flagged
that the early-2025 number is retired): the measured evidence is *thin and time-shifted*.
The cleanest RCT (METR early-2025) is retired; its late-2025 follow-up is uninterpretable;
the field RCTs use activity proxies, not time; the lab RCT is vendor and greenfield.

Six measured/controlled studies, in descending relevance to the user's condition:

1. **METR early-2025 RCT** — the only RCT on *experienced* developers on *familiar*
   codebases. Result: **+19% (slower)**, CI +2% to +39% (Source:
   [[sources/metr-early-2025-rct]]). Independent. **Now retired by its authors** — see #2.
   Matches the user on population + familiarity, **mismatches on tool generation** (early
   2025 chat/autocomplete, not the user's daily agentic workflow).
2. **METR late-2025 follow-up** — same design, agentic tools. Point-estimate **−18%
   (faster)**, CI −38% to +9%, but **selection-biased and uninterpretable** (Source:
   [[sources/metr-late-2025-uplift-update]]). The current state is unmeasured.
3. **Cui/Demirer 3-field-experiment study** — 4,867 devs at Microsoft/Accenture/Fortune
   100. **+26% tasks/week** throughput, but metric is activity not time, and the
   senior/long-tenure effect is small and non-significant (Source:
   [[sources/cui-demirer-mit-copilot-field-experiments]]). Mixed independence (vendor data,
   independent academic analysis, pre-registered). Confidence capped **medium**.
4. **Peng et al. Copilot 55.8% study** — lab, single greenfield task, mixed-experience
   *pooled* sample (NOT a junior-subgroup estimate). Vendor (Source:
   [[sources/github-copilot-55-percent-study]]). Confidence capped **medium**.
5. **NAV IT longitudinal** — 2 years, 26,317 commits. **No significant change in
   activity after Copilot adoption** despite positive self-report (Source:
   [[sources/nav-it-longitudinal-study]]). Independent, peer-reviewed (HICSS-59).
   **Observational, not an RCT.** Confidence **medium**.
6. **Anthropic skill-formation RCT** — novel/unfamiliar task, mostly junior. **No
   significant speedup; −17% comprehension** (Source:
   [[sources/anthropic-skill-formation-rct]]). Vendor but candid. Confidence **medium**.

Plus **four** observational/survey sources: DORA 2024, GitClear 2025, METR 2026 survey,
Horikawa MSR '26 (commit-mining, not a survey), and — added in Round 3 — the BNY Mellon
"Beyond the Commit" study (ICSE SEIP, 2,989 devs) and the Gao et al. systematic review of
bugs in AI-generated code.

### Q2 — Effect by task type

The effect size **shrinks as task realism increases** — this is the most robust
cross-study pattern. (Sign convention: % change in completion time, positive = slower.)

| Task type | Effect (completion time) | Source |
|---|---|---|
| Lab, single greenfield, well-specified | **−55.8%** (faster) — pooled treatment group, mixed-experience sample, vendor lab | [[sources/github-copilot-55-percent-study]] |
| Field, real work, mixed realism (throughput, not time) | **+26% tasks/wk** (activity, not time-to-ship) | [[sources/cui-demirer-mit-copilot-field-experiments]] |
| Real OSS PRs, high quality bars, familiar code (experienced devs) | **+19%** (slower), CI +2% to +39% — early-2025, now retired | [[sources/metr-early-2025-rct]] |
| Real OSS PRs, late-2025 agentic tools (experienced devs) | **−18%** (faster point-estimate), CI −38% to +9% — uninterpretable, selection-biased | [[sources/metr-late-2025-uplift-update]] |
| Novel/unfamiliar library (learning task, mostly junior) | **ns speedup; −17% comprehension** | [[sources/anthropic-skill-formation-rct]] |

Greenfield, boilerplate, and well-specified tasks show large positive effects. Existing
codebases with quality standards, novel logic, and ambiguous tasks show small, null, or
negative effects on speed — and AI actively degrades comprehension on novel material.

### Q3 — Effect by experience level and codebase familiarity

**The heterogeneity finding is robust across two studies**: AI helps less-experienced
developers more (Source: [[sources/github-copilot-55-percent-study]],
[[sources/cui-demirer-mit-copilot-field-experiments]]).

- Cui/Demirer: short-tenure **+27–39% throughput** vs long-tenure **+8–13%** (ns); junior
  **+21–40%** vs senior **+7–16%** (ns). (Throughput, not time; sign is "more output.")
- METR (experienced, familiar): the only study that *isolates* the
  experienced+familiar condition, and it shows **+19% completion time (slower)** in early
  2025 — retired; the late-2025 follow-up point-estimates −18% but is uninterpretable.

The implication for the user, who is experienced and works in familiar codebases, is
direct: **the population for which evidence is strongest that AI *helps* is not the
user's population.** The population that matches the user has the weakest (or negative)
measured effect. (Claim confidence: medium — METR is one study, now superseded by an
unreliable update; Cui/Demirer's senior subgroup is underpowered.)

### Q4 — Why the evidence conflicts

The conflicts are **not contradictions** — they are **different questions** answered by
**different methods on different populations with different metrics**:

- **Population**: juniors/transitions (Peng) → large positive; experienced OSS maintainers
  (METR) → negative; enterprise mixed-tenure (Cui/Demirer, NAV IT) → small positive to null.
- **Metric**: time-to-task (Peng, METR) vs activity throughput (Cui/Demirer, NAV IT) vs
  self-report (DORA, METR survey). A 26% increase in pull requests is not a 26% reduction
  in task time.
- **Tool era**: 2022 Copilot autocomplete (Peng, Cui/Demirer) → early-2025 Cursor + Claude
  3.5/3.7 (METR) → late-2025 agentic Claude Code/Codex (METR update). Capabilities changed;
  so did the relevant comparison.
- **Task realism**: lab single-task vs real PRs with quality bars. METR's own framing
  table makes this explicit (Source: [[sources/metr-early-2025-rct]]).

Once you control for these, the studies largely agree: **AI helps most on simple,
greenfield, well-specified work, for less-experienced developers, measured by
throughput or self-report; it helps least (and may hurt) on real, existing-codebase work
for experienced developers, measured by time or organizational delivery.**

### Q5 — Non-speed effects (defects, review, comprehension, maintenance)

This is where the evidence is **most consistently negative**:

- **Delivery stability**: a 25% increase in AI adoption associates with **-7.2%
  delivery stability** and -1.5% throughput at org level, despite +3.4% self-reported
  code quality (Source: [[sources/dora-2024-report]]).
- **Code maintainability**: cloned code rose 8.3%→12.3%; refactored/reused lines fell
  25%→<10% over the AI-adoption period (Source: [[sources/gitclear-code-quality-2025]]).
- **AI refactoring degrades metrics**: in 403 AI-agent refactoring commits,
  Maintainability Index decreased in **56.1%** and Cyclomatic Complexity increased in
  **42.7%** (Source: [[sources/horikawa-readability-2026]]). Independent, peer-reviewed.
- **Comprehension**: AI group scored 17% lower on a quiz on material they'd just coded,
  largest gap on debugging (Source: [[sources/anthropic-skill-formation-rct]]).
- **Trial-and-error coding**: +38% builds with no build-success improvement; Accenture
  showed -20.72% build success rate (Source:
  [[sources/cui-demirer-mit-copilot-field-experiments]]).

The pattern: **speed/throughput locally up; maintainability, stability, and
comprehension down or unclear.** This is the "productivity paradox" the user
anticipated. **The maintenance axis is mixed, not uniformly negative**: Xu et al. (found
by the second opinion) report AI shifts maintenance burden onto experienced devs,
reducing their productivity — directly on the user's condition; but Sawada et al. (also
from the second opinion) find agent-generated files received *less* frequent maintenance
in their study, a counterpoint. Net: non-speed effects skew negative across more sources
(DORA, GitClear, Horikawa, Anthropic, BNY Mellon, Xu) but not unanimously (Sawada), and
the non-speed evidence is correlational/preprint-grade.

### Q6 — Self-reported vs. measured divergence (the key finding)

**This is the most robust cross-study result and exactly what the user predicted.**

- METR RCT: forecast +24%, self-report after +20%, measured -19%. **~40-point gap**
  (Source: [[sources/metr-early-2025-rct]]).
- NAV IT: subjective experience positive, commit activity unchanged (Source:
  [[sources/nav-it-longitudinal-study]]).
- DORA: self-report +code quality, delivery stability -7.2% (Source:
  [[sources/dora-2024-report]]).
- METR 2026 survey: median self-report 1.4–2x value (3x speed); METR explicitly says
  "survey results are not necessarily grounded in reality" and that surveys "have
  tended to be greater than those from field experiments" (Source:
  [[sources/metr-2026-self-report-survey]]).

**The divergence is not a quirk of one study. It replicates across an RCT, a
longitudinal field study, an industry survey, and the survey-vs-experiment literature
meta-comparison.** Developers — especially experienced ones — systematically
overestimate how much AI speeds them up. The user's instruction to look for exactly
this divergence was well-founded.

## What the web CANNOT settle (mandatory section)

Every "is this right **for me**" claim is unanswerable from web evidence. Named:

1. **Does AI make Gabriel faster on his codebase?** — Gabriel's codebase, task mix, and
   AI fluency are unique. METR's experienced-dev result is the closest proxy and is (a) a
   different population, (b) early-2025 tools, (c) now superseded. No web source can
   answer this. **Local evaluation required** (see decision-guide.md §"The experiment
   you must run").
2. **Does AI make Gabriel's *system* faster (delivery, defects)?** — DORA's
   org-level instability finding may or may not apply to a solo/small-team workflow.
3. **Will the late-2025/2026 positive trajectory continue?** — extrapolation, not
   measurement.
4. **Whether Gabriel is an outlier** — the METR RCT had high variance; some devs may
   genuinely benefit. The study cannot say which devs.

These are not disclaimers — for a *fit* question, **the local evaluation IS the
answer**, and no amount of searching substitutes for it. See decision-guide.md.

## Caveats on the synthesis itself

- METR (-19%) is one RCT, n=16 devs, now superseded by an unreliable update. It is the
  *only* RCT on the user's exact condition; do not over-rely on the single number, but
  note the *direction* (experienced+familiar = small/negative) is corroborated by
  Cui/Demirer's underpowered senior subgroup.
- The late-2025 agentic-tool era is under-measured. METR's qualitative belief
  (interviews) is that devs are faster now, but the RCT data is broken by selection. The
  current state is genuinely uncertain.
- Non-speed effects (DORA, GitClear, Horikawa) are correlational/observational; they
  show consistent direction but not causation.
- The vendor studies (Peng, Anthropic) are capped at medium per Gate 4.5. Anthropic's
  comprehension finding is unusually candid for a vendor to publish, which slightly
  raises its credibility despite the vendor label.

## Confidence summary

Calibrated to the three-value scale (high/medium/low) per the review panel. No vendor
performance claim exceeds medium.

- **High**: self-reported vs. measured divergence exists and is systematic (replicates
  across an RCT, a longitudinal field study, an industry survey, a BNY Mellon mixed-methods
  study, and the survey-vs-experiment literature meta-comparison).
- **Medium**: effect-by-task-type gradient (lab/greenfield > field/existing) — direction is
  robust across studies, but the magnitude rests partly on vendor lab (Peng) and
  mixed-independence field RCT (Cui/Demirer). Heterogeneity toward juniors — consistent
  across two studies but the senior subgroups are underpowered and no independent
  non-vendor measured study isolates the junior-vs-senior gradient. Non-speed effects skew
  negative (correlational, consistent direction across DORA, GitClear, Horikawa, Gao
  review, BNY Mellon).
- **Low**: the magnitude of the *current* (late-2025/2026, agentic) speed effect for
  experienced devs on familiar code — the only direct attempt (METR late-2025) is
  uninterpretable due to selection. The fit question for the user — structurally
  unanswerable from web evidence.