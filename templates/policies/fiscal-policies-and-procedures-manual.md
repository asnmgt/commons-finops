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

**{{ORG_LEGAL_NAME}}**

**Fiscal Policies and Procedures Manual**

Version 1 --- Draft for Board Review, August 2026

**Introduction**

This manual documents the fiscal policies and procedures governing
{{ORG_LEGAL_NAME}} (EIN {{ORG_EIN}}), a {{ORG_STATE}}-registered 501(c)(3)
public charity headquartered at {{ORG_ADDRESS}}. It applies to all financial activity of {{ORG_NAME}}'s
general operations and the fiscally sponsored projects it hosts on the
{{PLATFORM_FISCAL_HOST}}, including both fiat and cryptocurrency
transactions.

The manual is structured in five parts: Accounting Procedures, Internal
Controls, Financial Planning and Reporting, Revenue and Accounts
Receivable, and Expense and Accounts Payable, followed by Asset
Management (including Cash, Investments, and Digital Assets) and a
Fiscal Sponsorship annex. It is modeled on nonprofit fiscal policy
templates adapted to {{ORG_NAME}}'s dual fiat and on-chain treasury, its
global contractor base, and its role as a fiscal host for research and
open-source projects.

This manual supersedes prior standalone finance memos and is intended to
be reviewed annually by the Finance Committee and re-approved by the
Board of Directors at least every two years. Interim updates may be made
administratively by the Director of Finance and Operations for routine
or clarifying changes; substantive policy changes require Board
approval.

**Approving body:** Board of Directors of {{ORG_LEGAL_NAME}}

**Policy owner:** Director of FinOps (DFO)

**Effective date:** Upon Board adoption

**Accounting Procedures**

**Basis of Accounting**

{{ORG_NAME}} maintains its books and records on the accrual basis of
accounting in accordance with U.S. Generally Accepted Accounting
Principles (GAAP) as promulgated by the Financial Accounting Standards
Board (FASB). Revenue is recognized when earned and expenses are
recognized when incurred, without regard to the timing of cash receipts
or disbursements. Net assets are classified as either without donor
restrictions or with donor restrictions, consistent with FASB ASU
2016-14.

The fiscal year is the calendar year (January 1 through December 31).
The general ledger is maintained in {{PLATFORM_GL}}. Subsidiary
ledgers for fiscally sponsored projects are maintained in Open
Collective, which synchronizes to {{PLATFORM_GL}} on a scheduled basis.
On-chain treasury activity is reconciled to book in {{PLATFORM_CRYPTO_SUB}} and posted
to {{PLATFORM_GL}} as summary journal entries. All amounts are stated in U.S.
dollars; non-USD and cryptocurrency balances are revalued at each period
end using the exchange rate then in effect.

**Journal Entries**

Journal entries are used to record transactions that do not originate
from a standard transactional workflow, including accruals, allocations,
reclassifications, and period-end adjustments.

**Preparation:** Journal entries are prepared by the external accountant
or, when required, by the DFO. Each entry must include a description,
the supporting rationale, references to source documentation, and the
preparer's initials.

**Review and posting:** All journal entries are reviewed by the DFO
before posting. Journal entries prepared by the DFO are reviewed by the
external accountant on the next scheduled close cycle. Entries greater
than $50,000 that are not part of routine period-end procedures require
concurrence from the Executive Director (ED) prior to posting.

**Retention:** Supporting documentation for every journal entry is
stored in {{ORG_NAME}}'s shared financial records archive and retained per
the schedule in this manual.

**Bank and Wallet Reconciliations**

All cash accounts, credit-card accounts, payment-processor accounts, and
on-chain wallets are reconciled monthly to independent third-party
statements or block-explorer records.

-   Mercury (primary operating), Axos, and Wise: reconciled monthly
    against downloaded bank statements.

-   {{PLATFORM_CARD_PROCESSOR}} and other payment processors: reconciled monthly against
    processor payout reports; gross-to-net differences booked to
    processing fees.

-   {{PLATFORM_FISCAL_HOST}} host and project balances: reconciled monthly
    against {{PLATFORM_FISCAL_HOST}} transaction exports; duplicate imports and
    Plaid transaction-ID collisions investigated at each close.

-   {{PLATFORM_CRYPTO_CUSTODIAN}} custodial balances: reconciled monthly against
    {{PLATFORM_CRYPTO_CUSTODIAN}} activity reports.

-   Self-custody wallets (Safe): reconciled monthly against on-chain
    balances via block-explorer queries and {{PLATFORM_CRYPTO_SUB}}.

The external accountant prepares reconciliations, which the DFO reviews.
Any reconciling item over \{{THRESHOLD_DFO_REVIEW}} that persists across two consecutive
months is escalated to the ED with a proposed resolution.

**Monthly Close**

{{ORG_NAME}} targets a monthly close within {{WINDOW_REIMBURSEMENT}} of month-end and a fiscal
year-end close within {{WINDOW_EXPLANATION}} of December 31. The close checklist
includes: transaction categorization complete, all reconciliations
complete, accruals and prepaid amortizations booked, allocation entries
booked, restricted-fund tracking updated, fiscally sponsored project
ledgers reviewed for restricted balance integrity, on-chain treasury
revalued to USD, and internal management reports issued to the ED.

**Document Retention and Destruction**

{{ORG_NAME}} retains financial and organizational records according to the
schedule below. Records are stored in {{ORG_NAME}}'s electronic archive with
restricted access. Records past their retention period are destroyed in
a manner that protects any confidential information they contain.

**Permanent retention**

-   Articles of incorporation, bylaws, and amendments

