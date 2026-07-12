#!/usr/bin/env python3
"""Cross-reference the panel's findings tables and compute what they agree on.

WHY group by target rather than by wording: two reviewers who spot the same problem will
describe it in different words, so text similarity would either miss the overlap or invent
it. The *target* — the file, or the file and line, that a finding challenges — is the one
thing they must state identically to be talking about the same thing. Grouping on it is
crude, and crude is exactly right here: it under-reports agreement rather than manufacturing
it, and a false "they all agree" is the one output that would make this whole exercise worse
than useless.

Read from $OUT (the panel round directory), writes consensus.md there.
"""
import os
import pathlib
import re
from collections import defaultdict

OUT = pathlib.Path(os.environ["OUT"])
ROUND = os.environ.get("ROUND", "1")

SEVERITY_ORDER = {"critical": 0, "major": 1, "minor": 2}


def parse_report(path: pathlib.Path):
    """Pull (severity, target, finding, reviewer) rows out of a report's findings table."""
    text = path.read_text(errors="replace")

    reviewer = path.stem
    m = re.search(r"^reviewer:\s*(.+)$", text, re.M)
    if m:
        reviewer = m.group(1).strip()

    verdict = "unknown"
    m = re.search(r"^verdict:\s*([a-z-]+)", text, re.M | re.I)
    if m:
        verdict = m.group(1).strip().lower()
    elif re.search(r"^status:\s*blocked", text, re.M | re.I):
        verdict = "blocked"

    rows = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|") or line.startswith("| ---") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 4:
            continue
        severity = cells[1].lower()
        if severity not in SEVERITY_ORDER:
            continue  # header row, or a table that is not the findings table
        rows.append({
            "severity": severity,
            "target": cells[2],
            "finding": cells[3],
            "reviewer": reviewer,
        })
    return reviewer, verdict, rows


def normalize_target(target: str) -> str:
    """`synthesis.md:42` and `synthesis.md:47` are the same neighbourhood; treat them as one.

    Line numbers drift between reviewers reading the same file — one cites the claim, another
    cites the sentence above it. Collapsing to the file keeps them in the same bucket. The
    cost is that two genuinely different problems in one long file merge; the benefit is that
    the same problem, cited two lines apart, does not read as two independent findings and
    silently fail to reach consensus.
    """
    return target.split(":")[0].strip().strip("`")


reports = sorted(p for p in OUT.glob("*.md") if p.name != "consensus.md")
if not reports:
    raise SystemExit(f"no reviewer reports in {OUT}")

reviewers, verdicts, all_rows = [], {}, []
for path in reports:
    reviewer, verdict, rows = parse_report(path)
    reviewers.append(reviewer)
    verdicts[reviewer] = verdict
    all_rows.extend(rows)

live = [r for r in reviewers if verdicts[r] != "blocked"]
blocked = [r for r in reviewers if verdicts[r] == "blocked"]

groups = defaultdict(list)
for row in all_rows:
    groups[normalize_target(row["target"])].append(row)

consensus, singles = [], []
for target, rows in groups.items():
    who = sorted({r["reviewer"] for r in rows})
    worst = min(rows, key=lambda r: SEVERITY_ORDER[r["severity"]])
    entry = {
        "target": target,
        "severity": worst["severity"],
        "count": len(who),
        "who": who,
        "findings": rows,
    }
    (consensus if len(who) >= 2 else singles).append(entry)

consensus.sort(key=lambda e: (-e["count"], SEVERITY_ORDER[e["severity"]]))
singles.sort(key=lambda e: SEVERITY_ORDER[e["severity"]])

lines = [
    "---",
    "type: review-consensus",
    f"round: {ROUND}",
    f"reviewers: {len(reviewers)}",
    f"blocked: {len(blocked)}",
    "---",
    "",
    f"# Review Panel — Consensus — Round {ROUND}",
    "",
    f"**Panel:** {', '.join(reviewers)}",
    f"**Verdicts:** " + ", ".join(f"{r} = `{verdicts[r]}`" for r in reviewers),
    "",
]

if blocked:
    lines += [
        f"> **{len(blocked)} of {len(reviewers)} reviewers failed to run** "
        f"({', '.join(blocked)}). This panel is smaller than it was configured to be — do "
        "not report its verdict as though every reviewer agreed.",
        "",
    ]

if len(live) < 2:
    lines += [
        "> **Fewer than two reviewers completed, so there is no consensus to compute.** "
        "Every finding below is a single opinion. Triage them on their merits, and do not "
        "let the presence of this file suggest a panel reviewed anything.",
        "",
    ]

lines += [
    "## Consensus findings — raised by 2 or more reviewers",
    "",
    "**Fix these, or refute them in writing with evidence.** Independent reviewers converging "
    "on the same target is the strongest signal this panel produces; disagreeing with a "
    "majority of them silently is not an option.",
    "",
]

if consensus:
    lines += ["| Target | Severity | Reviewers | What they said |", "| --- | --- | --- | --- |"]
    for e in consensus:
        said = "<br>".join(f"**{r['reviewer']}:** {r['finding']}" for r in e["findings"])
        lines.append(f"| `{e['target']}` | {e['severity']} | {e['count']}/{len(live)} — {', '.join(e['who'])} | {said} |")
else:
    lines.append("_None. No target was flagged by two or more reviewers._")

lines += [
    "",
    "## Single-reviewer findings — triage on merit",
    "",
    "One reviewer saw this and the others did not. That cuts both ways: it may be a sharp "
    "catch only one model was equipped to make, or it may be that model's bias. Decide "
    "explicitly, and record which — do not let these quietly expire.",
    "",
]

if singles:
    lines += ["| Target | Severity | Reviewer | Finding |", "| --- | --- | --- | --- |"]
    for e in singles:
        r = e["findings"][0]
        lines.append(f"| `{e['target']}` | {e['severity']} | {r['reviewer']} | {r['finding']} |")
else:
    lines.append("_None._")

lines += [
    "",
    "## Contradictions",
    "",
    "Where reviewers disagree **with each other** about the same target, the dossier is not "
    "the authority and neither is the reviewer you find most agreeable. **That is a gap:** "
    "send it back into the Gate 5/6 loop and let evidence settle it.",
    "",
]

contradictions = [
    e for e in consensus
    if len({r["severity"] for r in e["findings"]}) > 1
]
if contradictions:
    for e in contradictions:
        sevs = ", ".join(f"{r['reviewer']} says `{r['severity']}`" for r in e["findings"])
        lines.append(f"- `{e['target']}` — {sevs}. Reviewers do not agree on how bad this is.")
else:
    lines.append("_No reviewer graded the same target at conflicting severities._")

lines.append("")
(OUT / "consensus.md").write_text("\n".join(lines))

print(f"  reviewers: {len(reviewers)} ({len(blocked)} blocked)")
print(f"  consensus findings: {len(consensus)}")
print(f"  single-reviewer findings: {len(singles)}")
