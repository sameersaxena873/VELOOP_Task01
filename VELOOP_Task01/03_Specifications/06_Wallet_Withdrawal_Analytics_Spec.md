# Wallet and Withdrawal Analytics Specification (WP-D)

SIMULATED — CREATED FOR ANALYTICAL TESTING. Not actual VELOOP data.

## D1. Wallet transaction model
| Field | Type | Rule |
|---|---|---|
| transaction_id | String | Unique, idempotent key |
| user_id | String | Must exist in Users |
| timestamp | UTC datetime | ISO 8601 |
| transaction_type | Enum | Reward Credit, Redemption, Reversal, Adjustment (Adjustment is Proposed) |
| direction | Enum | credit or debit; must match the type |
| amount | Decimal | Positive; direction gives the sign |
| unit | Enum | To Be Verified (A011) |
| status | Enum | Pending, Completed, Reversed |
| source | Enum | Task, Daily Reward, Mission, Spin, Referral, Withdrawal |
| reference_id | String | Points to the source record |
| reversal_of_transaction_id | String | Only on reversal rows; original must be Completed |

Rule: a reversal is a new row. Original rows are never edited.

## D2. Withdrawal lifecycle
Requested → Processing → Completed, with Rejected and Reversed as alternative end states (Proposed).

| Field | Rule |
|---|---|
| withdrawal_id | Unique |
| user_id | Must exist |
| requested_amount | More than zero; not more than available balance |
| method | UPI, Bank Transfer, Other (placeholder until verified) |
| requested_at, processing_at, final_at | UTC; in this order |
| status | One of the lifecycle states |
| reason_category | Required for Rejected and Reversed |

Never store account numbers, card numbers or payment credentials in analytics tables.

## D3. Withdrawal KPIs
| KPI | Definition | Formula | Limitation |
|---|---|---|---|
| Withdrawal requests | Count of requests in period | COUNT(withdrawal_id) | Includes requests later rejected |
| Completed withdrawals | Count with final status Completed | COUNT where status = Completed | Provider lag can shift counts |
| Pending queue | Requests not yet final | COUNT where status in Requested, Processing; age in days | Snapshot only |
| Rejected withdrawals | Count with status Rejected | COUNT where status = Rejected | Reasons not standardised yet |
| Reversed withdrawals | Count with status Reversed | COUNT where status = Reversed | Reversal reasons vary |
| Processing time | Median hours from requested_at to final_at | MEDIAN(final_at − requested_at) | Use median, not mean |
| Completion rate | Completed / final withdrawals | COUNT(Completed) / COUNT(Completed+Rejected+Reversed) | Excludes pending, so it is not a success rate of all requests |
| Method distribution | Share by method | COUNT by method / total | Method names are placeholders |

Stakeholders: Finance (volume, reversals), Operations (queue, processing time), Product (method mix).

## Observed in simulated tables (not VELOOP results)
Withdrawal requests: 1,200. Completed: 857. Pending: 103. Rejected: 128. Reversed: 112.
