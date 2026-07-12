"""SQLite FTS5 search index over a captured corpus.

Built from the on-disk corpus (pages.jsonl + pages/*.md) so it can be regenerated
independently of a crawl. Full rebuild each time keeps it deterministic and simple.
"""

from __future__ import annotations

import json
import re
import sqlite3
from dataclasses import dataclass
from pathlib import Path

from . import frontmatter, paths

_CREATE = """
CREATE VIRTUAL TABLE pages_fts USING fts5(
    page_id UNINDEXED,
    source_url UNINDEXED,
    title,
    headings,
    section,
    categories,
    body,
    tokenize = 'porter unicode61'
);
"""

# Column weights for bm25 ranking (a match in the title matters far more than one
# buried in a long body). Order matches the table columns; UNINDEXED columns get 0.
# Lower bm25 = more relevant, so heavier weight pulls those matches to the top.
_BM25_WEIGHTS = (0.0, 0.0, 10.0, 5.0, 3.0, 4.0, 1.0)
# Zero-based index of the body column, for snippet() extraction.
_BODY_COLUMN = 6

# Only the lead of each page's prose is indexed. FTS5's bm25 normalizes by whole-
# document length, so a 150KB stat-table page would drown a title/heading match in
# length penalty and rank below tiny pages. Capping the indexed prose lets the
# title/heading boost actually bite. Headings are still extracted from the FULL
# body, so page structure stays searchable — only deep prose is dropped from search.
_BODY_INDEX_CHARS = 6000

# FTS5 treats bareword punctuation as syntax; keep only alphanumeric run tokens.
_TERM_RE = re.compile(r"[^\w]+", re.UNICODE)
# ATX headings (## Title) and the '=' underline of a Setext h1. The '-' Setext
# form is skipped: it collides with horizontal rules and markdown table separators.
_ATX_HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*$")


class IndexError_(RuntimeError):
    """Raised when the index cannot be built (e.g. SQLite lacks FTS5)."""


@dataclass(frozen=True, slots=True)
class SearchHit:
    page_id: str
    title: str
    section: str
    source_url: str
    snippet: str


def build_index(slug: str, data_root: Path | str = paths.DEFAULT_DATA_ROOT) -> int:
    """(Re)build index.sqlite from the corpus on disk. Returns rows indexed."""
    jsonl = paths.pages_jsonl(slug, data_root)
    if not jsonl.exists():
        raise IndexError_(f"no corpus at {jsonl}; run a crawl first")

    db_path = paths.index_db(slug, data_root)
    db_path.unlink(missing_ok=True)
    page_dir = paths.pages_dir(slug, data_root)

    conn = sqlite3.connect(db_path)
    try:
        try:
            conn.execute(_CREATE)
        except sqlite3.OperationalError as exc:
            raise IndexError_(f"SQLite FTS5 unavailable: {exc}") from exc
        rows = 0
        for line in jsonl.read_text(encoding="utf-8").splitlines():
            record = json.loads(line)
            _, body = frontmatter.parse((page_dir / f"{record['page_id']}.md").read_text(encoding="utf-8"))
            conn.execute(
                "INSERT INTO pages_fts "
                "(page_id, source_url, title, headings, section, categories, body) "
                "VALUES (?, ?, ?, ?, ?, ?, ?)",
                (record["page_id"], record["source_url"], record["title"],
                 _extract_headings(body), record["section"],
                 " ".join(record.get("categories", [])), body[:_BODY_INDEX_CHARS]),
            )
            rows += 1
        conn.commit()
        return rows
    finally:
        conn.close()


def search(slug: str, query: str, limit: int = 5, data_root: Path | str = paths.DEFAULT_DATA_ROOT) -> list[SearchHit]:
    """Return up to ``limit`` pages ranked by BM25 relevance to ``query``."""
    db_path = paths.index_db(slug, data_root)
    if not db_path.exists():
        raise IndexError_(f"no index at {db_path}; build it first")
    terms = _fts_terms(query)
    if not terms:
        return []

    conn = sqlite3.connect(db_path)
    try:
        # Require all terms first (precise); if nothing matches a multi-word,
        # natural-language query, fall back to any-term and let bm25 rank.
        hits = _run_match(conn, " ".join(terms), limit)
        if not hits and len(terms) > 1:
            hits = _run_match(conn, " OR ".join(terms), limit)
        return hits
    finally:
        conn.close()


def _run_match(conn: sqlite3.Connection, match: str, limit: int) -> list[SearchHit]:
    cursor = conn.execute(
        f"""
        SELECT page_id, title, section, source_url,
               snippet(pages_fts, {_BODY_COLUMN}, '', '', ' … ', 12)
        FROM pages_fts
        WHERE pages_fts MATCH ?
        ORDER BY bm25(pages_fts, {", ".join(str(w) for w in _BM25_WEIGHTS)})
        LIMIT ?
        """,
        (match, limit),
    )
    return [SearchHit(*row) for row in cursor.fetchall()]


def _extract_headings(markdown: str) -> str:
    """Collect heading text (ATX + Setext h1) so it can be weighted in ranking."""
    headings: list[str] = []
    lines = markdown.splitlines()
    for i, line in enumerate(lines):
        atx = _ATX_HEADING_RE.match(line)
        if atx:
            headings.append(atx.group(1).strip())
            continue
        stripped = line.strip()
        if stripped and i + 1 < len(lines):
            underline = lines[i + 1].strip()
            if len(underline) >= 3 and set(underline) == {"="}:
                headings.append(stripped)
    return "\n".join(headings)


def _fts_terms(raw: str) -> list[str]:
    """Split free text into safe, individually-quoted FTS5 terms (no syntax injection)."""
    return [f'"{term}"' for term in _TERM_RE.split(raw) if term]
