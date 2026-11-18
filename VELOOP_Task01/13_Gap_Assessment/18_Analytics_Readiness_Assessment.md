# VELOOP Rewards — Analytics Readiness Assessment (Deliverable 18)

**Status:** Proposed. This is an assessment of the analytics foundation, not of VELOOP's production systems.
**Data basis:** Simulated dataset only (SIMULATED — CREATED FOR ANALYTICAL TESTING). No score below describes actual VELOOP performance.
**Companion file:** `Analytics_Readiness_Scorecard.xlsx` (13_Gap_Assessment). Scores here must match that workbook.

---

## 1. What Readiness Means Here

Readiness asks: if VELOOP started sending real production data today, could it reliably measure what it needs to? It does not ask whether VELOOP is performing well.

Readiness is scored on a 0–5 scale for each area:

| Score | Meaning |
|---|---|
| 0 | Not defined |
| 1 | Defined only in discussion |
| 2 | Documented as a proposal |
| 3 | Documented and testable with simulated data |
| 4 | Confirmed against the real product |
| 5 | Confirmed, tested, and in production |

**Current position:** Most areas are at 2 or 3. None is at 4 or 5, because no area has been confirmed against the live VELOOP product.

---

## 2. Evidence Used

| Evidence | Verified Value |
|---|---|
| Product areas mapped | 12 areas, with status Proposed or To Be Verified |
| Event catalogue | Defined in Event Tracking Plan (naming standard `domain_object_action`) |
| Data dictionary | 76 fields (Excel title and row count match) |
| KPI catalogue | 37 KPIs (Excel title matches the sheet) |
| Simulated rows, Power BI tables | users 1,000; task_activity 9,846; sessions 7,913; feature_events 35,704; daily_activity 6,667; milestones 4,799 (total 65,929) |
| Simulated rows, other tables | Rewards 5,000; Wallet 3,357; Withdrawals 1,200; Referrals 900 (total 10,457) |
| Simulated total | 76,386 rows |
| Power BI dashboard | Built for user analytics only (Dashboard 1 of 7 specified) |
| Open assumptions | Items in the Assumption & Verification Register (A001–A014) |
| Open data-pipeline items | P001–P005 in the Data Pipeline Proposal |
| Open governance items | G001–G005 in the Privacy & Governance Proposal |

---

## 3. Readiness Scores by Area

| # | Area | Score (0–5) | Reason | Main Gap |
|---|---|---|---|---|
| 1 | Product data mapping | 3 | Mapped and documented; not confirmed against product | Feature implementation status unknown |
| 2 | Event coverage | 2 | Events defined as proposals | Backend emission not verified (A001) |
| 3 | Data model | 3 | Entities, keys and relationships documented; tested on simulated data | No production relationships checked |
| 4 | Data dictionary | 3 | 76 fields documented with type, source, sensitivity | Source systems unconfirmed |
| 5 | KPI definitions | 3 | 37 KPIs with formulas; some cannot be calculated from current fields | Several KPIs need fields not yet supplied |
| 6 | Data quality | 3 | Issues found in simulated data; controls proposed | Controls not implemented anywhere |
| 7 | Dashboards | 2 | One Power BI prototype; six others specified only | Active user definition missing on dashboard |
| 8 | Pipeline | 2 | Architecture proposed; diagram exists | Raw storage location unknown (P003) |
| 9 | Governance and access | 2 | Access model and sensitive-data rules proposed | Approvals, consent and retention To Be Verified (G001–G005) |
| 10 | Transaction integrity | 1 | Transaction model proposed | Stable transaction ID not confirmed (A003) |
| 11 | Reward accuracy | 1 | Credited vs. pending distinction defined | Reward units and credit timing unknown (A011) |
| 12 | Third-party reconciliation | 1 | Dependency identified | Reconciliation rule unknown (A012) |

**Overall:** Documentation is strong (mostly 3). Production readiness is weak (1 to 2 in the areas that affect money and trust).

---

## 4. Where Readiness Is Lowest

The three areas that matter most for trustworthy reporting are scored lowest:

1. **Transaction integrity (1):** Without a stable transaction ID, wallet and withdrawal deduplication cannot be guaranteed. This is a Critical gap.
2. **Reward accuracy (1):** Activity and credited value are easy to confuse. Reward reports could overstate earnings until credit status is confirmed. This is a Critical gap.
3. **Third-party reconciliation (1):** Ads and survey completions depend on external reporting. VELOOP cannot confirm these figures alone. This is a High gap.

---

## 5. What the Dashboard Does and Does Not Show

The Power BI dashboard (simulated data) shows:

- 1,000 users, 602 Active (60.2%), 248 Inactive (24.8%), 84 Pending Verification (8.4%), 66 Suspended (6.6%)
- Onboarding completion 68.50%
- Task completion 57.15%
- About 8,000 sessions
- Acquisition by source and device slicer

**Limits of the dashboard:**

- "Active" is not defined on the dashboard. It must link to the KPI definition for active users before the figure can be read.
- All values are simulated. They show that the dashboard works, not how VELOOP performs.
- It cannot yet show rewards, wallet, withdrawals, or referrals, because those dashboards are not built.

---

## 6. Conditions for Moving to Readiness Level 4

To move an area from 2 or 3 to 4, VELOOP must:

1. Confirm the backend emits the proposed event, and record the result in the Assumption Register.
2. Confirm the field exists in the product, with the same name and type as the data dictionary.
3. Run the relevant KPI formula on a real sample and compare it to a manual count.
4. Get approval for access and consent under the Privacy & Governance Proposal.

No area moves up a level on the basis of this document alone.

---

## 7. Summary

The analytics foundation is well documented and testable on simulated data. It is not yet ready for production reporting. The most important next steps are confirming the transaction ID, the reward credit status, and the event emission for tasks and withdrawals. Until those are verified, any production KPI on rewards or withdrawals should be treated as unreliable.
