# VELOOP Rewards — Implementation Backlog (Deliverable 20)

**Status:** Proposed. Priorities come from the Gap Assessment and the Data Quality Audit.
**Source of record:** `Implementation_Backlog.xlsx` (14_Backlog). If this summary and the workbook differ, the workbook wins.
**Owners:** Roles, not named people.

---

## 1. Priority Scale

| Priority | Meaning |
|---|---|
| Critical | Without this, reward, wallet, or withdrawal figures cannot be trusted. Must be done before launch. |
| High | Needed for reliable reporting. Should be done before launch. |
| Medium | Improves management reporting. Can follow launch. |

---

## 2. Critical Items (5)

| # | Requirement | Why | Dependency | Owner | Stage |
|---|---|---|---|---|---|
| 1 | Stable user_id shared across all tables | Cross-event analysis | Authentication | Engineering | Prelaunch |
| 2 | Wallet transaction_id (unique, idempotent) | Wallet dedupe and reconciliation | Wallet service | Engineering | Prelaunch |
| 3 | Single user master; fix cross-file identity conflict (DQ-006) | Trust in user-level joins | Data layer | Data Eng | Prelaunch |
| 4 | Keep reward credit only from Completed state (control for DQ-009) | Earnings accuracy | Task and reward services | Backend | Prelaunch |
| 5 | Withdrawal lifecycle states and timestamps | Payout KPIs | Withdrawal service | Backend + Finance | Prelaunch |

---

## 3. High Items

| Requirement | Why | Dependency | Owner | Stage |
|---|---|---|---|---|
| Implement Critical and High events from Event Tracking Plan | Measurement | Frontend and backend | Engineering | Prelaunch |
| Log all session outcomes, including Failed and Abandoned (DQ-011) | Reliability KPIs | Frontend | Engineering | Prelaunch |
| Define qualifying activity and fix active_flag (DQ-012, A005) | Active user KPIs | Product decision | Product + Data | Prelaunch |
| Data quality checks QR-01 to QR-10 | Prevent unreliable reporting | Data layer | Data Eng | Prelaunch |
| Referral activation rule and referral events | Referral KPIs | Product decision | Product + Backend | Prelaunch |
| Confirm reference date and activity window for inactivity KPI (DQ-018, A013) | Prevents wrong inactive-user reporting | Product decision | Product + Data | Prelaunch |

---

## 4. Medium Items

| Requirement | Why | Dependency | Owner | Stage |
|---|---|---|---|---|
| Canonical feature enum (DQ-013) | Consistent feature reporting | Event schema | Data Eng | Prelaunch |
| Advanced dashboards (Dashboards 2–7) | Management reporting | Production data | Analytics | Postlaunch |

---

## 5. Counts

- Critical: 5
- High: 6
- Medium: 2
- Total: 13 items

---

## 6. Dependency Chain

Most High and Critical items depend on two decisions that VELOOP has not made yet:

1. **Product decision on active user and referral activation rules** (A005, A006, A013). Until this is decided, Active User and Referral KPIs cannot be finalized.
2. **Engineering confirmation of event emission and transaction IDs** (A001, A003). Until this is confirmed, wallet, withdrawal, and task reporting cannot run from production.

---

## 7. Metric / Event Change Log (WP-Q)

| Date | Change | Old Definition | New Definition | Reason | Affected KPIs | Affected Dashboards | Affected Reports | Owner | Version |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-31 | Initial catalogue created | None | Proposed definitions in 04, 05, 07 | Project start | All | All | Final report | Analytics | 1.0 |

Future definition changes must add a new row with a new version number.

---

## 8. Open Items

- The Assumption & Verification Register (14_Backlog) lists the unknowns behind the Critical and High items.
- No item in this backlog is confirmed as done. Stage refers to when the work should happen, not whether it has started.
