# VELOOP Rewards - Data Analyst Task 01: Final Consolidated Report

Generated: 2026-11-04 16:52

## 1. Headline KPIs (SQL database and Power BI)

| KPI | Value |
|---|---|
| Total users | 1000 |
| Active users | 602 |
| Onboarding completion % | 68.5 |
| Total sessions | 7913 |
| Task completion % | 57.15 |

## 2. Users by acquisition source

| Source | Users |
|---|---|
| Organic Search | 258 |
| Direct | 194 |
| Social Media | 162 |
| Referral | 154 |
| Other | 97 |
| WhatsApp | 75 |
| Telegram | 60 |

## 3. Data quality results

- Basic issues found: 30 (missing values, duplicate IDs, invalid dates)
- Business rules checked: 7, failed: 2

| Rule | Records | Description | Status |
|---|---|---|---|
| BR-01 | 0 | session_end is before session_start | PASS |
| BR-02 | 0 | Negative session_duration_seconds | PASS |
| BR-03 | 0 | Sessions with user_id not in Users sheet | PASS |
| BR-04 | 0 | Events with session_id not in Sessions sheet | PASS |
| BR-05 | 1497 | Task activity for users with onboarding Not Started | FAIL |
| BR-06 | 1456 | Task activity for suspended or pending accounts | FAIL |
| BR-07 | 0 | Reward Credited but task not completed | PASS |

Key finding: BR-05 and BR-06 fail. Task activity exists for users whose onboarding is Not Started or whose account is Suspended or Pending Verification. Fix at source or filter in KPI calculations.

## 4. Deliverables

| Stage | Location |
|---|---|
| Data quality scripts | 09_Data_Quality |
| SQL database and KPI queries | 16_SQL_Database |
| Power BI data, measures, dashboard | 17_PowerBI |
| Earlier documentation | folders 00 to 14 |

## 5. Tools used

Python (pandas, sqlite3), SQLite, Power BI Desktop, VS Code, PowerShell.