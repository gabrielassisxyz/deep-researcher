---
type: evidence-ledger
slug: ai-coding-productivity
created: 2026-07-12
updated: 2026-07-12
---

# Evidence Ledger

Claim-level evidence. Each claim cites source notes. Confidence per Gate 4.5 claim typing.

## Q1. Controlled/measured evidence on AI coding tools and developer speed

### Claim 1.1 — Early-2025 frontier AI made experienced OSS devs 19% SLOWER on familiar repos
- Source: [[sources/metr-early-2025-rct]]
- Method: RCT, 16 devs, 246 tasks, within-subject randomization, Cursor + Claude 3.5/3.7.
- Effect: +19% completion time (CI +2% to +39%). Robust across estimators.
- Claim type: Performance. Independence: independent (METR nonprofit).
- Confidence: **high** (for the early-2025 setting).
- Recency caveat: METR says this is now outdated ([[sources/metr-late-2025-uplift-update]]).

### Claim 1.2 — In late-2025, the slowdown narrowed / possibly reversed, but data is unreliable
- Source: [[sources/metr-late-2025-uplift-update]]
- Effect: original-dev subset 18% speedup (CI -38% to +9%); new-dev subset 4% speedup
  (CI -15% to +9%).
- Selection effects (devs refuse to work without AI; tasks withheld) bias the estimate
  downward; METR gives only "very weak evidence" of size.
- Claim type: Performance. Confidence: **low** for the number; **medium** for direction
  (less slowdown than early-2025).

### Claim 1.3 — Copilot autocomplete on a single greenfield JS task: 55.8% faster (lab)
- Source: [[sources/github-copilot-55-percent-study]]
- Vendor study, lab setting, single self-contained task.
- Claim type: Performance. Independence: vendor → capped medium.
- Confidence: **medium** (for this exact task type); **low** for generalization.

### Claim 1.4 — Copilot autocomplete in real workplaces: +26.08% tasks/week (field RCT)
- Source: [[sources/cui-demirer-mit-copilot-field-experiments]]
- 3 RCTs, 4,867 devs, Microsoft/Accenture/Fortune-100. IV estimates.
- Metric is activity (PRs/commits/builds), not time-to-ship or value.
- Claim type: Performance. Independence: mixed (vendor data, independent academic
  analysis, pre-registered).
- Confidence: **medium** for the throughput effect on the pooled (junior-heavy)
  population (mixed independence, vendor data, activity-not-time metric); the
  senior/experienced effect is small and non-significant.

### Claim 1.5 — No statistically significant change in commit activity after Copilot adoption (NAV IT)
- Source: [[sources/nav-it-longitudinal-study]]
- Observational, 2 years, 26,317 commits, 25 users vs 14 non-users.
- Claim type: Performance. Confidence: **medium** (single org, activity proxy).

## Q2. Effect by task type (greenfield vs. existing, boilerplate vs. novel, specified vs. ambiguous)

### Claim 2.1 — Lab/greenfield/well-specified tasks show large positive effects; real-work/existing-codebase tasks show smaller or negative effects
- Sources: [[sources/github-copilot-55-percent-study]] (55.8% lab), [[sources/cui-demirer-mit-copilot-field-experiments]] (26% field; authors explicitly note field < lab), [[sources/metr-early-2025-rct]] (-19% on real OSS PRs with high quality standards).
- Claim type: Performance. Confidence: **medium** for the direction (effect size
  shrinks as task realism / existing-codebase / quality-standards increase).
- This is one of the strongest cross-study patterns in the dossier.

### Claim 2.2 — On novel/unfamiliar logic, AI gives no significant speedup AND reduces comprehension
- Source: [[sources/anthropic-skill-formation-rct]]
- 52 mostly-junior devs, Trio (unfamiliar lib). AI group: ~2 min faster (ns); quiz 17%
  lower (sig, d=0.738).
- Claim type: Performance. Confidence: **medium** (vendor but RCT, small n, short-term).