-   IRS determination letter and 501(c)(3) status documentation

-   Board minutes and resolutions

-   Filed Forms 990 and audited financial statements

-   Fiscal sponsorship agreements and grant agreements with material
    long-term terms

**Retain for 7 years**

-   General ledger, journals, and trial balances

-   Bank statements, wallet statements, and reconciliations

-   Invoices, receipts, expense reports, and supporting documentation

-   Payroll records, W-2s, W-9s, W-8BENs, and 1099s

-   Contracts, vendor agreements, and executed independent contractor
    agreements

-   Contribution acknowledgment letters and Form 8283 records

**Retain for the duration of the relationship plus 7 years**

-   Personnel files (subject to Justworks PEO retention where
    applicable)

-   Donor records and correspondence

-   Fiscally sponsored project files (during sponsorship plus 7 years
    after termination)

**Retain for 3 years**

-   Routine correspondence not related to legal, tax, or financial
    matters

-   Non-material vendor quotes not resulting in a purchase

**Internal Controls**

**Lines of Authority and Segregation of Duties**

Financial authority at {{ORG_NAME}} is delegated by the Board of Directors,
with segregation of duties designed so that no single individual
controls a transaction from initiation through recording, approval, and
reconciliation.

**Board of Directors:** Holds ultimate fiduciary responsibility for the
organization. Approves the annual budget, this manual, material policy
changes, transactions above the thresholds set below, appointment of the
ED and external auditor, and any material change in banking, custody, or
investment relationships.

**Finance Committee:** Standing committee of the Board chaired by the
Treasurer. Reviews quarterly financial reports, oversees implementation
of this manual, reviews the annual budget before Board approval,
recommends the external auditor, monitors compliance with the investment
and reserve policies, and reviews the crypto treasury policy at least
annually.

**Executive Director:** Responsible for the strategic and operational
execution of the organization within the Board-approved budget. Approves
expenses and commitments up to \{{THRESHOLD_BOARD_SECONDARY}}. Expenses and commitments
greater than \{{THRESHOLD_BOARD_SECONDARY}} and up to $150,000 require the ED's approval
plus a second approval from the DOF, Board President or Treasurer.

**Director of Finance and Operations** Owns day-to-day financial
operations, including accounts payable, accounts receivable, payroll
administration, treasury operations, fiscal sponsorship administration,
contractor onboarding, tax compliance, audit readiness, and
reconciliations. Authorizes routine expenses up to \{{THRESHOLD_BOARD_SECONDARY}} within
budgeted categories. Cannot self-approve any payment to themself; those
are approved by the ED.

**External Accountant:** Maintains the general ledger, prepares monthly
reconciliations and financial statements, prepares Form 990 and state
annual filings, prepares 1099 filings, and supports the annual audit.

**Bookkeeper/operations support:** Where used, performs first-line data
entry, invoice coding, receipt collection, and documentation gathering
under the direction of the DFO.

**Transaction approval thresholds**

-   **Up to \{{THRESHOLD_BOARD_SECONDARY}}:** DFO authorizes routine budgeted expenses up to
    \{{THRESHOLD_DFO_REVIEW}}. May not self-approve.

-   **$15,001 to \{{THRESHOLD_BOARD_SECONDARY}}:** ED approves. DFO may initiate.

-   **$15,001 to $150,000:** ED approves with a second approval from
    the DOF, Board President or Treasurer.

-   **Over $150,000 (single transaction or aggregate to a single vendor
    within a fiscal year):** Requires Board of Directors approval prior
    to commitment.

-   **Deviations from the approved annual budget greater than $50,000
    at the program or category level:** Requires Board of Directors
    approval as an amendment to the annual budget.

**Segregation-of-duties matrix**

-   Payment initiation is separated from payment approval. The DFO may
    prepare a payment in Mercury or {{PLATFORM_FISCAL_HOST}}, but approval
    requires a distinct user account holding the appropriate role.

-   Payment approval is separated from bank reconciliation.
    Reconciliations are prepared by the external accountant, not by the
    individual who approved the payment.

-   Vendor setup is separated from vendor payment. New vendor records
    must be established before payments are made, and vendor master data
    changes are logged.

-   On-chain transactions require multi-signature approval as specified
    in the Digital Asset Policy below.

**Conflict of Interest**

{{ORG_NAME}}'s Conflict of Interest (COI) Policy applies to all Directors,
officers, employees, contractors with significant financial authority,
and members of any standing committee with financial oversight
(collectively, Covered Persons).

**Covered Person:** Any Director, officer, employee, key contractor, or
standing-committee member.

**Covered Transaction:** Any transaction, contract, grant, compensation
arrangement, or other financial arrangement between {{ORG_NAME}} and a
Covered Person, a Related Party of a Covered Person, or an entity in
which a Covered Person or Related Party has a material financial
interest.

**Related Party:** A Covered Person's spouse or domestic partner,
ancestors, descendants, siblings, and any entity in which the Covered
Person or those individuals hold a controlling interest or serve as an
officer, director, trustee, or general partner.

**Disclosure and recusal**

Covered Persons complete an annual COI disclosure by August 1 each year
and update it promptly whenever a new potential conflict arises. In any
matter presenting an actual or apparent conflict, the Covered Person:
(a) discloses the interest to the Board or the applicable committee, (b)
recuses from deliberation and voting on the matter, and (c) does not
participate in the approval chain for any transaction affecting the
Covered Person or Related Party.

As a governing principle, no individual may sit in any position of the
approval chain for a payment to themself or a Related Party. This
principle overrides all delegated authority under this manual.

**Board determination**

