> **Template document — Commons FinOps.**
>
> This is an org-agnostic policy template from the [Commons FinOps](https://github.com/asnmgt/commons-finops) repository. Placeholder tokens like `{{ORG_NAME}}`, `{{THRESHOLD_DFO_REVIEW}}`, and `{{PLATFORM_FISCAL_HOST}}` are resolved from your local `context.yaml`.
>
> **To use this template:**
> 1. Run `finops-init` from the repo root, or copy [`ai/context.example.yaml`](../../ai/context.example.yaml) to `context.yaml` and fill it in.
> 2. Render this document with your values: `python ai/render.py templates/policies/<file>.md`.
> 3. Or connect the [MCP server](../../ai/mcp-server) to your AI assistant, which will serve this document (rendered with your context) as an addressable resource.
>
> **This template does not create legal, tax, or accounting obligations by itself.** Adopt it via your board and adapt it to your circumstances, jurisdiction, entity structure, and regulator.

---

**Project Expense Classification Guidelines**

**Purpose:** Help project leads and their bookkeepers decide, at the
moment of spending, whether an expense belongs to your project's ledger,
to {{ORG_NAME}}'s core operations, or nowhere in {{ORG_NAME}}'s books at all.
Consistent classification keeps your {{PLATFORM_FISCAL_HOST}} ledger honest,
keeps {{ORG_NAME}}'s 990 clean, and prevents the end-of-year
reclassifications that eat a full week of bookkeeping.

**Applies to:** All {{ORG_NAME}}-sponsored projects (fiscally sponsored
collectives on OC) and {{ORG_NAME}} core operations.

**Version:** 1.0 | **Effective date:** 2026-08-19. Supersedes prior ad
hoc guidance.

**How to use this document:** Part 1 gives the five principles: the
mental model. Part 2 gives the hard rules: the exact thresholds,
deadlines, and required fields you must comply with. When principle and
hard rule appear to conflict, the hard rule wins. When this document and
the {{ORG_NAME}} Fiscal Policies and Procedures Manual appear to conflict,
the Manual wins; when the Manual and your Fiscal Sponsorship Agreement
conflict, your Agreement wins for your project. Bring questions to
the DFO.

**Part 1: Principles**

These are the five ideas that make the hard rules make sense. Read them
once at the start of a fiscal year and you will get 80% of the
classification calls right without opening the rest of the doc.

**Principle 1: There is only one set of books**

Your {{PLATFORM_FISCAL_HOST}} ledger is a view into {{ORG_NAME}}'s general ledger, not a second set
of books. So the first question is never "is this a {{ORG_NAME}} expense or
a project expense?" A project expense paid from your collective **is**
a {{ORG_NAME}} expense. The first question is whether {{ORG_NAME}} is paying for
it at all. If the money did not come out of the balance {{ORG_NAME}} holds
for you, and is not going to, it does not belong in {{ORG_NAME}}'s books in
any form.

**Principle 2: Every dollar has a home**

Every dollar spent through {{ORG_NAME}} is either **project-restricted**
(benefits your specific project) or **unrestricted core** (benefits
{{ORG_NAME}} as a whole). There is no third bucket. "Miscellaneous" is not
a home. When you cannot tell which, default to charging your project and
flag it; never park it as uncategorized.

**Principle 3: Benefit is what determines the ledger**

The question is never "who paid?" or "whose credit card?" It is
"whose work benefits?" A {{ORG_NAME}} staff member's card can carry a
project expense. A project lead's reimbursement can be a core cost.
Follow the benefit, not the payment method.

**Principle 4: Classify at the point of entry, not at close**

Categorize every expense when you submit it, not at the end of the
month. Splits, allocations, and reviews get harder as time passes. The
bookkeeper's job is to verify, not to reconstruct.

**Principle 5: Document the basis for any judgment call**

Any expense that involves a split, an allocation, or a debatable
category needs one sentence in the memo explaining why. "3 of 5 seats
used by Project A" or "day 2 of conference was {{ORG_NAME}} fundraising"
is enough. An auditor should be able to reconstruct your logic from the
ledger alone.

**Part 2: Hard rules**

**2.1 First gate: does it run through {{ORG_NAME}} at all?**

Before you classify anything, establish that {{ORG_NAME}} is paying for it.
Three buckets, and only the first one reaches our books:

  -----------------------------------------------------------------------
  **Bucket**     **What it is**                 **Where it is recorded**
  -------------- ------------------------------ -------------------------
  **Paid by      Contractor invoices,           {{ORG_NAME}} general ledger,
  {{ORG_NAME}}**      reimbursements, subscriptions, coded to your project
                 travel, subawards, payroll:    class. Continue to 2.2.
                 anything drawn on your         
                 collective balance             

  **Paid by      Your own LLC or nonprofit,     That entity's books only.
  another        another fiscal sponsor, a      Do not submit it, and
  entity**       partner organization, a        keep it out of the budget
                 personal card you are not      columns you send us.
                 submitting                     

  **In-kind /    Pro-bono legal work, a donated Not a cash expense. Tell
  donated**      venue, volunteer time, donated {{ORG_NAME}} about it, since
                 software                       some of it is reportable
                                                on the 990, but do not
                                                submit it as an expense.
  -----------------------------------------------------------------------

Two rules follow from this gate and apply without exception:

-   **One project, one {{PLATFORM_FISCAL_HOST}} account.** Each sponsored project maps
    one-to-one to their assigned {{PLATFORM_FISCAL_HOST}} collective. Every transaction must
    carry the class.

-   **No deficit spending.** You may not spend more than your available
    balance. Pledged, awarded-but-unreceived, or anticipated revenue is
    not spendable.

-   **Restrictions travel with the money.** A grant restricted to a
    purpose or a period may only be spent that way. Tell {{ORG_NAME}} the
    restriction in writing when the grant arrives, with the agreement
    attached.

**2.2 The five-question decision tree**

Once you know {{ORG_NAME}} is paying, ask these in order. Stop at the first
"yes."

**1. Would this expense exist if my project did not exist?** If no →
**project-restricted**. Charge to your {{PLATFORM_FISCAL_HOST}} ledger.
>
*Examples: a contractor writing your project's code, travel to your
project's convening, a domain name for your project's website, a
research subscription your project team uses.*
>
**2. Is this a {{ORG_NAME}}-wide obligation that applies regardless of any
single project?** If yes → **unrestricted core**. Charge to {{ORG_NAME}},
Inc.
>
*Examples: the 990 filing, D&O insurance, board meeting costs, the
Executive Director's and DFO's time, the fiscal-sponsorship platform
itself.*
>
**3. Is this a benefit that {{ORG_NAME}} negotiates once and every project
uses?** If yes → **unrestricted core**, funded by fiscal sponsorship
fee revenue.
>
*Examples: {{PLATFORM_GL}}, Slack workspace, the bookkeeper's monthly
retainer, the general liability policy, the legal review of the master
fiscal-sponsorship agreement.*
>
**4. Does the expense have a clean, documented split between projects
(or between projects and core)?** If yes → **shared**, allocated at
the point of entry using the split rule in 2.4.
>
*Examples: a conference where staff speaks about the project and about
{{ORG_NAME}}'s fiscal-sponsorship model, a subscription used by two
projects, a grant proposal covering multiple projects.*
>
**5. Am I still unsure?** Charge to your project and put a one-line
note in the {{PLATFORM_FISCAL_HOST}} expense description: \[REVIEW: possible core\]. The
bookkeeper picks these up in the monthly close and either confirms or
reclassifies. Never leave the category blank. OC's (empty) category is
the biggest single source of month-end cleanup.

**2.3 Common categories and where they go**

Account names and numbers below are the {{ORG_NAME}} chart of accounts as it
appears in the {{PLATFORM_FISCAL_HOST}} category picker. Use the most specific account that
fits; use a parent account only when nothing below it applies.

**Charge to your project**

  ------------------------------------------------------------------------------
  **Expense**             **Ledger**   **Account**             **Why**
  ----------------------- ------------ ----------------------- -----------------
  Contractor invoice for  Project      Project Expenses:       Direct project
  a project deliverable                Contractors             benefit

  Project staff           Project      Personnel: Salaries &   Direct project
  compensation (via PEO)               Wages                   benefit

  Employer-of-record and  Project      Personnel: PEO Fees     Follows the
  PEO charges on that                                          salary
  staff                                                        

  Travel to a project     Project      Project Expenses:       Direct project
  convening                            Travel                  benefit

  Meals while traveling   Project      Project Expenses: Meals Direct project
  or working on the                                            benefit
  project                                                      

  Event or meeting costs  Project      Project Expenses:       Direct project
  for the project                      Event/Meeting Expense   benefit

  Software your project   Project      Administrative &        Direct project
  team uses (Figma,                    Operations: Application benefit
  Notion, GitHub org)                  Subscriptions           

  Domain names and        Project      Administrative &        Direct project
  hosting for the project              Operations: Application benefit
  site                                 Subscriptions           

  Research subscriptions  Project      Administrative &        Direct project
  used only by your team               Operations: Application benefit
                                       Subscriptions           

  Legal review of a       Project      Legal & Professional    Direct project
  project contract                     Services: Other         benefit
                                       Professional Fees       

  Bank and wire fees on   Project      Administrative &        Direct project
  project transactions                 Operations: Bank        benefit
                                       Charges & Fees          

  Crypto processing and   Project      Administrative &        Direct project
  gas fees on project                  Operations: {{PLATFORM_CRYPTO_SUB}} -   benefit
  payouts                              Crypto Fees             

  Subaward or regrant to  Project      Direct Support: Grant   Regrant, not a
  another organization                 Expense                 purchase;
                                                               agreement and EIN
                                                               required

  Fellowship or stipend   Project      Direct Support:         Direct support,
  program for individuals              Fellowships             not contractor
                                                               work

  Sponsoring another      Project      Direct Support:         Direct project
  organization's event                 Sponsorships            benefit

  Fundraising costs for   Project      Per the underlying      Functional
  the project                          account; tell us it is  classification,
  (grantwriter, donor                  fundraising             not a different
  event)                                                       account
  ------------------------------------------------------------------------------

**Always core, never charged to a project**

  -----------------------------------------------------------------------------
  **Expense**             **Ledger**   **Account**             **Why**
  ----------------------- ------------ ----------------------- ----------------
  {{PLATFORM_GL}} and general  Core         Administrative &        {{ORG_NAME}}-wide
  accounting software                  Operations: Application obligation
                                       Subscriptions           

  990 preparation and     Core         Legal & Professional    {{ORG_NAME}}-wide
  external audit                       Services: Accounting    obligation
                                       Fees                    

  D&O insurance, general  Core         Administrative &        {{ORG_NAME}}-wide
  liability                            Operations: Insurance   obligation

  ED and DFO time,        Core         Legal & Professional    {{ORG_NAME}}-wide
  bookkeeper retainer                  Services: Accounting    obligation
                                       Fees                    

  State registration and  Core         Legal & Professional    {{ORG_NAME}}-wide
  charity registration                 Services: Registration  obligation
  fees                                 Fee                     

  Board meeting costs,    Core         On the {{ORG_NAME}} ledger   Governance, not
  board dinners                                                program

  Fundraising for {{ORG_NAME}} Core         Administrative &        Not project
  itself                               Operations: Advertising fundraising
                                       & Marketing             

  Slack workspace,        Core         Administrative &        Every project
  org-wide Zoom                        Operations: Application uses it
                                       Subscriptions           

  Conference where you    Shared       Allocate by time or     Genuine dual
  present both project                 session count           benefit
  and {{ORG_NAME}} content                                          
  -----------------------------------------------------------------------------

If an expense is not on this table and you are unsure, apply the
decision tree and use the \[REVIEW\] tag.

**A note on functional classification.** {{ORG_NAME}}'s 990 reports every
dollar as Program, Management & General, or Fundraising. Project
spending is normally Program, and the account alone does not tell us
otherwise. If a cost is fundraising (a grantwriter, a donor
cultivation event, campaign design), say so in the memo.
Under-reporting fundraising expense is a visible and avoidable 990
error.

**2.4 Split rule for shared expenses**

When an expense genuinely benefits more than one project, or benefits
your project and {{ORG_NAME}} core, split it at the point of entry using a
documented, defensible allocation basis. Do not book the whole thing to
one side and true up later. That is where errors compound.

**Approved allocation bases** (pick the one that fits and write it in
the expense note):

-   **Time-based:** For a person's time or a person's travel, split by
    hours or by day-of-conference. Example: "2 days at conference: day
    1 project work (100% project), day 2 {{ORG_NAME}} fundraising (100%
    core)."

-   **Beneficiary count:** For a subscription used by N teams, split by
    seat count. Example: "5 Notion seats: 3 for Project A, 2 for
    Project B, a 60/40 split."

-   **Revenue-based:** For a shared grant proposal that mentions
    multiple projects, split by the grant's own budget line items.

-   **FTE ratio:** For anything that would otherwise take an hour to
    allocate cleanly, use the current FTE ratio published in the {{ORG_NAME}}
    cost allocation memo. This is the default when no better basis
    exists.

**Every split expense must include three fields**, in the {{PLATFORM_FISCAL_HOST}} description
or the {{PLATFORM_GL}} memo:

**1.** Total amount
>
**2.** The two (or more) sides of the split, in dollars
>
**3.** One-sentence justification of the basis
>
**Example:** Total $1,200. $800 to Project A (Application
Subscriptions), $400 to core (Application Subscriptions). Basis: 4 of
6 seats used by Project A team; 2 seats used by cross-project ops.

**2.5 Paying people**

Most project spending is payments to people, and most delayed payments
trace to one of the rules below.

-   **No payment before tax forms.** A completed Form W-9 (US) or Form
    W-8BEN / W-8BEN-E (non-US) must be on file before the first payment
    to any individual or entity. **W-9s are collected through OC** as
    part of payee setup, so have the payee complete it when you agree to
    engage them, not when the first invoice arrives.

-   **Contractor versus employee is {{ORG_NAME}}'s determination, not
    yours.** If someone works on your schedule, under your direction,
    with your tools, on an ongoing basis, flag it before you engage
    them. **Any request to hire a full-time W-2 staff member must go to
    the {{ORG_NAME}} FinOps Director** before an offer is discussed. Anyone
    functioning as an employee must be placed on {{ORG_NAME}} payroll.

-   **Invoice versus receipt.** In OC, an **Invoice** is someone billing
    for services and a **Receipt** is reimbursement of money already
    spent. Either way, attach the document: an invoice stating the work
    and the period covered, or an itemized receipt. A card statement
    line is not a receipt.

-   **1099 reporting.** {{ORG_NAME}} issues Form 1099-NEC to US contractors
    at or above the \{{THRESHOLD_1099_MIN}} threshold for calendar 2026. Payments made
    in digital assets count at USD fair market value on the payment
    date.

-   **Project leads cannot commit {{ORG_NAME}}.** Contracts, engagement
    letters, offers, and leases are signed by an authorized {{ORG_NAME}}
    signer only.

-   **Non-US payees** need a W-8, a treaty determination, and possibly
    withholding. Build extra time into the first payment.

**2.6 What comes off the top**

Four costs reduce what you can actually spend. Put all four in the
budget explicitly rather than discovering them in the ledger.

  ------------------------------------------------------------------------
  **Cost**             **Typical magnitude**   **How it appears**
  -------------------- ----------------------- ---------------------------
  Fiscal sponsorship   **10% of gross          A "Host Fee from
  (admin) fee          receipts**, per your    \<Project\> to {{ORG_NAME}}"
                       Fiscal Sponsorship      line deducted as each
                       Agreement               contribution settles, so
                                               your balance rises by the
                                               net

  Payment processing   Roughly 2.2--3.5% plus  Netted against the
                       a fixed fee on card     contribution by {{PLATFORM_CARD_PROCESSOR}} or
                       gifts; bank transfers   the processor
                       are usually free        

  FX and international Roughly 0.5--1.5% on    A separate fee line, or an
  transfers            non-USD payouts         FX spread inside the
                                               transfer

  Employer costs on    Roughly 18--25% on top  Employer taxes, benefits,
  payroll              of gross salary         and PEO fees, charged to
                                               the project alongside the
                                               salary
  ------------------------------------------------------------------------

**Worked example.** A \{{THRESHOLD_BOARD_EXCEPTION}} grant at a 10% fee, funding one
half-time staff member and contractor work:

  -----------------------------------------------------------------------
  **Line**                                       **Amount**
  ---------------------------------------------- ------------------------
  Grant received (gross)                         \{{THRESHOLD_BOARD_EXCEPTION}}

  Less fiscal sponsorship fee at {{HOST_FEE_RATE}}             (\{{THRESHOLD_DFO_REVIEW}})

  **Available to spend**                         **$90,000**

  Staff member at $45,000 salary, fully loaded  ($54,000)
  at \~20%                                       

  Contractors                                    (\{{THRESHOLD_COMPETITIVE_BIDS}})

  Travel, software, and processing costs         (\{{THRESHOLD_CAPITALIZATION}})

  **Remaining**                                  **$1,000**
  -----------------------------------------------------------------------

The line that catches people is the fourth. A budget built on a $45,000
salary rather than the $54,000 loaded cost is short by $9,000 before
anything goes wrong.

**2.7 Spending authority, approvals, and budget amendments**

Two different things are being approved, and it is worth keeping them
apart. **Budget amendments** are about moving money between lines.
**Spending authority** is about the size of the commitment itself, and
it applies whether or not the spend is already in your budget.

**Budget amendments.** Your project's budget on {{PLATFORM_FISCAL_HOST}} is the source of
truth for what you can spend without asking. You do not need permission
to move money within budgeted categories. You do need a budget amendment
for:

-   **Category moves over \{{THRESHOLD_LINE_ITEM_REVIEW}}** between line items (for example,
    moving \{{THRESHOLD_1099_MIN}} from Contractors to Event Expenses).

-   **Total budget increase** of any size; this requires new funds
    committed to your project.

-   **New category** not in your approved budget (for example, hiring a
    first employee when your budget only had contractors).

-   **Any transaction over 30% of your project's remaining balance**,
    regardless of category.

Budget amendments are a one-line Slack message to the DFO or a comment on
your project's budget doc. Approvals are same-day for anything within
existing funds.

**Approval authority.** Every project expense takes two approvals, and
only two:

  ------------------------------------------------------------------------
  **Step**           **Who**                **Applies to**
  ------------------ ---------------------- ------------------------------
  First approval     Project Lead           Any amount. There is no
                                            ceiling on a Project Lead's
                                            approval authority for their
                                            own project.

  Second approval    {{ORG_NAME}} Director of    Every project expense, at
                     Finance & Operations   every amount, before payment
                                            is released.

  Board approval     Not required           Board approval is not required
                                            for project expenses. The
                                            Board thresholds in the Fiscal
                                            Policies and Procedures Manual
                                            govern {{ORG_NAME}} core spending,
                                            not project ledgers.
  ------------------------------------------------------------------------

Two further rules sit alongside the approval chain and are not
approvals. A single vendor engagement over **\{{THRESHOLD_COMPETITIVE_BIDS}}** requires three
competitive bids before commitment, and equipment costing **\{{THRESHOLD_CAPITALIZATION}} or
more** is capitalized rather than expensed.

**In short:** you can approve a $40,000 contractor engagement for
your own project. It still needs three competitive bids on file and
the DFO as second approver before payment is released, and the spend
still has to sit inside your available balance.

**2.8 Crypto and digital-asset expenses**

Crypto payments and stablecoin disbursements follow the same
benefit-based classification as fiat, but they carry extra bookkeeping
obligations because every on-chain movement is reconciled through
{{PLATFORM_CRYPTO_SUB}} and revalued at fair market value.

**Same benefit rule, different plumbing.** A USDC payout to a project
contractor is a project expense (Project Expenses: Contractors)
regardless of which wallet paid it. A USDC transfer to top up {{ORG_NAME}}'s
operating stablecoin float is a core cost. A gas fee is charged to
whichever ledger owns the underlying transaction. Do not bury gas fees
in a generic "crypto fees" bucket unless the transaction itself was
pure treasury movement.

**Hard rules for crypto expenses:**

-   **Every wallet must be in the {{ORG_NAME}} wallet register** maintained
    in {{PLATFORM_CRYPTO_SUB}}. Projects may not open wallets or direct token grants to
    addresses outside the register, including personal wallets. If a
    funder offers your project tokens, bring {{ORG_NAME}} finance in before
    you share an address.

-   **Every on-chain payment must include the transaction hash in the OC
    memo.** Format: tx: 0xabc... with the first 6 and last 4 characters
    is enough for lookup. {{PLATFORM_CRYPTO_SUB}} uses this to reconcile.

-   **The recipient's wallet address goes in the memo, not just the
    name.** For any recipient not already in the {{ORG_NAME}} address book,
    note NEW ADDRESS so the operations team can add and screen it. New
    addresses require a test transaction and allowlisting above
    \{{THRESHOLD_DFO_REVIEW}}.

-   **Gas fees are booked to the ledger that owns the underlying
    transaction**, not to a shared bucket. If you pay a project
    contractor \{{THRESHOLD_LINE_ITEM_REVIEW}} USDC and the gas is $3, both go to your project
    (Project Expenses: Contractors for the \{{THRESHOLD_LINE_ITEM_REVIEW}}, Administrative &
    Operations: {{PLATFORM_CRYPTO_SUB}} - Crypto Fees for the $3).

-   **{{PLATFORM_CRYPTO_SUB}} subscription and reconciliation fees are core costs**,
    funded by fiscal sponsorship fee revenue. Do not pass them to
    project ledgers.

-   **Stablecoin transfers between {{ORG_NAME}} wallets are treasury
    movements, not expenses.** They do not appear on any project ledger.
    If a movement looks like an expense on your ledger and you know it
    was a treasury sweep, flag it \[REVIEW: treasury movement\].

-   **Crypto contributions to your project** are recognized at fair
    market value on the date received, under ASU 2023-08, with {{PLATFORM_CRYPTO_SUB}}
    as the subledger of record. Operations books this. You will see it
    on your ledger with the FMV already applied. If the USD value looks
    off by more than 5% from the day's price, flag it.

-   **Non-stablecoin payments (ETH, BTC, and other volatile tokens)
    require pre-approval** from the Director of Finance & Operations
    before the payout is initiated. Volatility on a five-day payables
    cycle can move the USD value 10--20% and needs a conversion
    decision. Payments above \{{THRESHOLD_DFO_REVIEW}} also require dual approval on the
    custodial platform.

-   **Volatile tokens received are converted** to USDC or fiat within
    {{WINDOW_CRYPTO_CONVERSION}} by default. Strategic holdings require Board
    designation. Staking, lending, and DeFi deployment require prior
    Board approval. Projects may not deploy project assets on their own
    initiative.

-   **Contractor payments in digital assets** are recorded at USD fair
    market value on the payment date and are included in 1099 reporting.

**When in doubt on a crypto expense:** copy the transaction hash into
the {{PLATFORM_FISCAL_HOST}} memo and tag \[REVIEW: crypto\]. The operations team runs a
weekly {{PLATFORM_CRYPTO_SUB}} sync and picks these up within {{WINDOW_CRYPTO_CONVERSION}}.

**2.9 What {{ORG_NAME}} core will never charge to your project**

The following are always core costs. If any of these appear on your
project's {{PLATFORM_FISCAL_HOST}} ledger, flag it. It is a classification error and needs to
be reclassified.

-   990 preparation, external audit fees, IRS filings

-   D&O insurance, general liability, cyber liability

-   Board meeting costs, board member expenses, board recruitment

-   ED and DFO time, bookkeeper retainer, controller time on close

-   {{PLATFORM_GL}} and general accounting infrastructure

-   {{PLATFORM_CRYPTO_SUB}} subscription and crypto reconciliation platform fees

-   State charity registration renewals

-   Legal review of the master fiscal-sponsorship agreement or {{ORG_NAME}}
    bylaws

-   {{ORG_NAME}}-wide fundraising expenses (not project fundraising)

-   The {{ORG_NAME}} fiscal sponsorship fee itself; it is revenue to {{ORG_NAME}},
    not an expense charged to you

**2.10 What cannot be paid through {{ORG_NAME}} at all**

Distinct from 2.9: these are not core costs either. They cannot be paid
from any {{ORG_NAME}} ledger.

-   Personal expenses, or the personal portion of any mixed expense

-   Political campaign activity of any kind; lobbying only within
    permitted limits and only with prior written approval

-   Any payment providing more than incidental private benefit to a
    project leader, a family member, or a business they control

-   Anything outside the charitable purpose described in your Fiscal
    Sponsorship Agreement

-   Payments to sanctioned parties or jurisdictions

-   Gift cards and cash-equivalent gifts; penalties, fines, and
    interest; alcohol without prior approval

-   Spending in excess of your available balance, including against
    anticipated revenue

-   Any commitment creating a legal obligation for {{ORG_NAME}}, such as
    leases, employment offers, or multi-year contracts, unless signed by
    an authorized {{ORG_NAME}} signer

Conflicts of interest are not prohibited; undisclosed ones are. If a
payment would go to you, someone close to you, or an entity you are
involved with, disclose it before it is committed. Annual disclosures
are renewed by August 1 and cover token holdings, DAO roles, and
protocol foundation affiliations as well as conventional vendor and
board relationships.

**2.11 Receipt and documentation standards**

**Every expense requires supporting documentation**, an invoice or an
itemized receipt, with no de minimis threshold. This applies to
everything submitted through {{PLATFORM_FISCAL_HOST}} as well; submitting through the platform
does not replace the receipt.

**Reimbursements must be submitted within {{WINDOW_REIMBURSEMENT}}** of the transaction
date. Submissions between 30 and 90 days will be reviewed and may
require additional substantiation. Anything older than 90 days requires
a written explanation and DFO approval before payment.

Whatever you submit should carry, in one sentence a stranger could
follow: what was purchased, who was paid, and why it advances the
project's charitable purpose. Beyond that:

-   Receipts must be **itemized**. A card statement line or a bank
    screenshot is not sufficient substantiation.

-   Meals and events need the **attendees and the business purpose**.

-   Travel needs the **event, dates, and purpose**; personal extensions
    must be excluded from the amount submitted.

-   Subawards need a **signed grant agreement and the grantee's EIN and
    address** before payment. {{ORG_NAME}} reports these on 990 Schedules I
    and F, and foreign grantees need extra detail.

-   For any expense that is split or that could reasonably be questioned
    by an auditor, keep the basis documentation with the receipt. A
    one-line note in {{PLATFORM_FISCAL_HOST}} is sufficient; do not rely on memory.

**2.12 Monthly review workflow**

The last business day of each month, the project lead should:

**1.** Open your project's {{PLATFORM_FISCAL_HOST}} ledger for the month.
>
**2.** Skim every transaction and confirm the category is correct.
>
**3.** Flag any \[REVIEW\] items with a decision.
>
**4.** Confirm all crypto transactions show a tx hash in the memo.
>
**5.** Confirm that spending against any restricted grant is on track
and within its period.
>
**6.** Compare month-to-date spend against your monthly budget on the
rolling forecast tab.
>
**7.** Send any budget amendments to the DFO before the 5th of the
following month.

This takes 20 minutes for a project spending under $10K/month and 45
minutes for a larger project. Doing this monthly prevents the
end-of-year reconciliation from becoming a two-week project.

**2.13 What {{ORG_NAME}} will ask you for once a year**

None of this is a surprise if you have kept up with 2.12. It is listed
here so you can gather it as you go rather than in March.

-   Grant agreements or award letters for every subaward you made, with
    the grantee's EIN, address, and the purpose of the grant.

-   Confirmed addresses and tax forms for every contractor, before the
    January 1099 run.

-   A short program accomplishment narrative for the 990.

-   A list of in-kind goods and services received, and approximate
    volunteer counts.

-   Confirmation of any grant restrictions still unspent at year end.

**Questions and edge cases**

For anything not covered here, message the DFO directly with the
transaction details. Do not guess. A five-minute Slack thread now saves
an hour of reclassification at year-end.

For questions about the underlying policies (allowable expenses,
allocation methodology, related-party rules, conflict-of-interest
requirements), refer to the {{ORG_NAME}} Fiscal Policies and Procedures
Manual.

**Appendix: Quick reference**

  ------------------------------------------------------------------------
  **Situation**           **Which         **What to do**
                          ledger?**       
  ----------------------- --------------- --------------------------------
  A contractor doing      Project         Agreement and W-9/W-8 first;
  project work                            submit as an Invoice under
                                          Project Expenses: Contractors

  You bought a domain on  Project, if     Submit as a Receipt with
  a personal card         reimbursed      itemized proof within {{WINDOW_REIMBURSEMENT}},
                                          under Administrative &
                                          Operations: Application
                                          Subscriptions

  Your other organization Neither         It stays in that entity's books;
  paid for the venue                      do not submit it

  A law firm donated ten  Neither;        Report it to {{ORG_NAME}}; it is not
  hours                   in-kind         an {{PLATFORM_FISCAL_HOST}} expense

  A subaward to a         Project         Grant agreement and EIN
  university or nonprofit                 required; Direct Support: Grant
                                          Expense

  A token grant offered   Project         Registered {{ORG_NAME}} address only;
  to your project                         ask finance before sharing an
                                          address

  Conference flights and  Project         Travel; meals go separately to
  hotel                                   Project Expenses: Meals

  A team dinner           Project         Meals; record attendees and
                                          business purpose

  Someone working 30      Project, but as Talk to {{ORG_NAME}} before engaging
  hours a week under your payroll         them
  direction                               

  Spending against a      Neither, yet    Not until the funds land in the
  grant you expect to                     balance
  receive                                 

  Signing a twelve-month  {{ORG_NAME}} signs,  Route it to the Executive
  lease                   not you         Director

  A vendor engagement     Project         Three competitive bids before
  over \{{THRESHOLD_COMPETITIVE_BIDS}}                           commitment; you approve, DFO
                                          second-approves

  {{PLATFORM_GL}}, Slack, D&O  Core            Never charged to your project;
  insurance                               flag it if you see it

  A subscription two      Shared          Split at entry; three memo
  projects share                          fields per 2.4

  Gas fee on a project    Project         {{PLATFORM_CRYPTO_SUB}} - Crypto Fees; goes with
  contractor payout                       the underlying transaction

  Genuinely cannot tell   Project, tagged \[REVIEW: possible core\] in the
                                          description; bookkeeper resolves
                                          at close
  ------------------------------------------------------------------------

**Glossary**

Terms used in this document, in the sense {{ORG_NAME}} uses them.

**Available balance.** The cash {{ORG_NAME}} currently holds for your project
and that you may actually spend. It is net of the fiscal sponsorship fee
and processing costs, and it excludes any revenue that has been pledged
or awarded but not yet received.

**{{PLATFORM_CRYPTO_SUB}}.** The digital-asset subledger {{ORG_NAME}} uses to track wallets,
on-chain transactions, and fair-value reporting. It reconciles to the
general ledger and to the custodian.

**Class.** The tag in {{PLATFORM_GL}} that assigns a transaction to a
specific project. Every transaction must carry one; anything left
unclassed lands in "Not specified" at year end.

**Collective.** Your project's page and ledger in OC. One project maps
to one collective.

**Core (unrestricted core).** {{ORG_NAME}} as a whole. Costs that benefit the
organization rather than any single project are charged here and funded
by fiscal sponsorship fee revenue.

**DFO.** Director of Finance & Operations, the {{ORG_NAME}} role that reviews
and second-approves project spending, sets classification policy, and
manages the annual close.

**Dual approval.** Two named people approving the same transaction
before it is released. Required on custodial platform movements above
\{{THRESHOLD_DFO_REVIEW}}.

**Fair market value (FMV).** The USD value of a digital asset on the
date of receipt or payment. It is the amount recorded in the books and
reported on tax forms, regardless of what the asset is worth later.

**Fiscal sponsorship.** The arrangement under which {{ORG_NAME}}, a
501(c)(3), receives and holds charitable funds for a project that is not
itself a separate tax-exempt entity, and takes legal responsibility for
how those funds are spent.

**Fiscal Sponsorship Agreement (FSA).** The contract between {{ORG_NAME}} and
your project. It sets the charitable purpose, the fee, and the terms of
the relationship, and it controls where it differs from general
guidance.

**Fiscal sponsorship fee (host fee).** {{HOST_FEE_RATE}} of gross incoming funds, per
the FSA. It is deducted as each contribution settles and appears on the
{{PLATFORM_FISCAL_HOST}} ledger as a "Host Fee" line.

**Form 990.** The annual information return {{ORG_NAME}} files with the IRS.
It reports every dollar of revenue and expense, including your
project's, split across Program, Management & General, and Fundraising.

**Form 1099-NEC.** The IRS form {{ORG_NAME}} issues to US contractors paid at
or above the reporting threshold in a calendar year (\{{THRESHOLD_1099_MIN}} for 2026).
Digital-asset payments count at USD fair market value.

**Form W-9 / W-8BEN.** Tax identification forms collected before the
first payment to a payee. W-9 for US persons and entities, W-8BEN or
W-8BEN-E for non-US. Both are collected through {{PLATFORM_FISCAL_HOST}} as part of payee
setup.

**Functional classification.** The split of expenses into Program,
Management & General, and Fundraising on the 990. The account alone does
not determine it, which is why fundraising costs must be identified in
the memo.

**Gas fee.** The network fee paid to execute an on-chain transaction. It
is charged to whichever ledger owns the underlying payment, not to a
shared bucket.

**In-kind contribution.** Donated goods or services, such as pro-bono
legal work or a donated venue. Not a cash expense and not submitted
through OC, but reportable, so tell {{ORG_NAME}} when you receive one.

**Invoice (in OC).** A submission type used when someone is billing for
services. The invoice document must state the work performed and the
period covered.

**Loaded cost.** The true cost of employing someone: gross salary plus
employer taxes, benefits, and PEO fees. Typically 18 to 25% above
salary, and the figure to budget.

**OC ({{PLATFORM_FISCAL_HOST}}).** The platform {{ORG_NAME}} uses to run project
ledgers, collect contributions, and process expense submissions. It is a
subledger and a view into {{ORG_NAME}}'s books, not a separate set of books.

**PEO.** Professional Employer Organization, the employer-of-record
service through which {{ORG_NAME}} runs payroll. Its fees are charged to the
project alongside the salary.

**Project-restricted.** Funds or costs that belong to one specific
project. Restricted funds may only be spent on that project's
charitable purpose, and any further donor restriction travels with the
money.

**{{PLATFORM_GL}}.** {{ORG_NAME}}'s general ledger and the system of
record. {{PLATFORM_FISCAL_HOST}} and {{PLATFORM_CRYPTO_SUB}} are subledgers that reconcile to it.

**Receipt (in OC).** A submission type used to reimburse money already
spent. An itemized receipt must be attached; a card statement line is
not sufficient.

**Regrant / subaward.** A grant made from your project to another
organization. It requires a signed grant agreement and the grantee's
EIN and address before payment, and it is reported on 990 Schedules I
and F.

**\[REVIEW\] tag.** A note added to an {{PLATFORM_FISCAL_HOST}} expense description when you
cannot determine the right classification. The bookkeeper resolves
tagged items at monthly close. Variants in use: \[REVIEW: possible
core\], \[REVIEW: crypto\], \[REVIEW: treasury movement\].

**Schedule I / Schedule F.** The 990 schedules that report grants made
to organizations inside the US (I) and outside it (F). Both require
grantee detail your project supplies.

**Split expense.** A cost that genuinely benefits more than one project,
or a project and core, allocated at the point of entry using a
documented basis such as time, seat count, or FTE ratio.

**Stablecoin / USDC.** A digital asset pegged to the US dollar. USDC may
be held as an operating treasury asset; volatile tokens are converted to
USDC or fiat within {{WINDOW_CRYPTO_CONVERSION}} by default.

**Treasury movement.** A transfer of funds between {{ORG_NAME}}'s own
accounts or wallets. It is not an expense and does not appear on any
project ledger.

**Transaction hash (tx hash).** The unique identifier of an on-chain
transaction. Required in the {{PLATFORM_FISCAL_HOST}} memo for every crypto payment so {{PLATFORM_CRYPTO_SUB}}
can reconcile it.

**Wallet register.** The list of wallets authorized to hold or move
{{ORG_NAME}} funds, maintained in {{PLATFORM_CRYPTO_SUB}}. Projects may not use addresses
outside it, including personal wallets.

**W-2 employee vs. 1099 contractor.** Two different legal relationships.
{{ORG_NAME}}, not the project, makes the determination. Any request to hire a
full-time W-2 staff member goes to the {{ORG_NAME}} FinOps Director before an
offer is discussed.


---

## Template variables

The tokens below appear in this document. Set them in your local `context.yaml` (see [`ai/context.example.yaml`](../../ai/context.example.yaml) for the full schema, defaults, and validation).

### Organization identity
| Token | Meaning | Example |
|---|---|---|
| `{{ORG_NAME}}` | Short name | `Example Sponsor` |
| `{{ORG_LEGAL_NAME}}` | Legal name with entity type | `Example Sponsor, Inc.` |
| `{{ORG_LEGAL_NAME_UPPER}}` | Uppercase legal name for title pages | `EXAMPLE SPONSOR, INC.` |
| `{{ORG_STATE}}` | State of incorporation | `Delaware` |
| `{{ORG_EIN}}` | Employer Identification Number | `12-3456789` |
| `{{ORG_ADDRESS}}` | Principal office address | `123 Main Street, Anytown, ST 12345` |

### Approval thresholds (USD; set to your board-adopted values)
| Token | Meaning | Common value |
|---|---|---|
| `{{THRESHOLD_DFO_REVIEW}}` | DFO review required above this | `$10,000` |
| `{{THRESHOLD_BOARD_SECONDARY}}` | Board President secondary approval | `$15,000` |
| `{{THRESHOLD_COMPETITIVE_BIDS}}` | Competitive bidding required | `$30,000` |
| `{{THRESHOLD_BOARD_EXCEPTION}}` | Full Board exception required | `$100,000` |
| `{{THRESHOLD_DEVIATION}}` | Budget-deviation prior approval | `$20,000` |
| `{{THRESHOLD_CAPITALIZATION}}` | Capitalize as fixed asset above this | `$5,000` |
| `{{THRESHOLD_SOFTWARE_REVIEW}}` | Software/SaaS review threshold | `$2,500` |
| `{{THRESHOLD_1099_MIN}}` | 1099-NEC issuance floor | `$600` (federal min) or `$2,000` |
| `{{THRESHOLD_LINE_ITEM_REVIEW}}` | Category-move review threshold | `$500` |

### Time windows
| Token | Meaning | Common value |
|---|---|---|
| `{{WINDOW_REIMBURSEMENT}}` | Reimbursement submission window | `30 days` |
| `{{WINDOW_EXPLANATION}}` | Window requiring written explanation | `60 days` |
| `{{WINDOW_DFO_APPROVAL}}` | Window requiring DFO approval | `90 days` |
| `{{WINDOW_MISCODE_FLAG}}` | Miscode-flag window after month close | `30 days` |
| `{{WINDOW_CRYPTO_CONVERSION}}` | Volatile-token conversion window | `5 business days` |

### Platform bindings
| Token | Meaning | Common values |
|---|---|---|
| `{{PLATFORM_GL}}` | General-ledger accounting system | `QuickBooks Online`, `Xero`, `Sage Intacct`, `NetSuite` |
| `{{PLATFORM_FISCAL_HOST}}` | Fiscal-sponsorship platform | `Open Collective`, `HCB`, `custom ledger` |
| `{{PLATFORM_CRYPTO_SUB}}` | Digital-asset subledger | `Bitwave`, `Cryptio`, `TRES Finance` |
| `{{PLATFORM_CRYPTO_CUSTODIAN}}` | Qualified crypto custodian | `Coinbase Prime`, `Anchorage Digital`, `BitGo` |
| `{{PLATFORM_CARD_PROCESSOR}}` | Card / donation processor | `Stripe`, `Every.org`, `Donorbox` |
| `{{EXTERNAL_ACCOUNTANT}}` | Outside audit/accounting firm | firm name |

### Rates
| Token | Meaning | Common value |
|---|---|---|
| `{{HOST_FEE_RATE}}` | Default fiscal-sponsorship fee on gross receipts | `10%` |
