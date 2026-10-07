#!/usr/bin/env python3
"""Generate one Markdown bug report per row of bug-reports/bugs.csv.

Usage (no arguments, run from anywhere):

    python scripts/generate_bug_reports.py

What it does:
  1. Reads  bug-reports/bugs.csv (standard library `csv` module only).
  2. For every data row, writes bug-reports/<Bug_ID>.md using the same
     layout as bug-reports/TEMPLATE.md.
  3. Embeds the screenshot from evidence/ when the file exists
     (evidence/<Bug_ID>.png by default, or the file named in the
     Evidence column). Otherwise it inserts the visible placeholder
     "[TODO: screenshot]" instead of inventing evidence.
  4. If the CSV has a header but no data rows, it skips gracefully
     with a friendly message and exits with status 0.

Only the Python standard library is used.
"""

import csv
import sys
from pathlib import Path

# Repo root = parent of the scripts/ folder that contains this file.
ROOT = Path(__file__).resolve().parent.parent
BUGS_CSV = ROOT / "bug-reports" / "bugs.csv"
OUT_DIR = ROOT / "bug-reports"  # one <Bug_ID>.md per CSV data row
EVIDENCE_DIR = ROOT / "evidence"

# Extensions tried (in order) when the Evidence column does not name a file.
IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp", ".gif")

# Fields shown in the top summary table, in order.
TABLE_FIELDS = [
    ("Bug_ID", "Bug_ID"),
    ("Title", "Title"),
    ("Related_TC", "Related_TC"),
    ("Module", "Module"),
    ("Severity", "Severity"),
    ("Priority", "Priority"),
    ("Environment", "Environment"),
    ("Frequency", "Frequency"),
    ("Status", "Status"),
]


def find_evidence(bug_id, evidence_value):
    """Return a repo-relative image path, or None when no screenshot exists.

    Never guesses: the image must physically exist in evidence/ or the
    report gets a [TODO: screenshot] placeholder instead.
    """
    if not EVIDENCE_DIR.is_dir():
        return None

    candidates = []
    if evidence_value and evidence_value.strip():
        # The Evidence column may store a bare file name or evidence/XX.png.
        name = evidence_value.strip().replace(chr(92), "/").split("/")[-1]
        candidates.append(name)
    else:
        candidates.extend(bug_id + ext for ext in IMAGE_EXTENSIONS)

    for name in candidates:
        if (EVIDENCE_DIR / name).is_file():
            return "../evidence/" + name
    return None


def split_steps(text):
    """Split a Steps_To_Reproduce cell into a numbered list.

    Supports both newline-separated steps and " | " separated steps
    (the same separator used by test_cases.csv).
    """
    raw = (text or "").strip()
    if not raw:
        return ["[TODO: steps to reproduce]"]
    parts = []
    for line in raw.splitlines():
        parts.extend(chunk.strip() for chunk in line.split("|"))
    parts = [p for p in parts if p]
    return parts or ["[TODO: steps to reproduce]"]


def render_bug_report(row):
    """Render one bugs.csv row as Markdown following TEMPLATE.md."""
    bug_id = (row.get("Bug_ID") or "").strip()
    if not bug_id:
        return None

    def field(name):
        value = (row.get(name) or "").strip()
        return value if value else "[TODO: fill in]"

    lines = ["# Bug Report: " + field("Title"), ""]
    lines.append("| Field | Value |")
    lines.append("|-------|-------|")
    for label, key in TABLE_FIELDS:
        if key == "Bug_ID":
            lines.append("| **%s** | %s |" % (label, bug_id))
        else:
            lines.append("| **%s** | %s |" % (label, field(key)))
    lines.append("")

    lines.append("## Steps to Reproduce")
    lines.append("")
    for i, step in enumerate(split_steps(row.get("Steps_To_Reproduce")), 1):
        lines.append("%d. %s" % (i, step))
    lines.append("")

    lines.append("## Expected Result")
    lines.append("")
    lines.append(field("Expected_Result"))
    lines.append("")

    lines.append("## Actual Result")
    lines.append("")
    lines.append(field("Actual_Result"))
    lines.append("")

    lines.append("## Evidence")
    lines.append("")
    image = find_evidence(bug_id, row.get("Evidence"))
    if image:
        lines.append("![%s evidence](%s)" % (bug_id, image))
    else:
        lines.append("[TODO: screenshot]")
        lines.append("")
        lines.append("_Save the screenshot as `evidence/%s.png` and re-run "
                     "this script to embed it._" % bug_id)
    lines.append("")

    lines.append("## Notes")
    lines.append("")
    notes = (row.get("Notes") or "").strip()
    lines.append(notes if notes else "[TODO: notes]")
    lines.append("")

    return "\n".join(lines)


def main():
    """Read bugs.csv and write one Markdown file per data row."""
    if not BUGS_CSV.is_file():
        print("ERROR: %s not found." % BUGS_CSV)
        return 1

    with BUGS_CSV.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        rows = [r for r in reader if (r.get("Bug_ID") or "").strip()]

    if not rows:
        # Graceful skip: a header-only CSV is the normal state pre-execution.
        print("bugs.csv has no data rows yet - nothing to generate. "
              "(This is expected before testing starts.)")
        return 0

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    written = 0
    for row in rows:
        bug_id = (row.get("Bug_ID") or "").strip()
        content = render_bug_report(row)
        if content is None:
            print("  skipped row without Bug_ID")
            continue
        out_path = OUT_DIR / (bug_id + ".md")
        out_path.write_text(content, encoding="utf-8")
        print("  wrote %s" % out_path.relative_to(ROOT))
        written += 1

    print("Done: %d bug report(s) generated." % written)
    return 0


if __name__ == "__main__":
    sys.exit(main())
