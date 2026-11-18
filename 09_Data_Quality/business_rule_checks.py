from pathlib import Path
import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
FILE = ROOT / "input_data" / "VELOOP_Simulated_User_Behavior_1000.xlsx"
OUT = HERE / "automated_audit"
OUT.mkdir(exist_ok=True)

users = pd.read_excel(FILE, sheet_name="01_Users_1000")
sessions = pd.read_excel(FILE, sheet_name="02_Sessions")
events = pd.read_excel(FILE, sheet_name="03_Feature_Events")
tasks = pd.read_excel(FILE, sheet_name="05_Task_Activity")

print("account_status values:", users["account_status"].dropna().unique().tolist())
print("onboarding_status values:", users["onboarding_status"].dropna().unique().tolist())
print("task_status values:", tasks["task_status"].dropna().unique().tolist())
print("reward_status values:", tasks["reward_status"].dropna().unique().tolist())
print("-" * 50)

results = []

def add(rule, desc, severity, count):
    results.append({"rule": rule, "description": desc, "severity": severity, "records": int(count)})
    print(f"{rule} | {severity} | {count} records | {desc}")

# BR-01 session_end before session_start
s_start = pd.to_datetime(sessions["session_start"], errors="coerce")
s_end = pd.to_datetime(sessions["session_end"], errors="coerce")
add("BR-01", "session_end is before session_start", "High", (s_end < s_start).sum())

# BR-02 negative session duration
dur = pd.to_numeric(sessions["session_duration_seconds"], errors="coerce")
add("BR-02", "Negative session_duration_seconds", "High", (dur < 0).sum())

# BR-03 sessions with unknown user_id
add("BR-03", "Sessions with user_id not in Users sheet", "Critical",
    (~sessions["user_id"].isin(users["user_id"])).sum())

# BR-04 events with unknown session_id
add("BR-04", "Events with session_id not in Sessions sheet", "High",
    (~events["session_id"].isin(sessions["session_id"])).sum())

# Users lookup (one row per user_id)
ulook = users.drop_duplicates("user_id")[["user_id", "onboarding_status", "account_status"]]
t = tasks.merge(ulook, on="user_id", how="left")

# BR-05 task activity but onboarding Not Started
ob = t["onboarding_status"].fillna("").str.strip().str.lower()
add("BR-05", "Task activity for users with onboarding Not Started", "High",
    (ob == "not started").sum())

# BR-06 task activity for suspended/pending accounts
acc = t["account_status"].fillna("").str.strip().str.lower()
add("BR-06", "Task activity for suspended or pending accounts", "High",
    (acc.str.startswith("suspended") | acc.str.startswith("pending")).sum())

# BR-07 reward credited but task not completed
ts = t["task_status"].fillna("").str.strip().str.lower()
rs = t["reward_status"].fillna("").str.strip().str.lower()
add("BR-07", "Reward Credited but task not completed", "Critical",
    ((rs == "credited") & (~ts.str.contains("complet"))).sum())

pd.DataFrame(results).to_csv(OUT / "business_rule_issues.csv", index=False)
print("-" * 50)
print("Saved:", OUT / "business_rule_issues.csv")

