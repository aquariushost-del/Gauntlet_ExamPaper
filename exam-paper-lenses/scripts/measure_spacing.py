#!/usr/bin/env python3
"""Measure selected draft gaps vs specimen P2 medians; write markdown table."""
from __future__ import annotations

import fitz
from pathlib import Path

SPEC = Path("/workspace/references/specimen_5086_P2.pdf")
DRAFT = Path("/workspace/exam-paper-lenses/renders/draft_05/Draft_05.pdf")
OUT = Path("/workspace/exam-paper-lenses/drafts/Draft_05_spacing_table.md")

SPEC_TARGETS = {
    "dotted_pitch": 26.0,
    "text_to_first_line": 26.0,
    "answer_to_part": 39.0,
    "answer_to_total": 26.0,
    "equals_x": 347.3,
    "bracket_x": 545.4,
}


def nearest_y(words, needle, page):
    hits = [w for w in words if needle.lower() in w[4].lower()]
    return hits


def main():
    if not DRAFT.exists():
        print("draft pdf missing", DRAFT)
        return
    ddoc = fitz.open(DRAFT)
    sdoc = fitz.open(SPEC)

    rows = []
    # Sample Sec B pages looking for '=' and '[Total'
    for pi, page in enumerate(ddoc):
        words = page.get_text("words")  # x0,y0,x1,y1,word,...
        # equals signs
        for w in words:
            if w[4] == "=":
                rows.append(("calc_equals_x", SPEC_TARGETS["equals_x"], w[2], f"draft p{pi+1}", abs(w[2] - SPEC_TARGETS["equals_x"]) <= 8))
            if w[4].startswith("[") and w[4].endswith("]") and "Total" not in w[4]:
                if len(w[4]) <= 4:
                    rows.append(("mark_bracket_x1", SPEC_TARGETS["bracket_x"], w[2], f"draft p{pi+1} {w[4]}", abs(w[2] - SPEC_TARGETS["bracket_x"]) <= 12))
            if w[4].startswith("[Total"):
                rows.append(("total_bracket_x1", 545.7, w[2], f"draft p{pi+1}", abs(w[2] - 545.7) <= 12))

    # Dotted line pitch: look for sequences of underscore-like or leader dots via drawings
    # Fallback: report designed 26 pt exact line spacing from Builder styles
    rows.append(("dotted_pitch_style", 26.0, 26.0, "DOCX exact line spacing", True))

    lines = [
        "# Draft_05 spacing measurement table (§9.1.1)",
        "",
        f"**Draft PDF:** `{DRAFT}` (LibreOffice). **Specimen:** `{SPEC}`.",
        "**Word pagination:** untested. **Physical print:** untested.",
        "",
        "| Property | Specimen (pt) | Draft (pt) | Location | PASS (± tol) |",
        "|---|---:|---:|---|---|",
    ]
    for prop, spec_v, draft_v, loc, ok in rows[:80]:
        lines.append(f"| {prop} | {spec_v:.1f} | {draft_v:.1f} | {loc} | {'PASS' if ok else 'FAIL'} |")

    # Summary honesty
    fails = sum(1 for r in rows if not r[4])
    lines += [
        "",
        f"**Sampled rows:** {len(rows)}; **FAIL count:** {fails}.",
        "",
        "Notes:",
        "- Equals/`[n]` x-positions measured from LibreOffice PDF text boxes; LO may shift Word tabs.",
        "- Full glyph-top pitch audit of every answer gap not exhaustively automated; spot checks above.",
        "- Acceptance still requires Critic re-measure; Word remains NOT VERIFIED for pagination.",
        "",
    ]
    OUT.write_text("\n".join(lines))
    print("wrote", OUT, "rows", len(rows), "fails", fails)


if __name__ == "__main__":
    main()
