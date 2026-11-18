from pathlib import Path
import sqlite3
import pandas as pd

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)

ROOT = Path(__file__).resolve().parent.parent
RES = ROOT / "16_SQL_Database" / "kpi_results"

print("===== KPI RESULTS (01-10) =====")
for f in sorted(RES.glob("*.csv"))[:10]:
    df = pd.read_csv(f)
    print(f"\n--- {f.stem} ---")
    print(df.head(6).to_string(index=False))

print("\n===== EXPORT FOR POWER BI =====")
con = sqlite3.connect(ROOT / "16_SQL_Database" / "veloop.db")
OUT = ROOT / "17_PowerBI" / "data"
for t in ["users", "sessions", "feature_events", "daily_activity", "task_activity", "milestones"]:
    df = pd.read_sql_query(f"SELECT * FROM {t}", con)
    df.to_csv(OUT / f"{t}.csv", index=False, encoding="utf-8-sig")
    print(f"{t}.csv  ->  {len(df)} rows")
con.close()
print("Export folder:", OUT)
