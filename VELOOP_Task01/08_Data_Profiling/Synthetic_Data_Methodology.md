# Synthetic Data Methodology

SIMULATED DATA — CREATED FOR ANALYTICAL TESTING. Not actual VELOOP data.

## Why this data exists
The supplied workbooks do not contain Rewards, Wallet, Withdrawals or Referrals. The Task 01 brief allows analysts to create additional simulated data if it is labelled and documented. This file is that data.

## Source
- user_id: taken from 01_Users_1000 in VELOOP_Simulated_User_Behavior_1000.xlsx.
- Rewards: sampled from 05_Task_Activity rows where reward_status is Credited or Pending. Reversals are added for 200 Credited rewards.

## Distributions (chosen by analyst, not VELOOP rates)
- Withdrawal status: Requested 5%, Processing 5%, Completed 70%, Rejected 12%, Reversed 8%.
- Referral status: Created 15%, Registered 25%, Activated 25%, Converted 25%, Expired 10%.
- Withdrawal method: UPI 50%, Bank Transfer 35%, Other 15% (placeholder).
- Reward amounts: fixed list 5 to 100. Reward unit is SIM_UNIT (placeholder, see Assumption A011).

## Rules enforced
- Foreign keys between tables are checked in 08_Data_Profiling/Simulated_Tables_Integrity_Checks.xlsx.
- Reversals reference an original Credited record.
- Redemptions reference Completed withdrawals only.
- No self-referrals, and each referred user appears once.

## Known limits
- Referral and reward timestamps are random and not aligned to user registration dates.
- Wallet credits are a sample of rewards, so totals will not reconcile.
- Reason codes and methods are placeholders, not VELOOP's real codes.
- Nothing here shows real VELOOP performance. Do not quote any figure from this file as a VELOOP result.

## Reproduce
Random seed 42 with numpy default_rng. Running the same script on the same inputs gives the same output.
