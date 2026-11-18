# Developer Analytics Handoff (WP-N)

Each event below is PROPOSED. Engineering must confirm feasibility and the acceptance tests.

## REQ-001 — task_completed
- Trigger: task completion has passed the applicable validation process.
- Payload fields: user_id (string, required), task_id (string, required), task_category (enum, required), timestamp (UTC ISO 8601, required), status (Completed, required), reward_amount (decimal, required if reward exists), reward_unit (enum, required with reward_amount), event_id (UUID, required), session_id (string, optional).
- Validation: task_category in allowed list; reward_amount >= 0.
- Deduplication: event_id unique; also one task_completed per (user_id, task_id, attempt).
- KPI dependency: KPI-10, KPI-11.
- Acceptance test: when one valid completion occurs, exactly one task_completed event is stored. Retrying the same completion sends the same event_id and is stored once.
- Priority: Critical.

## REQ-002 — reward_credited
- Trigger: reward is added to the user balance.
- Payload: user_id, reward_id, source_event_id (must be task_completed event_id or mission/spin id), reward_amount, reward_unit, timestamp, transaction_id.
- Rule: reward_credited may only occur for a source event in Completed state.
- Acceptance test: a Failed or Abandoned task never produces reward_credited.
- Priority: Critical.

## REQ-003 — wallet_transaction_created / completed / reversed
- Trigger: wallet ledger row created, finalised or reversed.
- Payload: transaction_id (unique, required), user_id, transaction_type, amount, unit, status, reference_id, reversal_of_transaction_id (reversal only).
- Rule: reversal must reference an existing completed transaction. Amounts never edited; reversal is a new row.
- Acceptance test: resending the same transaction_id is rejected with no second row.
- Priority: Critical.

## REQ-004 — withdrawal_requested
- Trigger: user submits a withdrawal request that passes eligibility checks.
- Payload: withdrawal_id, user_id, requested_amount, unit, method (enum), requested_at.
- Rule: no account numbers or payment credentials in analytics payload.
- Acceptance test: request stored once; subsequent state changes reference the same withdrawal_id.
- Priority: Critical.

## REQ-005 — referral_converted
- Trigger: referral reaches Converted status (rule To Be Verified, A006).
- Payload: referral_id, referring_user_id, referred_user_id, converted_at.
- Acceptance test: a referral with status Registered but not Activated never emits referral_converted.
- Priority: High (blocked by A006).
