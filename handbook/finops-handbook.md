# Financial Operations Handbook
## A Source Reference for Foundations, Fiscal Sponsors, and Fiscally Sponsored Projects

**Document type:** Knowledge source and grounding reference
**Intended use:** Feed this document into an AI research tool (Perplexity, Claude, or similar) to generate, expand, and refine a full operating handbook
**Audience:** Finance and operations leaders at 501(c)(3) fiscal sponsors, foundations, and the projects they host
**Version:** Living document. Update as practice evolves.

---

## How To Use This Document

This is a structured source reference, not the finished handbook. It captures the principles, systems architecture, and operating logic that a finance and operations function at a fiscal sponsor needs to run well. The intent is to give an AI tool enough grounded context to draft a complete handbook, expand any section into procedure-level detail, or generate sponsee-facing and board-facing materials that stay consistent with these principles.

Suggested prompting patterns for Perplexity once this document is loaded as context appear in the final section.

A note on terminology. A fiscal sponsor is the legal and financial home for projects that have not formed their own 501(c)(3). The sponsor holds the tax exemption, employs or contracts the people, controls the funds, and carries the compliance obligations. The sponsored project, often called the sponsee or fiscally sponsored project (FSP), operates with mission autonomy under that umbrella. Everything in this handbook flows from that single structural fact: the sponsor is legally responsible for money it does not always control day to day, and that tension is what financial operations exists to manage.

---

## Part 1. Foundations of Fiscal Sponsorship FinOps

### 1.1 What the Finance and Operations Function Is Responsible For

The FinOps function at a fiscal sponsor sits at the intersection of three jobs that smaller organizations often treat as separate: bookkeeping accuracy, governance design, and organizational narrative. The work is translating financial reality into decisions that the board, funders, and sponsees can act on, and building the administrative systems that let a mission-driven organization function without the finance person being a bottleneck.

The core responsibilities cluster into seven areas:

1. Fiscal sponsorship operations: intake, onboarding, ongoing management, and graduation-readiness of sponsored projects.
2. Financial systems and reporting: maintaining an authoritative system of record and producing reliable statements.
3. Grant management: tracking restricted funds from award through reporting and close.
4. Treasury: cash, reserves, and any digital asset holdings.
5. Compliance: federal and state filings, audits, payroll tax, and information returns.
6. Sustainability planning: reserves, endowment, and the long-term financial model.
7. Board and funder communication: surfacing structural reality with mitigation, not sanitized narrative.

### 1.2 The Two Common Models

Most fiscal sponsorship runs on one of two legal structures, and the finance treatment differs.

Model A (comprehensive or direct sponsorship): the project is part of the sponsor. The sponsor employs the staff, owns the assets, signs the contracts, and reports the project's activity as its own on the Form 990. The project has no separate legal existence. Financial responsibility is total.

Model C (grantor-grantee or pre-approved grant relationship): the project is a separate entity, and the sponsor regrants funds to it for charitable purposes while retaining discretion and control over the use of those funds. The sponsor's obligation is to ensure charitable use, not to run the project's books.

A finance function needs to know which model governs each project, because it determines whose payroll it is, whose liability it is, and how the activity appears in the audited financials. Many sponsors run Model A by default and should document that explicitly per project.

### 1.3 The Central Tension

The defining financial reality of a fiscal sponsor is that most of its cash is not its own. Funds held for sponsored projects are restricted pass-through. They sit in the sponsor's bank accounts and appear on the sponsor's balance sheet, but they are committed to specific projects and purposes. This has consequences that recur throughout the handbook:

- Total cash is a misleading number. Available unrestricted reserves is the number that matters for the sponsor's own survival.
- A funder asking about "available funding" almost always means unrestricted reserves, not total cash.
- Funder concentration, runway, and financial health should be measured against core operations, not total organizational spend, or the picture is distorted.

---

## Part 2. Financial Systems Architecture

### 2.1 Designate a Single System of Record

