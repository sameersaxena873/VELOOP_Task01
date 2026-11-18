# Earning and Reward Analytics Specification (WP-C)

SIMULATED — CREATED FOR ANALYTICAL TESTING. Not actual VELOOP data.

## Lifecycle and what to measure
| Stage | What happens | What to measure | Event (Proposed) |
|---|---|---|---|
| Discovery | Task shown or opened | Views and opens | task_viewed, task_opened |
| Start | User begins task | Starts | task_started |
| Completion | User finishes the task | Completion attempts and outcomes | task_completed, task_failed |
| Validation | Platform or third party confirms completion | Validation outcome and time | Validation fields on task_completed |
| Reward | Reward credited, pending or reversed | Credited value, pending value, reversals | reward_credited, reward_pending, reward_reversed |

The key rule: **activity occurred is not the same as reward credited.** A task can be completed but its reward still pending, or later reversed.

## C1. Task-level fields
task_id, task_category (feature), user_id, task_started_at, task_completed_at, task_status, reward_amount, reward_unit, validation_status, validation_source, session_id. Field-level details are in 05_Data_Dictionary.

## C2. Failed activity (Proposed classification)
Only reasons present in the supplied data are used: Validation failed, Timeout, Task unavailable, Incomplete action, User exited. "Abandoned" is a task status, not a reason. "System error" is a proposed category that does not yet exist in the data, so it is marked Proposed.

## C3. Reward events
- **Credited:** value added to the user balance.
- **Pending:** awaiting validation or confirmation.
- **Reversed:** a credited reward removed; must reference the original reward.
- **Corrected:** amount or status fixed after a mistake (Proposed; not in supplied data).

## C4. Third-party dependency
Ads, surveys, offers, games and tracking tasks depend on external providers. A provider can delay, reject or fail to confirm completion. Analytics must store the provider's status separately (validation_source, provider status). VELOOP does not control these outcomes, so a missing provider signal is recorded as "pending", not as "failed".

## Observed in supplied simulated data (not VELOOP results)
Task rows: 9,846. Completed: 5,627. Failed: 1,520. Abandoned: 2,051. Pending: 648. Reward status Credited: 5,627.
