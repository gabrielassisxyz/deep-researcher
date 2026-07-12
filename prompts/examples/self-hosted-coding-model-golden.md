# Golden Test Prompt: A Cheap Default Model For My Agent Harness

> **What this prompt is for.** The other golden prompt (`llm-models-golden.md`) hands the
> agent a list of 15 models and 5 aggregator URLs, and the first real run answered it by
> scraping the official page of each model on the list — 21 sources, zero search queries,
> a list read back to the user. This prompt is built to make that failure impossible to
> repeat and easy to detect: it **names almost nothing**, so the units of analysis have to
> be *discovered*; it asks a question vendors are the worst possible witnesses for; and it
> ends in a **fit** claim, which the web cannot settle at all.

## Primary Objective

I run coding agents through several harnesses (opencode, pi, Claude Code, Codex) against a
LiteLLM proxy. I want to pick a **cheap default model** for the bulk of my agent work —
the model that runs first on any task, before anything gets escalated.

The decision I want to support: **which model should be the default executor, and at what
point is escalating to a frontier model actually paying for itself?**

## What I Am Deliberately Not Telling You

I am not giving you a candidate list, and that is on purpose.

Part of the research is finding out **which models are even in the running** — including
the ones I have never heard of. If you end up evaluating only models that are famous
enough for me to have named them unprompted, you have done retrieval, not research.

I am also not giving you starting URLs. Find the sources.

## Constraints That Should Shape The Answer

- **Budget matters more than ceiling.** This model runs on nearly every task, so price per
  token dominates. A model that is 3% better and 10x the price is a bad default.
- **It must hold up over long, multi-file work in a real repository** — not one-shot
  benchmark tasks. This is the axis I most distrust benchmark numbers on.
- **Open weights are a plus, not a requirement.** I have a homelab, but a single RX 580;
  assume I am calling hosted APIs unless local inference is genuinely viable.
- **Tool calling and instruction adherence are non-negotiable.** A model that writes lovely
  code and cannot reliably call a tool is useless in an agent loop.

## Required Outputs

- The candidate set you **discovered**, and the ones you rejected, with reasons. I want to
  see the ones that did not make the cut.
- A routing recommendation: the default executor, and the escalation rule.
- A cost model: what this actually costs at my volume, versus a frontier-only baseline.
- **An explicit statement of what you could not settle.** See below.

## What I Expect You To Tell Me You Cannot Answer

The real question underneath this one is *"which model is best **for my** work"* — my repos,
my task mix, my harnesses. **No amount of web research answers that**, and I would rather
have that said plainly than have an inference from a leaderboard dressed up as a finding.

So: when you hit that wall, name it, and give me the **evaluation I would have to run** to
settle it — the task set, the scoring, and the number of runs it would take to mean anything.

A dossier that ends in "here is the experiment you need to run, and here is why the web
cannot substitute for it" is a **success**, not a failure.

## How I Will Judge This Run

Not by whether the answer is agreeable, but by the audit trail:

- Is the search ledger in `log.md` non-empty, with the fruitless queries in it too?
- Did discovery surface units of analysis that are absent from this prompt?
- Did every high-impact gap reach `resolved` or `blocked` — with no `partially resolved`
  hiding an early exit?
- Is any performance claim resting on a vendor's own page at `high` confidence?
- Is the fit question named as unanswerable, rather than quietly answered?
