import sqlite3
from pathlib import Path
import pandas as pd
con = sqlite3.connect(Path(__file__).resolve().parent / "veloop.db")
q = "SELECT account_status, COUNT(*) AS users FROM users GROUP BY account_status ORDER BY users DESC"
print(q)
print(pd.read_sql_query(q, con).to_string(index=False))