The Board (or the applicable committee) determines whether a proposed
Covered Transaction is in {{ORG_NAME}}'s best interest, at fair value or
better, and no more advantageous to {{ORG_NAME}} than what could reasonably
be obtained from an unrelated party. The determination and the
underlying facts are recorded in the minutes.

**Physical and Digital Security**

{{ORG_NAME}} is a distributed, majority-remote organization. Physical
security controls are minimal because there is no central office holding
cash, checkbooks, or material physical assets; digital security controls
are correspondingly more extensive.

-   All financial systems require multi-factor authentication. Recovery
    methods use hardware keys or authenticator apps rather than SMS.

-   Access is provisioned on a least-privilege basis and reviewed at
    least quarterly by the DFO.

-   Onboarding of a new user to any financial system requires ED or DFO
    approval. Offboarding removes access within one business day of
    separation.

-   Physical checks are not used as a primary payment method. Any
    residual physical checks received are logged, endorsed for deposit
    only, and deposited within {{WINDOW_CRYPTO_CONVERSION}}.

-   Digital asset key management is governed by the Digital Asset Policy
    below.

**Financial Planning and Reporting**

**Budgeting Process**

The annual operating budget is prepared by the ED and the DFO, reviewed
by the Finance Committee, and approved by the Board of Directors prior
to the start of the fiscal year. The budget covers the general
operations of {{ORG_LEGAL_NAME}} and its administrative fee income from
fiscally sponsored projects. It does not consolidate the project-level
budgets of fiscally sponsored projects, which are governed by each
project's own budget process within the constraints of its fiscal
sponsorship agreement.

Budget-to-actual variance is reviewed monthly by the DFO and reported
quarterly to the Finance Committee. Variances above $50,000 at the
program or category level require a proposed course correction;
sustained variance requires a formal Board-approved budget amendment.

**Internal Financial Reports**

-   **Monthly to the ED:** Statement of Financial Position, Statement of
    Activities (with budget comparison), and cash-and-wallet summary
    issued by the DFO within {{WINDOW_REIMBURSEMENT}} of month-end.

-   **Quarterly to the Finance Committee:** Financial statements,
    budget-to-actual, fiscal-sponsorship portfolio summary, and digital
    asset holdings summary issued to the Finance Committee within 45
    days of quarter-end.

-   **Annually to the Board:** Full-year financial statements, audit or
    review results (once available), 990 summary, and reserve status
    included in the year-end reporting package.

**Audit and Review**

Under Massachusetts G.L. c. 12, s. 8F, as amended in November 2024, a
public charity with gross support and revenue greater than $1,000,000
must submit audited financial statements with Form PC; between \{{THRESHOLD_LINE_ITEM_REVIEW}},000
and $1,000,000, either audited or reviewed statements are acceptable.
{{ORG_NAME}}'s recent revenue history places the organization above the
audit threshold, and {{ORG_NAME}}'s policy is to obtain audited financial
statements each fiscal year regardless of whether the threshold is met,
in order to support grantor requirements and audit-ready posture. The
independent auditor is engaged by the Board upon recommendation of the
Finance Committee and is rotated or reassessed at least every five
years.

**Auditor selection:** The DOF reviews audit engagement scope, fees, and
independence annually and recommends selection or reappointment to the
Board.

**Audit fieldwork:** The DFO and external accountant serve as the
primary points of contact. The audit management letter is presented to
the Finance Committee and the Board, with a written management response
to each finding.

**Tax Compliance**

-   Form 990 is filed annually with the IRS. The filing deadline is the
    15th day of the 5th month after fiscal year-end (May 15 for a
    calendar-year filer), with an available 6-month extension. {{ORG_NAME}}
    targets a May 15 initial filing and uses extension only when needed.
    The DFO reviews the completed 990 before ED and Board President
    signature.

-   Form PC is filed annually with the Massachusetts Attorney General's
    Non-Profit Organizations/Public Charities Division. Audited
    financial statements are attached where required under M.G.L. c.
    12, s. 8F.

-   Form MA-990-T is filed if {{ORG_NAME}} has unrelated business taxable
    income (UBTI) exceeding thresholds.

-   State charitable solicitation registrations are maintained in states
    where {{ORG_NAME}} actively solicits contributions above the applicable
    thresholds. The DFO maintains the state-registration matrix and
    confirms status annually.

-   Forms 1099-NEC and 1099-MISC are prepared for U.S. contractors paid
    \{{THRESHOLD_1099_MIN}} or more in the calendar year and filed by January 31.
    {{ORG_NAME}}'s threshold is set below the federal $600 default to avoid
    inadvertent under-filing in cases where a contractor's total is
    reached across multiple accounting classes.

-   Forms 1042 and 1042-S are prepared for reportable payments to
    foreign persons and filed by March 15.

-   Form 8283 is signed by {{ORG_NAME}} as done for non-cash contributions
    greater than \{{THRESHOLD_CAPITALIZATION}}, including cryptocurrency donations. Form 8282
    is filed if a donated asset is sold within three years and is above
    the threshold.

**Fiscal Sponsorship**

{{ORG_NAME}} operates a fiscal sponsorship program through the Open
Collective platform. Sponsored projects are {{ORG_NAME}}'s programs for
legal and tax purposes; their funds are restricted for the project's
charitable purpose but remain {{ORG_NAME}}'s assets. Detailed procedures for
onboarding, financial administration, restricted-fund accounting,
grantee compliance, and offboarding are set out in the Fiscal
Sponsorship Annex to this manual.

**Revenue and Accounts Receivable**

**Invoice Preparation**

