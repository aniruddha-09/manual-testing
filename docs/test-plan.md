# Test Plan — SauceDemo (Swag Labs)

**Author:** Aniruddha Yadav (QA fresher)
**Target application:** https://www.saucedemo.com — a public practice e-commerce site built for testing practice.
**Type of testing:** Manual testing only (no automation, no load testing).
**Status:** Draft — awaiting execution ([TODO: date tested]).

---

## 1. Objective

Design and execute a structured set of manual test cases against the public SauceDemo
practice site to demonstrate core QA skills: test planning, test case design
(positive, negative, boundary, UI and exploratory), defect reporting, and result
summary reporting. The exercise focuses on correctness of the end-to-end shopping
flow (login → browse → cart → checkout) and on clear, honest documentation of
expected versus actual behaviour.

## 2. Scope (Modules in Scope)

| # | Module | What it covers |
|---|--------|----------------|
| 1 | Login | Valid/invalid credentials, empty fields, locked-out user, error wording, password masking, edge-case inputs |
| 2 | Inventory (product list) | Item count, product images, name/price consistency, add/remove from list, cart badge |
| 3 | Sorting | Name sort (A–Z, Z–A) and price sort (low→high, high→low) |
| 4 | Product details | Navigation to detail page, back button, add to cart from detail page |
| 5 | Cart | Multiple items, remove item, continue shopping, persistence after refresh |
| 6 | Checkout | Information form validation, order overview totals, cancel, finish, order confirmation |
| 7 | Menu / Logout | Logout, browser back button after logout, About link, Reset App State |
| 8 | Cross-user behaviour | Exploratory comparison of `problem_user` and `visual_user` against `standard_user` |
| 9 | Responsive / UI basics | One basic responsive layout and UI consistency spot check |

## 3. Out of Scope

- Automated tests (UI, API or otherwise) and load/stress/performance testing.
- Backend, database and server-side verification (SauceDemo is a front-end practice app).
- Payment processing, real orders, real accounts or any transaction beyond the demo flow.
- Accessibility audits, security penetration testing and SEO.
- Visual regression tooling, screenshots as pass/fail proof of undocumented behaviour.
- Any action that modifies the public site or its data outside normal demo usage.

## 4. Test Approach

All testing is **manual**, executed through the browser UI against
https://www.saucedemo.com.

- **Manual functional testing** — verify each happy-path flow works as described
  (login, browsing, sorting, cart, checkout, logout).
- **Negative testing** — invalid credentials, locked-out user, empty required
  fields, SQL-injection-style strings, special characters; confirm the app
  rejects them with clear errors and no state corruption.
- **Boundary and edge-case testing** — minimal/maximum inputs for required
  fields (single character, long strings), empty-vs-whitespace values, cart
  badge transitions (0 → 1 → 0), and totals at the exact calculation boundary.
- **UI/usability testing** — element visibility, label wording, error message
  wording, password masking, button state changes (Add to cart ↔ Remove),
  layout at a basic responsive breakpoint.
- **Exploratory testing** — time-boxed, charter-based sessions comparing the
  behaviour of `problem_user` and `visual_user` against `standard_user` on the
  same flows; observations are logged as exploratory test cases.
- **Cross-browser spot check** — repeat a small smoke subset (login, add to
  cart, checkout) on [TODO: browser + version] and a second browser
  [TODO: second browser + version] to check for browser-specific issues.
  Spot check only; not a full matrix.

## 5. Test Environment

| Item | Value |
|------|-------|
| Application URL | https://www.saucedemo.com |
| Browser + version | [TODO: browser + version] |
| OS | [TODO: OS] |
| Device | [TODO: device] |
| Screen resolution | [TODO: screen resolution] |
| Date tested | [TODO: date tested] |
| Network | Standard broadband/Wi-Fi (public internet access required) |

## 6. Test Data

All data is **public demo data published by SauceDemo** — no real personal data
is used.

| Account | Purpose |
|---------|---------|
| `standard_user` | Normal, active account for positive-path testing |
| `locked_out_user` | Account that must be rejected with a locked-out message |
| `problem_user` | Account with known UI/behaviour problems (exploratory comparison) |
| `performance_glitch_user` | Account with known performance quirks (not executed in this round; out of scope) |
| `error_user` | Account that surfaces errors in flows (available for exploratory sessions) |
| `visual_user` | Account with known visual defects (exploratory comparison) |
| Shared password | The single shared password **as published on the SauceDemo login page** — all accounts above use it |

