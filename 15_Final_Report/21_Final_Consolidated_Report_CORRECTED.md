# VELOOP Rewards — Data Analyst Task 01: Final Consolidated Report

SIMULATED — CREATED FOR ANALYTICAL TESTING. Not actual VELOOP data.

**Status:** Complete as a draft for review. Based on the Task 01 brief and the simulated files. Product documentation in the Google Drive folder was not reviewed. All product facts are Proposed or To Be Verified.

Items marked **[VERIFY]** have not been re-checked against the source files.

---

## 1. Purpose

This report brings together all 21 deliverables of the task. It answers: what VELOOP should collect, how the data should be structured, how to know the data can be trusted, what management should measure, and what engineering should implement.

---

## 2. Deliverables

| # | Deliverable | Location | Format Available |
|---|---|---|---|
| 01 | Executive Summary | 15_Final_Report/Executive_Summary | Markdown, Word |
| 02 | Product Data Audit | 01_Product_Audit | Markdown only |
| 03 | Data Coverage Matrix | 02_Coverage_Matrix | Excel |
| 04 | User Analytics Specification | 03_Specifications | Excel, Markdown |
| 05 | Earning & Reward Analytics Spec | 03_Specifications | Markdown, Word |
| 06 | Wallet & Withdrawal Analytics Spec | 03_Specifications | Markdown, Word |
| 07 | Referral & Engagement Analytics Spec | 03_Specifications | Markdown, Word |
| 08 | Event Tracking Plan | 04_Event_Tracking | Excel |
| 09 | Data Dictionary (76 fields) | 05_Data_Dictionary | Excel |
| 10 | Logical Data Model and ER diagram | 06_Logical_Model | Markdown, Word, PNG |
| 11 | KPI Catalogue (37 KPIs) | 07_KPI_Catalogue | Excel |
| 12 | Simulated Data Profiling and KPI Test | 08_Data_Profiling | Excel, Markdown |
| 13 | Data Quality Audit | 09_Data_Quality | Excel, Markdown |
| 14 | Dashboard Blueprint and Power BI prototype | 10_Dashboard_Blueprint, 17_PowerBI | Excel, Markdown, PNG, PBIX |
| 15 | Developer Analytics Handoff | 11_Developer_Handoff | Excel, Markdown |
| 16 | Data Pipeline Proposal | 12_Pipeline_Governance | Markdown only |
| 17 | Privacy & Governance Proposal | 12_Pipeline_Governance | Markdown only |
| 18 | Analytics Readiness Assessment | 13_Gap_Assessment | Excel, Markdown |
| 19 | Assumption & Verification Register | 14_Backlog | Excel |
| 20 | Implementation Backlog | 14_Backlog | Excel, Markdown |
| 21 | Final Consolidated Report | 15_Final_Report | Markdown, Word |

**Presentation and handover (Day 25):** not yet prepared.

---

## 3. Simulated Data Volume

| Source | Tables | Rows |
|---|---|---|
| Power BI data folder (17_PowerBI) | users 1,000; task_activity 9,846; sessions 7,913; feature_events 35,704; daily_activity 6,667; milestones 4,799 | 65,929 |
| Simulated_Rewards_Wallet_Withdrawals_Referrals.xlsx (08_Data_Profiling) | Rewards 5,000; Wallet 3,357; Withdrawals 1,200; Referrals 900 | 10,457 |
| **Total** | | **76,386** |

Row counts are verified from the files. The Data Dictionary (76 fields) and KPI Catalogue (37 KPIs) are verified from workbook titles and row ranges.

---

## 4. What Was Discovered

1. **Identity conflict (DQ-006, Critical):** The same user_id has different names in the two supplied files, so user-level joins are unreliable. **[VERIFY]** number of mismatched names.

2. **Credit before completion (DQ-009, Critical):** In the first review, rewards were marked Credited for tasks that were not completed. The latest business rule check (BR-07) returns 0 records. This suggests the issue may be fixed in the current data, but the fix is **not yet confirmed**. Do not report it as resolved until the source logic is checked. **[VERIFY]**