Invoices to grantors, contract funders, and program purchasers are
prepared by the DFO or delegated project leads with DFO oversight. Each
invoice references the underlying agreement, the deliverable or
milestone (if applicable), payment terms (default Net 30), the accepted
payment methods (ACH, wire, Wise, or cryptocurrency where explicitly
agreed), and any restricted-purpose language required by the grantor.

**Revenue Recognition**

Revenue is recognized in accordance with FASB ASC 958 (Not-for-Profit
Entities) and ASC 606 (Revenue from Contracts with Customers) as
applicable. Contributions and grants are recognized when the donor's or
grantor's unconditional promise is made; conditional contributions are
recognized when the barrier is overcome. Exchange transactions are
recognized as the underlying performance obligation is satisfied.
Restricted contributions are recorded as revenue with donor restrictions
and released to net assets without donor restrictions as the restriction
is satisfied.

**Review threshold:** The DFO reviews the recognition treatment of any
single revenue arrangement of \{{THRESHOLD_CAPITALIZATION}} or more and documents the
classification (contribution vs. exchange, unconditional vs.
conditional, restricted vs. unrestricted) before booking.

**Cryptocurrency contributions:** Recognized at fair market value on the
date received, with the specific procedures described in the Digital
Asset Policy below.

**Deposits**

Deposits are made to {{ORG_NAME}}'s primary operating accounts. Cash and
physical checks are not the norm; the rare check received is deposited
within {{WINDOW_CRYPTO_CONVERSION}} through Mercury mobile deposit or, where
limits require, by mailed deposit. Cryptocurrency deposits are made to
designated {{ORG_NAME}} wallets or the {{PLATFORM_CRYPTO_CUSTODIAN}} custodial account as
described in the Digital Asset Policy.

**Expense and Accounts Payable**

**Payroll**

{{ORG_NAME}}'s U.S. employees are paid through Justworks, a Professional
Employer Organization (PEO), which serves as the employer of record for
payroll tax, benefits administration, and workers' compensation
purposes. International employees and long-term contractors requiring an
Employer of Record are engaged through Deel where appropriate.

-   The ED authorizes hires, terminations, and material compensation
    changes within the Board-approved budget.

-   The DFO administers payroll runs in Justworks, reviews pre-run
    summaries, and reconciles PEO debits to the general ledger monthly.

-   The ED's compensation is reviewed and approved by the Board
    Compensation Committee (or full Board where no committee exists) at
    least every three years, with a written comparability analysis on
    file.

-   Payroll registers and journal entries are retained per the retention
    schedule above.

**Purchases and Procurement**

All purchases must be within the approved budget, reasonable for the
intended charitable purpose, and supported by adequate documentation.

-   **Purchases up to \{{THRESHOLD_BOARD_SECONDARY}}:** Requires an approved requisition or
    documented justification from the requester, DFO authorization
    within the DFO threshold, and vendor onboarding documentation on
    file (W-9 or W-8 series as applicable).

-   **Purchases $15,001 to $25,000:** Requires ED approval in addition
    to DFO authorization.

-   **Purchases $25,001 to $150,000:** Requires ED plus Board
    President or Treasurer approval.

-   **Purchases over $150,000 in a single commitment or aggregate to a
    single vendor within the fiscal year:** Requires prior Board
    approval.

-   Competitive bidding required: at least three written bids or a
    documented sole-source justification must accompany any single
    procurement of \{{THRESHOLD_COMPETITIVE_BIDS}} or more, other than payments to independent
    contractors engaged for services governed by the Independent
    Contractor section below.

-   Former Directors and officers may not be engaged as vendors or
    contractors on new contracts exceeding [\{{THRESHOLD_BOARD_SECONDARY}} within 12 months of
    the end of their service,]{.mark} absent a Board-approved
    competitive process documented in the minutes.

**Independent Contractors and Foreign Payees**

{{ORG_NAME}} engages a substantial number of independent researchers,
developers, and advisors, many of whom are located outside the United
States. {{ORG_NAME}} applies consistent onboarding and payment controls
regardless of the payment rail.

**Onboarding documentation**

-   U.S. persons: signed independent contractor agreement, current Form
    W-9.

-   Foreign individuals: signed independent contractor agreement,
    current Form W-8BEN, and completed tax-residency documentation.

-   Foreign entities: signed contract, current Form W-8BEN-E, and
    evidence of beneficial ownership sufficient to determine treaty
    eligibility.

-   Sanctions and integrity screening: OFAC Specially Designated
    Nationals (SDN) and Consolidated Sanctions List screening on every
    new contractor and on annual re-verification. Payment address (bank
    or wallet) is screened at onboarding and at any change.

**Withholding**

-   Payments to foreign persons for services performed outside the
    United States are generally not U.S.-source income and are not
    subject to U.S. withholding. Documentation of place of performance
    is retained.

-   Payments to foreign persons for U.S.-source services are subject to
    30% withholding unless reduced or eliminated by an applicable tax
    treaty and supported by a valid W-8BEN or W-8BEN-E claiming the
    treaty position. The DFO documents the treaty analysis before
    releasing payment.

**Reporting thresholds**

-   U.S. contractors: 1099-NEC or 1099-MISC issued for aggregate
    calendar-year payments of \{{THRESHOLD_1099_MIN}} or more, filed by January 31.

-   Foreign persons: 1042-S issued for any reportable U.S.-source
    payment regardless of amount, filed by March 15.

**OFAC and Sanctions Compliance**

{{ORG_NAME}} screens all counterparties against the OFAC Specially Designated
Nationals and Blocked Persons list, the Consolidated Sanctions List, and
applicable jurisdiction-based sanctions programs before payment or funds
transfer. Counterparty screening covers vendors, contractors,
sub-grantees, fiscally sponsored project leads, and recipient wallet
addresses on all outbound cryptocurrency transactions. Screening
evidence is retained with the vendor or grantee file.

