# VELOOP Rewards — Data Pipeline Proposal (Deliverable 16)

**Status:** Proposed. No component described here is confirmed as existing in VELOOP production systems.
**Data basis:** Simulated dataset (SIMULATED — CREATED FOR ANALYTICAL TESTING).
**Diagram:** See `pipeline_architecture.png` in this folder.

---

## 1. Purpose

This document describes a practical analytics pipeline for VELOOP Rewards: how events are produced, collected, stored, validated, transformed, and reported. It is designed for a developing product. It avoids expensive infrastructure unless the volume justifies it.

---

## 2. Design Principles

1. **Start simple.** Use reliable, low-cost components first. Add complexity only when data volume or reporting needs require it.
2. **Validate early.** Bad data is cheaper to stop at ingestion than to clean up in dashboards.
3. **Keep raw data.** Raw events are stored unchanged so that transformations can be re-run if definitions change.
4. **Separate layers.** Raw, validated, and analytical layers are distinct so that errors in one do not silently reach another.
5. **Traceability.** Every KPI must trace back to a defined event, field, and source.

---

## 3. Pipeline Stages

```
VELOOP Application (Frontend / Backend)
        ↓
Application Events (defined in Event Tracking Plan)
        ↓
Collection (event API or logging service)
        ↓
Raw Data Storage (append-only, unchanged)
        ↓
Validation (quality rules from Data Quality Control Framework)
        ↓
Transformation (cleaning, joining, deduplication)
        ↓
Analytical Data Layer (Users, Tasks, Rewards, Wallet, Withdrawals, Referrals, Feature Events)
        ↓
BI / Dashboard (Power BI, per Dashboard Blueprint)
        ↓
Business Reporting (KPI Catalogue)
```

### 3.1 Source Systems and Event Producers

| Source | Produces | Status |
|---|---|---|
| Frontend app (web / mobile) | Feature views, task opens, UI actions | To Be Verified |
| Backend services | Task completion validation, reward credits, wallet transactions, withdrawal status changes | To Be Verified |
| Third-party providers (ads, surveys) | Completion reports, provider status | To Be Verified (reconciliation rule is an open item) |
| Support / help system | Ticket records, help-page views | To Be Verified |

**Rule:** Backend systems are the authoritative source for reward, wallet, and withdrawal events. Frontend events are useful for engagement but cannot confirm that money moved.

### 3.2 Collection

- Events are sent using the naming standard `domain_object_action` (for example `task_completed`, `withdrawal_requested`).
- Each event carries `event_id`, `user_id`, `timestamp` (UTC), and the required properties listed in the Developer Analytics Handoff.
- **Deduplication key:** `event_id`. The same event sent twice must be recorded once.
- **Option A (simplest):** Application writes events directly to a database table.
- **Option B (when volume grows):** Events go through a message queue before storage. Not required at the current simulated scale.

### 3.3 Raw Data Storage

- Append-only. Raw events are never edited in place.
- Stored with the received timestamp and the source system name, so late or re-sent events can be identified.
- Personal data must follow the rules in the Privacy & Governance Proposal (Deliverable 17).

### 3.4 Validation

Checks run at ingestion or immediately after. Examples:

- `event_id`, `user_id`, and `timestamp` are present
- `event_name` and `event_status` are in the approved list
- Timestamps are valid ISO 8601 in UTC
- Numeric amounts are not negative where that is invalid
- `user_id` exists in the Users table (referential integrity)
- No duplicate `event_id`

Invalid records are routed to a **quarantine table** with the reason, not silently dropped. The full rule set is in the Data Quality Control Framework.

### 3.5 Transformation

- Clean and standardize values (trim spaces, normalize capitalization, map status values)
- Deduplicate events
- Join related events into entities (for example, task start and task completion into Task Activity)
- Derive daily and period aggregates (for example, Daily Activity)
- Apply reward reversals and corrections as separate records, not edits to the original

Transformation logic should be versioned, so that a definition change can be traced (see Change Management in the Final Consolidated Report).

### 3.6 Analytical Data Layer

Tables defined in the Logical Data Model and Data Dictionary:

Users, Task Activity, Rewards, Wallet Transactions, Withdrawals, Referrals, Feature Events, Daily Activity, Sessions.

These are the only tables dashboards and KPIs should read from.

### 3.7 BI and Reporting

- Dashboards follow the Dashboard Blueprint (seven dashboards, specification only).
- KPIs follow the KPI Catalogue definitions exactly. A KPI that cannot be calculated from the available fields must say so.
- The Power BI prototype built in this project uses simulated data and is labelled as such.

---

## 4. Refresh, Monitoring, and Failure Handling

| Item | Proposal | Status |
|---|---|---|
| Refresh frequency | Daily for most KPIs; near-real-time only where a use case exists | Proposed |
| Monitoring | Count of events received per day per source; alert if a source drops to zero | Proposed |
| Quality monitoring | Quarantine count and rejection rate reported with each refresh | Proposed |
| Failure handling | Failed loads are retried; the previous successful analytical layer stays live until the new one passes validation | Proposed |
| Backfill | Re-run transformation from raw data when a definition changes | Proposed |

---

## 5. Ownership

| Responsibility | Owner |
|---|---|
| Event implementation in app and backend | Engineering |
| Raw storage and collection service | Engineering (To Be Verified) |
| Validation rules and quarantine review | Data / Engineering |
| Transformation and analytical layer | Data Analyst |
| Dashboards and KPI reporting | Analytics / Product |
| Access and governance | See Privacy & Governance Proposal |

---

## 6. Practicality Note

This pipeline does not require a data warehouse, streaming platform, or cloud service to start. The simulated dataset (76,386 rows in total: 65,929 across the six Power BI tables, plus 10,457 in the Rewards, Wallet, Withdrawals and Referrals sheets of Simulated_Rewards_Wallet_Withdrawals_Referrals.xlsx) can be processed on a single machine with Python and SQLite, which is what this project already uses. Heavier infrastructure should be proposed only when production volume, latency needs, or reporting scale make it necessary, and that decision is To Be Verified.

---

## 7. Open Items (To Be Verified)

| ID | Item | Why It Matters |
|---|---|---|
| P001 | Whether backend emits task completion events (A001) | Without this, task analytics cannot run from production |
| P002 | Whether a stable transaction ID exists (A003) | Needed for wallet deduplication |
| P003 | Where raw events are stored today | Determines the starting point for collection |
| P004 | Whether third-party completions can be reconciled (A012) | Affects reward accuracy |
| P005 | Expected event volume per day | Determines whether a queue is needed |

---

## 8. Summary

The proposed pipeline is simple: events are collected with clear names, stored raw, validated, transformed into a small set of analytical tables, and reported through KPIs with traceable definitions. Backend systems are the source of truth for money-related events. Everything that VELOOP has not confirmed is marked To Be Verified.
