# Analytics Specifications (WP-B to WP-E)

All items are PROPOSED unless marked otherwise. Simulated data must never be described as VELOOP results.

## B. User and account lifecycle
- Stable identifier: user_id (never reused, never derived from email).
- Lifecycle timestamps: registration_datetime, email verified time, onboarding started/completed, last activity, status changed time.
- Account status values: Active, Inactive, Pending Verification, Suspended. Transitions must be logged (see 05_Data_Dictionary).
- Do not collect unnecessary personal data. Analytics uses user_id and attributes; names and emails are restricted and not needed for analysis.

## C. Earning and reward lifecycle
Discovery → Start → Completion → Validation → Reward.
- Activity occurred (task_completed) is NOT the same as reward credited (reward_credited).
- Failed activity uses a proposed classification: failure_reason = Validation failed, Timeout, Task unavailable, Incomplete action, User exited (values from supplied data; to be confirmed).
- Reward states: Pending, Credited, Reversed, Corrected.
- Third-party dependency: ad and survey providers may not report completion. Reconciliation is required before reward analytics can be treated as final.

## D. Wallet and withdrawals
- Wallet transaction key: transaction_id (unique, idempotent). Types: Reward Credit, Redemption, Reversal, Adjustment (Proposed).
- Withdrawal lifecycle: Requested → Processing → Completed, with Rejected and Reversed as alternate end states (Proposed).
- Required withdrawal fields: withdrawal_id, user_id, requested amount, method, requested_at, processing_at, final_at, status, reason category.
- Never store account numbers or payment credentials in analytics tables.

## E. Referrals and engagement
Referral Created → User Registered → User Activated → Referral Converted.
- Registration does NOT equal conversion.
- Activation rule is unknown (Assumption A006).
- Engagement metrics: feature adoption, repeat usage, task activity, daily activity, feature frequency, active users, returning users.