**Invoice Approval and Payment**

Invoices are received centrally through Bill.com (rolling into
production during 2026), {{PLATFORM_FISCAL_HOST}} (for sponsored-project
expenses), or direct submission to the DFO. Every invoice must reference
a purchase authorization, a contract, or a budgeted category; must be
from an onboarded vendor; and must be supported by adequate
documentation.

**Standard payment terms:** Net 30 from invoice receipt for approved
invoices, or in accordance with the underlying contract if different.

**Approval turnaround:** Approved invoices are entered into the payables
system within 1{{WINDOW_CRYPTO_CONVERSION}} of receipt. Disputed invoices are worked
to resolution and are not aged silently.

**Payment execution:** Payments are executed through Mercury (ACH and
domestic wire), Wise (international), {{PLATFORM_FISCAL_HOST}} (sponsored-project
payables), or approved credit card. Cryptocurrency payments follow the
Digital Asset Policy below.

**Petty Cash**

{{ORG_NAME}} does not maintain a petty cash fund. All expenditures are
processed through credit card, ACH, wire, Wise, {{PLATFORM_FISCAL_HOST}}, or
approved crypto rails.

**Credit Cards**

Credit cards issued to staff (through Mercury, Ramp/Brex, or the PEO)
are used for business expenses only. Cardholders must obtain and submit
itemized receipts for every transaction of $25 or more, and code every
transaction to the correct account and program within 14 days of the
transaction date. Unsubstantiated transactions are reclassified to the
cardholder's payroll advance receivable until substantiated.

Reconciliation of card transactions to {{PLATFORM_FISCAL_HOST}} is an area of
known operational friction where the Mercury-{{PLATFORM_FISCAL_HOST}} sync does
not carry credit-card transactions automatically; manual CSV uploads and
a longer-term platform review (including evaluation of an integrated
per-collective card model) are captured in the DFO's operational
roadmap.

**Expense Reimbursements**

Employees and contractors incurring reimbursable expenses submit an
expense report with receipts within {{WINDOW_REIMBURSEMENT}} of the expense. The DFO
reviews for policy compliance, budget availability, and adequate
documentation before approval. Reimbursements are paid on the next
scheduled payables run and are treated as accountable-plan
reimbursements for tax purposes.

**Expense Allocations**

Shared administrative and infrastructure costs are allocated to program,
fundraising, and general-and-administrative functions on a rational and
consistent basis. Allocation methodology is proposed by the DFO,
reviewed by the Finance Committee, and approved by the Board. Routine
updates to allocation ratios (for example, a change in a staff member's
program mix) are documented by the DFO without Board approval.

**Typical allocation bases**

-   Occupancy costs: allocated by full-time-equivalent (FTE) ratio since
    {{ORG_NAME}} does not maintain program-specific space.

-   Administrative salaries: allocated by documented FTE ratio or
    documented percentage of effort.

-   Software and IT: allocated by FTE ratio or, where usage is
    user-specific, by seat count.

-   Insurance: allocated by FTE ratio.

-   External accounting and audit fees: allocated by FTE ratio, with the
    fiscal-sponsorship-attributable portion supported by administrative
    fee revenue.

Allocation journal entries are prepared and posted by the external
accountant monthly, and reviewed by the DFO. Any significant change in
methodology is reviewed by the Finance Committee and approved by the
Board.

**Asset Management**

**Cash Management and Investments**

{{ORG_NAME}} manages its cash and investment assets to support its mission,
preserve capital, and provide sufficient liquidity to meet operational
and grantee-payment needs. This policy applies to operating cash,
board-designated reserves, and any investment assets.

**Investment objectives, in order of priority**

-   **Safety:** Preservation of principal, particularly for operating
    cash and reserve balances.

-   **Liquidity:** A sufficient portion of assets held in instruments
    convertible to cash within one to {{WINDOW_CRYPTO_CONVERSION}} to meet
    operating needs and grantee payments.

-   **Yield:** A reasonable return net of fees and inflation, consistent
    with the safety and liquidity objectives.

**Roles**

-   Board of Directors: approves this policy and reviews performance at
    least annually.

-   Finance Committee: oversees implementation, monitors performance,
    and recommends changes to the Board.

-   ED: manages day-to-day treasury within this policy, selects and
    terminates financial-institution relationships within Board-approved
    parameters, and reports to the Finance Committee quarterly.

-   DFO: executes treasury operations, maintains counterparty
    documentation, and prepares treasury reports.

**Permitted holdings**

-   U.S. Treasury bills, notes, and bonds; U.S. agency securities.

-   Money market funds invested exclusively in U.S. government
    securities or investment-grade instruments.

-   FDIC-insured deposit accounts and Certificates of Deposit at
    chartered U.S. banks.

-   Investment-grade corporate bonds (rated BBB- or higher by a
    nationally recognized statistical rating organization).

-   Publicly traded U.S. equity securities and Exchange-Traded Funds
    (ETFs), only when explicitly authorized by the Board as part of a
    reserve investment strategy.

-   USD-denominated stablecoins issued by U.S.-regulated issuers, held
    for operational cryptocurrency payment purposes, subject to the
    concentration and counterparty limits in the Digital Asset Policy.

**Prohibited holdings**

-   Options, futures, short positions, or other derivative instruments
    held for speculation.

-   Direct real estate, private equity, and commodity holdings.

-   Individual equity or fixed-income positions in issuers materially
    misaligned with {{ORG_NAME}}'s mission.

