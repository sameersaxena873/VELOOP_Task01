# Referral and Engagement Analytics Specification (WP-E)

SIMULATED — CREATED FOR ANALYTICAL TESTING. Not actual VELOOP data.

## E1. Referral funnel
Referral Created → User Registered → User Activated → Referral Converted.

Registration does **not** equal conversion. Each step has its own timestamp and status.

| Field | Rule |
|---|---|
| referral_id | Unique |
| referring_user_id | Must exist; cannot equal referred_user_id |
| referred_user_id | Must exist; one referral per referred user |
| referral_created_at | UTC datetime |
| referral_registered_at | At or after created |
| referral_activated_at | At or after registered; activation rule To Be Verified (A006) |
| referral_status | Created, Registered, Activated, Converted, Expired (Proposed) |
| source | Channel the code was shared on (Proposed) |

## E2. Engagement measures
- **Feature adoption:** unique users using a feature divided by active users (KPI-17).
- **Repeat usage:** users with two or more sessions divided by users with at least one (KPI-13).
- **Task activity and daily activity:** task starts and completions per day (KPI-09, KPI-10).
- **Feature frequency:** events per feature per user per week (Proposed).
- **Active users:** users with a qualifying event in the period; qualifying list To Be Verified (A005).
- **Returning users:** active on two or more distinct days (KPI-03).

## Observed in simulated tables (not VELOOP results)
Referrals: 900. Registered: 688. Activated: 459. Converted: 239.
