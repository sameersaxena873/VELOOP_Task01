from pathlib import Path
from datetime import datetime
import pandas as pd

HERE = Path(__file__).resolve().parent
AUDIT = HERE / "automated_audit"

prof = pd.read_csv(AUDIT / "dataset_profile.csv")
basic = pd.read_csv(AUDIT / "data_quality_issues.csv")
br = pd.read_csv(AUDIT / "business_rule_issues.csv")

lines = []
lines.append("# VELOOP Automated Data Quality Summary")
lines.append("")
lines.append("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M"))
lines.append("")
lines.append("## 1. Overview")
lines.append("")
lines.append(f"- Datasets profiled: {len(prof)}")
lines.append(f"- Basic issues detected: {len(basic)}")
lines.append(f"- Business rules checked: {len(br)}")
lines.append(f"- Business rules failed: {int((br['records'] > 0).sum())}")
lines.append("")
lines.append("## 2. Basic issues by type")
lines.append("")
lines.append("| Issue | Count |")
lines.append("|---|---|")
for k, v in basic["issue"].value_counts().items():
    lines.append(f"| {k} | {v} |")
lines.append("")
lines.append("## 3. Business rule results")
lines.append("")
lines.append("| Rule | Severity | Records | Description | Status |")
lines.append("|---|---|---|---|---|")
for _, r in br.iterrows():
    status = "FAIL" if r["records"] > 0 else "PASS"
    lines.append(f"| {r['rule']} | {r['severity']} | {r['records']} | {r['description']} | {status} |")
lines.append("")
lines.append("## 4. Notes")
lines.append("")
lines.append("- BR-05 and BR-06 fail: task activity exists for users whose onboarding is Not Started or whose account is Suspended / Pending Verification.")
lines.append("- BR-07 passes: every Credited reward belongs to a Completed task.")
lines.append("- Messy audit sheets (Users_Messy_Audit, 10_Event_Data_Quality_Audit) contain intentional issues for testing.")

(HERE / "Automated_Audit_Summary.md").write_text("\n".join(lines), encoding="utf-8")
print("Created:", HERE / "Automated_Audit_Summary.md")
