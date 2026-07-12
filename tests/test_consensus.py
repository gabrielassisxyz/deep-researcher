"""The consensus computation is the one piece of real logic here, so it gets the tests.

The panel exists because a single reviewer gives you findings with no way to weigh them.
Consensus turns three opinions into a vote — which means the *wrong* answer here is worse
than no answer at all: a false "they all agree" would launder one model's mistake into a
verdict. Every test below is aimed at that failure.
"""

from __future__ import annotations

import os
import pathlib
import subprocess
import sys

SCRIPT = pathlib.Path(__file__).resolve().parent.parent / "scripts" / "consensus.py"


def report(reviewer: str, verdict: str, rows: list[tuple[str, str, str]]) -> str:
    """One reviewer's report: frontmatter plus a findings table."""
    table = "\n".join(
        f"| F{i} | {sev} | {target} | {finding} | why | fix |"
        for i, (sev, target, finding) in enumerate(rows, 1)
    )
    return (
        f"---\nreviewer: {reviewer}\nverdict: {verdict}\n---\n\n"
        "| ID | Severity | Target | Finding | Why | Fix |\n"
        "| --- | --- | --- | --- | --- | --- |\n" + table + "\n"
    )


def run(tmp_path: pathlib.Path, reports: dict[str, str]) -> str:
    for name, text in reports.items():
        (tmp_path / f"{name}.md").write_text(text, encoding="utf-8")
    env = {**os.environ, "OUT": str(tmp_path), "ROUND": "1"}
    subprocess.run([sys.executable, str(SCRIPT)], env=env, check=True, capture_output=True)
    return (tmp_path / "consensus.md").read_text(encoding="utf-8")


def test_two_reviewers_on_the_same_target_reach_consensus(tmp_path):
    """Different line numbers, different words, same file: that is agreement."""
    out = run(tmp_path, {
        "glm": report("pi:glm-5.2", "needs-fixes",
                      [("critical", "synthesis.md:42", "Perf claim cites only the vendor blog.")]),
        "kimi": report("pi:kimi-k2.7", "needs-fixes",
                       [("major", "synthesis.md:47", "The comparison rests on one vendor source.")]),
    })
    consensus = out.split("## Single-reviewer findings")[0]
    assert "`synthesis.md`" in consensus
    assert "2/2" in consensus


def test_a_lone_finding_does_not_become_consensus(tmp_path):
    """The failure that would make the panel worse than useless: manufacturing agreement."""
    out = run(tmp_path, {
        "glm": report("pi:glm-5.2", "needs-fixes",
                      [("critical", "log.md", "Search ledger is empty.")]),
        "kimi": report("pi:kimi-k2.7", "needs-fixes",
                       [("minor", "README.md", "Typo.")]),
    })
    consensus, singles = out.split("## Single-reviewer findings")
    assert "None. No target was flagged by two or more reviewers." in consensus
    assert "`log.md`" in singles
    assert "`README.md`" in singles


def test_reviewers_disagreeing_on_severity_is_reported_as_a_contradiction(tmp_path):
    """Reviewers who cannot agree how bad something is have found a gap, not a finding."""
    out = run(tmp_path, {
        "glm": report("pi:glm-5.2", "needs-fixes",
                      [("critical", "decision-guide.md", "Overstates the recommendation.")]),
        "kimi": report("pi:kimi-k2.7", "needs-fixes",
                       [("minor", "decision-guide.md", "Slightly strong wording.")]),
    })
    contradictions = out.split("## Contradictions")[1]
    assert "`decision-guide.md`" in contradictions
    assert "critical" in contradictions and "minor" in contradictions


def test_a_blocked_reviewer_is_not_counted_as_agreement(tmp_path):
    """A panel of three that quietly became a panel of two must not be scored out of three."""
    out = run(tmp_path, {
        "glm": report("pi:glm-5.2", "needs-fixes",
                      [("critical", "synthesis.md", "Unsupported claim.")]),
        "kimi": report("pi:kimi-k2.7", "needs-fixes",
                       [("major", "synthesis.md", "Same claim, no source.")]),
        "agy": "---\nreviewer: agy\nverdict: blocked\n---\n\nCould not be invoked.\n",
    })
    assert "1 of 3 reviewers failed to run" in out
    assert "2/2" in out  # scored against the reviewers who actually ran


def test_a_panel_of_one_refuses_to_look_like_a_panel(tmp_path):
    """The dangerous case: a consensus.md exists, so it reads as though a panel reviewed."""
    out = run(tmp_path, {
        "glm": report("pi:glm-5.2", "needs-fixes",
                      [("critical", "synthesis.md", "Unsupported claim.")]),
        "kimi": "---\nreviewer: pi:kimi-k2.7\nverdict: blocked\n---\n\nCould not be invoked.\n",
        "agy": "---\nreviewer: agy\nverdict: blocked\n---\n\nCould not be invoked.\n",
    })
    assert "Fewer than two reviewers completed" in out
    assert "do not let the presence of this file suggest a panel reviewed anything" in out
