# Reviewers

Two of the gates call a *different* model than the one doing the research:

- **Second opinion** (Gate 8.4) — **one** model, re-researches the questions from scratch
  without seeing the dossier. Attacks **omission**: the candidate nobody considered, which a
  reviewer reading the finished dossier structurally cannot see.
- **Review panel** (Gate 8.5) — **any number** of models, critiquing the finished dossier.
  Attacks **error**. This is where triangulation belongs, because reviewing is one read of a
  document — cheap enough to buy several — and disagreement *between reviewers* is itself
  signal.

Both are optional. Both draw from the same catalogue: **whatever this machine actually has.**

## Find out what you have

```sh
scripts/detect-reviewers
```

It reports the agent CLIs on your PATH and, if a LiteLLM proxy is running, the models it
serves. **Run it before your first research — do not trust an example.** The selectors below
are what *one* setup produced; yours will differ, and picking a reviewer you do not have gets
you a `blocked` reviewer and a smaller panel than you thought you had.

## Selector syntax

| Form | Means |
| --- | --- |
| `claude:opus`, `claude:sonnet` | Claude Code, that model alias |
| `codex` | Codex |
| `agy`, `agy:flash` | Antigravity (`agy models` lists its models) |
| `pi:<model>` | pi, calling `<model>` through a local LiteLLM proxy |

Example of what `detect-reviewers` might print on a machine with everything installed:

```
claude:opus  claude:sonnet  codex  agy  agy:flash
pi:glm-5.2   pi:kimi-k2.7   pi:deepseek-v4-flash-max   pi:deepseek-v4-pro-high
```

An empty catalogue is a legitimate answer: with no second harness installed, both gates are
simply unavailable, and the workflow says so rather than pretending a review happened.

## Picking a panel

**Diversity of training beats raw capability.** Three checkpoints of the same family share
their blind spots, and a panel that shares blind spots is an expensive way to feel reassured
— it will agree with itself about exactly the things it is collectively wrong about. Prefer
one model per lineage over three from the best one.

- **Cheap panel** — three different labs, all inexpensive (e.g. a GLM, a Kimi, a DeepSeek
  through LiteLLM). Good enough for most dossiers.
- **High-stakes panel** — three frontier models from three vendors (e.g. Claude, GPT, Gemini).
  Expensive; worth it when the decision is.
- **Mixed** — one frontier reader plus two cheap ones from unrelated lineages.

## Picking a second opinion

One only, and it re-runs the **entire research** — so this, not the panel, is the expensive
check. Pick a model from a **different lineage than the one that did the research**: an
independent look is the whole point, and the same family tends to miss the same things.

## Turning them off

- **Skipping the second opinion is normal.** It roughly doubles the cost of the research, for
  a check that matters most when the option set itself is uncertain.
- **Skipping the review panel is allowed and is not recommended.** A review is the cheapest
  check there is, and the last thing standing between a confident, well-cited, *wrong* dossier
  and a decision made on it.
- **Either way, the dossier must say which checks ran** — in `log.md` and in the final answer.
  An unreviewed dossier that never mentions it went unreviewed reads exactly like one that
  passed review, and that is the more dangerous of the two.

## When a reviewer fails

`scripts/review-panel` records it as `blocked` and carries on with the rest of the panel. It is
never silently dropped: a panel of three that quietly became a panel of two would still have
its consensus scored against a denominator of three, and "two of three reviewers agree" would
then mean something it does not mean.
