from pathlib import Path
import sqlite3
import pandas as pd

pd.set_option("display.width", 250)
pd.set_option("display.max_columns", 30)
pd.set_option("display.max_colwidth", 45)

ROOT = Path(__file__).resolve().parent.parent

print("===== DB ROW COUNTS =====")
con = sqlite3.connect(ROOT / "16_SQL_Database" / "veloop.db")
for t in ["users", "sessions", "feature_events", "daily_activity", "task_activity", "milestones"]:
    n = con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
    print(f"{t:16} {n}")
con.close()

print("\n===== KPI CATALOGUE =====")
x = pd.ExcelFile(ROOT / "07_KPI_Catalogue" / "VELOOP_KPI_Catalogue.xlsx")
for s in x.sheet_names:
    df = x.parse(s)
    print(f"\n--- Sheet: {s} | {df.shape[0]} rows x {df.shape[1]} cols")
    print("Columns:", list(df.columns))

main = x.parse(x.sheet_names[0])
print("\n===== FIRST 6 ROWS OF FIRST SHEET =====")
print(main.head(6).to_string(index=False))