Additional test data (special characters, SQL-injection-style strings,
whitespace-padded values) is defined per test case in the `Test_Data` column of
[test-cases/test_cases.csv](../test-cases/test_cases.csv).

## 7. Entry / Exit Criteria

**Entry criteria**
- This test plan is reviewed and approved ([TODO: reviewer, if any]).
- Test cases are written and reviewed; environment details above are filled in.
- https://www.saucedemo.com is reachable from the test machine.
- Public demo accounts and the published shared password are available.

**Exit criteria**
- 100% of planned test cases executed, or remaining cases explicitly marked
  Blocked/Not Run with a reason in Notes.
- All failed cases have a corresponding entry in `bug-reports/bugs.csv`
  (or an explanatory note).
- No open Critical/High defect left un-triaged without an agreed action.
- Test summary report generated (`reports/test-summary.md`) and reviewed.

## 8. Risks and Assumptions

**Risks**
- SauceDemo is a third-party public site: content, behaviour or availability may
  change without notice, invalidating earlier results.
- The site is shared by many testers worldwide; no sandbox or test isolation exists.
- `problem_user`, `visual_user` and `performance_glitch_user` intentionally misbehave;
  results from these accounts must not be reported as defects against `standard_user`.
- Browser/OS updates during the testing window may change observed behaviour.
- Evidence screenshots may contain only demo data; anything else must not be captured.

**Assumptions**
- Testing is manual only; no automated or load tests are written against the site.
- Only publicly available demo data is used; no real credentials or personal data.
- Expected results describe intended behaviour; Actual Result, Status, Evidence and
  Notes are filled only during real execution — never in advance.
- Environment placeholders marked `[TODO: ...]` are completed before execution.

## 9. Deliverables

| Deliverable | Location |
|-------------|----------|
| Test plan (this document) | `docs/test-plan.md` |
| Severity & priority guide | `docs/severity-priority-guide.md` |
| Test cases (CSV) | `test-cases/test_cases.csv` |
| How to use the test-case sheet | `test-cases/README.md` |
| Bug report template | `bug-reports/TEMPLATE.md` |
| Bug log (CSV) | `bug-reports/bugs.csv` |
| Evidence screenshots | `evidence/` |
| Test summary report (generated) | `reports/test-summary.md` |
| Generator scripts (Python stdlib only) | `scripts/` |

## 10. Defect Management

**Defect lifecycle:** `New → Assigned → Fixed → Retest → Closed` (or
`Reopened` if the fix is incomplete; `Reopened` returns to `Assigned`).

1. **New** — tester logs the defect in `bug-reports/bugs.csv` with steps,
   expected vs actual, severity, priority and evidence.
2. **Assigned** — defect is triaged and assigned for fixing.
3. **Fixed** — developer marks it fixed.
4. **Retest** — tester re-executes the related test case.
5. **Closed** — verified fixed; **Reopened** — still reproducible.

**Severity vs Priority:** Severity describes the *technical impact* of the defect
(data loss, flow blocked, cosmetic); Priority describes the *scheduling urgency*
of the fix. They are independent — a cosmetic bug can be High priority if it
appears on the first screen every customer sees, and a severe bug can be Low
priority if few users ever hit it. Full definitions with examples:
[docs/severity-priority-guide.md](severity-priority-guide.md).

## 11. Test Case Format

Test cases live in `test-cases/test_cases.csv` with these columns:

| Column | Meaning |
|--------|---------|
| `TC_ID` | Unique ID, `TC-001` onwards |
| `Module` | Module under test (Login, Cart, Checkout, …) |
| `Scenario` | One-line description of what is tested |
| `Type` | Positive / Negative / Boundary / Edge Case / UI / Exploratory |
| `Preconditions` | State required before the test starts |
| `Steps` | Numbered actions separated by ` \| ` |
| `Test_Data` | Credentials/inputs used |
| `Expected_Result` | What the application should do (written before execution) |
| `Actual_Result` | **Left empty — filled only during execution** |
| `Status` | **Left empty — Pass / Fail / Blocked / Not Run after execution** |
| `Severity_If_Failed` | Severity to assign if this test fails |
| `Evidence` | **Left empty — evidence file name after execution (e.g. `evidence/TC-001.png`)** |
| `Notes` | **Left empty — observations, bug IDs, blockers** |

Rules:
- Expected results are written **before** testing; actual results, status,
  evidence and notes are filled **only** when the test is really executed.
- Multi-step procedures use ` | ` as the step separator inside one CSV cell.
- Evidence files follow `evidence/TC-001.png` for test cases and
  `evidence/BUG-001.png` for defects.
