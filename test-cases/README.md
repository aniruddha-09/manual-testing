# Test Cases

`test_cases.csv` contains the manual test cases for SauceDemo
(https://www.saucedemo.com). One row = one test case. Expected results are
written **before** execution; everything to the right of `Expected_Result`
(`Actual_Result`, `Status`, `Evidence`, `Notes`) is filled in **only during a
real test run** — never in advance.

Columns:
`TC_ID, Module, Scenario, Type, Preconditions, Steps, Test_Data, Expected_Result, Actual_Result, Status, Severity_If_Failed, Evidence, Notes`

Multi-step procedures use ` | ` as the step separator inside the `Steps` cell.

## Import into Google Sheets

1. Open Google Drive → **New → File upload** and choose `test_cases.csv`
   (or go to [sheets.new](https://sheets.new) and use **File → Import → Upload**).
2. In the import dialog choose **Separator type: Custom** and type a comma,
   or leave **Detect automatically** — the file uses standard quoted CSV.
3. Click **Import data**. The first row becomes the header.
4. Freeze the header row (**View → Freeze → 1 row**) and optionally the
   `TC_ID` column (**View → Freeze → 1 column**) for easy scrolling.

## Filling in Actual_Result and Status

- **Actual_Result** — write what really happened, factually and specifically
  (screens shown, messages displayed, values observed). Leave it empty until
  the test has actually been executed.
- **Status** — exactly one of:
  - `Pass` — observed behaviour matches Expected_Result.
  - `Fail` — observed behaviour differs from Expected_Result → log a bug in
    `bug-reports/bugs.csv` and put the bug ID (e.g. `BUG-001`) in Notes.
  - `Blocked` — cannot be executed (dependency failed, site down) → say why in Notes.
  - `Not Run` — not yet executed (leave the cell empty or write `Not Run`).
- **Evidence** — file name of the screenshot (see below).
- **Notes** — observations, bug IDs, blockers, retest comments.

## Naming evidence files

- Test-case evidence: `evidence/TC-001.png` — same ID as the test case.
- Bug evidence: `evidence/BUG-001.png` — same ID as the bug report.
- Use PNG (or JPG); keep one screenshot per file; add extra shots as
  `evidence/TC-001-2.png`, `evidence/TC-001-3.png`.
- Never commit evidence containing real personal data — only SauceDemo demo data.

## Export a PDF copy

1. In Google Sheets: **File → Download → PDF Document (.pdf)**.
2. Before exporting, set **File → Print → Formatting → Landscape** and enable
   **Fit to width** so wide rows are not cut off.
3. Save the PDF as `reports/test-cases.pdf` (this folder is ignored by the
   generator scripts; keep the CSV as the source of truth).

The summary of execution results is generated into `reports/test-summary.md`
by `scripts/generate_summary.py` after the CSV has been filled.
