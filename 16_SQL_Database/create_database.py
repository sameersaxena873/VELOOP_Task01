from pathlib import Path
import sqlite3
import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
FILE = ROOT / "input_data" / "VELOOP_Simulated_User_Behavior_1000.xlsx"
DB = HERE / "veloop.db"

tables = {
    "users": "01_Users_1000",
    "sessions": "02_Sessions",
    "feature_events": "03_Feature_Events",
    "daily_activity": "04_Daily_Activity",
    "task_activity": "05_Task_Activity",
    "milestones": "06_Milestones",
}

con = sqlite3.connect(DB)
for table, sheet in tables.items():
    df = pd.read_excel(FILE, sheet_name=sheet)
    df.to_sql(table, con, if_exists="replace", index=False)
    print(f"Loaded {table:16} <- {sheet:20} | {len(df)} rows")

con.execute("CREATE INDEX IF NOT EXISTS idx_sessions_user ON sessions(user_id)")
con.execute("CREATE INDEX IF NOT EXISTS idx_events_user ON feature_events(user_id)")
con.execute("CREATE INDEX IF NOT EXISTS idx_tasks_user ON task_activity(user_id)")
con.commit()

print("-" * 50)
print("TEST QUERY: users by account_status")
for row in con.execute("SELECT account_status, COUNT(*) FROM users GROUP BY account_status ORDER BY 2 DESC"):
    print(row)
con.close()
print("-" * 50)
print("Database created:", DB)
