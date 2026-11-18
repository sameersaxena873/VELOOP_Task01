# Analytics Readiness Gap Assessment (WP-R)

## Scorecard (evidence-based; 1 = absent, 5 = ready)
| Area | Score | Evidence |
|---|---|---|
| Event coverage | 1 | 32 events proposed; none confirmed in product |
| Data model | 2 | ER model designed; Rewards/Wallet/Withdrawals/Referrals exist only as SIMULATED tables |
| Data dictionary | 2 | 76 proposed fields; none confirmed |
| KPI definitions | 2 | 37 KPIs defined; 1 not calculable (support tickets); 15 calculable only on SIMULATED tables; 5 partial |
| Data quality | 2 | 17 issues logged; 1 Critical confirmed (DQ-006); DQ-009 not observed |
| Dashboard readiness | 1 | Specification only |
| Engineering instrumentation | 1 | Not verified |
| Access control | 2 | Model defined, not implemented |
| Documentation | 3 | Full set produced in this project |
| Reporting | 1 | None |

## Priority gaps
- G01 (Critical): No stable transaction ID for wallet movements — Wallet tables not in supplied data; transaction_id not in any sheet
- G02 (Critical): Reward_credited vs task_completed not separated — Task_Activity has reward_status but no reward table
- G03 (Critical): Cross-file user identity conflict (same user_id, different names) — Names match only 0.0% of shared IDs
- G04 (High): No failure reason for failed/abandoned tasks in Sessions (all sessions Completed) — All 7913 sessions have session_status=Completed
- G05 (High): Daily activity flag not informative (all Yes) — active_flag = Yes for all 6667 rows
- G06 (High): Referral data (created / registered / activated / converted) absent — No referral table in supplied data
- G07 (Critical): Withdrawal lifecycle absent — No withdrawal table in supplied data
- G08 (High): No definition of "activated" for referrals — Brief WP-E asks for it; nothing supplied
- G09 (High): Account status vs activity logic unverified — 601 task rows belong to Suspended users
- G10 (Medium): Platform field has one value only in messy file — platform has 1 unique value(s) in Users_Messy_Audit
- G11 (Medium): Feature naming inconsistent in audit sheet — 5 rows in 10_Event_Data_Quality_Audit use non-canonical feature names
- G12 (Medium): Exchange Center and Help Center have no event definitions — Feature_Events includes Exchange Center but no spec
- G13 (High): No third-party reconciliation fields for ads/surveys — No provider status or external ID in any sheet

## Key message
The biggest gap is identity and transaction integrity, not dashboards. Until a single user master and unique transaction IDs exist, reporting cannot be trusted.
