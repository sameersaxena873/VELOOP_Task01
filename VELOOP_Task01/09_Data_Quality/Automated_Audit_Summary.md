# VELOOP Automated Data Quality Summary

Generated: 2026-10-31 14:02

## 1. Overview

- Datasets profiled: 15
- Basic issues detected: 30
- Business rules checked: 7
- Business rules failed: 2

## 2. Basic issues by type

| Issue | Count |
|---|---|
| Missing values | 17 |
| Duplicate ID | 12 |
| Invalid date/time | 1 |

## 3. Business rule results

| Rule | Severity | Records | Description | Status |
|---|---|---|---|---|
| BR-01 | High | 0 | session_end is before session_start | PASS |
| BR-02 | High | 0 | Negative session_duration_seconds | PASS |
| BR-03 | Critical | 0 | Sessions with user_id not in Users sheet | PASS |
| BR-04 | High | 0 | Events with session_id not in Sessions sheet | PASS |
| BR-05 | High | 1497 | Task activity for users with onboarding Not Started | FAIL |
| BR-06 | High | 1456 | Task activity for suspended or pending accounts | FAIL |
| BR-07 | Critical | 0 | Reward Credited but task not completed | PASS |

## 4. Notes

- BR-05 and BR-06 fail: task activity exists for users whose onboarding is Not Started or whose account is Suspended / Pending Verification.
- BR-07 passes: every Credited reward belongs to a Completed task.
- Messy audit sheets (Users_Messy_Audit, 10_Event_Data_Quality_Audit) contain intentional issues for testing.