-   Cryptocurrencies held for speculative purposes. Cryptocurrencies
    held as a result of contributions or programmatic activity are
    governed by the Digital Asset Policy.

The DFO provides an annual treasury and investment summary to the
Finance Committee. This policy is reviewed annually by the Finance
Committee and re-approved by the Board at least every two years.

**Digital Asset Policy (Cryptocurrency Operations)**

{{ORG_NAME}} holds and transacts in cryptocurrency as part of its
programmatic and treasury operations. This policy governs custody, key
management, transaction approval, contribution acceptance, valuation,
sanctions screening, and reconciliation for all digital assets held by
{{ORG_NAME}}, whether directly in {{ORG_NAME}}'s operations or in restricted
funds held for fiscally sponsored projects.

**Scope and definitions**

-   Digital assets subject to this policy include (a) cryptocurrencies
    such as ETH, BTC, and other layer-1 or layer-2 native tokens; (b)
    fiat-referenced stablecoins such as USDC, USDT, and DAI; and (c)
    other blockchain-native tokens received as contributions or in the
    ordinary course of programmatic activity.

-   Custodial digital assets are those held by a regulated custodian
    (currently {{PLATFORM_CRYPTO_CUSTODIAN}}). Self-custody digital assets are those
    held on {{ORG_NAME}}-controlled wallets, including multi-signature
    wallets and, where applicable, project-designated wallets.

**Approved custody arrangements**

-   {{PLATFORM_CRYPTO_CUSTODIAN}} is the approved primary custodian for cryptocurrency
    treasury balances not held for immediate operational use.

-   Self-custody wallets are limited to multi-signature wallets (Safe /
    Gnosis Safe or equivalent) with signer configurations approved by
    the DFO and, for wallets holding balances above the multisig
    threshold below, the ED.

-   Non-multisig or hot wallets are permitted only for operational
    balances below \{{THRESHOLD_DFO_REVIEW}} USD-equivalent, and only for a documented
    operational purpose (e.g., gas payments, small-payee disbursement
    wallets).

-   The DFO maintains a wallet registry that lists every
    {{ORG_NAME}}-controlled address, its chain, its purpose, its signer set
    (for multisig), its approval threshold, and the identifier of any
    associated fiscally sponsored project.

**Key management**

-   Signer roles on multi-signature wallets are held by named
    individuals in specified organizational roles. Signer eligibility,
    addition, and removal are approved by the ED, documented in the
    wallet registry, and reflected on-chain within {{WINDOW_CRYPTO_CONVERSION}} of
    the change.

-   Private keys corresponding to signer roles are held on hardware
    security devices (hardware wallets) or comparably secured
    infrastructure. Seed phrases are stored in a manner that requires at
    least two independent actions to recover, and are never stored in
    plain text on a network-connected device.

-   A signer offboarding checklist requires (i) verification that the
    offboarded signer is removed from every applicable multisig, (ii)
    confirmation that the offboarded signer no longer holds any hardware
    device or seed material with {{ORG_NAME}} key access, and (iii) an
    updated wallet registry entry within {{WINDOW_CRYPTO_CONVERSION}} of
    separation.

-   For any wallet with a USD-equivalent balance above $50,000, the
    multisig configuration must require at least a 2-of-3 approval, and
    the signer set must include at least one {{ORG_NAME}} signer who is not
    the DFO.

**\[Confirm: The specific signer set for each production multisig,
once staffed. the DFO to draft the wallet registry as a companion
document.\]**

**Transaction authorization**

-   On-chain transactions follow the same dollar-value approval
    thresholds as fiat transactions: DFO up to \{{THRESHOLD_DFO_REVIEW}}, ED up to
    \{{THRESHOLD_BOARD_SECONDARY}}, ED plus Board President or Treasurer up to \{{THRESHOLD_BOARD_EXCEPTION}}, and
    Board approval above \{{THRESHOLD_BOARD_EXCEPTION}}. USD-equivalent value is measured at
    the time of transaction using a documented reference source
    ({{PLATFORM_CRYPTO_CUSTODIAN}} quote or, for stablecoins, par).

-   Every outbound wallet address (including exchange deposit addresses)
    must be recorded in a whitelist maintained by the DFO. Addresses are
    added to the whitelist only after (a) OFAC and sanctions
    screening, (b) high-risk-cluster screening through a chain-analysis
    provider for any outbound transfer with a USD-equivalent value above
    \{{THRESHOLD_DFO_REVIEW}}, and (c) verification with the counterparty of the address
    through a channel independent of the address disclosure.

-   Test transactions in a small notional amount are required for any
    first-time outbound transfer to a new address of \{{THRESHOLD_DFO_REVIEW}} or more
    USD-equivalent, before releasing the full amount.

-   Multi-signature approval on any outbound transaction is executed by
    signers who did not initiate the transaction. Self-approval by the
    transaction initiator is prohibited.

**Acceptance of cryptocurrency contributions**

-   {{ORG_NAME}} accepts cryptocurrency contributions in supported assets.
    The list of supported assets is maintained by the DFO and approved
    by the ED. Contributions in unsupported assets are accepted on a
    case-by-case basis with ED approval.

-   The DFO screens the contributing wallet against OFAC and sanctions
    lists prior to accepting the contribution. Contributions from
    screened-negative sources are refused or, where already received,
    escalated to legal counsel and, if required, reported.

-   Contributions are recorded at fair market value on the date
    received. Fair market value is determined by reference to the
    primary market for the asset ({{PLATFORM_CRYPTO_CUSTODIAN}} spot for supported
    assets; for less-liquid assets, a documented reference price and
    methodology). The USD-equivalent value is the amount recognized as
    contribution revenue.

