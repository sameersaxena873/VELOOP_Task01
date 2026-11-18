# VELOOP — Data Quality Control Framework

## 1. Objective

The objective of this framework is to prevent,
detect and correct data quality issues in the
VELOOP analytics system.

This framework is a proposed design.
It is not a confirmation of existing controls.

## 2. Data Quality Rules

| ID | Quality Rule | Validation |
|----|--------------|------------|
| DQ01 | User ID | Must not be blank |
| DQ02 | Transaction ID | Must be unique |
| DQ03 | Timestamp | Must be valid |
| DQ04 | Status | Must match allowed values |
| DQ05 | Amount | Must be numeric |
| DQ06 | Duplicate Records | Detect duplicate IDs |
| DQ07 | User Relationship | User ID must exist |
| DQ08 | Missing Values | Check required fields |
| DQ09 | Date Format | Use standard date format |
| DQ10 | Event ID | Must be unique |

## 3. Data Quality Control Stages

### Stage 1 — Application
Validate required fields before submission.

### Stage 2 — Data Collection
Check event names, IDs and timestamps.

### Stage 3 — Raw Data
Store original records and identify errors.

### Stage 4 — Transformation
Clean formats and detect duplicates.

### Stage 5 — Analytics Layer
Validate calculations and table relationships.

### Stage 6 — Dashboard
Display validated data only.

## 4. Responsibility

| Team | Responsibility |
|------|----------------|
| Engineering | Application validation |
| Data Team | Data quality checks |
| Analyst | Data profiling and reporting |
| Product Team | Business rule verification |

## 5. Error Handling

1. Identify the incorrect record.
2. Record the issue.
3. Assign severity.
4. Identify the responsible team.
5. Correct the issue after verification.
6. Re-run validation.

## 6. Important Note

All controls listed in this document are
proposed recommendations.

Their actual implementation status
requires engineering verification.