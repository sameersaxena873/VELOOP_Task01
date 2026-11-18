# VELOOP Rewards — Privacy & Governance Proposal (Deliverable 17)

**Status:** Proposed. Nothing in this document is confirmed as implemented in VELOOP production systems.
**Data basis:** Simulated dataset (SIMULATED — CREATED FOR ANALYTICAL TESTING). No real user data is used or described.

---

## 1. Purpose

This document proposes how analytics data for VELOOP Rewards should be collected, accessed, protected, and retained. It covers who may see what, which information must stay out of analytics entirely, and what rules apply when production data eventually replaces the simulated dataset.

It does not define security controls for VELOOP's infrastructure. Those belong to the engineering and security teams and must be verified by them.

---

## 2. Guiding Principles

1. **Collect only what is needed.** Every analytics field must have a stated analytical purpose recorded in the Data Dictionary.
2. **Use identifiers, not identities.** Analytics tables use `user_id`, `task_id`, `transaction_id` and similar IDs. Names, contact details, and government identifiers are not analytics fields.
3. **Aggregate for wider audiences.** Most stakeholders should see aggregated figures, not row-level records.
4. **Separate simulated and production data.** They must never be mixed silently. Simulated tables carry the label "SIMULATED — CREATED FOR ANALYTICAL TESTING".
5. **Record what is unknown.** Access and retention rules that VELOOP has not confirmed are marked To Be Verified.

---

## 3. Access Model (Proposed)

| Role | Access Level | Examples of Data |
|---|---|---|
| Engineering | Event implementation and technical validation. Access to raw event schemas, not to bulk personal data. | Event payload definitions, schema tests, pipeline logs without personal content |
| Data Analyst | Approved analytical datasets only. | Sanitized user-level tables using `user_id` and analytical attributes |
| Product / Operations | Aggregated business reporting. | KPI dashboards, counts and rates by feature or period |
| Content Team | Aggregated content performance data where required. | Help-center views and issue categories, aggregated |
| Intern / Trainee | Only approved, sanitized, or simulated datasets. | Simulated dataset from this project |

**Rule:** Access is granted by role and purpose, not by personal request. Actual role assignments and approval processes are To Be Verified with VELOOP.

---

## 4. Data That Must Not Enter Analytics

The following must never be stored in analytics tables, event payloads, or dashboards:

- Passwords, password hashes, or any authentication secrets
- API keys, tokens, session secrets, or private keys
- Payment credentials, card numbers, bank account details
- Government identifiers (for example national ID or PAN-type numbers)
- Full contact details (phone number, email address) in analytics tables
- Precise location data beyond the country or state level
- Internal security control details, such as fraud rule thresholds

**Note:** This project does not define fraud thresholds or security rules. Any such mechanism, if it exists in VELOOP, is confidential and must not be reverse-engineered or documented here.

---

## 5. Sensitive Attributes: Handling Rules

The Data Dictionary includes fields that need extra care:

| Field | Concern | Proposed Handling |
|---|---|---|
| `user_id` | Pseudonymous identifier | Allowed. Must not be derived from personal data. |
| `age_band` | Sensitive demographic | Store as a band (e.g., 25-34), never exact age. Under-18 users are excluded by policy (see Data Dictionary). |
| `country` / `state` | Location | Country and state only. No city, address, or GPS coordinates. |
| `consent_status` | Consent record | Required. Analytics should only use data where consent permits it. Consent rules are To Be Verified. |
| `marketing_opt_in` | Consent preference | Boolean only. Must be respected in any outreach reporting. |
| `email_verification_status` | Account state | Status only. The email address itself is not stored in analytics. |
| `account_status` | Account state | Allowed. Used for lifecycle analysis. |

---

## 6. Consent and Purpose

- Analytics on user behavior should rely on a documented purpose and, where required, user consent. The exact consent requirements under applicable law are **To Be Verified** and should be confirmed by VELOOP legal or compliance.
- A `consent_status` field is proposed in the Data Dictionary so that analysts can exclude users who have not consented, once VELOOP confirms the rule.
- This document does not give legal advice. Consent and data protection obligations depend on the jurisdictions where VELOOP operates.

---

## 7. Retention (Proposed)

| Data Type | Proposed Retention | Status |
|---|---|---|
| Raw event data | To Be Verified by VELOOP | To Be Verified |
| Aggregated KPI tables | Long-term, if they contain no personal data | Proposed |
| Simulated datasets | Retain for project submission, then delete or archive with label | Proposed |

Specific retention periods should be set by VELOOP based on legal requirements and business need. This document does not invent a retention period.

---

## 8. Data Quality as a Governance Control

Governance includes trust in the data. The following checks are proposed at each stage (detailed in the Data Quality Control Framework):

- ID validation at ingestion
- Status values checked against an approved list
- Duplicate transaction detection using `transaction_id`
- Timestamp format and timezone validation (UTC)
- Referential integrity: every `user_id` in related tables must exist in the Users table

---

## 9. Change Management

Changes to events, fields, KPIs, or access rules must be recorded in the Metric/Event Change Log (Deliverable 20 / Implementation Backlog) with date, old and new definition, reason, affected KPIs and dashboards, owner, and version.

---

## 10. Ownership (Proposed)

| Responsibility | Owner |
|---|---|
| Event implementation | Engineering |
| Analytical definitions and KPI catalogue | Data Analyst |
| Access approvals | To Be Verified (VELOOP leadership) |
| Consent and legal compliance | To Be Verified (VELOOP legal/compliance) |
| Dashboard publishing | Analytics / Product |

---

## 11. Open Items (To Be Verified)

| ID | Item | Why It Matters |
|---|---|---|
| G001 | Which consent rules apply to behavioral analytics | Determines whether users can be included |
| G002 | Approved retention periods for raw and aggregated data | Required for storage and compliance |
| G003 | Actual role-to-access mapping in VELOOP | Required before any dataset is shared |
| G004 | Whether any personal data currently flows into analytics systems | Determines urgency of cleanup |
| G005 | Who approves access requests and how | Needed for the access model to work |

---

## 12. Summary

Analytics for VELOOP should use pseudonymous IDs and aggregated outputs wherever possible. Passwords, secrets, payment credentials, and government identifiers must never enter analytics. Consent, retention, and access approvals are open items that VELOOP must confirm. This proposal is a starting point, not a verified policy.
