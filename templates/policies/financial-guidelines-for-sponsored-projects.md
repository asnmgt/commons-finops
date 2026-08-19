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

**{{ORG_LEGAL_NAME_UPPER}}**

**Financial Guidelines for**

**Fiscally Sponsored Projects**

How project spending is recorded, coded, approved, and reconciled, and
what each project team is responsible for.

**Version 1.0 · Issued August 2026**

Companion to the {{ORG_NAME}} Fiscal Policies & Procedures Manual

Prepared by the Office of the Director of Finance & Operations

*This document summarizes {{ORG_NAME}}'s financial policies as they apply to
sponsored projects. Where it differs from the Fiscal Policies &
Procedures Manual, the Manual controls; where the Manual differs from a
project's Fiscal Sponsorship Agreement, that Agreement controls for that
project.*

**Contents**

[[1. Purpose and How to Use This Document](#sec0)
>
[[2. The Short Answer: What Counts as a "{{ORG_NAME}}
Expense"](#sec1)
>
[[3. How the Money Is Held and Recorded](#sec2)
>
[[4. Coding Expenses: The Shared Category Set](#sec3)
>
[[5. What It Costs to Run Through {{ORG_NAME}}](#sec4)
>
[[6. Paying People](#sec5)
>
[[7. Approvals and Documentation](#sec6)
>
[[8. What Cannot Be Paid Through {{ORG_NAME}}](#sec7)
>
[[9. Digital Assets](#sec8)
>
[[10. The Monthly and Annual Rhythm](#sec9)
>
[[11. Building a Budget That Reconciles](#sec10)
>
[[12. Quick Reference](#sec11)
>
[[13. Questions](#sec12)
>
[[Appendix A: Month-End Checklist for Project
Leads](#sec13)
>
[[Appendix B: Before You Commit](#sec14)
>
[[Glossary](#sec15)

[]{#sec0 .anchor}**1. Purpose and How to Use This Document**

These guidelines explain how {{ORG_LEGAL_NAME}} ("{{ORG_NAME}}") accounts for
money it holds on behalf of the projects it fiscally sponsors, and what
each project needs to do so that its own budget and {{ORG_NAME}}'s books
agree.

They are a companion to the **{{ORG_NAME}} Fiscal Policies & Procedures
Manual**, which is the governing document. Rates, thresholds, and
category names are current as of the issue date on the cover. Where
these guidelines and the Manual differ, the Manual controls; where the
Manual and your **Fiscal Sponsorship Agreement (FSA)** differ, the FSA
controls for your project.

Every section is written in two layers:

-   **Policy**: a requirement. {{ORG_NAME}}'s general ledger, its audit, and
    its Form 990 depend on it.

-   **In practice**: how to actually do it, and what it looks like in
    {{PLATFORM_FISCAL_HOST}}.

If you read nothing else, read Section 2 and the quick-reference table
in Section 12.

[]{#sec1 .anchor}**2. The Short Answer: What Counts as a "{{ORG_NAME}}
Expense"**

**POLICY**
>
Funds raised for a fiscally sponsored project are the legal property
of {{ORG_NAME}}, held and expended for that project's charitable purpose.
**Every disbursement from a project's balance is a {{ORG_NAME}} expense**,
recorded in {{ORG_NAME}}'s general ledger and tagged with the project's
class. Expenses paid from any other source are not {{ORG_NAME}} expenses
and must not appear in {{ORG_NAME}}'s books or in {{ORG_NAME}}-facing reports.
>
**IN PRACTICE**
>
There is only one set of books, and they are {{ORG_NAME}}'s. Your {{PLATFORM_FISCAL_HOST}} ledger
is a view into them, not a second set. So the question is not "is
this a {{ORG_NAME}} expense or a project expense?" A project expense paid
from your collective **is** a {{ORG_NAME}} expense. The real question is
simply:
>
**Did the money come out of the balance {{ORG_NAME}} holds for us, or is it
going to?**

If yes, it belongs in {{ORG_NAME}}'s books, coded to your project. If no, it
belongs in whatever other entity paid it, and it should never be
submitted to {{ORG_NAME}}.

**2.1 The three buckets**

  -------------------------------------------------------------------------
  **Bucket**   **What it is**              **Where it is      **In your OC
                                           recorded**         balance?**
  ------------ --------------------------- ------------------ -------------
  **A. Paid by Contractor invoices,        {{ORG_NAME}} general    Yes
  {{ORG_NAME}}**    reimbursements,             ledger, coded to   
               subscriptions, travel,      your project class 
               subawards, payroll:                            
               anything drawn on your                         
               collective balance                             

  **B. Paid by Your own LLC or nonprofit,  That entity's      No
  someone      another fiscal sponsor, a   books only         
  else**       partner organization, a                        
               personal card you do not                       
               submit                                         

  **C. In-kind Pro-bono legal work, a      Not a cash         No
  / donated**  donated venue, volunteer    expense; certain   
               time, donated software      in-kind items are  
                                           separately         
                                           recorded by        
                                           {{ORG_NAME}} for the    
                                           990                
  -------------------------------------------------------------------------

**2.2 The five-question test**

1.  Will {{ORG_NAME}} pay it, from your collective balance, a {{ORG_NAME}} card,
    or {{ORG_NAME}} payroll? **If yes, stop: it is a {{ORG_NAME}} expense.**

2.  Did someone pay out of pocket and intend to be reimbursed? Then yes.
    It becomes a {{ORG_NAME}} expense on the date {{ORG_NAME}} reimburses it.

3.  Was it paid by another entity and will never be reimbursed? Then no.
    Keep it out of {{ORG_NAME}}'s books entirely, including out of the budget
    columns you send us.

4.  Is it a donated good or service? That is in-kind. Tell {{ORG_NAME}} about
    it; do not submit it as an expense.

5.  Still unsure? Ask before you spend. Fixing a transaction after it
    settles costs far more time than a two-line email.

**NOTE**
>
**Timing.** An expense generally enters the ledger on the date {{ORG_NAME}}
pays it, not the date you incur it. Year-end accruals are handled by
the finance team. This is why a December commitment paid in January
lands in the following year. Plan around it if a grant period ends on
December 31.

[]{#sec2 .anchor}**3. How the Money Is Held and Recorded**

**POLICY**
>
**Legal ownership.** Contributions are made to {{ORG_NAME}} and restricted
to your project's purpose. {{ORG_NAME}} retains the discretion and control
over those funds that the IRS requires of a fiscal sponsor.
>
**One project, one {{PLATFORM_FISCAL_HOST}} account.** Each sponsored project maps
one-to-one to their assigned {{PLATFORM_FISCAL_HOST}} collective. Every transaction must
carry the class.
>
**Books of record.** {{PLATFORM_GL}} is the general ledger. {{PLATFORM_FISCAL_HOST}} is
the subledger for collective activity; {{PLATFORM_CRYPTO_SUB}} is the subledger for
digital assets; bank, card, and processor statements are the
underlying source. All are reconciled monthly.
>
**No deficit spending.** A project may not spend more than its
available balance. Pledged, awarded-but-unreceived, or anticipated
revenue is not spendable.
>
**Restrictions travel with the money.** A grant restricted to a
purpose or a period may only be spent that way. The project is
responsible for telling {{ORG_NAME}} the restriction when the grant
arrives, in writing, with the grant agreement attached.
>
**Closure.** On termination or transfer, a project's balance must be
brought to zero and disposed of as the FSA provides.
>
**IN PRACTICE**
>
Your collective's **available balance** is the only number that tells
you what you can actually spend today. Build your budget from it. If
the plan spends more than the available balance plus already-received
income, the difference is contingent. Label it as contingent in the
meeting rather than letting it sit in the same column as committed
spending.

[]{#sec3 .anchor}**4. Coding Expenses: The Shared Category Set**

**POLICY**
>
Every transaction must be coded to (a) an account from {{ORG_NAME}}'s chart
of accounts and (b) the project's class. Uncoded, miscoded, or
unclassed items must be corrected within **{{WINDOW_MISCODE_FLAG}} of month close**.
Items left unclassed at year end flow to "Not specified" on the
Statement of Functional Expenses and have to be researched during the
990 preparation, an avoidable cost to your project and to {{ORG_NAME}}.
>
**IN PRACTICE**
>
These are the categories you will see in the {{PLATFORM_FISCAL_HOST}} picker. Use the most
specific one that fits; use the parent only when nothing below it
applies.

**Income**

  -----------------------------------------------------------------------
  **Account**               **Use it for**
  ------------------------- ---------------------------------------------
  Contributed Revenue:      Individual gifts, small unrestricted
  Donations                 contributions, crowdfunding

  Contributed Revenue:      Foundation, DAF, corporate, and
  Grants                    protocol-foundation grants; attach the
                            agreement

  Memberships               Recurring membership or subscription support

  Other Income              Ticket sales, earned income, sponsorship
                            income, reimbursements received
  -----------------------------------------------------------------------

**Expenses most projects use**

  -----------------------------------------------------------------------
  **Account**                  **Use it for**
  ---------------------------- ------------------------------------------
  Personnel: Salaries & Wages  People on {{ORG_NAME}} payroll only; never
                               contractors

  Personnel: PEO Fees          Employer-of-record and PEO charges
                               attributable to your staff

  Legal & Professional         Legal counsel; the specific sub-accounts
  Services                     below are preferred

   • Accounting Fees           Bookkeeping, audit, tax preparation
                               attributable to the project

   • Other Professional Fees   Firms and agencies providing professional
                               services (not individuals doing project
                               work)

  Administrative & Operations  Parent account, used for core sponsorship
                               overhead; prefer a sub-account

   • Advertising & Marketing   Paid promotion, design for outreach,
                               printed materials

   • Application Subscriptions Software and SaaS under \{{THRESHOLD_SOFTWARE_REVIEW}}: Zoom,
                               Notion, hosting, domains

   • Bank Charges & Fees       Wire fees, processor fees, FX costs

   • Insurance                 Event, liability, or D&O insurance
                               attributable to the project

   • Licenses & Dues           Memberships, permits, registrations

   • {{PLATFORM_CRYPTO_SUB}} -- Crypto Fees    Gas, bridge, and exchange fees on
                               digital-asset activity

   • Computer & Software       Hardware and software purchases below the
                               capitalization threshold

   • Other Business Expenses   Training, conference registration,
                               anything genuinely uncategorized

  Project Expenses:            Individuals and sole proprietors doing
  Contractors                  project work under a 1099

  Project Expenses:            Venue, catering, AV, event platform,
  Event/Meeting                honoraria for speakers

  Project Expenses: Travel     Flights, trains, lodging, ground
                               transport; not meals

  Project Expenses: Meals      Meals while traveling and working meals;
                               record attendees and purpose

  Direct Support: Fellowships  Fellowship and stipend programs for
                               individuals

  Direct Support: Grant        Subawards and regrants to other
  Expense                      organizations; agreement and EIN required

  Direct Support: Sponsorships Sponsoring another organization's event or
                               program
  -----------------------------------------------------------------------

**4.1 Functional classification (why we ask "what was it for?")**

{{ORG_NAME}}'s Form 990 reports every dollar in one of three functional
columns: **Program**, **Management & General**, and **Fundraising**.
Project spending is normally Program. Two things routinely need your
input, because the invoice alone does not reveal them:

-   **Fundraising costs**: a grantwriter, a donor cultivation event, or
    campaign design work. These must be labeled fundraising.
    Under-reporting fundraising expense is a common and visible 990
    error.

-   **Administrative costs of running the project itself**:
    project-level bookkeeping, insurance, or legal work that supports
    the organization rather than the program.

**4.2 The five miscodes we correct most often**

-   A person doing project work billed to **Legal & Professional
    Services: Other Professional Fees** instead of **Project Expenses:
    Contractors**. This breaks 1099 tracking and is the single most
    expensive error to unwind in January.

-   Conference costs all dumped into **Project Expenses: Event/Meeting
    Expense**. Flights and hotels are **Project Expenses: Travel**;
    meals are **Project Expenses: Meals**; the venue and catering are
    **Project Expenses: Event/Meeting Expense**.

-   A subaward to another organization coded as **Project Expenses:
    Contractors**. Regrants must be **Direct Support: Grant Expense**.
    They drive 990 Schedules I and F and require a grant agreement and
    EIN.

-   Annual software over \{{THRESHOLD_SOFTWARE_REVIEW}} posted to **Administrative &
    Operations: Application Subscriptions**. Ask first; it may need to
    be capitalized or spread.

-   **No class on the transaction.** If you submit through your
    collective this is handled automatically; it is manual payments and
    journal entries that go astray.

[]{#sec4 .anchor}**5. What It Costs to Run Through {{ORG_NAME}}**

**POLICY**
>
{{ORG_NAME}} assesses a fiscal sponsorship fee of **10% of gross incoming
funds**, as set out in the project's Fiscal Sponsorship Agreement.
Payment processing fees, foreign-exchange and transfer costs, and all
employer payroll costs are borne by the project and charged to the
project's balance.
>
**IN PRACTICE**
>
Four costs surprise project teams at budget time. Put all four in the
budget explicitly rather than discovering them in the ledger:

  -----------------------------------------------------------------------
  **Cost**             **Typical magnitude**   **How it appears**
  -------------------- ----------------------- --------------------------
  **Fiscal sponsorship **10% of gross          A "Host Fee from
  (host) fee**         receipts**, per your    \<Project\> to {{ORG_NAME}}"
                       Fiscal Sponsorship      line deducted as each
                       Agreement               contribution settles, so
                                               your balance rises by the
                                               net

  **Payment            Roughly 2.2--3.5% plus  Netted against the
  processing**         a fixed fee on card     contribution by {{PLATFORM_CARD_PROCESSOR}} or
                       gifts; bank transfers   the processor
                       are usually free        

  **FX and             Roughly 0.5--1.5% on    A separate fee line, or an
  international        non-USD payouts         FX spread inside the
  transfers**                                  transfer

  **Employer costs on  Roughly 18--25% on top  Employer taxes, benefits,
  payroll**            of gross salary         and PEO fees, charged to
                                               the project alongside the
                                               salary
  -----------------------------------------------------------------------

**5.1 A worked example**

A \{{THRESHOLD_BOARD_EXCEPTION}} grant, with a {{HOST_FEE_RATE}} host fee, funding one half-time staff
member and contractor work:

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

**NOTE**
>
The lesson is the fourth line. A budget built on a $45,000 salary
rather than the $54,000 loaded cost is short by $9,000 before
anything goes wrong.

[]{#sec5 .anchor}**6. Paying People**

**POLICY**
>
No payment may be made to any individual or entity before a completed
**Form W-9** (US) or **Form W-8BEN / W-8BEN-E** (non-US) is on file.
**W-9s are collected through OC** as part of the payee setup; do not
email them separately.
>
Whether a person is a **contractor or an employee** is determined by
{{ORG_NAME}}, not by the project. **Any request to hire a full-time W-2
staff member must be submitted to the {{ORG_NAME}} FinOps Director** before
an offer is discussed. Anyone functioning as an employee must be
placed on {{ORG_NAME}} payroll.
>
**Supporting documentation is always required**, including for
submissions made through OC. Contractors submit **invoices**;
reimbursements require **itemized receipts**. There is no de minimis
threshold. Reimbursements must be submitted within **30 days** of the
transaction date. Submissions between 30 and 90 days will be reviewed
and may require additional substantiation; anything older than 90 days
requires a written explanation and DFO approval before payment.
>
{{ORG_NAME}} issues Form 1099-NEC to US contractors at or above the
**\{{THRESHOLD_1099_MIN}} threshold for calendar 2026**. Payments made in digital
assets count at USD fair market value on the payment date.
>
Project leads may not commit {{ORG_NAME}} to an engagement. Contracts and
offers are signed by an authorized {{ORG_NAME}} signer only.
>
**IN PRACTICE**
>
In OC, **"Invoice"** means someone is billing for services and
**"Receipt"** means reimbursing money already spent. Either way,
attach the document: an invoice stating the work and the period
covered, or an itemized receipt. A card statement line is not a
receipt.
>
Have the payee complete their W-9 or W-8 **in {{PLATFORM_FISCAL_HOST}} at the moment you
agree to engage them**, not when the first invoice arrives. Missing
tax forms are the most common cause of delayed payments.
>
If you are paying the same person every month for ongoing work, on
your schedule, under your direction, using your tools, flag it to
{{ORG_NAME}}. That is very likely an employee, and getting it wrong creates
real liability for {{ORG_NAME}} and for the project.
>
Stipends and honoraria are taxable payments and need the same
paperwork as any other engagement.
>
Fellowships and scholarships to individuals are treated differently
from contractor payments. Talk to {{ORG_NAME}} before you announce one.
>
Non-US payees: expect the W-8, a treaty question, and possible
withholding. Build extra time into the first payment.

[]{#sec6 .anchor}**7. Approvals and Documentation**

**POLICY**
>
Project expenses follow a two-step approval process. The Project Lead
approves, and the {{ORG_NAME}} Director of Finance & Operations approves as
second reviewer. No Board approval is required for project expenses at
any amount.

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

**IN PRACTICE**
>
Two rules sit alongside the approval chain and are not approvals. A
single vendor engagement over **\{{THRESHOLD_COMPETITIVE_BIDS}}** requires three competitive
bids before commitment, and equipment costing **\{{THRESHOLD_CAPITALIZATION}} or more** is
capitalized rather than expensed. Digital-asset commitments are
measured in USD at the time the commitment is made, and payments above
\{{THRESHOLD_DFO_REVIEW}} require dual approval on the custodial platform.
>
**IN PRACTICE**
>
Documentation minimums for anything you submit:

-   **What** was purchased, **who** was paid, **why** it advances the
    project's charitable purpose, in the description field, in one
    sentence a stranger could follow.

-   An **itemized** receipt or invoice. A card statement line or a bank
    screenshot is not sufficient substantiation.

-   A **signed agreement** for any engagement, and a **grant agreement
    plus EIN** for any subaward.

-   For meals and events: the **attendees and the business purpose**.

-   For travel: the **event, dates, and purpose**; personal extensions
    must be excluded from the amount submitted.

[]{#sec7 .anchor}**8. What Cannot Be Paid Through {{ORG_NAME}}**

**POLICY**
>
Personal expenses, or the personal portion of any mixed expense.
>
Political campaign activity of any kind. Lobbying only within
permitted limits and only with prior written approval.
>
Any payment providing more than incidental private benefit to a
project leader, a family member, or a business they control.
Related-party payments must be disclosed in advance and approved.
>
Anything outside the charitable purpose described in the project's
Fiscal Sponsorship Agreement.
>
Payments to sanctioned parties or jurisdictions.
>
Gift cards and cash-equivalent gifts; penalties, fines, and interest;
alcohol without prior approval.
>
Spending in excess of the available balance, including against
anticipated revenue.
>
Any commitment that creates a legal obligation for {{ORG_NAME}}, such as
leases, employment offers, or multi-year contracts, unless signed by
an authorized {{ORG_NAME}} signer.
>
**IN PRACTICE**
>
Conflicts of interest are not prohibited; undisclosed ones are. If a
payment would go to you, someone close to you, or an entity you are
involved with, disclose it before it is committed. Annual
conflict-of-interest disclosures are renewed by **August 1** each year
and cover token holdings, DAO roles, and protocol foundation
affiliations as well as conventional board and vendor relationships.

[]{#sec8 .anchor}**9. Digital Assets**

This section applies to any project that receives token grants, accepts
crypto donations, or pays contributors in digital assets. If your
project is fiat-only, you can skip it.

**POLICY**
>
**Custody.** Project digital assets are custodied by {{ORG_NAME}}, with
{{PLATFORM_CRYPTO_CUSTODIAN}} as qualified custodian. Self-custody is permitted only
where operationally required, with monthly sweeps to custody.
>
**Wallet register.** Every wallet used for project funds must appear
in the {{ORG_NAME}} wallet register maintained in {{PLATFORM_CRYPTO_SUB}}. Projects may not
open wallets or direct token grants to addresses outside the register,
including personal wallets.
>
**Valuation.** Contributions are recorded at fair value on the date
received under ASU 2023-08; {{PLATFORM_CRYPTO_SUB}} is the subledger of record.
>
**Treasury.** Volatile tokens are converted to USDC or fiat within
**{{WINDOW_CRYPTO_CONVERSION}}** by default. USDC may be held as an operating
treasury asset. Strategic holdings require Board designation, and
volatile holdings are subject to a default cap of **10% of liquid
assets**. Staking, lending, and DeFi deployment require prior Board
approval.
>
**Outbound payments.** New addresses require a test transaction and
allowlisting above \{{THRESHOLD_DFO_REVIEW}}; payments above \{{THRESHOLD_DFO_REVIEW}} require dual
approval. Payments to contributors are recorded at USD fair market
value on the payment date and are included in 1099 reporting. Any
required withholding is set aside in fiat before sending.
>
**Acknowledgments and tax forms.** Donor acknowledgments for crypto
gifts do not state a value. Gifts above \{{THRESHOLD_CAPITALIZATION}} may require a Form
8283 signature, and disposition within three years may require Form
8282.
>
**IN PRACTICE**
>
If a protocol foundation offers your project tokens, bring {{ORG_NAME}}
finance in **before** you give anyone an address. Retro-fitting a
wallet into the register after funds have moved is painful and
sometimes impossible to reconcile cleanly.
>
Budget in USD, not in tokens. Convert at the receipt-date value for
planning and treat any upside as unbudgeted.
>
Gas and bridge fees are real expenses; code them to Administrative &
Operations: {{PLATFORM_CRYPTO_SUB}} - Crypto Fees.
>
Never pay a contributor from a personal wallet and then seek
reimbursement. There is no clean way to record it.

[]{#sec9 .anchor}**10. The Monthly and Annual Rhythm**

**10.1 Monthly: about thirty minutes**

-   Read your collective's ledger for the month, line by line.

-   Confirm every expense has a sensible category and a description that
    will still make sense in a year.

-   Confirm the closing balance matches what you believe you have.

-   Flag anything miscoded to {{ORG_NAME}} finance **within 30 days of month
    close**.

-   Confirm that spending against any restricted grant is on track and
    within its period.

**10.2 Quarterly**

-   Compare actuals to your budget in the Plan tab and update the
    full-year forecast.

-   Reconfirm which pipeline revenue has become committed.

**10.3 Annually: what {{ORG_NAME}} will ask you for**

-   Grant agreements or award letters for every subaward you made, with
    the grantee's EIN, address, and the purpose of the grant (needed for
    990 Schedules I and F; foreign grantees need extra detail).

-   Confirmed addresses and tax forms for every contractor, before the
    January 1099 run.

-   A short program accomplishment narrative for the 990.

-   A list of in-kind goods and services received, and approximate
    volunteer counts.

-   Confirmation of any grant restrictions still unspent at year end.

[]{#sec10 .anchor}**11. Building a Budget That Reconciles**

**IN PRACTICE**
>
For a team budget meeting, seven habits keep the budget and the ledger
in agreement:

1.  **Start from the available balance**, not from the grant total. The
    host fee and any processing fees have already come out.

2.  **Include only committed income**: signed agreements or cash
    received. Put pipeline in a separate, clearly labeled column and do
    not sum the two.

3.  **Net the host fee** off anything not yet received, so the revenue
    line is what will actually be spendable.

4.  **Budget people fully loaded**: salary plus employer taxes,
    benefits, and PEO fees; contractor rates plus any platform or
    transfer costs.

5.  **Use the same categories as the ledger** (Section 4). Then
    budget-versus-actual works with no mapping exercise, every month,
    for free.

6.  **Hold a reserve**: one to two months of committed obligations,
    unspent.

7.  **Segregate restricted funds.** A restricted balance is not general
    operating money, even though it sits in the same total.

{{ORG_NAME}} maintains a **"Plan -- \<Project\>"** tab for each collective
in the finance workbook. It carries the current year's actuals by month,
a monthly-by-category budget grid for the planning year, and automatic
budget-versus-actual and full-year forecast sections. Ask your {{ORG_NAME}}
finance contact for your tab and enter your numbers in the yellow input
cells, and then your budget and our books stay in sync by construction
rather than by reconciliation.

[]{#sec11 .anchor}**12. Quick Reference**

  ------------------------------------------------------------------------
  **Situation**             **Through       **What to do**
                            {{ORG_NAME}}?**      
  ------------------------- --------------- ------------------------------
  A contractor doing        Yes             Agreement and W-9/W-8 first;
  project work                              submit as an Invoice under
                                            Project Expenses: Contractors

  You bought a domain on a  Yes, if         Submit as a Receipt with
  personal card             reimbursed      itemized proof within {{WINDOW_REIMBURSEMENT}},
                                            under Administrative &
                                            Operations: Application
                                            Subscriptions

  Your other organization   No              It stays in that entity's
  paid for the venue                        books; do not submit it

  A law firm donated ten    No; in-kind     Report it to {{ORG_NAME}}; it is
  hours                                     not an {{PLATFORM_FISCAL_HOST}} expense

  A subaward to a           Yes             Grant agreement and EIN
  university or nonprofit                   required; Direct Support:
                                            Grant Expense

  A token grant offered to  Yes             Registered {{ORG_NAME}} address
  your project                              only; ask finance before
                                            sharing an address

  Conference flights and    Yes             Project Expenses: Travel;
  hotel                                     meals go separately to Project
                                            Expenses: Meals

  A team dinner             Yes             Project Expenses: Meals;
                                            record attendees and business
                                            purpose

  Someone working 30 hours  Yes, but as     Talk to {{ORG_NAME}} before
  a week under your         payroll         engaging them
  direction                                 

  Spending against a grant  No              Not until the funds land in
  you expect to receive                     the balance

  Signing a twelve-month    {{ORG_NAME}} signs,  Route it to the Executive
  lease                     not you         Director

  A vendor engagement over  Yes             Three competitive bids before
  \{{THRESHOLD_COMPETITIVE_BIDS}}                                  commitment; Project Lead then
                                            DFO approve
  ------------------------------------------------------------------------

[]{#sec12 .anchor}**13. Questions**

Ask early rather than late. A question before a commitment takes a
minute; the same question after a payment settles can take a month and
may not have a clean answer.

Direct questions on coding, approvals, payments, and budgets to **the DFO
Sané, Director of Finance & Operations**, or to your {{ORG_NAME}} finance
contact.

[]{#sec13 .anchor}**Appendix A: Month-End Checklist for Project Leads**

-   Ledger for the month reviewed line by line

-   Every expense has the right category and a description that stands
    on its own

-   No expense sitting in a parent account where a sub-account applies

-   Fundraising costs identified as fundraising

-   Closing balance agrees to expectation

-   Any miscodes reported to {{ORG_NAME}} finance (within 30 days of close)

-   Restricted grant spending on track and within period

-   Outstanding W-9s / W-8s chased for anyone engaged this month

-   Reimbursements older than 30 days submitted, or escalated with an
    explanation

-   Forecast updated if anything material changed

[]{#sec14 .anchor}**Appendix B: Before You Commit**

-   The available balance covers it today, not on the strength of
    expected revenue

-   It fits the charitable purpose in the Fiscal Sponsorship Agreement

-   It fits an approved budget line, or a budget amendment has been
    requested

-   Tax forms are on file for the payee, or requested

-   Project Lead approval recorded, and routed to the DFO as second
    approver

-   Three bids obtained if the engagement exceeds \{{THRESHOLD_COMPETITIVE_BIDS}}

-   No undisclosed related-party interest

-   Nobody is signing on {{ORG_NAME}}'s behalf who is not authorized to

-   If digital assets are involved, the address is in the wallet
    register

[]{#sec15 .anchor}**Glossary**

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
