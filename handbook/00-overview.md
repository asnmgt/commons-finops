# Handbook Overview

The Commons FinOps handbook is structured as five plain-language sections. Each section is anchored in a real compliance framework or accounting standard, calls out where automation belongs, and points to the templates and schema artifacts that operationalize the guidance.

Read in order if you're new. Jump straight to the section you need if you're not.

## The five sections

| # | Section | What it covers | Anchored in |
|---|---|---|---|
| 1 | [Operating the books](./01-operating-the-books.md) | Chart of accounts. Class taxonomy. Monthly close cadence. Restricted vs. unrestricted fund accounting. Reconciliation discipline. | FASB ASC 958 (Not-for-Profit Entities). GAAP. |
| 2 | [Compliance gates](./02-compliance-gates.md) | KYB at the host level. OFAC sanctions screening. 1099, W-9, W-8BEN. Federal Uniform Guidance. Single Audit threshold. State charitable solicitation registration. International tax treaties. | 2 CFR 200 (Uniform Guidance). IRS rules. FATCA. OFAC. |
| 3 | [Publishing the data](./03-publishing-the-data.md) | The funding-block v0.1 spec. Public ledger requirements. Class taxonomy as a machine-readable surface. Audit-trail integrity. Append-only disbursement feeds. | The schema lives in [`schema/`](../schema). |
| 4 | [Fiscal sponsor operations](./04-fiscal-sponsor-ops.md) | Sponsee onboarding flow. Lifecycle: insertion, orbit, accretion, ejection, sunsetting. Fee structure (direct cost, indirect, in-kind). Internal controls. Board governance. | COSO Internal Control Framework. Comprehensive Fiscal Sponsorship (Adler model). |
| 5 | [Working with funders](./05-working-with-funders.md) | Grant agreements. Reporting cadence. Indirect cost rates and how to publish them. Expenditure responsibility for private foundations giving to non-501(c)(3) projects. Restricted funds policy. | IRS Section 4945. NACUBO Indirect Cost Recovery Best Practices. |

## How each section is written

Every section has the same shape:

1. **The compliance ground**, in two paragraphs of plain language. What rule. What it requires. What happens if you miss it.
2. **The operational practice**, in checklist form. What you actually do, in order, monthly or per-grant or per-event.
3. **Automation notes**, called out separately. Which steps can be automated today. Which need human review. Which audit trails must survive the automation. Tooling examples (QuickBooks Online, Sage Intacct, Open Collective, Ramp, Bill.com, Stripe, Plaid).
4. **What to publish**, mapping each step to a field in the funding-block schema. Operational practice surfaces to public ledger surfaces to machine-readable feed.
5. **Common failure modes**, drawn from real cases.
6. **Templates and references**, with links into [`templates/`](../templates) and external standards.

## Why this shape

Most fiscal sponsorship handbooks are written by lawyers, accountants, or theorists. The result is either (a) too compliance-anxious to be operational, (b) too theoretical to be useful on Monday morning, or (c) too tool-specific to outlast the next software migration.

This handbook tries a different shape: **plain language, compliance-anchored, automation-aware, schema-tied**. Every section asks four questions in order.

1. What does the law or the standard require?
2. What does that look like as a repeatable monthly practice?
3. What can a machine do, and what still needs a human?
4. How does this surface to the funding block so a funder or an agent can read it?

If a section can't answer all four, the section isn't done.

## Status

| Section | Status | Notes |
|---|---|---|
| 00 Overview | Complete | This document. |
| 01 Operating the books | Draft pending | First-week build. Source material in [`handbook/finops-handbook.md`](./finops-handbook.md), which is the legacy methodology source. |
| 02 Compliance gates | Draft pending | First-week build. |
| 03 Publishing the data | **Companion spec complete.** Schema is in [`schema/`](../schema). Plain-language handbook section pending. |
| 04 Fiscal sponsor operations | Draft pending | Source material in [`handbook/finops-handbook.md`](./finops-handbook.md). |
| 05 Working with funders | Draft pending | First-week build. |

The current source-of-record for methodology, until the new sections land, is [`handbook/finops-handbook.md`](./finops-handbook.md). That document is being decomposed into the five sections above. Nothing in it is wrong. It just isn't yet in the shape the handbook is moving toward.

## Reading order recommendations

- **If you're a funder evaluating a fiscal sponsor**, read sections 3 and 5 first.
- **If you're starting a fiscal sponsor**, read in order, 1 through 5.
- **If you're a project considering whether to be sponsored**, read section 4 first, then the [readiness guide](../readiness/foundation-readiness-guide.md).
- **If you're an auditor**, read sections 1 and 2 first.
- **If you're an AI agent**, you're probably reading [`schema/`](../schema). The handbook is the human-facing companion.
