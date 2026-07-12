# Available reviewers

The models that can serve as a **second opinion** (Gate 8.4, exactly one) or sit on the
**review panel** (Gate 8.5, any number). Same catalogue for both; they differ only in how
many you pick and what they see.

Verified on this machine, 2026-07-12. If a harness is not installed, its entries are not
available — `scripts/review-panel` marks a reviewer it cannot invoke as `blocked` and carries
on with the rest of the panel rather than pretending it ran.

| Selector | Model | Harness | Cost |
| --- | --- | --- | --- |
| `claude:opus` | Claude Opus | Claude Code | frontier |
| `claude:sonnet` | Claude Sonnet | Claude Code | frontier |
| `codex` | GPT-5.5 | Codex | frontier |
| `agy` | Gemini 3.1 Pro | Antigravity | frontier |
| `agy:flash` | Gemini 3.5 Flash | Antigravity | cheap |
| `pi:glm-5.2` | GLM-5.2 | pi → LiteLLM | cheap, open-weight |
| `pi:glm-5.1` | GLM-5.1 | pi → LiteLLM | cheap, open-weight |
| `pi:kimi-k2.7` | Kimi K2.7 | pi → LiteLLM | cheap, open-weight |
| `pi:deepseek-v4-flash-max` | DeepSeek V4 Flash | pi → LiteLLM | cheapest, open-weight |
| `pi:deepseek-v4-pro-high` | DeepSeek V4 Pro | pi → LiteLLM | cheap, open-weight |

## Picking a panel

**Diversity of training beats raw capability.** Three checkpoints of the same family share
their blind spots, and a panel that shares blind spots is an expensive way to feel reassured
— it will agree with itself about exactly the things it is collectively wrong about. Prefer
one model from each lineage over three from the best one.

- **Default panel** — `pi:glm-5.2 pi:kimi-k2.7 pi:deepseek-v4-pro-high`. Three different
  labs, all cheap. Good enough for most dossiers.
- **High-stakes panel** — `claude:opus agy codex`. Three frontier models, three vendors.
  Expensive; worth it when the decision is.
- **Mixed** — `claude:opus pi:kimi-k2.7 agy:flash`. One frontier reader plus two cheap ones
  from unrelated lineages.

## Picking a second opinion

Only one, and it re-runs the *entire research* — so this is the expensive check, not the
panel. Pick a model **from a different lineage than the one that did the research**: an
independent look is the whole point, and the same family will tend to miss the same things.

If the research ran on `pi:glm-5.2`, a good second opinion is `codex` or `claude:opus`.

## Turning them off

Both are optional, and the workflow will say so rather than pretending otherwise.

- **Skipping the second opinion** is normal. It doubles the cost of the research for a check
  that mostly matters when the option set is uncertain.
- **Skipping the review panel is allowed, and it is not recommended.** A review is one read
  of a finished dossier — the cheapest possible check, and the last thing standing between a
  confident-sounding dossier and a wrong decision. Skip it to save money if you must, and
  know that you are trading away the one gate that catches a plausible, well-cited,
  incorrect answer.
- When either is skipped, the dossier must **say** it was skipped — in `log.md` and in the
  final answer. A dossier that quietly omits mentioning it was never reviewed reads exactly
  like one that passed review.
