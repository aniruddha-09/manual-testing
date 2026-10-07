# Severity & Priority Guide

This guide defines how defects are graded in this repository. Every bug logged in
`bug-reports/bugs.csv` must carry both a **Severity** and a **Priority**.

## Severity vs Priority — they are different things

- **Severity** = the *technical impact* of the defect on the software: how badly
  is the product broken? It is usually judged by the tester.
- **Priority** = the *scheduling urgency* of the fix: how soon should the team
  work on it? It is usually set by the product/team lead.
- The two are **independent**. A cosmetic defect can be High priority (it sits on
  the first screen every customer sees), and a severe defect can be Low priority
  (only reachable in an obscure edge case that will be retired next release).

## Severity levels (with SauceDemo-style examples)

| Severity | Definition | SauceDemo-style example |
|----------|------------|-------------------------|
| **Critical** | The defect blocks the core flow completely; no workaround; data loss or security impact. | Clicking **Login** with valid `standard_user` credentials does nothing — the user can never reach the inventory page, so the entire application is unusable. |
| **High** | A major function is broken; a workaround exists but is painful or unreliable. | The **Checkout → Finish** button does not create an order confirmation, so the whole purchase flow cannot be completed end-to-end. |
| **Medium** | A normal function behaves incorrectly, or incorrect information is shown, but the flow can continue. | The cart badge shows `1` after two items are added to the cart, so the count is wrong even though both items are listed correctly in the cart. |
| **Low** | Minor UI/cosmetic/usability issue with no functional impact. | The product name on the details page wraps awkwardly and is truncated at the default screen resolution; everything else works. |

## Priority levels (with SauceDemo-style examples)

| Priority | Definition | SauceDemo-style example |
|----------|------------|-------------------------|
| **P0** | Fix immediately / release blocker; drop everything else. | The login page throws a JavaScript error and the Login button is unresponsive for all users — nobody can sign in at all. |
| **P1** | Fix as soon as possible; must be in the current release. | The **Finish** button on checkout silently fails, so no customer can complete a purchase. |
| **P2** | Fix in the normal course of work; next release is fine. | Sorting by **Price (low to high)** keeps the items in the default order — annoying, but users can still buy items. |
| **P3** | Fix when convenient; cosmetic or nice-to-have. | The cart badge digits are not vertically centred by 1–2 pixels on the inventory page. |

## Quick mapping (starting point, not a rule)

|  | P0 | P1 | P2 | P3 |
|--|----|----|----|----|
| **Critical** | ✔ typical | ✔ | rare | rare |
| **High** | ✔ | ✔ typical | ✔ | rare |
| **Medium** | rare | ✔ | ✔ typical | ✔ |
| **Low** | rare | rare | ✔ | ✔ typical |

A tester proposes severity; the team decides priority. Always justify both in the
bug report's Notes/fields when they fall outside the typical mapping.
