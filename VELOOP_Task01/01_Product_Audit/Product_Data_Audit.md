# Product Data Audit (WP-A)

SIMULATED — CREATED FOR ANALYTICAL TESTING. Not actual VELOOP data.

## 1. Scope and sources
- Task 01 brief (PDF): the only product-level source supplied in this run.
- Two simulated workbooks: user, session, feature, daily and task data; plus a rewards-users file with a messy-data sheet.
- The Google Drive product folder was **not** reviewed. Every product fact below is either Proposed or To Be Verified.

## 2. Product area mapping (A1)
Each row is one product area. Status shows whether the area is Proposed, To Be Verified or Confirmed. Nothing is Confirmed yet.

| Product Area | Feature | User Action | System Action | Business Outcome | Data Required | Business Question | Status | Priority |
|---|---|---|---|---|---|---|---|---|
| Registration | Sign up | Enters details, verifies email | Creates account, sends verification | Account created | user_id, registration_datetime, acquisition_source, platform | How many users join and from which source? | Proposed | Critical |
| Login | Login | Logs in | Session starts | Successful session | user_id, session_id, timestamp, device | How often do users return? | Proposed | High |
| Onboarding | Complete onboarding | Completes steps | Status updated | Onboarding completed | onboarding_status, milestone timestamps | Where do users drop off during onboarding? | Proposed | High |
| Tasks | Task viewed / opened / started | Browses and starts a task | Task record created | Task started | task_id, task_type, timestamps | Which tasks get started? | Proposed | Critical |
| Tasks | Task completed | Finishes task | Validation runs (may be third-party) | Completed / Failed / Abandoned | task_status, failure_reason, validated_at | What share of started tasks succeed? | Proposed | Critical |
| Rewards | Reward credit | None (system) | Reward credited to balance | Reward credited / pending / reversed | reward_amount, reward_unit, reward_status | Are earnings actually credited? | Proposed | Critical |
| Daily Rewards | Claim daily reward | Taps claim | Reward credited | Claimed | claim_date, reward_amount | Are daily rewards used? | Proposed | Medium |
| Streaks | Daily activity | Returns on consecutive days | Streak counter updated | Streak length | streak_count, activity_date | Does streak mechanic drive retention? | Proposed | Medium |
| Missions | Start / complete mission | Starts and finishes | Mission status updated | Mission complete | mission_id, status | Which missions are completed? | Proposed | High |
| Spin | Spin the wheel | Spins | Outcome generated, reward credited | Spin result | spin_id, outcome, reward_amount | Spin usage vs reward cost? | Proposed | Medium |
| Badges & Levels | Earn badge / level up | None (system) | Badge awarded | Badge earned | badge_id, level, timestamp | Do badges affect engagement? | Proposed | Low |
| Referrals | Share referral code | Shares code | Referral record created | Referral created | referral_id, referring_user_id | How many referrals are created? | Proposed | High |
| Referrals | Referred user registers | Registers with code | Link recorded | Registered | referred_user_id, registration_datetime | Does registration convert? | Proposed | High |
| Referrals | Referred user activated | Completes activation step (definition To Be Verified) | Activation recorded | Activated / converted | activation_datetime, activation_rule | Which referrals become valuable users? | To Be Verified | High |
| Wallet | Wallet transaction | None or redeem | Transaction recorded | Completed / reversed | transaction_id, type, amount, status, reference_id | Where does balance move? | Proposed | Critical |
| Withdrawals | Request withdrawal | Requests payout | Request queued | Requested | withdrawal_id, amount, method, requested_at | How many payouts are requested? | Proposed | Critical |
| Withdrawals | Processing / approval | nan | Processed / rejected / completed | Final status | processed_at, completed_at, reason_category | How long does processing take? | Proposed | Critical |
| Exchange Center | Exchange conversion | Exchanges currency | Conversion recorded | Converted | exchange_id, from_unit, to_unit, amount | Is exchange used and at what volume? | To Be Verified | Medium |
| Help Center | Views help content / contacts support | Opens help page | Support ticket (if raised) | Ticket / view | page_id, issue_category | Which issues drive support requests? | To Be Verified | Low |
| Advertisements / Surveys (third-party) | Watch ad / take survey | Completes ad or survey | Third-party reports completion | Completed (external) | external_offer_id, provider_status | Can completion be reconciled with provider? | To Be Verified | High |

## 3. User actions, system actions and business outcomes (A2, A3)
Not every step is a user action. The task lifecycle shows the difference:

| Step | Type | Who produces it |
|---|---|---|
| Task viewed / opened / started | User event | Frontend |
| Task completed | User action with system validation | User action, then backend validation |
| Completion validated | System event | Backend or third party |
| Reward credited / reversed | System event | Rewards service |
| Reward activity over time | Business outcome | Analytics (derived) |

The same split applies to withdrawals (user requests, system processes, business outcome is completed payout volume) and referrals (user shares, system registers and activates, business outcome is conversion).

## 4. Findings from supplied data (simulated, not VELOOP results)
1. Feature names in the event data cover 15 areas, but none is confirmed as live in production.
2. Rewards, Wallet, Withdrawals and Referrals are not in the supplied files. Simulated tables were created and labelled.
3. Data quality issues found are listed in 09_Data_Quality. The most serious are identity conflict across files (DQ-006) and credits before completion (DQ-009).
4. Several proposed fields depend on unknowns recorded in the Assumption Register (A001 to A014).

## 5. What is not known
See 14_Backlog/Assumption_Verification_Register.xlsx. The most important: backend event emission (A001), transaction ID uniqueness (A003), referral activation rule (A006), reward units (A011), and third-party reconciliation (A012).