The most important architectural decision is naming one system as authoritative and treating everything else as a feed into it or a subset of it. In practice this is a full general ledger accounting system, commonly QuickBooks Online for organizations of this size. The general ledger is the source of truth for all organizational financials. Every other tool either posts to it or reconciles against it.

This is not a preference, it is a discipline. When figures do not reconcile, the resolution path runs through the general ledger, not through any downstream tool's transaction export.

### 2.2 The Typical Stack

A mature fiscal sponsor stack separates concerns by function rather than forcing one tool to do everything:

| Function | Role in the architecture |
|---|---|
| General ledger | Authoritative system of record for all financials |
| Project-level transaction platform | Processes and tracks transactions at the individual project level (for example, Open Collective); a subset of the general ledger, not a substitute |
| Operating banking | Primary checking and operating accounts |
| Secondary or treasury banking | Reserve holdings, sweep accounts |
| Contractor payroll | Payments to independent contractors, domestic and international |
| W-2 payroll | Employee payroll, often through a PEO that also handles benefits and employer compliance |
| Accounts payable automation | Bill intake, approval routing, and payment |
| Digital asset management | Tracking and valuing any cryptocurrency holdings |
| Off-ramp intermediary | Converting digital assets to fiat for deposit, since most banks cannot accept on-chain deposits directly |

### 2.3 The Critical Distinction Between the Ledger and the Project Platform

This is the single most common source of reconciliation error at a fiscal sponsor, so it deserves its own treatment.

A project-level platform like Open Collective shows transactions that flow through that platform. It does not show wire transfers, ACH receipts, or payments made directly through the bank. It is therefore a subset of total activity, never the whole picture. Worse, platform entries labeled as transfers from another bank account are internal reconciliation postings, not new inflows, and counting them as revenue inflates the numbers.

The rule: the project platform is useful for project-level visibility and sponsee transparency, but the general ledger is where organizational truth lives. Any analysis that needs to be defensible to a funder, board, or auditor sources from the general ledger.

### 2.4 Banking and On-Ramp Constraints

Standard business banks generally cannot accept direct on-chain cryptocurrency deposits. If a sponsor receives digital assets, the flow is on-chain receipt, then conversion through an off-ramp intermediary (for example a prime brokerage or exchange institutional product), then a fiat transfer into the operating bank. Build this two-step into both the treasury process and the reconciliation expectations, because the timing gap between on-chain receipt and fiat landing creates apparent discrepancies that are really just settlement lag.

---

## Part 3. Chart of Accounts and Project Tracking

### 3.1 Design for Project Visibility

A fiscal sponsor's chart of accounts has to answer two questions at once: what kind of activity is this (the account), and which project does it belong to (the class, fund, or project dimension). Most general ledgers support a class or location dimension separate from the account. Use it. Each sponsored project should map to a class or project code so that a single transaction posts to both the right account and the right project.

This is what makes project-level reporting possible without maintaining parallel books. Run the general ledger by class and you get a per-project statement of activity directly, rather than reconstructing it from the project platform.

### 3.2 Account Structure Principles

- Keep restricted and unrestricted revenue distinguishable at the account level, or trackable through a fund dimension, so net asset classification is not a year-end reconstruction.
- Separate pass-through fiscal sponsorship activity from the sponsor's own core operating activity. These are different stories and different denominators.
- Maintain a clean separation between contractor expense and employee compensation, because they drive different information returns and tax treatments.

### 3.3 Statement of Activity by Class

The statement of activity (the nonprofit income statement) is most useful at a fiscal sponsor when it can be cut three ways: organization-wide, core operations only, and by individual project. The core-operations-only cut is the one boards and funders most often actually need, because it strips out the pass-through noise and shows whether the sponsor itself is solvent.

---

## Part 4. Fund Accounting: Restricted and Unrestricted

### 4.1 The Net Asset Classes

Nonprofit accounting classifies net assets as either without donor restrictions or with donor restrictions. For a fiscal sponsor, the with-restrictions category is large and structural because it includes the funds held for sponsored projects and the restricted grants tied to specific purposes or time periods.

