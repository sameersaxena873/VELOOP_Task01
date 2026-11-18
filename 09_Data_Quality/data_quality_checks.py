
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "input_data"
OUTPUT = Path(__file__).resolve().parent / "automated_audit"

OUTPUT.mkdir(exist_ok=True)

files = list(INPUT.glob("*.xlsx"))

if not files:
    raise FileNotFoundError("No Excel files found in input_data")

profiles = []
issues = []
user_ids = set()

print("\nVELOOP DATA QUALITY AUDIT")
print("=" * 50)

for file in files:
    excel = pd.ExcelFile(file)

    for sheet in excel.sheet_names:
        df = pd.read_excel(file, sheet_name=sheet)

        if df.empty:
            continue

        id_cols = [
            c for c in df.columns
            if c.lower() in ["user_id", "event_id",
                             "transaction_id", "activity_id",
                             "session_id", "withdrawal_id",
                             "referral_id"]
        ]

        for col in id_cols:
            if col == "user_id" and "Users" in sheet:
                user_ids.update(
                    df[col].dropna().astype(str).str.strip()
                )

        duplicate_count = 0
        for col in id_cols:
            count = int(df[col].duplicated().sum())
            duplicate_count += count

            if count:
                issues.append({
                    "file": file.name,
                    "sheet": sheet,
                    "field": col,
                    "issue": "Duplicate ID",
                    "records": count
                })

        missing = int(df.isna().sum().sum())

        profiles.append({
            "file": file.name,
            "sheet": sheet,
            "records": len(df),
            "columns": len(df.columns),
            "missing_values": missing,
            "duplicate_id_count": duplicate_count
        })

        for col in df.columns:
            count = int(df[col].isna().sum())

            if count:
                issues.append({
                    "file": file.name,
                    "sheet": sheet,
                    "field": col,
                    "issue": "Missing values",
                    "records": count
                })

        for col in df.columns:
            if "date" in col.lower() or "time" in col.lower():
                parsed = pd.to_datetime(df[col], errors="coerce")
                invalid = int((df[col].notna() & parsed.isna()).sum())

                if invalid:
                    issues.append({
                        "file": file.name,
                        "sheet": sheet,
                        "field": col,
                        "issue": "Invalid date/time",
                        "records": invalid
                    })

        print(
            f"Checked: {file.name} | {sheet} | "
            f"{len(df)} rows"
        )

pd.DataFrame(profiles).to_csv(
    OUTPUT / "dataset_profile.csv", index=False
)

pd.DataFrame(issues).to_csv(
    OUTPUT / "data_quality_issues.csv", index=False
)

print("\nAUDIT COMPLETED")
print("Datasets profiled:", len(profiles))
print("Issues detected:", len(issues))
print("Output folder:", OUTPUT)
print("=" * 50)