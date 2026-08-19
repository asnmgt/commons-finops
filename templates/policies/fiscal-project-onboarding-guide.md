> **Template document — Commons FinOps.**
>
> This is an org-agnostic policy template from the [Commons FinOps](https://github.com/asnmgt/commons-finops) repository. Placeholder tokens like `{{ORG_NAME}}`, `{{THRESHOLD_DFO_REVIEW}}`, and `{{PLATFORM_FISCAL_HOST}}` are resolved from your local `context.yaml`.
>
> **To use this template:**
> 1. Run `python ai/init.py` from the repo root, or copy [`ai/context.example.yaml`](../../ai/context.example.yaml) to `context.yaml` and fill it in.
> 2. Render this document with your values: `python ai/render.py templates/policies/<file>.md`.
> 3. Or connect the [MCP server](../../ai/mcp-server) to your AI assistant, which will serve this document (rendered with your context) as an addressable resource.
>
> **This template does not create legal, tax, or accounting obligations by itself.** Adopt it via your board and adapt it to your circumstances, jurisdiction, entity structure, and regulator.

---

**Fiscal Project Onboarding Guide**

**Purpose:** Walk a prospective project from first conversation to a live fiscally sponsored home at {{ORG_NAME}}. Set clear mutual expectations before money moves.

**Applies to:** Prospective and newly onboarded fiscally sponsored projects at {{ORG_NAME}}, and the {{ORG_NAME}} staff who steward them.

**Version:** 1.0 | **Effective date:** {{POLICY_EFFECTIVE_DATE}}. Supersedes prior ad hoc onboarding practice.

**How to use this document:** Read Part 1 before any first conversation with {{ORG_NAME}}; it tells you whether we are a plausible fit. Part 2 is the shared expectations you commit to by signing. Part 3 is our internal 30-day sequence, published for transparency so you can see what is happening behind the scenes. Part 4 is what happens after you are live. Part 5 covers what happens when you outgrow us. When this document and your Fiscal Sponsorship Agreement conflict, the Agreement wins.

---

**Part 1: Fit assessment**

Many projects approach {{ORG_NAME}} for fiscal sponsorship. Fit is the first question, not the last — a project that is not a fit for us is not badly served by hearing so early.

**What we need from you**

To have a productive fit conversation, we ask you to exchange the following:

- Review our Fiscal Sponsorship Agreement (FSA) template. If you disagree with a clause, flag it now.
- Provide the CVs of your project leads.
- Provide your project description, highlighting any commercial activity happening elsewhere under related branding, IP, or leadership.

**What signing the Agreement means for you**

By signing the FSA, you are clear that:

- The title of "Project Lead at {{ORG_NAME}}" does not authorize the titleholder to act on behalf of {{ORG_NAME}} as a legal entity. You cannot sign contracts in our name, apply for grants in our name without the Executive Director's involvement, or represent that your project speaks for the organization.
- No campaigning for or against anyone running for public office. This is a hard 501(c)(3) rule, not our preference.
- No activities that are illegal under United States federal law, regardless of state-level status. This includes cannabis-related activity in states where it is state-legal.

**What {{ORG_NAME}} does not do**

Being explicit about our operational envelope up front prevents disappointment later:

1. **Payroll.** Project leads and project contributors are not {{ORG_NAME}} employees unless explicitly hired by {{ORG_NAME}}. Everyone else is a contractor or a grantee.
2. **Own or commercialize project intellectual property.** The project lead retains IP rights per the FSA. We hold the fiscal shell, not the code, the data, or the trademark.
3. **501(c)(4) advocacy or political endorsement work.** If your project needs to endorse candidates or engage in unlimited lobbying, we are the wrong host.
4. **Hold funds for projects that have not had a fit conversation.** Do not direct donors to send us money for your project until the FSA is signed. We will refund or return unsolicited inbound funds that arrive prior to sponsorship being finalized.

---

**Part 2: Once you are a fiscally sponsored project**

The moment your FSA is countersigned, these expectations kick in.

**Public affiliation and branding**

- All use of {{ORG_NAME}}'s name, branding, or affiliation must be pre-approved in writing by the Executive Director and must accurately represent the nature of the fiscal sponsorship relationship. See the "Public Affiliation" section in your FSA.
- When describing the relationship publicly, "fiscally sponsored by {{ORG_NAME}}" is the standard phrasing. "A program of {{ORG_NAME}}" is not accurate for Model C sponsorship and should not be used.

**Grants and funder coordination**

- As soon as you decide to apply for a grant, coordinate with the Executive Director. Two projects applying to the same funder simultaneously is a coordination failure we can prevent — but only if we know.
- Send the Executive Director the full text of grant applications at least one week in advance so they can review, sign as required, and flag conflicts with other in-flight applications.
- Send us the conferences you are applying to or planning to present at so we can coordinate cross-project representation.

**Financial operations**

Your project will operate under the following defaults:

| Item | Default |
|---|---|
| Overhead / host fee | {{HOST_FEE_RATE}} of grant amount or gross funds raised, including donations made through {{PLATFORM_FISCAL_HOST}}, taken off the top. Waivers are rare; written justification and Executive Director approval required. |
| Fiscal-host platform | {{PLATFORM_FISCAL_HOST}}. One page per project. Sub-projects are allowed. |
| Spending workflow | Project lead submits via {{PLATFORM_FISCAL_HOST}}. In year one, your assigned {{ORG_NAME}} staff member approves. Thereafter, the project lead becomes an approver in their own right. |
| Payment cadence | Weekly on {{PAYMENT_CADENCE_DAY}}. ACH lands in 2–3 business days. |
| Speed expectation | Net {{WINDOW_REIMBURSEMENT}} for reimbursements and invoices. |

Full operating detail lives in the [Financial Guidelines for Sponsored Projects](./financial-guidelines-for-sponsored-projects.md) and the [Expense Classification Guidelines](./expense-classification-guidelines.md). This guide is the on-ramp; those two are the manual.

---

**Part 3: The first 30 days (internal sequence)**

We publish this so you know what is happening on our side. If someone approaches {{ORG_NAME}} whom we do not yet know, we follow all steps below. If someone we already know approaches us, steps may begin with the budget and end with the FSA.

| Days | Milestone | Owner |
|---|---|---|
| 1–3 | Fit conversation with the Executive Director. FinOps conversation with the Director of Finance and Operations. Project Lead and internal Relationship Director assignment. | Executive Director + Director of Finance and Operations |
| 4–7 | Fiscal Sponsorship Agreement sent for signature via e-signature platform. | Director of Finance and Operations |
| 8–10 | FSA signed. W-9 and conflict-of-interest disclosure collected from Project Lead. | Director of Finance and Operations |
| 11–15 | {{PLATFORM_FISCAL_HOST}} page live. Project Lead added as an admin. | Director of Finance and Operations |
| 16–20 | Initial budget posted. Bank rules and virtual cards configured as needed. | Director of Finance and Operations |
| 21–30 | Test transaction executed. First weekly payment cycle runs. | Director of Finance and Operations + Executive Director |

**Documents collected during the first 30 days**

- Signed Fiscal Sponsorship Agreement
- W-9 for the Project Lead
- Conflict-of-interest disclosure from the Project Lead
- Initial project budget (may be revised at any time; the point is to have a baseline)
- Project description and public-facing one-liner
- CVs / bios of key project leads on file

---

**Part 4: Your working relationship with {{ORG_NAME}}**

**Who to ask about what**

| Question | Contact |
|---|---|
| Fit decisions, sponsorship approvals, fundraising strategy, funder coordination, board relations, "how does this project define success" | Executive Director |
| Finance (EIN, audits, IRS letters, 990, organizational financial narratives), operations, {{PLATFORM_FISCAL_HOST}}, legal, contracts, tax compliance, banking | Director of Finance and Operations |
| Appropriate interaction with {{ORG_NAME}} community infrastructure | Community Lead |
| Legal inquiries and review | Work through the Executive Director and Director of Finance and Operations. |
| Default rule | If unsure who handles it, email the Director of Finance and Operations. Reply target is one business day. |

**Communications channels**

1. **Day-to-day finance and operations:** email the Director of Finance and Operations.
2. **Strategic, funding, or programmatic questions:** email the Executive Director.
3. **Community channels ({{PLATFORM_COMMUNITY}} or equivalent):** cross-project conversations happen in project-specific channels where they exist. Never post project-specific financial detail in shared channels.
4. **Semi-annual:** budget review with the Director of Finance and Operations.
5. **Annual:** one paragraph from the project for {{ORG_NAME}}'s annual report — successes, achievements, constituents reached, and any impact metrics you track.

**Meeting cadence**

- One-on-one with the Executive Director on a cadence appropriate to your project's size and stage.
- Ad-hoc with the Director of Finance and Operations for anything operational or financial.
- Any shared meetings across sponsored projects will be scheduled explicitly and communicated in advance.

---

**Part 5: Graduation, wind-down, or transition**

Fiscal sponsorship is a stage, not a permanent home. Most projects eventually either graduate to their own 501(c)(3), transition to another fiscal home that fits better, or wind down.

**How graduation works**

When a project outgrows fiscal sponsorship at {{ORG_NAME}}:

1. Draft a **transfer agreement** outlining which assets stay with {{ORG_NAME}} and which move with the project.
2. Conduct **legal reviews** on both sides.
3. The Executive Director signs.
4. **Unspent balance moves with the project**, net of any outstanding obligations {{ORG_NAME}} has incurred on the project's behalf and net of the standard host fee on any funds still to be transferred out.
5. A **final accounting memo** closes the file on {{ORG_NAME}}'s books.

**Detecting when a project is ready to graduate**

We are attuned to indicators that a specific project may be exceeding our operational envelope. These are heuristics, not rules:

- **Legal exposure growing.** Legal fees hitting {{ORG_NAME}} because your open-source or research project has become "load-bearing" for societal-scale uses, and is making bigger enemies as it does so.
- **User base diversifying and identifying commercial value.** Grant funding may be waning as user-derived revenue becomes viable; the project may be ready for its own corporate shell.
- **Staff scale exceeds what a fiscal-sponsor relationship comfortably holds.** More than a handful of dedicated staff typically warrants direct employment, not sponsored-project contractor status.
- **Board formation is a live conversation on your side.** If your funders or your leads are asking about a governance board specific to your project, graduation is likely the next 6–18 months' work.

When we see these signals, we open the conversation early. Graduating well is a mark of a healthy sponsorship, not a failure.

**Wind-down**

If a project decides not to continue and does not have a graduation target, we work with the Project Lead to:

- Notify any active funders per grant terms.
- Return unspent restricted funds to funders where required.
- Assign residual unrestricted funds per the FSA — either to {{ORG_NAME}} general operations, to a designated successor project, or as otherwise specified in the wind-down memo.
- Publish a final accounting to the {{PLATFORM_FISCAL_HOST}} page and archive it.

---

**Appendix A: Template variable reference**

This section maps the placeholder tokens used in this document to the fields you populate in `context.yaml`. See [`ai/context.example.yaml`](../../ai/context.example.yaml) for the full schema.

| Token | Meaning | Example values |
|---|---|---|
| `{{ORG_NAME}}` | Short name of the fiscal sponsor | `Example Sponsor`, `Acme Foundation` |
| `{{HOST_FEE_RATE}}` | Standard overhead / host-fee percentage | `10%`, `12%`, `15%` |
| `{{PLATFORM_FISCAL_HOST}}` | Fiscal-sponsorship platform | `Open Collective`, `HCB`, `custom ledger` |
| `{{PLATFORM_COMMUNITY}}` | Community messaging platform | `Slack`, `Discord`, `Matrix` |
| `{{PAYMENT_CADENCE_DAY}}` | Weekly payment run day | `Wednesdays`, `Fridays` |
| `{{WINDOW_REIMBURSEMENT}}` | Reimbursement / invoice payment window | `30 days`, `Net 30` |
| `{{POLICY_EFFECTIVE_DATE}}` | Effective date of this version of the guide | `2026-08-19` |

**Roles referenced in this guide**

This guide references three named roles. Adapt to your organization's actual titles:

- **Executive Director** — highest-level program authority; fit and strategic decisions.
- **Director of Finance and Operations** — signatory for financial and operational matters; the default first contact for sponsored projects.
- **Community Lead** — steward of shared community infrastructure across projects.

If your organization uses different titles (Managing Director, Head of Operations, Program Director, etc.), do a find-and-replace when you fork this document.