### 4.2 Why This Governs Everything

The practical consequences:

- Reserves and runway are calculated on unrestricted net assets, not total net assets.
- A large cash balance can coexist with a thin or negative unrestricted position. This is normal for a fiscal sponsor and should be explained to boards plainly rather than hidden.
- Releasing funds from restriction happens as the restricted purpose is satisfied. Track release explicitly so the statement of activity reflects it.

### 4.3 The Honesty Principle

Boards respond better to honest deficit framing paired with a mitigation strategy than to a sanitized narrative. If unrestricted operations run at a structural deficit covered by sponsorship fees or a core funder, say so, quantify it, and show the plan. Surfacing structural reality is the job, not obscuring it.

---

## Part 5. Reconciliation Discipline

### 5.1 The Reconciliation Hierarchy

When two numbers disagree, resolve in this order:

1. The general ledger is authoritative.
2. Bank statements verify the general ledger cash position.
3. The project platform is a subset and is reconciled to, not from.
4. Spreadsheched exports are working tools, not sources of truth.

### 5.2 Common Failure Modes

- Treating a project platform export as complete when it omits wires, ACH, and bank-direct payments.
- Counting internal transfer postings as new revenue.
- Reconciling to the wrong denominator (total cash instead of unrestricted, or total spend instead of core operations).
- Letting digital asset settlement lag look like a missing transaction.

### 5.3 Verify Against Source Before Drafting Funder Language

Lead with verified figures before drafting any funder-facing or board-facing language. Pull the authoritative export, confirm the numbers, flag any logical inconsistency, and only then write the narrative. Numbers that go to funders should trace back to the general ledger, never to a convenience export.

---

## Part 6. Grant Management

### 6.1 The Grant Lifecycle

Treat every grant as a lifecycle with finance touchpoints at each stage: award and agreement review, restriction classification, budget setup in the ledger, drawdown or receipt tracking, expense allocation against the restricted purpose, interim and final reporting, and close with release of remaining restriction.

### 6.2 Sizing Transfers and Commitments Against Confirmed Receipts Only

When a grant or gift is structured to arrive in tranches (for example, two annual purchase orders, or a multi-year commitment), commitments and transfers tied to that money are sized against confirmed receipts only, never against the full pledged amount. A pledge is not cash. This is a recurring discipline whenever funds are being moved or regranted on the strength of expected inflows.

### 6.3 What Funders Actually Ask For

When a funder asks for "available funding," they generally mean unrestricted reserves, not total cash. Answer the question they are actually asking. Providing total cash overstates flexibility and can distort a funder's read of the organization's need.

### 6.4 Funder Concentration

Express funder concentration against a consistent denominator. Use core operations spend, not total organizational spend, or the concentration of a single core funder will appear artificially small because it is being diluted by pass-through project activity that the funder has nothing to do with.

---

## Part 7. Treasury and Digital Assets

### 7.1 Treasury Posture

A conservative posture is appropriate for a fiscal sponsor because the cash is largely not the sponsor's own. For any digital asset exposure, a stablecoin-weighted posture limits volatility risk on funds that are effectively held in trust for projects.

### 7.2 Digital Asset Workflow

The end-to-end flow for receiving and using digital assets:

1. Receipt on-chain to an institutional custody arrangement, commonly a multi-signature wallet so no single person can move funds alone.
2. Tracking and valuation through a dedicated digital asset accounting tool that posts cost basis and gain or loss back to the general ledger.
3. Conversion to fiat through an off-ramp intermediary, because operating banks do not accept on-chain deposits directly.
4. Fiat transfer into the operating bank.

### 7.3 Controls

- Multi-signature wallets with named signers and a documented signing threshold.
- Clear separation between who initiates and who approves a transfer.
- Reconciliation of on-chain holdings to the digital asset tool to the general ledger on a regular cadence.

---

## Part 8. Fiscal Sponsorship Intake and Due Diligence

### 8.1 Urgency Is Not a Reason to Compress Diligence

