from pathlib import Path
from datetime import datetime
import sqlite3
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
con = sqlite3.connect(ROOT / "16_SQL_Database" / "veloop.db")
q = lambda s: con.execute(s).fetchone()[0]

total_users = q("SELECT COUNT(DISTINCT user_id) FROM users")
active = q("SELECT COUNT(*) FROM users WHERE account_status='Active'")
onb = q("SELECT ROUND(100.0*SUM(onboarding_status='Completed')/COUNT(*),2) FROM users")
sessions = q("SELECT COUNT(*) FROM sessions")
task_pct = q("SELECT ROUND(100.0*SUM(task_status='Completed')/COUNT(*),2) FROM task_activity")
src = pd.read_sql_query("SELECT acquisition_source, COUNT(*) AS users FROM users GROUP BY 1 ORDER BY 2 DESC", con)
br = pd.read_csv(ROOT / "09_Data_Quality" / "automated_audit" / "business_rule_issues.csv")
basic = pd.read_csv(ROOT / "09_Data_Quality" / "automated_audit" / "data_quality_issues.csv")

L = ["# VELOOP Rewards - Data Analyst Task 01: Final Consolidated Report", "",
     "Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M"), "",
     "## 1. Headline KPIs (SQL database and Power BI)", "",
     "| KPI | Value |", "|---|---|",
     f"| Total users | {total_users} |", f"| Active users | {active} |",
     f"| Onboarding completion % | {onb} |", f"| Total sessions | {sessions} |",
     f"| Task completion % | {task_pct} |", "",
     "## 2. Users by acquisition source", "", "| Source | Users |", "|---|---|"]
for _, r in src.iterrows():
    L.append(f"| {r['acquisition_source']} | {r['users']} |")
L += ["", "## 3. Data quality results", "",
      f"- Basic issues found: {len(basic)} (missing values, duplicate IDs, invalid dates)",
      f"- Business rules checked: {len(br)}, failed: {int((br['records'] > 0).sum())}", "",
      "| Rule | Records | Description | Status |", "|---|---|---|---|"]
for _, r in br.iterrows():
    L.append(f"| {r['rule']} | {r['records']} | {r['description']} | {'FAIL' if r['records'] > 0 else 'PASS'} |")
L += ["", "Key finding: BR-05 and BR-06 fail. Task activity exists for users whose onboarding is Not Started or whose account is Suspended or Pending Verification. Fix at source or filter in KPI calculations.", "",
      "## 4. Deliverables", "", "| Stage | Location |", "|---|---|",
      "| Data quality scripts | 09_Data_Quality |",
      "| SQL database and KPI queries | 16_SQL_Database |",
      "| Power BI data, measures, dashboard | 17_PowerBI |",
      "| Earlier documentation | folders 00 to 14 |", "",
      "## 5. Tools used", "", "Python (pandas, sqlite3), SQLite, Power BI Desktop, VS Code, PowerShell."]
out = ROOT / "15_Final_Report" / "VELOOP_Final_Consolidated_Report.md"
out.write_text("\n".join(L), encoding="utf-8")

S = ["# SQL Queries Explained (Hinglish)", "",
     "- SELECT: kaun se columns dikhane hain. FROM: kis table se.",
     "- WHERE: sirf wahi rows jo condition match karein.",
     "- GROUP BY: ek category ke hisaab se rows ki gathri banana.",
     "- COUNT(*): rows ginna. COUNT(DISTINCT x): alag-alag values ginna.",
     "- ORDER BY ... DESC: bade se chhota sort. HAVING: GROUP BY ke baad condition.",
     "- CASE WHEN: SQL ka if-else, percentage nikalne ke liye.", "",
     "## 12 KPI queries", "",
     "1. total_users: alag user_id ginta hai.",
     "2. active_users: Active account wale users aur percentage.",
     "3. onboarding_completion_rate: Completed onboarding / total users * 100.",
     "4. users_by_acquisition_source: har source se kitne users.",
     "5. session_summary: total sessions, average duration, sessions per user.",
     "6. avg_daily_active_users: har date ke unique users ka average.",
     "7. returning_users: 2 ya zyada alag dino par active users.",
     "8. task_status_breakdown: Completed/Failed/Abandoned/Pending count aur percentage.",
     "9. task_completion_by_category: har category ka completion percentage.",
     "10. reward_credit_rate: completed tasks mein se kitno ka reward Credited.",
     "11. top_features_by_events: sabse zyada use hone wale features.",
     "12. milestones_by_type: har milestone type kitni baar aaya aur kitne users."]
(ROOT / "16_SQL_Database" / "SQL_Explained.md").write_text("\n".join(S), encoding="utf-8")

print("Created:", out)
print("Created:", ROOT / "16_SQL_Database" / "SQL_Explained.md")
print("\n===== PROJECT CHECK =====")
for d in sorted(p for p in ROOT.iterdir() if p.is_dir() and p.name[:2].isdigit()):
    n = sum(1 for f in d.rglob("*") if f.is_file())
    print(f"{d.name:28} {n} files")
