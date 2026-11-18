# Data Quality Report (WP-K and WP-L)

SIMULATED — CREATED FOR ANALYTICAL TESTING. Not actual VELOOP data.

## 1. Summary
The Data Quality Audit workbook logs **32 issues** in total: 18 from the first round and 7 from the latest review. The workbook also has a Checks_Passed sheet listing 257 checks that found no problems. Passing checks are recorded so reviewers can see what was tested.

Severity of the latest findings: High: 5, Low: 1, Medium: 1.

## 2. Method
Every text column was checked for leading or trailing spaces, and for inconsistent capitalisation or spelling. Every numeric column was checked for negative values. Event, task and session records were checked for duplicates (same content, different ID). Status and category fields were checked against allowed values. Age was checked for non-integer and out-of-range values. Task activity was checked against onboarding state. Each check counts records, so results can be reproduced.

## 3. Issues found in the latest review
- **DQ-019** (High): Duplicate events / records (same content, different ID) in Behavior file / 03_Feature_Events, field row content except event_id, 17 records.
- **DQ-020** (Low): Leading/trailing spaces in Behavior file / 10_Event_Data_Quality_Audit, field event_status, 4 records.
- **DQ-021** (Medium): Inconsistent capitalisation / spelling in Behavior file / 10_Event_Data_Quality_Audit, field event_status, 4 records.
- **DQ-022** (High): Invalid status / category value in Behavior file / 10_Event_Data_Quality_Audit, field event_status, 4 records.
- **DQ-023** (High): Negative values in Rewards/Users file / Users_1000_Clean, field days_since_registration, 4 records.
- **DQ-024** (High): Negative values in Rewards/Users file / Users_Messy_Audit, field days_since_registration, 4 records.
- **DQ-025** (High): Impossible state: task activity for users whose onboarding is Not Started in Behavior file / 01_Users_1000 + 05_Task_Activity, field onboarding_status, 1497 records.

## 4. Serious issues from the first round
- **DQ-006 (Critical):** the same user_id has different names in the two files, so user-level joins are unreliable.
- **DQ-009 (Critical):** rewards are marked Credited for tasks that are not completed.
- **DQ-007, DQ-008 (High):** activity and credits for suspended or pending users.
- **DQ-011, DQ-012 (High):** sessions and active flags carry no information.

## 5. Controls
Prevention rules for each layer (application, collection, raw, transformation, analytics, dashboard) are in 09_Data_Quality/Data_Quality_Audit.xlsx, sheet Quality_Control_Rules (QR-01 to QR-10).

## 6. Limits
All checks run on simulated files. A zero result means "no problem in this sample", not "no problem in production".

## 7. Later findings (added in the final review)
- **DQ-026 (Medium):** Exchange Center, Leaderboard and Wallet record events but never a success status (5,698 events in total).
- **DQ-027 (High):** The Rewards/Users file and the behavior file describe different populations for the same 1,000 IDs. Suspended counts (77 vs 66) and active 30-day counts (325 vs 819) do not match. Assumption A014 tracks the decision on which file is authoritative.

## 8. Final checks (missing IDs and timestamps)
- **DQ-028** (Medium): Missing timestamps (null date/time) in Behavior file / 05_Task_Activity, field task_completed_at, 4219 records.
- **DQ-029** (High): Missing IDs (null identifier) in Behavior file / 06_Milestones, field session_id, 40 records.
- **DQ-030** (Medium): Missing timestamps (null date/time) in Rewards/Users file / Users_1000_Clean, field last_login_datetime, 72 records.
- **DQ-031** (Medium): Missing timestamps (null date/time) in Rewards/Users file / Users_Messy_Audit, field registration_datetime, 1 records.
- **DQ-032** (Medium): Missing timestamps (null date/time) in Rewards/Users file / Users_Messy_Audit, field last_login_datetime, 73 records.

Checks with zero nulls: 25 additional checks passed.