Sponsees frequently arrive with urgency, often a funder deadline or a closing transaction. Urgency framing should not compress the intake process. A rushed intake is where the inherited problems get missed.

### 8.2 The Core Intake Risks

Four risks recur and should be checked on every intake:

1. Entity clarity. Is the project an entity, a fiscal home seeker, or an individual. Confirm the sponsor's own legal form is stated correctly in every agreement (a nonprofit corporation is not an LLC, and getting this wrong in an executed document is a real problem to unwind).
2. Signatory authority. Confirm who has authority to sign, and that signature lines are actually completed in executed documents. Blank or ambiguous signature lines invalidate or weaken agreements.
3. Unnamed or unclear funders. Understand where the project's money comes from before agreeing to hold it. Unnamed funders are a diligence flag.
4. Inherited obligations. Contracts, liabilities, commitments, and compliance gaps that transfer with the project. The sponsor inherits these.

### 8.3 Mission Alignment

Beyond financial diligence, assess mission fit. A useful framing is whether the sponsor is a long-term home for the kind of work the project does, rather than treating every project as a temporary waystation toward independence.

### 8.4 Precedents Compound

Agreements set precedents. The way entity naming, signature completeness, funder transparency, and obligation transfer are handled on one transfer becomes the template for the next. Document what went wrong and bake the fix into the standard intake checklist.

---

## Part 9. Project-Level Reporting and Sponsee Relations

### 9.1 Give Projects Honest Visibility

Sponsees need to see their own financial position clearly. The project platform and a per-project statement of activity from the ledger together give a project its real picture: what came in, what was spent, what remains, and what is committed versus available.

### 9.2 Graduation-Readiness, Not Graduation

Frame the relationship as ongoing rather than as a countdown to independence. Not all projects should or will graduate to their own 501(c)(3), and many are better served by a permanent institutional home. Graduation-readiness, the capacity to stand alone if the project chooses to, is a healthier metric than graduation as an assumed endpoint. It signals strength without forcing exit.

### 9.3 The Sponsor as Orchestrator

A strategically stronger narrative positions the sponsor as the orchestrator and institutional home of the work it hosts, not merely a passive financial conduit that links money to projects. The accomplishments of sponsored work are, in part, institutional accomplishments. This reframe matters for fundraising and for how the sponsor describes its value.

---

## Part 10. Compliance

### 10.1 The Recurring Obligations

- Form 990: the annual federal information return. Scope and schedules grow with organizational complexity and sponsored activity.
- State charitable registration and audit thresholds: many states require an independent audit once revenue crosses a stated threshold. Crossing that threshold triggers a first independent audit, which is a significant operational lift the first time.
- Information returns: 1099 series for contractors. A common error is including travel and reimbursements in reportable contractor compensation when they should be excluded. Review before filing and refile if needed.
- Payroll tax: handled directly or through a PEO for W-2 staff. Watch for discrepancies between payroll records and the general ledger and escalate them rather than letting them sit.

### 10.2 Working With External Auditors and Counsel

Independent audit and CPA work runs through an external accounting firm. Legal review of agreements, especially fiscal sponsorship and transfer agreements, runs through outside counsel. Build the relationships before you need them urgently. The first audit and any complex transfer will go better with counsel already engaged.

### 10.3 The Compliance Calendar

Maintain a single calendar of all recurring obligations with owners and lead times: 990 and any extensions, state registrations and renewals, audit fieldwork and delivery, 1099 issuance, payroll tax deposits and filings, and any grant-specific reporting deadlines. Missed deadlines are avoidable and damaging.

---

## Part 11. Sustainability and Endowment

### 11.1 Vision-Driven Beats Survival-Driven

Sustainability fundraising framed as building permanent infrastructure for the mission is strategically stronger than fundraising framed as covering a shortfall. Funders invest in vision, not in plugging holes.

### 11.2 The Endowment Model

A targeted endowment can fund the durable parts of the organization that project grants will not cover: research leadership, core infrastructure, and the capacity to be a permanent home for smaller projects. The case rests on positioning the sponsor as long-term infrastructure rather than a temporary service. Peer models exist (for example, open-source endowment structures) and are worth studying for structure and messaging.