3. **Activity and credits for suspended or pending users (DQ-007, DQ-008, High):** The latest business rule check (BR-06) finds 1,456 task activity records for suspended or pending accounts. **[VERIFY]** against the source files.

4. **Activity for users whose onboarding is Not Started (DQ-025, High):** The latest check (BR-05) finds 1,497 task activity records for these users. Fix at source, or filter in KPI calculations.

5. **Sessions and active flags carry no information (DQ-011, DQ-012, High):** All simulated sessions are marked Completed, and every daily activity row is flagged active. Neither is credible as real behaviour. **[VERIFY]**

6. **Two user-status sources disagree (DQ-027, High):** The Rewards/Users file and the behaviour file give different figures for the same 1,000 IDs:
   - Suspended users: 77 (Rewards/Users) vs. 66 (behaviour file)
   - Active 30-day users: 325 (Rewards/Users) vs. 819 (behaviour file)

   Assumption A014 tracks the decision on which file is authoritative. Until that is decided, every KPI must state which file it uses.

7. **Events with no success status (DQ-026, Medium):** Exchange Center, Leaderboard and Wallet record events but never a success status (5,698 events in total). **[VERIFY]**

8. **Missing task completion timestamps (DQ-028, Medium):** 4,219 records in task_activity have no task_completed_at value. **[VERIFY]**

9. **Inactivity KPI date dependence (DQ-018):** The inactivity KPI depended on the report date. The fix uses the data cut-off date.

10. **Missing tables in the supplied data:** Rewards, Wallet, Withdrawals and Referrals were not in the supplied files. Labelled SIMULATED versions were created (see Section 3). **[VERIFY]** integrity checks (foreign keys, duplicates, status logic).

---

## 5. Business Rule Results (latest run)

| Rule | Description | Records | Result |
|---|---|---|---|
| BR-05 | Task activity for users with onboarding Not Started | 1,497 | Fail |
| BR-06 | Task activity for suspended or pending accounts | 1,456 | Fail |
| BR-07 | Reward credited but task not completed | 0 | Pass on this sample |

A zero result means "no problem in this sample", not "no problem in production".

---

## 6. Unknowns

The main unknowns are recorded in the Assumption & Verification Register (A001 to A014). The most important:

- Whether the backend emits task completion events (A001)
- Whether wallet transaction IDs are unique (A003)
- How referral activation is defined (A006)
- Whether reward units are XP, VE, Gems or Tokens (A011)
- Which date window applies to inactivity (A013)
- Which user-status file is authoritative (A014)

---

## 7. What VELOOP Should Implement First

1. A single stable user ID, with one user master table.
2. A unique, idempotent transaction ID for every wallet movement.
3. Reward credit only from a completed task state.
4. A withdrawal lifecycle with state and timestamps for each step.
5. The Critical and High events in the Event Tracking Plan.
6. A written definition of qualifying activity for active users.
7. One authoritative user-status source, or explicit labelling of which source each KPI uses.

Full list: see the Implementation Backlog (13 items: 5 Critical, 6 High, 2 Medium).

---

## 8. Major Risks

- Identity conflicts across sources make user-level analysis unreliable.
- Non-unique transactions can lead to double counting of rewards and payouts.
- Activity and credits for suspended or pending users can overstate engagement and earnings.
- Earnings from third-party tasks (ads, surveys) cannot be verified without provider status.
- KPIs with unclear definitions can mislead management.

---

## 9. Integrity Statement

- No figure in this report is an actual VELOOP result. Every number comes from simulated data, or from counts of files and workbook rows.
- No product feature is confirmed as live. All events and fields are Proposed unless marked otherwise.
- No target values are set. KPIs are defined, not targeted.

---

## 10. Next Steps

1. Verify the **[VERIFY]** items against the source files.
2. Confirm whether the DQ-009 fix is real in the source logic.
3. Decide the authoritative user-status file (A014).
4. Share the Google Drive product documents for review.
5. Once production data exists, replace the simulated tables. Do not mix simulated and production data.