-   The default disposition of non-stablecoin cryptocurrency
    contributions is prompt liquidation to USD (or to a supported
    stablecoin as an interim step) through {{PLATFORM_CRYPTO_CUSTODIAN}}, unless the
    ED, with input from the DFO, determines that a specific contribution
    should be held for a documented programmatic purpose. Any hold
    decision is documented and reviewed by the Finance Committee at its
    next meeting.

-   For non-cash cryptocurrency contributions with a claimed fair market
    value greater than \{{THRESHOLD_CAPITALIZATION}}, {{ORG_NAME}} signs Form 8283 as the donee
    upon donor request. If {{ORG_NAME}} disposes of a contributed asset
    within three years and the amount is above the reporting threshold,
    {{ORG_NAME}} files Form 8282.

**Stablecoin operations**

-   USDC and other fully-reserved, U.S.-regulated stablecoins may be
    held as cash equivalents for programmatic and payment-rail purposes.
    Concentration in any single stablecoin issuer above $250,000
    requires ED approval and documented consideration of issuer
    counterparty risk.

-   Because Mercury does not accept direct USDC deposits, the standard
    flow for on-chain USD-equivalent revenue is: incoming to {{ORG_NAME}}
    Safe, transfer to {{PLATFORM_CRYPTO_CUSTODIAN}}, conversion to USD, and ACH or wire
    to Mercury. The DFO documents this flow at each occurrence and
    reconciles the timing and price differences.

-   Stablecoin holdings are revalued at each period-end at par unless a
    material depegging or credit event indicates otherwise.

**Revaluation, gain/loss recognition, and reconciliation**

-   Non-stablecoin digital-asset holdings are revalued at each
    month-end. Unrealized gains and losses are recorded in accordance
    with the applicable GAAP guidance (FASB ASU 2023-08 for entities
    within its scope). Realized gains and losses on disposition are
    recognized in the period of disposition.

-   The DFO reconciles on-chain balances (custodial and self-custody) to
    the {{PLATFORM_CRYPTO_SUB}} subledger and to the {{PLATFORM_GL}} general ledger monthly.
    Discrepancies above 1% of the wallet balance or \{{THRESHOLD_LINE_ITEM_REVIEW}}, whichever is
    lower, are investigated and resolved before the close is finalized.

**Reporting**

-   A wallet-and-custody inventory is included in the quarterly report
    to the Finance Committee, showing the balance of each
    {{ORG_NAME}}-controlled wallet or custodial account, its purpose, and its
    associated project (if any).

-   A summary of digital-asset contributions received, digital-asset
    expenses paid, and material gains and losses is included in the
    annual report to the Board.

**Fiscally sponsored projects with on-chain balances**

-   Sponsored projects that hold or transact in digital assets do so
    through {{ORG_NAME}}-controlled wallets specifically designated to the
    project. Sponsored-project wallets are subject to this Digital Asset
    Policy in full.

-   Project-designated wallet balances are tracked in the project's
    {{PLATFORM_FISCAL_HOST}} ledger and reconciled monthly. Project leads may not
    directly execute on-chain transactions from {{ORG_NAME}}-controlled
    wallets; execution follows the multi-signature approval process
    above.

**Non-Cash Donations Other Than Cryptocurrency**

{{ORG_NAME}} may accept non-cash donations of publicly traded securities,
tangible property, or in-kind services where consistent with mission and
free of material restrictions or liabilities. Publicly traded securities
are ordinarily liquidated promptly upon receipt. In-kind service
contributions are recorded at fair value when the services meet the
recognition criteria under FASB ASC 958. Form 8283 is signed for
qualifying non-cash contributions.

**Capital Equipment**

{{ORG_NAME}} capitalizes tangible property with a useful life greater than
one year and an acquisition cost of \{{THRESHOLD_CAPITALIZATION}} or more. Purchases of
capital equipment require the same approvals as any other expenditure at
the same dollar threshold. Because {{ORG_NAME}} currently operates without a
central office and holds minimal tangible property, no depreciation
schedule is currently maintained; if material capital assets are
acquired, the DFO will establish a fixed-asset register and depreciation
policy at that time.

**Operating Reserve**

{{ORG_NAME}} maintains a Board-designated operating reserve to provide
financial resilience against cash-flow fluctuations, unforeseen
expenses, and temporary revenue shortfalls. The reserve is unrestricted
net assets that the Board has designated for this purpose, and it is
reported as Board-designated within unrestricted net assets on the
Statement of Financial Position.

**Target level:** A minimum of six months and a target of twelve months
of unrestricted operating expenditures. Operating expenditures for this
purpose include recurring compensation, contractor payments, program
expenses, and ongoing professional services, but exclude depreciation,
in-kind expenses, and other non-cash items. The target is reviewed and
reaffirmed annually as part of the budget process.

**Building the reserve:** Until the target level is reached, the Board
prioritizes reserve building. Funding sources include Board-designated
portions of annual operating surpluses, one-time unrestricted revenue
events (large bequests, unrestricted major gifts, legal settlements),
and investment returns specifically allocated by the Board.

**Use of the reserve:** Draws from the reserve require formal Board
approval and a simultaneously approved written replenishment plan with a
source and a timeline not to exceed 24 months to restore the reserve.
Approved uses include: (i) temporary revenue shortfalls not reflective
of structural deficit, (ii) unforeseen non-recurring expenditures not in
the budget, and (iii) time-limited strategic opportunities with a clear
long-term return to mission.

**Investment of reserve balances:** Reserve funds are held in highly
liquid, low-risk instruments: FDIC-insured deposits, U.S. government
money market funds, or short-term U.S. Treasury instruments. Reserve
balances are monitored quarterly by the ED and DFO and reported to the
Finance Committee.