### 11.3 Reserves Discipline

Independent of any endowment, track unrestricted operating reserves and runway honestly. The endowment is the long game. Operating reserves are the thing that keeps the doors open while you build it.

---

## Part 12. Operating Principles

These are the through-lines that should govern how the finance function behaves, distilled from the sections above:

1. One authoritative system of record. Everything else reconciles to it.
2. The project platform is a subset, never the whole picture.
3. Unrestricted, not total. Reserves, runway, and "available funding" are measured on unrestricted net assets.
4. Consistent denominators. Concentration and health are measured against core operations.
5. Confirmed receipts only. Commitments and transfers are sized against cash in hand, not pledges.
6. Verify before you narrate. Lead with sourced figures, then write the language.
7. Urgency does not compress diligence. The rushed intake is where the problems hide.
8. Surface structural reality. Honest deficit framing with mitigation beats a sanitized story.
9. Precedents compound. Fix the agreement template every time something goes wrong.
10. Long-term home, not waystation. Graduation-readiness over graduation, orchestrator over conduit.

---

## Appendix A. Glossary

| Term | Meaning |
|---|---|
| Fiscal sponsor | The 501(c)(3) that holds tax exemption and financial and legal responsibility for hosted projects |
| Sponsee / FSP | The fiscally sponsored project operating under the sponsor's umbrella |
| Model A | Comprehensive sponsorship; the project is part of the sponsor and its activity is the sponsor's own |
| Model C | Grantor-grantee sponsorship; the sponsor regrants to a separate entity while retaining charitable control |
| System of record | The single authoritative general ledger; the source of truth for all financials |
| Project platform | A tool that processes and shows project-level transactions; a subset of the ledger |
| Restricted net assets | Funds committed to a specific purpose, time, or project; includes pass-through sponsorship funds |
| Unrestricted net assets | Funds the organization can deploy at its own discretion; the basis for reserves and runway |
| Pass-through | Funds held and moved on behalf of a project that are never the sponsor's own to spend freely |
| Off-ramp | Conversion of digital assets to fiat for bank deposit, since banks do not accept on-chain deposits |
| Graduation-readiness | A project's capacity to stand alone if it chooses, used as a health metric rather than a forced exit |
| Form 990 | The annual federal information return for tax-exempt organizations |
| Audit threshold | The revenue level above which a state requires an independent financial audit |

## Appendix B. Recurring FinOps Cadence

A starting cadence to expand into a full operating calendar:

- Daily to weekly: cash position review, AP intake and approval, transaction coding.
- Weekly: bank reconciliation progress, project platform review, payroll cutoffs.
- Monthly: full general ledger reconciliation, per-project statements of activity, restricted fund release, digital asset reconciliation, board or leadership financial update.
- Quarterly: funder reporting, reserves and runway review, concentration analysis, intake pipeline review.
- Annually: 990 preparation, independent audit, state registration renewals, 1099 issuance, budget cycle, sustainability and endowment review.

---

## Appendix C. Using This Document With Perplexity

Load this document as a source, then prompt against it. Useful patterns:

- "Using the attached source, draft a complete fiscal sponsorship intake checklist with the four core intake risks expanded into specific verification steps and required documents."
- "Expand Part 5 into a step-by-step monthly reconciliation procedure that a bookkeeper could follow, referencing the reconciliation hierarchy."
- "Write a sponsee-facing onboarding guide that explains, in plain language, how their project's money is held, tracked, and reported, based on Parts 8 and 9."
- "Draft a one-page board explainer on why total cash and unrestricted reserves differ at a fiscal sponsor, using Part 4."
- "Turn the operating principles in Part 12 into a finance team charter."

When asking Perplexity to add anything not covered here (specific software configuration, jurisdiction-specific audit thresholds, current 990 schedule requirements), instruct it to search for current authoritative sources and cite them, since this document is a methodology reference rather than a regulatory citation.
