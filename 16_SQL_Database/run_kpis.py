from pathlib import Path
import re
import sqlite3
import pandas as pd

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)

HERE = Path(__file__).resolve().parent
OUT = HERE / "kpi_results"
OUT.mkdir(exist_ok=True)

sql_text = (HERE / "kpi_queries.sql").read_text(encoding="utf-8")
blocks = re.split(r"-- KPI:\s*", sql_text)[1:]

con = sqlite3.connect(HERE / "veloop.db")
ok = 0
for b in blocks:
    name, _, query = b.partition("\n")
    name = name.strip()
    try:
        df = pd.read_sql_query(query.strip(), con)
        df.to_csv(OUT / f"{name}.csv", index=False)
        print(f"\n=== {name} ===")
        print(df.to_string(index=False))
        ok += 1
    except Exception as e:
        print(f"\n=== {name} === ERROR: {e}")
con.close()
print(f"\nKPIs run OK: {ok} / {len(blocks)}")
print("CSV folder:", OUT)