### Claim 2.3 — Agentic tools may be more helpful than autocomplete on the right tasks, but evidence is thin
- Source: [[sources/metr-late-2025-uplift-update]] (qualitative belief from interviews that
  late-2025 agentic tools sped devs up, but RCT data unreliable).
- Claim type: Performance. Confidence: **low** (self-report + broken RCT).

## Q3. Effect by developer experience and codebase familiarity

### Claim 3.1 — Gains concentrate in less-experienced / junior / short-tenure developers
- Sources: [[sources/github-copilot-55-percent-study]] ("help people transition into
  software development"), [[sources/cui-demirer-mit-copilot-field-experiments]]
  (short-tenure +27-39% vs long-tenure +8-13%; junior +21-40% vs senior +7-16%; less
  productive devs gain more).
- Claim type: Performance. Confidence: **medium** (consistent across two studies,
  though senior subgroups underpowered; the gradient rests partly on vendor lab and
  mixed-independence field data).
- This is the most robust heterogeneity finding.

### Claim 3.2 — For experienced developers on codebases they know well, measured effect is small or negative (and the current state is unmeasured)
- Sources: [[sources/metr-early-2025-rct]] (experienced, familiar repos: +19% slower,
  early-2025, now retired), [[sources/metr-late-2025-uplift-update]] (late-2025 agentic
  point-estimate −18% faster, uninterpretable), [[sources/cui-demirer-mit-copilot-field-experiments]]
  (senior/long-tenure: small, ns throughput effect).
- Claim type: Performance. Confidence: **medium** for the *direction* in early 2025
  (experienced+familiar saw a slowdown in the one clean RCT, and the senior subgroup in
  the field RCT was small/ns); **low** for the *current* state (the only late-2025
  measurement is uninterpretable).
- **This is the crux for the user's decision — and the honest answer is that the current
  state is unmeasured.**

## Q4. Why evidence conflicts

### Claim 4.1 — Conflicts are explained by population, task realism, metric, and tool generation (methodology inference)
- Populations: juniors/transitions (Peng) vs experienced OSS maintainers (METR) vs
  enterprise mixed-tenure (Cui/Demirer).
- Task realism: lab single-task (Peng) vs real PRs with quality bars (METR) vs weekly PR
  counts (Cui/Demirer).
- Metrics: time-to-task (Peng, METR) vs activity throughput (Cui/Demirer, NAV IT) vs
  self-report (surveys, DORA).
- Tool era: 2022 Copilot autocomplete (Peng, Cui/Demirer) vs early-2025 Cursor+Claude
  (METR) vs late-2025 agentic Claude Code/Codex (METR update).
- Claim type: **Methodology/inference** (cross-study comparison, not a single-source fact
  and not a user-specific fit claim). Confidence: **medium** — the inference is sound and
  the studies articulate these distinctions themselves, but it is an inference across
  studies with different designs, not a measured result.

## Q5. Non-speed effects (defects, review, comprehension, maintenance)

### Claim 5.1 — AI adoption at org level correlates with WORSE delivery stability and throughput, despite positive self-report
- Source: [[sources/dora-2024-report]]
- 25% increase in AI adoption ↔ -1.5% delivery throughput, -7.2% delivery stability.
  Simultaneously +3.4% self-reported code quality, +3.1% review speed.
- Claim type: Performance. Independence: mixed (Google-sponsored, independent program).
- Confidence: **medium** (large survey, correlational; the divergence is the finding).

### Claim 5.2 — AI-era code shows more duplication, less refactoring/reuse
- Source: [[sources/gitclear-code-quality-2025]]
- Cloned lines 8.3%→12.3% (2021→2024); moved/refactored lines 25%→<10%.
- Claim type: Performance. Confidence: **medium** (large dataset, correlational).

### Claim 5.3 — AI assistance reduces comprehension of novel material, especially debugging
- Source: [[sources/anthropic-skill-formation-rct]]
- 17% lower quiz score, largest gap on debugging.
- Claim type: Performance. Confidence: **medium** (vendor RCT, small n, short-term).

### Claim 5.4 — More builds/trial-and-error may indicate lower-quality coding style
- Source: [[sources/cui-demirer-mit-copilot-field-experiments]]
- +38.38% builds with no commensurate build-success improvement; authors flag this as a
  possible "trial-and-error" signal. Accenture showed -20.72% build success rate.
- Claim type: Performance. Confidence: **medium** (speculative, one site; single-site
  speculative signal).

### Claim 5.5 — AI-generated code has documented, patterned bug/defect types (systematic review)
- Source: [[sources/gao-survey-bugs-ai-code]] (Round 3)
- Systematic literature review consolidating scattered bug/defect findings in
  AI-generated code; classifies bug types by model; discusses remediation.
- Claim type: Performance. Confidence: **medium** (independent systematic review;
  aggregates rather than measures anew; corroborates the direction of 5.1–5.4).

### Claim 5.6 — Long-term factors (technical expertise, ownership) are undercounted by short-term metrics
- Source: [[sources/beyond-the-commit-bny-mellon]] (Round 3)
- BNY Mellon, 2,989 devs + 11 interviews. Survey responses show **conflicting
  perspectives** on AI usefulness; interviews elicit six factors, highlighting long-term
  metrics (technical expertise, ownership of work) that short-term speed/commit metrics
  miss. "In contrast to prior work..."
- Claim type: Performance/methodology. Confidence: **medium** (large survey,
  peer-reviewed ICSE SEIP, but self-report + qualitative).

### Claim 5.7 — AI shifts maintenance burden onto experienced developers, reducing their productivity
- Source: [[sources/xu-maintenance-burden-2025]] (found by second opinion)
- AI-assisted programming decreases experienced-dev productivity by increasing technical
  debt/maintenance burden; aggregate gains driven by peripheral devs; core devs carry
  more review/rework and lose original-code productivity.
- Claim type: Performance. Confidence: **medium** (independent, directly on-condition;
  preprint).
- **This is the clearest single-study explanation of *why* AI can slow experienced devs
  even when org metrics look positive.**

### Claim 5.8 — COUNTERPOINT: agent-generated files sometimes require LESS maintenance
- Source: [[sources/sawada-agent-maintenance-2026]] (found by second opinion)
- Agent-generated files received less frequent maintenance than human-authored files in
  this empirical study.
- Claim type: Performance. Confidence: **medium** (independent; proxy metric;
  preprint).
- The maintenance axis is **mixed**, not uniformly negative. This counterpoint is
  included per Gate 8.4 to avoid a one-sided non-speed section.

## Q6. Self-reported vs. measured divergence (the user's predicted key finding)

### Claim 6.1 — Developers' self-reported speedup diverges sharply from measured speedup
- Source: [[sources/metr-early-2025-rct]] — the canonical result (sign convention:
  positive = slower):
  - Forecast: −24% (expected faster).
  - Self-report after: −20% (believed faster).
  - Measured: +19% (actually slower).
  - Gap: ~40 percentage points.
- Corroborated by [[sources/nav-it-longitudinal-study]] (subjective experience diverges
  from commit activity), [[sources/dora-2024-report]] (self-report positive, delivery
  metrics negative), and [[sources/beyond-the-commit-bny-mellon]] (Round 3: conflicting
  perspectives on AI usefulness; long-term costs undercounted).
- Claim type: Performance/methodology. Confidence: **high** — this is the most robust
  cross-study finding in the dossier, replicating across an RCT, a longitudinal field
  study, an industry survey, a BNY Mellon mixed-methods study, and the
  survey-vs-experiment literature meta-comparison. Exactly what the user predicted.

### Claim 6.2 — Even in 2026, with agentic tools, self-report says 1.4–2x value (3x speed) but METR distrusts it
- Source: [[sources/metr-2026-self-report-survey]]
- METR explicitly: "survey results are not necessarily grounded in reality"; "public
  estimates from surveys have tended to be greater than those from field experiments."
- Claim type: Performance. Confidence: **high** that this is what people say; **low** that
  it reflects reality.