**Annex A: Fiscal Sponsorship**

**Program overview**

{{ORG_NAME}}'s fiscal sponsorship program supports research and open-source
initiatives advancing digital governance, civic technology, and
democratic innovation. Sponsored projects operate as programs of {{ORG_NAME}}
and are administered on the {{PLATFORM_FISCAL_HOST}}, with {{ORG_NAME}}
serving as the fiscal host. Sponsored-project funds are restricted for
the project's charitable purpose but are legally {{ORG_NAME}}'s assets.
{{ORG_NAME}} exercises variance power over sponsored-project funds and, in
accordance with sponsorship agreements, may redirect funds to consistent
charitable purposes if a project cannot fulfill its purpose.

**Onboarding**

-   Project inquiry: intake form completed by the project lead,
    including mission summary, alignment with {{ORG_NAME}}'s charitable
    purpose, projected budget, funding pipeline, jurisdiction of the
    project lead, and disclosure of any wallets used by the project.

-   Due diligence: DFO or delegate reviews for mission alignment,
    feasibility, sanctions and integrity screening on project leads and
    known funders, and material risk.

-   Approval: ED approves inclusion; sponsorship agreement is executed
    between {{ORG_NAME}} and the project lead(s).

-   Setup: {{PLATFORM_FISCAL_HOST}} collective is provisioned; a
    project-designated wallet is established if the project transacts
    on-chain; the project is added to the wallet registry, the vendor
    and contractor master data as applicable, and the DFO's
    fiscal-sponsorship portfolio tracker.

**Ongoing administration**

-   Restricted-fund tracking: each project's revenue and expense flows
    through a distinct class in {{PLATFORM_GL}} (via {{PLATFORM_FISCAL_HOST}}'s class
    mapping) so that restricted balances can be reported at any time.

-   Expense approval: project-level expenses are proposed by project
    leads, reviewed for policy compliance and available restricted
    balance by the DFO or a delegated project reviewer, and paid on the
    applicable rail ({{PLATFORM_FISCAL_HOST}}, Wise, or crypto).

-   Administrative fee: {{ORG_NAME}} retains an administrative fee on
    incoming revenue as specified in each fiscal sponsorship agreement.
    Administrative fee revenue supports {{ORG_NAME}}'s general operations
    and the fiscal-sponsorship operational function.

-   Reporting to projects: {{PLATFORM_FISCAL_HOST}} provides near-real-time
    visibility to project leads; the DFO issues a project-level
    statement at least annually.

**Compliance**

-   Grantee compliance: sub-grants issued by a sponsored project are
    subject to {{ORG_NAME}}'s grant-agreement template, expenditure
    responsibility documentation where the sub-grantee is not a U.S.
    public charity, and OFAC screening.

-   Sanctions screening: applies to project leads, funders,
    sub-grantees, and outbound wallet addresses.

-   Change of control: material changes in project leadership are
    reported to the DFO and reflected in {{PLATFORM_FISCAL_HOST}} and {{ORG_NAME}}'s
    records within 10 business days.

**Offboarding, transfer, and termination**

-   Transfer to another 501(c)(3): a project may transfer to another
    qualified fiscal sponsor or independent 501(c)(3) with ED approval
    and full documentation of the transferred restricted balance and any
    liabilities.

-   Termination: if a project cannot fulfill its purpose or materially
    breaches its sponsorship agreement, the ED and DFO exercise
    {{ORG_NAME}}'s variance power to redirect restricted funds to a
    consistent charitable purpose, documented and reported to the Board.

-   Wallet closure: project-designated wallets are drained to {{ORG_NAME}}'s
    operating wallet or custodian, and the wallet registry is updated
    within {{WINDOW_CRYPTO_CONVERSION}} of the offboarding effective date.

**Annex B: Policy Administration**

**Review and amendment**

The DOF and ED review this manual annually. The Board re-approves the
manual at least every two years and whenever a material amendment is
made. The DFO maintains the current version and the version history, and
files the current version in {{ORG_NAME}}'s electronic archive.

**Exceptions**

Deviations from this manual are permitted only where the ED and DFO
jointly determine that a deviation is in the organization's interest
and where the deviation does not violate law, contract, or the
Board-approved budget. Any material or recurring deviation is reported
to the Finance Committee at its next meeting and considered for
permanent incorporation into the manual.

**Definitions**

-   **Board:** The Board of Directors of {{ORG_LEGAL_NAME}}

-   **ED:** Executive Director

-   **DFO:** Director of Finance and Operations

-   **External Accountant:** {{ORG_NAME}}'s external accounting firm
    including named engagement lead.

-   **Covered Person:** A director, officer, employee, or contractor
    with material financial authority; a member of a standing financial
    committee; and their Related Parties.

-   **Covered Transaction:** Any transaction between {{ORG_NAME}} and a
    Covered Person or Related Party.

-   **Digital Asset:** Cryptocurrencies, stablecoins, and other
    blockchain-native tokens.

-   **Multi-Signature Wallet:** A {{ORG_NAME}}-owned wallet controlled
    through multi-signature approval, typically implemented as a Safe
    (Gnosis Safe) or equivalent.

**Adoption**

This Manual is adopted by resolution of the Board of Directors of
{{ORG_LEGAL_NAME}} The undersigned officers certify that this Manual reflects
the fiscal policies and procedures approved by the Board.

_______________________________________
_______________

**Board President** Date

_______________________________________
_______________

**Treasurer** Date

_______________________________________
_______________

**Executive Director** Date


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
