# VELOOP Rewards — Data Analyst Task 01

Product Analytics, Data Readiness & Data Management Blueprint.

## Data Authenticity
All datasets in this project are SIMULATED / FICTIONAL for analytical testing only.
No result in this project represents actual VELOOP users, earnings, withdrawals, revenue, retention, or performance.

## Folder Structure
- 00_Source_Register — Source & Verification Register (Confirmed / Proposed / To Be Verified)
- 01_Product_Audit — Product data readiness audit (WP-A)
- 02_Coverage_Matrix — Data coverage matrix and analytics gaps
- 03_Specifications — User, Reward, Wallet/Withdrawal, Referral specs (WP-B to WP-E)
- 04_Event_Tracking — Event catalogue and naming standard (WP-F)
- 05_Data_Dictionary — Data dictionary, 75+ fields (WP-G)
- 06_Logical_Model — Entities, keys, relationships, ER diagram (WP-H)
- 07_KPI_Catalogue — 30+ KPIs (WP-I)
- 08_Data_Profiling — Simulated dataset profiling (WP-J)
- 09_Data_Quality — Data quality audit and controls (WP-K, WP-L)
- 10_Dashboard_Blueprint — Dashboard specs (WP-M)
- 11_Developer_Handoff — Engineering handoff (WP-N)
- 12_Pipeline_Governance — Pipeline and privacy/governance (WP-O, WP-P)
- 13_Gap_Assessment — Analytics readiness gap assessment (WP-R)
- 14_Backlog — Assumption register, change log, implementation backlog (WP-Q, WP-S, Final backlog)
- 15_Final_Report — Executive summary and consolidated report
- input_data — Copies of the task PDF and datasets (originals untouched)

## Status of deliverables (as of 2026-10-31)
- Done (draft): source register, coverage matrix, event tracking plan (32 events), data dictionary, KPI catalogue (37 KPIs), profiling, data quality audit, assumption register, backlog, specs, logical model, dashboard blueprint, developer handoff, pipeline and governance, gap assessment, executive summary.
- Done (SIMULATED, labelled): Rewards, Wallet, Withdrawals and Referrals tables in 08_Data_Profiling/Simulated_Rewards_Wallet_Withdrawals_Referrals.xlsx. Product docs in Google Drive not reviewed.
- Owners named in the backlog are roles, not people.

- Synthetic data methodology: 08_Data_Profiling/Synthetic_Data_Methodology.md

- Dashboard specs: 10_Dashboard_Blueprint/Dashboard_Specifications.xlsx
- Developer requirements: 11_Developer_Handoff/Developer_Analytics_Handoff.xlsx
- KPI calculation test: 08_Data_Profiling/KPI_Calculation_Test.xlsx
- Readiness scorecard: 13_Gap_Assessment/Analytics_Readiness_Scorecard.xlsx
- User analytics spec: 03_Specifications/User_Analytics_Specification.xlsx

- Known issue DQ-018: inactivity KPI reference date fixed to data cut-off. See 09_Data_Quality and 08_Data_Profiling/KPI_Calculation_Test.xlsx.

## Final package (v6, updated in v7)
- Word versions of every document: Word_Versions/ (11 .docx files)
- ER diagram image: 06_Logical_Model/er_diagram.png
- Dashboard wireframes (layout only): 10_Dashboard_Blueprint/wireframes/
- Final consolidated report (deliverable 21): 15_Final_Report/Final_Consolidated_Report.md and Word_Versions/Final_Consolidated_Report.docx
- All Excel deliverables: see the folders above; 16 workbooks in total.
- Status: all 21 deliverables produced as drafts for review. Items marked To Be Verified need product or engineering confirmation.

## v7 completion summary
- All 21 deliverables are produced. Specs 05, 06 and 07 are now separate documents.
- Product Data Audit is detailed, with the full product-area table.
- Data Quality: 32 issues logged (18 first round + 7 new). 4 earlier issues (DQ-009, DQ-010, DQ-014, DQ-015) have 0 records in the supplied data and are closed. The rule for each stays as a prevention control. 257 checks passed with no problems.
- Event Tracking Plan has Data Type and KPI Dependency columns.
- Pipeline architecture diagram: 12_Pipeline_Governance/pipeline_architecture.png
- Data Quality Report (narrative): 09_Data_Quality/Data_Quality_Report.md
- Word versions of every Markdown document: Word_Versions/
