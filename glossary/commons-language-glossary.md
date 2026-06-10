# Commons Language Glossary
## A Cross-Walk of Commons, Polycentric Governance, and OSS Vocabulary into FinOps Translation and Practice

**By Andrew Ngeseyan · ASN Management LLC · Finance and Operations Director, Metagov**

---

## Section 1: How to Use This Glossary

This is a bilingual document. One side speaks the language of commons governance theory: Elinor Ostrom, institutional analysis, polycentric design, resource stewardship, collective action. The other side speaks the language of nonprofit financial operations: general ledgers, restricted net assets, audit thresholds, chart of accounts, treasury posture.

Most people working in the OSS funding world speak one of these languages fluently and the other haltingly, or not at all. Funders and foundation program officers understand grant compliance and restricted funds but have not read Ostrom. Governance researchers understand institutional design and polycentric theory but do not know what a statement of activity is or why total cash misleads. Fiscal sponsor executives stand in the middle trying to translate in real time for both audiences.

This glossary exists to make that translation faster and more precise.

**Source disciplines.** The commons-side vocabulary draws on Elinor Ostrom's Governing the Commons (1990), the Institutional Analysis and Development (IAD) framework she developed with colleagues at Indiana University's Workshop in Political Theory and Policy Analysis, and forty years of empirical research on how resource-sharing communities sustain themselves across fisheries, forests, irrigation systems, and digital infrastructure. The OSS funding vocabulary draws on practice: what fiscal sponsors actually do, what funders actually ask for, what auditors actually examine.

**The proof point.** Metagov Inc. is the operating example throughout this glossary. Metagov is a 501(c)(3) fiscal sponsor for digital governance research, with EisnerAmper as its CPA and One Project as its anchor funder at $150K per year through 2028. In its first full operating year, Metagov channeled more than $2 million in fiscal sponsorship funding, set the operational foundation for its first independent audit, published its first written onboarding manual, and closed the Atlas Computing to Renaissance Philanthropy project transfer. Five sponsored projects are in active development across a budget range from under $10,000 to $200,000. Metagov is not a hypothetical. It is the laboratory in which these translations are being tested in real time.

---

## Section 2: Core Theory Terms

### **Commons / Common-Pool Resource**

**Commons meaning.** A commons is a resource managed collectively by a community of users, governed by rules those users have developed together rather than by private ownership or state administration. A common-pool resource (CPR) is a resource that is non-excludable (it is difficult or costly to prevent others from using it) and rivalrous (one person's use can subtract from another's). Classic examples: fisheries, groundwater basins, shared pastures, irrigation systems. Digital examples: open source libraries, open datasets, shared research infrastructure, the internet routing tables.

**FinOps translation.** In fiscal sponsorship terms, the commons is the shared institutional infrastructure the fiscal sponsor provides: the tax exemption, the audit history, the compliance machinery, the banking relationships, the general ledger architecture. Every sponsored project benefits from this infrastructure. None of them built it alone. The fiscal sponsor is the institutional commons holder.

**Practical example.** NumFOCUS holds the commons for the scientific Python ecosystem. NumPy, SciPy, matplotlib, pandas, Jupyter, and dozens of others share NumFOCUS's 501(c)(3) status, its grant administration capacity, and its legal and operational services ([NumFOCUS Sponsored Projects](https://numfocus.org/sponsored-projects)). No individual project could afford to build and maintain that infrastructure independently. The shared infrastructure is the commons.

---

### **Polycentricity / Polycentric Governance**

**Commons meaning.** Polycentricity, as developed by Vincent and Elinor Ostrom drawing on Michael Polanyi's earlier work, describes a governance system with many decision-making centers operating independently but under an overarching rule system. In contrast to monocentrism (one center, typically the state or a single firm), polycentric systems allow each center to make rules adapted to local conditions while coordinating through shared protocols. Neither pure market nor pure hierarchy, polycentrism is the third institutional form.

**FinOps translation.** A polycentric funding architecture is one in which multiple fiscal sponsors, domain cores, and satellite projects each make decisions appropriate to their scale and context, while sharing common reporting standards, audit norms, and governance protocols. No single entity controls all funding decisions. The fiscal sponsor is one center; the funder is another; the project itself is a third. The question for the FinOps function is: what rules govern the interfaces between these centers?

**Practical example.** The OSS funding world is already polycentric in practice: NumFOCUS, the Linux Foundation, the Software Freedom Conservancy, Open Collective, the Freedom of the Press Foundation, and Metagov each serve distinct project communities with different governance models. The problem is that these centers currently lack shared protocol standards for restricted fund accounting, audit requirements, and funder reporting. Commons FinOps is the name for the discipline of designing and operating those shared standards.

---

### **Polycentric Models (the Architecture)**

**Commons meaning.** A polycentric model describes the actual institutional structure: many centers of decision-making, each with its own legitimate authority, coordinated by overarching rules rather than central command. In OSS funding, the core-and-satellite model proposed for sustainable OSS funding is a polycentric architecture. Domain cores (Cryptography, Bioconductor, Astronomy, Climate, SciPy stack, Privacy Tech, Civic Tech) each act as a center of governance for their satellite projects. A coordinating layer sits above the cores, setting interoperability standards and shared protocol requirements.

**FinOps translation.** Each polycentric layer requires its own financial books and its own monitoring function. Cross-layer transactions (satellite to core, core to coordinating body) require defined accounting treatment. The FinOps requirement of a polycentric model is not optional overhead; it is the operational cost of sustaining the architecture.

**Practical example.** Metagov itself is a polycentric system in development. Five sponsored projects sit inside Metagov. Metagov sits inside a wider ecosystem including One Project (anchor funder), EisnerAmper (CPA), and the emerging BLOOM^n / win^n institutional design that Liz Barry is developing as a potential coordinating layer above the fiscal sponsor level.

---

### **IAD Framework (Institutional Analysis and Development)**

**Commons meaning.** The IAD framework, developed by Elinor Ostrom, Vincent Ostrom, and colleagues at Indiana University, is an analytical tool for understanding how institutions shape individual behavior and collective outcomes around shared resources. The framework identifies three nested levels of rules:

- **Constitutional level:** rules about who can make rules (who has standing, what processes are legitimate for changing the governance structure itself)
- **Collective-choice level:** rules made by authorized participants about how the operational rules should work (policy-making, governance design, sanctioning schedules)
- **Operational level:** rules that directly govern day-to-day resource use (who can access what, when, under what conditions, with what reporting obligations)

**FinOps translation.** Every fiscal sponsor is running an IAD structure whether it knows it or not:

- Constitutional level in FinOps: the bylaws, the board composition rules, the audit firm selection process, the fiscal sponsorship policy adoption procedure. These determine who can change the rules.
- Collective-choice level in FinOps: the fiscal sponsorship agreement template, the intake policy, the graduated sanctions schedule, the conflict resolution procedure. These are the rules that authorized participants (board, staff, legal counsel) set to govern operations.
- Operational level in FinOps: the chart of accounts, the monthly reconciliation cadence, the per-project statement of activity process, the restricted fund release procedure. These are the rules the bookkeeper executes every week.

Confusing these levels is a common failure mode. The operational level cannot fix a constitutional-level problem (a board that cannot make decisions). The collective-choice level cannot fix an operational-level failure (a chart of accounts that does not distinguish restricted from unrestricted funds). Diagnosis requires naming which level the problem is at.

**Practical example.** When Metagov adopted its written fiscal sponsorship intake policy in 2025/2026, requiring project leads to be personally known to Research Directors, that was a collective-choice level action. It changed how the operational level would function going forward. The board ratification of that policy was the constitutional-level step that gave it authority.

---

### **Ostrom's 8 Design Principles (with FinOps requirement for each)**

Ostrom identified eight design principles that characterize commons institutions that endure across decades and generations of use. Each is a governance condition. Read from the operator's seat, each is also an operational requirement.

**1. Clearly defined boundaries.** Who is in the commons and who is out must be determinable. FinOps requirement: a written satellite intake and exit policy with specific triggering criteria, executed agreements, and defined moments of recognition and termination.

**2. Congruence between rules and local conditions.** Rules must fit the actual scale and cadence of the resource and community. FinOps requirement: a layered chart of accounts that separates regulatory-floor rules (non-negotiable, set by IRS and state law) from sponsorship-choice rules (adaptable to each project's actual work pattern).

**3. Collective choice arrangements.** Most people affected by the rules can participate in modifying them. FinOps requirement: a standing policy review process with documented channels for sponsored projects to propose rule changes and a defined response obligation for the core.

**4. Monitoring.** Monitors accountable to resource users observe behavior and resource conditions. FinOps requirement: a monitoring cadence (monthly per-project statements, quarterly reviews, annual audit) designed as a service to satellites, not a control over them; monitors and monitored look at the same numbers.

**5. Graduated sanctions.** Sanctions for violations increase with severity and repetition. FinOps requirement: a written graduated sanctions schedule adopted before the first sanction is ever needed; the schedule is an audit readiness artifact as much as a fairness mechanism.

**6. Conflict resolution mechanisms.** Low-cost arenas exist for resolving disputes between users and between users and officials. FinOps requirement: a named conflict resolution path (designated mediator, peer review panel, or escalation protocol) cheap enough that satellites will actually invoke it rather than suppressing disputes.

**7. Minimal recognition of rights to organize.** External governmental authorities do not challenge the right of users to devise their own institutions. FinOps requirement: the operational maturity of the core (clean audits, documented policies, governance records) is what gives it standing to push back on funder overreach and platform overreach; without credible books, there is no leverage.

**8. Nested enterprises.** For larger systems, governance activities are organized in multiple layers of nested enterprises. FinOps requirement: each nested layer needs its own financial books and monitoring function; cross-layer transactions require defined accounting treatment; the cost of this operational overhead must be explicitly funded.

---

### **Nested Enterprises**

**Commons meaning.** For commons that operate at scale, governance is organized in layers. A small group manages local operations. A group of local groups manages regional coordination. A regional body participates in system-wide rule-making. Each layer has authority appropriate to its scope, and decisions are made at the lowest level capable of making them well (see: subsidiarity). This is the architectural principle underlying federalism, the European Union, and most durable large-scale commons.

**FinOps translation.** Nested enterprises generate specific accounting requirements: each layer needs its own chart-of-accounts dimension (class, fund, or project code), transactions between layers need defined accounting treatment (intercompany eliminations in consolidated statements, transfer pricing protocols, clear restricted fund release rules), and reporting must flow up cleanly from the deepest layer to the consolidated filing.

**Practical example.** Metagov's own nesting illustrates the architecture. Layer one: individual sponsored projects (The Wind Down, Relational Design Lab, Open Machine, NELA Computer Club, Civic AI Tools), each with its own class in the QuickBooks general ledger, its own restricted fund balance, and its own per-project statement of activity. Layer two: Metagov Inc. itself, the fiscal sponsor, which consolidates all project activity into a single Form 990 and, once the first independent audit is complete, a single audited annual statement. Layer three: the wider ecosystem of funders (One Project, anonymous digital identity funder, Toda Foundation), peer fiscal sponsors, and the emerging BLOOM^n coordination layer. The FinOps function at Metagov manages the layer-one/layer-two interface operationally every day. The layer-two/layer-three interface is managed through funder reporting, grant agreements, and the audit.

---

### **Subsidiarity**

**Commons meaning.** Decisions should be made at the lowest level of governance capable of making them well. Higher-level bodies handle only what lower-level bodies cannot. The principle originated in Catholic social teaching and was operationalized by Ostrom and others in commons governance design.

**FinOps translation.** In fiscal sponsorship, subsidiarity means that projects manage their own spending decisions within their restricted fund balance (operational level), the fiscal sponsor sets the rules those decisions must follow (collective-choice level), and the board governs the overall institutional structure (constitutional level). Violating subsidiarity downward (the sponsor micromanages every project transaction) produces attrition. Violating it upward (projects make commitments without sponsor awareness) produces audit findings.

**Practical example.** Metagov's current practice: project leads see their own per-project statement of activity and make spending decisions within their restricted fund balance. Andrew reviews the ledger entries for coding accuracy and policy compliance. The board sets the overall fiscal sponsorship policy. Three levels, three distinct roles.

---

### **Boundary Rule / Clearly Defined Boundaries**

**Commons meaning.** The first of Ostrom's eight design principles. Membership in the commons must be determinable. If no one can tell who is in and who is out, free-riding is unlimited and the resource degrades.

**FinOps translation.** At a fiscal sponsor, boundary rules determine when a project's cash is the sponsor's legal responsibility and when it is not. This has direct implications for the Form 990, the audit scope, and funder reporting. A fuzzy boundary is an audit finding waiting to happen.

**Practical example.** Metagov's current boundary rule: "Only accepting project leads personally known to our Research Directors." This is written, not informal. Once Metagov accepts a project into intake, that project's cash lands on Metagov's balance sheet as a restricted net asset and appears in the consolidated audit. Open Machine's $200,000 deposit becomes Metagov's legal responsibility the moment the intake agreement is signed. The boundary rule determines exactly when that obligation begins.

---

### **Monitoring**

**Commons meaning.** Ostrom's fourth design principle. Effective commons require monitors who are accountable to resource users (or who are users themselves) and who actively observe resource conditions and participant behavior. External monitoring imposed without legitimacy fails.

**FinOps translation.** Monitoring is what FinOps does for a living. Monthly reconciliations, period-end close, restricted fund tracking, variance analysis, annual audit: these are all monitoring activities. The FinOps insight that extends Ostrom: monitoring must be designed as a service to satellites, not a control over them. The monitor and the monitored should see the same numbers.

**Practical example.** At Metagov, project leads receive per-project statements of activity directly from the general ledger, cut by class. They see the same data Andrew sees. This is the legitimacy move: monitoring is transparent and bilateral, not asymmetric and unilateral. The AWS gift episode illustrates what monitoring catches: the Open Collective platform showed three entries that looked like $225,000 in receipts; the general ledger showed only $75,000 had actually arrived (two entries were internal Mercury-to-platform reconciliation postings). Monitoring resolved the discrepancy before it reached the funder.

---

### **Graduated Sanctions**

**Commons meaning.** Ostrom's fifth design principle. Violations are punished with responses scaled to severity and repetition. First offenses receive mild responses. Repeated or egregious violations escalate. Binary punishment (compliant or expelled) destroys community trust and incentivizes hiding problems.

**FinOps translation.** A graduated sanctions framework, written before the first sanction is needed, is both a fairness mechanism and an audit readiness mechanism. Audit firms have standard questions about how findings are raised, escalated, and resolved, and Metagov's CPA at EisnerAmper has been preparing the books for that scrutiny. "We handle it case by case" fails that test. "Here is the schedule, here is the log" passes.

**Practical example.** A workable graduated schedule for a fiscal sponsor: missed reporting deadline, first instance: written reminder. Third missed deadline in twelve months: mandatory review meeting with written corrective plan. Modest misuse of restricted funds, self-reported: course correction, no public sanction. Material misuse discovered through audit: formal review, possible funder notification, possible termination. Pattern of misuse: termination, funder notification, recovery action.

---

### **Collective Choice Arrangements**

**Commons meaning.** Ostrom's third design principle. The people most affected by the operational rules have a real voice in modifying them. Rule-making is not purely top-down. Participation in rule revision is what produces compliance that is genuine rather than theater.

**FinOps translation.** The fiscal sponsorship agreement is not just a document; it is the protocol for ongoing negotiation. Collective choice, operationally, means: channels exist for sponsored projects to flag friction with policies, a regular policy review cadence creates structure for that feedback, and the sponsor has a defined obligation to respond. At small scale, this happens in standing relationships. At scale, it requires explicit mechanisms before standing relationships fail.

**Practical example.** Metagov's current intake policy was shaped by lessons from operating Atlas Computing, the Grant Innovation Lab, and Public AI as sponsored projects. The Atlas transfer to Renaissance Philanthropy taught specific lessons about transfer agreement language, entity naming conventions, and blank signatory lines. Those lessons went directly into the next version of the intake template. The satellites effectively wrote the policy by living it. That is collective choice in practice.

---

### **Conflict Resolution**

**Commons meaning.** Ostrom's sixth design principle. Low-cost, accessible arenas for resolving disputes among users, or between users and officials, must exist. Without accessible dispute resolution, conflicts either accumulate as silent resentment or escalate externally and become expensive and relationship-destroying.

**FinOps translation.** The FinOps function is frequently the first place a conflict surfaces: "You charged this to the wrong project class." "That grant was not restricted to this purpose." "The platform shows a different number than the ledger." These conflicts need fast, cheap resolution paths. Outside counsel (Karl Mill at Mill Law Center in Metagov's case) is the right tool for complex transfers and agreement disputes, not for day-to-day accounting disagreements. Build the cheap path first.

**Practical example.** Metagov used outside counsel for the Atlas to Renaissance Philanthropy transfer specifically because the executed document had entity naming inconsistencies and a blank signatory line: legitimately counsel-level issues. But the operational lesson was to build better intake standards so those issues never arise in the first place. Prevention is cheaper than resolution.

---

### **Minimal Recognition of Rights to Organize**

**Commons meaning.** Ostrom's seventh design principle. External governmental authorities do not challenge the right of commons users to organize and devise their own institutional rules. This condition is mostly outside the commons participants' control; it is a background condition the political environment either provides or does not.

**FinOps translation.** In the OSS funding context, this principle extends to funder behavior. Funders who dictate not just spending restrictions but also governance structure, board composition, or audit firm choice are violating the spirit of this principle. The FinOps counter to funder overreach is operational maturity: clean audits, documented policies, governance records, and a credible system of record give the core legitimate standing to negotiate funder terms as a peer rather than as a supplicant. Without books a funder respects, there is no leverage.

**Practical example.** Metagov's 2026 operational security concern illustrates a modern variant: Liz Barry was warned that organizing on third-party platforms (Slack, Google) creates latent legal disclosure risks if those platforms receive investigation subpoenas. The response under consideration is self-hosted communication and knowledge management infrastructure, potentially as the core of a paid membership program. Platform choice is an expression of the right to organize.

---

## Section 3: OSS Funding Vocabulary

### **Core (in the Core-and-Satellite Model)**

A domain core is the anchor fiscal sponsor or governance body for a cluster of related OSS projects within a shared scientific or technical domain. The core holds the domain's shared institutional infrastructure: the audit history, the compliance capacity, the funder relationships, the community governance protocols. The core is distinguished from individual projects by its durability: it is designed to outlast any individual project and to serve the community after specific projects graduate, sunset, or transform. In FinOps terms, the core runs its own general ledger, maintains its own audit history, and manages its own funder relationships, while also holding restricted funds on behalf of satellites.

---

### **Satellite (in the Core-and-Satellite Model)**

A satellite is an individual project that operates under the institutional umbrella of a domain core. The satellite has mission autonomy (it makes its own technical and programmatic decisions) but financial and legal dependence (its funds are held and reported by the core, its legal exposure is covered by the core's tax exemption, and it operates under the core's compliance framework). In FinOps terms, each satellite maps to a separate class or fund dimension in the core's general ledger, allowing per-project statement of activity without maintaining separate books.

---

### **Domain**

A domain is a scientific or technical community organized around a shared set of tools, methods, or research questions. The "domain core" concept organizes fiscal sponsorship and OSS funding around these natural communities rather than around legal form or organizational history. The domains illustrated in the core-and-satellite OSS funding diagram include: Cryptography, Bioconductor (bioinformatics), AstroPy/Astronomy, Privacy Tech, Civic Tech, Climate, and the SciPy stack (scientific Python computing). Each domain has its own community norms, funding cycles, governance cultures, and FinOps shapes.

---

### **Fiscal Sponsor (Model A vs. Model C)**

A fiscal sponsor is a 501(c)(3) that holds tax-exempt status and legal/financial responsibility for hosted projects.

**Model A (Comprehensive or Direct Sponsorship):** The project is formally part of the sponsor. The sponsor employs staff, owns assets, signs contracts, and reports the project's activity as its own on the Form 990. Financial responsibility is total. Most fiscal sponsors, including Metagov, operate under Model A by default for the projects they manage most directly.

**Model C (Grantor-Grantee or Pre-Approved Grant Relationship):** The project is a separate legal entity. The sponsor regrants funds to it for charitable purposes while retaining discretion and oversight over how those funds are used. The sponsor's obligation is to ensure charitable use, not to run the project's books. NumFOCUS's "Grantor-Grantee Model" is an example of this lighter-touch structure ([NumFOCUS Projects Overview](https://numfocus.org/projects-overview)).

**FinOps implication:** Knowing which model applies to each project is not optional. It determines whose payroll it is, whose liability it is, and how the activity appears in the audited financials.

---

### **Fiscally Sponsored Project (FSP)**

A fiscally sponsored project (FSP), also called a sponsee, is the project operating under a fiscal sponsor's umbrella. The FSP has mission autonomy but not independent legal or financial status under the fiscal sponsor's umbrella. Its tax-deductible contributions flow through the sponsor's 501(c)(3). Its funds sit on the sponsor's balance sheet as restricted net assets. Its compliance obligations are subsumed into the sponsor's Form 990 and audit. In Metagov's portfolio: The Wind Down, Relational Design Lab, Open Machine, NELA Computer Club, and Civic AI Tools are all FSPs.

---

### **Pass-Through Funding**

Funds that flow through a fiscal sponsor to an FSP without becoming the sponsor's own operating resources. The sponsor holds the funds, administers them, and ensures their charitable use, but the funds are restricted to the FSP's purposes and are not available for the sponsor's core operations. The FinOps discipline: total cash at a fiscal sponsor is a misleading metric because most of it is pass-through. The number that matters for the sponsor's own operational health is unrestricted net assets (core operating reserves), not total cash.

---

### **Restricted vs. Unrestricted Net Assets**

**Restricted net assets:** funds committed to a specific purpose, project, or time period. Includes both donor-restricted grants (restricted by the funder to specific programmatic uses) and funds held for sponsored projects (restricted by the fiscal sponsorship agreement to those projects). At a fiscal sponsor, the with-restrictions category is large and structural.

**Unrestricted net assets:** funds the organization can deploy at its own discretion. The basis for calculating reserves and runway. The number a funder asking about "available funding" is almost always actually asking about.

**Why this matters:** A large cash balance can coexist with a thin or negative unrestricted position. This is normal for a fiscal sponsor and must be explained to boards plainly rather than hidden. Metagov, for example, may hold $400,000 in total cash while having only $50,000 in unrestricted reserves available for core operations. The $400,000 number, if offered to a funder as evidence of financial health, misrepresents the organization's actual operational runway.

---

### **Endowment / Endowed Support**

An endowment is a permanent fund whose principal is invested and preserved in perpetuity; only the investment return (typically 4–5% per year) is spent on operations or grants. For OSS projects, endowed support is the funding model that most closely mirrors the commons ideal: a permanent resource that generates income without being depleted by use. The [Open Source Endowment](https://endowment.dev) (endowment.dev) is the first purpose-built endowment for OSS: $773K raised from 116 donors, targeting a 5% annual spend rate, with principal preserved permanently. This peer model is directly relevant to any domain core seeking structural sustainability beyond the annual grant cycle.

---

### **Grant Lifecycle**

The complete sequence of finance touchpoints from a grant award through final close: award and agreement review (restriction classification, allowable cost analysis), budget setup in the general ledger (establishing the restricted fund), receipt tracking (confirming cash actually arrived, not just pledged), expense allocation against the restricted purpose, interim and final funder reporting, and close with explicit release of any remaining restriction. Each stage has specific accounting treatment and documentation requirements. Metagov's operating discipline: commitments and transfers are sized against confirmed receipts only, never against the pledged amount. A pledge is not cash.

---

### **Funder Concentration**

The percentage of a core's (or sponsor's) operating funding coming from a single funder or a small number of funders. High concentration creates existential risk: one funder's exit can threaten core operations regardless of total budget size. The FinOps discipline: express concentration as a percentage of core operations spend, not total organizational spend. For a fiscal sponsor with $2M in total revenue but $1.8M in pass-through project funds, expressing concentration against the $2M denominator makes a core funder providing $150K look like 7.5% concentration. Against the $200K core operations denominator, that same funder represents 75% concentration: a genuinely different risk picture. Metagov's One Project anchor at $150K/yr through 2028 is the example. Against core operations, that is meaningful concentration. The risk is real, and the board should see the honest number.

---

## Section 4: Domain Examples

### AstroPy / Astronomy Software

**Domain in one sentence.** Professional astronomy's computational infrastructure: a Python package ecosystem (Astropy, astroquery, specutils, and dozens of affiliated packages) enabling spectral analysis, coordinate transforms, FITS file handling, and increasingly, machine learning pipelines over telescope survey data.

**Flagship projects.** [Astropy](https://www.astropy.org) (core package, NumFOCUS-sponsored since 2014); affiliated packages coordinated through the Astropy Project governance; IAU (International Astronomical Union) as domain standards body.

**Funding and governance pattern.** NumFOCUS provides comprehensive fiscal sponsorship; individual contributions and grants from agencies including NASA, the NSF, and institutional contributors (STScI, ESA). The Astropy Project is explicitly federated: a core package plus a growing set of affiliated packages that meet interoperability and quality standards. Governance is distributed across a Coordination Committee with contributor representation.

**FinOps shape.** A domain core holding multiple affiliated packages under NumFOCUS, with agency grants as primary revenue. Funding cycles align with federal research grant cycles (1–3 year awards). FinOps requirements include grant compliance for federal awards, restriction tracking across many concurrent grants, and governance documentation at the affiliated-package level to satisfy NumFOCUS's transparency requirements. Funder concentration risk is real: agency grant programs can shift with administration priorities.

---

### Bioconductor

**Domain in one sentence.** Bioinformatics: an open-source software project providing tools for the analysis and comprehension of high-throughput genomic data, primarily in R, with over 2,200 packages and a global user base in genomics, proteomics, and computational biology.

**Flagship projects.** Bioconductor core (package ecosystem); Posit/RStudio (major infrastructure partner); R Consortium (governance peer).

**Funding and governance pattern.** Bioconductor transitioned to NumFOCUS fiscal sponsorship in 2024, dissolving the Bioconductor Foundation of N.A., Inc., and transferring assets to NumFOCUS ([Bioconductor 2024 Annual Report](https://www.bioconductor.org/about/annual-reports/AnnRep2024.pdf)). Prior to the transition, it maintained its own nonprofit entity: a signal that some domains graduate out of fiscal sponsorship when they reach sufficient scale. The community is governed by a Technical Advisory Board and Community Advisory Board.

**FinOps shape.** A mature domain core that ran its own nonprofit for years before choosing the efficiency of fiscal sponsorship. The FinOps lesson: fiscal sponsorship is not just for early-stage projects. A domain core may rationally choose to fold administrative overhead into a larger institutional commons (NumFOCUS) even at significant scale. Industry sponsorship of the annual BioC conference is a major revenue source alongside grants, requiring clear separation of conference revenue from project development funding in the chart of accounts.

---

### Cryptography

**Domain in one sentence.** Open-source cryptographic libraries and security audit infrastructure: the tooling that secures the internet's connections, encrypts files, validates certificates, and underpins the privacy stack of virtually every OSS project in every other domain.

**Flagship projects.** OpenSSL (TLS/SSL library, now governed jointly by the [OpenSSL Foundation](https://openssl.foundation) and OpenSSL Corporation, a structure adopted in 2024 to separate the public-interest mission from commercial support services ([OpenSSL Wikipedia](https://en.wikipedia.org/wiki/OpenSSL))); Bouncy Castle (Java/C# cryptographic library, maintained by The Legion of the Bouncy Castle Inc., a not-for-profit Australian association); Open Crypto Audit Project (OCAP, historically funded security audits of critical libraries including TrueCrypt and OpenSSL).

**Funding and governance pattern.** Post-Heartbleed (2014), the Linux Foundation's Core Infrastructure Initiative (CII) provided emergency stabilization funding for OpenSSL. Since 2020, OpenSSL's primary income is support contracts. The OpenSSL 2024 governance restructuring separates the mission-holding Foundation from the revenue-generating Corporation. Bouncy Castle operates on donations and volunteer labor. The OCAP model funded one-time audits; it was not designed for ongoing maintenance funding.

**FinOps shape.** The cryptography domain illustrates two distinct FinOps problems: (1) critical infrastructure that receives reactive emergency funding (Heartbleed, Log4Shell) but lacks proactive endowed support, and (2) governance bifurcation (Foundation vs. Corporation) that creates a dual-entity accounting structure requiring clean intercompany accounting between the public-benefit entity and the commercial one. A domain core for Cryptography would need to hold the audit and governance function separately from any commercial service function.

---

### SciPy Stack

**Domain in one sentence.** The foundational scientific Python computing stack: NumPy (array computing), SciPy (algorithms), matplotlib (visualization), pandas (data frames), scikit-learn (machine learning), and Jupyter (interactive computing), collectively the computational substrate for most data science and scientific research globally.

**Flagship projects.** NumPy, SciPy, matplotlib, pandas, scikit-learn, Jupyter: all [NumFOCUS-sponsored projects](https://numfocus.org/sponsored-projects). NumFOCUS acts as the domain core for this cluster.

**Funding and governance pattern.** NumFOCUS is the primary fiscal sponsor across this stack, providing financial administration, legal services, and event planning while projects maintain independent governance. Funding sources include corporate sponsors (Microsoft, Google, Bloomberg, Quansight), individual donations via GitHub Sponsors, and grants from foundations. Google Summer of Code (administered through NumFOCUS) provides structured contributor funding annually.

**FinOps shape.** The most mature and deeply institutionalized domain core in existence. NumFOCUS's portfolio is itself a polycentric architecture: dozens of sponsored projects, each with its own governance and funding relationships, sharing a single institutional commons. The FinOps challenge at this scale is maintaining project-level financial visibility (per-project restricted fund balances, per-project statements of activity) without losing organizational coherence. New project applications are currently closed due to demand and capacity constraints ([NumFOCUS Projects Overview](https://numfocus.org/projects-overview)): a signal that even a mature domain core has an intake capacity ceiling.

---

### Privacy Tech

**Domain in one sentence.** Open-source tools for private communication, anonymous browsing, end-to-end encryption, and digital rights protection: the infrastructure of press freedom, political organizing, and personal security in adversarial environments.

**Flagship projects.** [Tor Project](https://www.torproject.org) (anonymity network, 501(c)(3), $7.3M budget in FY2023–2024 with 43% government funding and 22% corporate); [Signal Foundation](https://signalfoundation.org) (Signal messaging, 501(c)(3), $29M revenue in 2024, originally fiscally sponsored by Freedom of the Press Foundation before establishing its own 501(c)(3) in 2018 with $50M seed from Brian Acton); OpenPGP/GnuPG (email encryption infrastructure, GNU project, primarily volunteer).

**Funding and governance pattern.** Signal graduated from fiscal sponsorship to its own foundation at sufficient scale. Tor has maintained its own nonprofit structure while diversifying revenue from government-dominated (80% in 2012) to more balanced (35% government, 22% corporate, 19% from Mullvad VPN alone, 15% individual as of 2024). The Freedom of the Press Foundation remains an active fiscal sponsor for privacy tools at earlier stages.

**FinOps shape.** This domain illustrates the graduation pathway: projects start under fiscal sponsorship (Signal under Freedom of the Press Foundation), grow to sufficient scale and funder diversity to establish their own nonprofit, and become independent institutions. The FinOps requirement at transition is a clean transfer of restricted fund balances, executed grant novation agreements, and a documented handoff of compliance obligations. Tor's funding structure also illustrates the funder concentration problem in reverse: high government funding concentration (80%) is a governance risk, and Tor has actively diversified over a decade.

---

### Civic Tech

**Domain in one sentence.** Open-source tools and infrastructure for participatory democracy, government service delivery, civic data standards, and community self-determination: software that helps governments work better and communities engage more effectively.

**Flagship projects.** [Code for America](https://codeforamerica.org) (501(c)(3), $100M+ seven-year investments from Audacious Project and Blue Meridian Partners announced 2022, focused on safety net modernization); Open Civic Data (legislative and government data standards); Civic AI Tools (Metagov FSP, led by Nathan Storey, pursuing grants and potential government contracts); Harmonica and Talk to the City (deliberative technology tools in Metagov's research ecosystem, both exploring Public AI Apertus integration).

**Funding and governance pattern.** Civic tech spans a wide funding range: from small fiscally sponsored projects pursuing their first grants to large standalone nonprofits with eight-figure funders. Government contracts are a significant and structurally distinct revenue type in this domain: they carry different compliance overlays (DCAA cost principles, federal indirect cost rates, FAR requirements) that differ materially from philanthropic grant compliance.

**FinOps shape.** Civic AI Tools is a live example inside Metagov: a project pursuing both philanthropic grants and potential government contracts simultaneously. The FinOps requirement is a chart of accounts and cost allocation methodology that can serve both compliance frameworks at once. Government contract revenue is recognized differently from grant revenue, has different audit standards (Single Audit thresholds), and requires different documentation. A civic tech domain core needs to build those dual-track capabilities into its fiscal sponsorship infrastructure from intake.

---

### Climate

**Domain in one sentence.** Open-source software infrastructure for climate science, earth system modeling, climate finance analytics, and sustainable energy data: the computational layer underneath climate research, policy analysis, and ESG reporting.

**Flagship projects.** [Pangeo](https://pangeo.io) (community platform for scalable geoscience; NumFOCUS-sponsored since 2024; primary funders historically NSF, NASA, EarthCube, Gordon and Betty Moore Foundation ([Galaxy Training Network](https://training.galaxyproject.org/training-material/topics/climate/tutorials/pangeo/slides-plain.html))); OS-Climate (open-source climate risk data; joined FINOS, a Linux Foundation project, in June 2024 with founding members including Goldman Sachs and Red Hat ([Linux Foundation](https://www.linuxfoundation.org/press/os-climate-joins-forces-with-finos-to-enable-industry-wide-open-collaboration-for-climate-and-sustainability-aligned-finance))).

**Funding and governance pattern.** Pangeo illustrates multi-funder coordination around shared infrastructure: multiple concurrent grants from different federal agencies and private foundations support overlapping but non-identical purposes, requiring careful restriction tracking. OS-Climate's move to FINOS illustrates a corporate-member model for sustainability data infrastructure, with founding member dues replacing philanthropic grant funding.

**FinOps shape.** Climate OSS spans two distinct funding cultures: the research-grant culture (federal agencies, private science foundations, peer review, multi-year awards with milestones) and the ESG/finance culture (corporate members, dues-funded, compliance-driven). A climate domain core needs accounting architecture that can serve both. The multi-funder grant environment requires a robust restriction tracking system: many concurrent grants, each with its own allowable costs and reporting deadlines, all flowing through a single institutional commons. Renaissance Philanthropy's May 2026 launch of the Open Source for Science Fund (seeded with $20M from Biohub and Wellcome) is a new multi-donor mechanism that could serve as a climate domain core funding channel ([Renaissance Philanthropy](https://www.renaissancephilanthropy.org/insights/open-source-for-science-fund-launches)).

---

### AI Safety Research

**Domain in one sentence.** Research and infrastructure for understanding, evaluating, and governing advanced AI systems: technical alignment work, governance frameworks, interpretability research, and institutional design for AI accountability.

**Flagship projects.** [Atlas Computing](https://atlascomputing.org) (problem-first AI risk identification, previously fiscally sponsored under Metagov before transitioning to Renaissance Philanthropy); Public AI (civic AI research; active in Metagov ecosystem); Alignment Forum (community publishing platform); MIRI (Machine Intelligence Research Institute, standalone 501(c)(3)).

**Funding and governance pattern.** AI safety is a rapidly evolving funding landscape: large philanthropic commitments (Open Philanthropy, Survival and Flourishing Fund) dominate early-stage funding. Fiscal sponsorship is a common starting point, with multiple specialized sponsors now serving this domain ([AISafety.com Founder Toolkit](https://aisafety.com/founders)). Atlas Computing's transition from Metagov to Renaissance Philanthropy is a documented example of a project outgrowing one institutional home and moving to a better-fit sponsor.

**FinOps shape.** Atlas Computing's transition, as documented in Metagov's operations, illustrates the specific FinOps requirements at project graduation: a transfer agreement with clean entity naming and complete signature blocks; fund balance confirmation against confirmed receipts (the $68,000–$68,750 transfer was sized against the $75,000 actually received, not the full pledge); resolution of inherited obligations before close. The domain's growth pace creates intake pressure on fiscal sponsors: urgency framing by project leads (funder deadlines, closing transactions) should not compress diligence. Rushed intake is where inherited problems hide.

---

### OSS Funding Mechanisms

**Domain in one sentence.** The institutional infrastructure through which money moves into open-source software: endowments, fiscal sponsors, corporate giving programs, crowdfunding platforms, foundation grant programs, and government research funding.

**Flagship mechanisms.** [Open Source Endowment](https://endowment.dev) (endowment.dev: $773K raised from 116 donors, 5% spend rate, permanent principal, founded 2025); [GitHub Sponsors](https://github.com/sponsors) (direct developer-to-maintainer individual contributions, integrated into repository workflows); [Open Collective](https://opencollective.com) (project-level transparent ledger platform, used as a subset of the general ledger at many fiscal sponsors including Metagov); [NumFOCUS](https://numfocus.org) (domain core fiscal sponsor for scientific Python and statistics ecosystems); [Linux Foundation](https://linuxfoundation.org) (corporate-member-funded umbrella for enterprise OSS including OS-Climate via FINOS); [Software Freedom Conservancy](https://sfconservancy.org) (comprehensive fiscal sponsor for copyleft-oriented projects).

**FinOps shape.** Different mechanisms generate different FinOps requirements. Endowment income is unrestricted investment return: low compliance burden, high stability. Grant income is typically restricted: high documentation burden, reporting deadlines, allowable cost constraints. GitHub Sponsors income is often unrestricted individual donations: moderate volume, low individual size, requiring platform reconciliation against the general ledger. Corporate membership dues (Linux Foundation model) are typically unrestricted: predictable, contractual, but dependent on corporate program officer relationships rather than community funder relationships. A mature domain core will use several of these mechanisms simultaneously, requiring a chart of accounts that can distinguish and report on each revenue type cleanly.

---

## Section 5: FinOps Mechanics Vocabulary

### **General Ledger (System of Record)**

The single authoritative accounting system that records all organizational financial activity. At Metagov: QuickBooks Online. The general ledger is not one tool among several; it is the tool that all others reconcile against. When two numbers disagree, the general ledger wins. Every other system (project platform, bank exports, spreadsheets, contractor payroll) is either a feed into the general ledger or a subset of it. The discipline of naming one system as authoritative and never substituting a downstream export for it is the foundational FinOps principle. Without it, reconciliation collapses under the weight of contradictory sources.

---

### **Project Platform (Subset of Ledger)**

A tool that processes and displays transactions at the individual project level, making per-project activity visible to both the fiscal sponsor and the sponsored project. Open Collective is the standard example in OSS fiscal sponsorship. The critical operational fact: the project platform is a subset of the general ledger, never the whole picture. Open Collective shows transactions processed through that platform; it does not show wire transfers, ACH receipts, or payments made directly through the bank. Internal transfer postings (bank to platform reconciliation entries) appear in Open Collective as transactions but are not new inflows. Mistaking them for revenue inflates the numbers. The AWS gift episode at Metagov: Open Collective showed $225,000; the ledger showed $75,000 had actually arrived. The platform was technically accurate about what it had processed. The ledger was accurate about what was real.

---

### **Chart of Accounts**

The structured list of all accounts in the general ledger: revenue categories, expense categories, asset accounts, liability accounts, and net asset classes. For a fiscal sponsor, the chart of accounts must answer two questions simultaneously: what kind of activity is this (account), and which project does it belong to (class or fund dimension). The class dimension is the mechanism that allows per-project reporting without maintaining separate books. A transaction posts to the right account (what kind of cost or revenue) and the right class (which project). Run the ledger by class: get a per-project statement of activity. Run it by account: get the organizational income statement. The chart of accounts is the architectural decision that makes everything else possible or impossible.

---

### **Class / Fund Dimension**

A secondary dimension in the general ledger, separate from the account, that identifies which project, program, or fund a transaction belongs to. At Metagov: each sponsored project is a separate class. Each grant may also be a separate class or sub-class, allowing tracking of grant-specific restricted fund balances. The class dimension is what separates the regulatory-floor rules (account layer: what kind of activity) from the sponsorship-context rules (class layer: which project, which restriction). These two dimensions allow one general ledger to support a $10,000 wind-down project and a $200,000 research deposit simultaneously without confusion between their restricted balances.

---

### **Statement of Activity**

The nonprofit equivalent of an income statement: a summary of revenues and expenses over a period, showing the change in net assets. For a fiscal sponsor, the statement of activity is most useful when it can be cut three ways: organization-wide (for the consolidated audit and Form 990), core operations only (for board and funder review of the sponsor's own solvency), and by individual project (for per-project sponsee reporting). The core-operations-only cut strips out pass-through project activity and shows whether the sponsor itself is financially viable. This is the number boards actually need for governance decisions. Presenting only the organization-wide statement at a fiscal sponsor conflates the sponsor's health with the aggregate health of all its projects: a misleading picture for any governance purpose.

---

### **Restricted vs. Unrestricted (and Why Total Cash Misleads)**

See Section 3 (Restricted vs. Unrestricted Net Assets) for full treatment. The operational emphasis: total cash is the wrong denominator for almost every governance and funder question at a fiscal sponsor. A sponsor holding $600,000 in total cash but only $40,000 in unrestricted reserves has 40,000 dollars, not $600,000, available to cover an unexpected operational cost, a staff transition, or a funder gap. The $560,000 difference is pass-through: legally committed to sponsored projects, auditorially scoped, and not the sponsor's money to spend. Presenting total cash as a measure of financial health is not lying; it is choosing the wrong number. The FinOps discipline is always to surface the unrestricted position alongside total cash, with plain language explanation of the difference.

---

### **Form 990**

The annual federal information return required of tax-exempt organizations. Not a tax return: 501(c)(3) organizations are generally not subject to federal income tax. A public disclosure document: Form 990 filings are publicly available and are how funders, journalists, researchers, and the public understand an organization's finances, governance, and programmatic work. For a fiscal sponsor, the Form 990 scope grows with organizational complexity: sponsored project activity appears in the consolidated filing, and the schedules (particularly Schedule O for supplemental narrative) are where the fiscal sponsorship structure and significant transactions get explained. The first Form 990 that reflects independent audit results is a significant milestone in institutional credibility.

---

### **Audit Threshold**

The revenue level above which a state requires an independent financial audit of a nonprofit organization. Thresholds vary by state; many states require an audit at $500,000 or $750,000 in annual revenue, with some as low as $250,000. At the federal level, the Single Audit Act imposes audit requirements on organizations spending $750,000 or more in federal awards in a single year. Crossing the audit threshold the first time is a significant operational lift: the audit firm will test internal controls, examine restricted fund accounting, and issue findings that become part of the public record. (For Metagov, EisnerAmper serves as the CPA preparing for that first independent audit.) Building audit-ready practices before crossing the threshold is the strategic FinOps move: it is far cheaper to design the right controls from the start than to retrofit them under audit pressure.

---

### **Graduation-Readiness**

A project's demonstrated capacity to operate as a standalone organization if it chooses to: its own bank accounts, its own payroll processing, its own audit relationship, its own legal counsel, its own board governance structure. Graduation-readiness is a health metric for fiscal sponsors to track, not a forced exit condition. Not every project should or will graduate to its own 501(c)(3). Many are better served by a permanent institutional home. The metric is useful because it measures whether the project has accumulated the organizational capacity to be sustainable, regardless of whether it ever uses that capacity to leave. For Signal, the graduation moment (establishing its own 501(c)(3) with Brian Acton's $50M seed) was a natural outgrowth of scale. For most projects in a fiscal sponsorship portfolio, graduation-readiness is a measure of health, not an expected endpoint.

---

### **Treasury Posture (Especially for Crypto-Receiving Fiscal Sponsors)**

A fiscal sponsor's overall approach to holding and managing its cash and investment assets: what proportion is kept liquid, what is invested, what is held in digital assets, and what risk parameters govern each category. For a fiscal sponsor, a conservative posture is appropriate because most of the cash is not the organization's own. Funds held in trust for projects are effectively held in trust: volatility in their value is a fiduciary problem. For organizations receiving cryptocurrency donations or grants (common in digital governance and Web3 adjacent domains), the additional complexity is the off-ramp workflow and the stablecoin-weighting question: holding volatile crypto on behalf of a project exposes that project to market risk on its operating funds, which is generally not acceptable. The prudent policy: convert to fiat promptly, or hold in stablecoins only, with documented signing thresholds and custodial controls.

---

### **Off-Ramp (Digital Asset to Fiat Conversion)**

The process of converting cryptocurrency holdings to fiat currency for deposit in an operating bank account. Standard business banks cannot accept on-chain cryptocurrency deposits directly. The conversion workflow: on-chain receipt to an institutional custody arrangement (Coinbase Prime for Metagov), then conversion through the prime brokerage's off-ramp facilities, then fiat wire transfer to the operating bank (Mercury). The timing gap between on-chain receipt and fiat landing in the bank creates apparent reconciliation discrepancies that are settlement lag, not missing transactions. Build this two-step into both the treasury procedures and the reconciliation calendar.

---

### **Multi-Signature Wallet**

A cryptocurrency wallet requiring multiple private key holders to co-sign before any transaction can be executed. The institutional controls analog to dual-signature checking accounts or dual-approval wire transfers. For a fiscal sponsor holding crypto on behalf of a project, multi-signature custody means no single person can move funds unilaterally. The documented signing threshold (e.g., 2 of 3 named signers must approve) is the control. The named signers and threshold should appear in the treasury policy. The auditor will ask.

---

### **Reconciliation Hierarchy**

When two numbers disagree, resolve in this order: the general ledger is authoritative; bank statements verify the ledger's cash position; the project platform is a subset reconciled to (not from); spreadsheet exports are working tools, not sources of truth. This hierarchy sounds obvious but is violated constantly in practice, especially when project managers or program staff pull numbers from Open Collective exports and present them as organizational financials. The FinOps discipline is to make the hierarchy explicit, written, and known to everyone who touches financial data: the finance team, the program staff, the board, and any funder who asks for a financial update.

---

## Section 6: Cross-Domain Patterns (The Synthesis)

Across every domain examined in this glossary, a set of structural patterns recurs with enough consistency to name a discipline.

Every domain has a shared infrastructure problem. Astronomy's Astropy, bioinformatics' Bioconductor, scientific Python's NumPy/SciPy stack, privacy's Tor and Signal ecosystem, civic tech's deliberative tools, climate's Pangeo: each community depends on a layer of open-source infrastructure that is expensive to maintain, difficult to fund through project grants, and existentially important to everyone in the domain. The domain core is the institutional form designed to hold that infrastructure across generations of projects and funders. The fiscal sponsor is the operational expression of that institutional form.

Every domain faces the same FinOps tension. The funds flowing through a domain core are mostly not the core's own. Pass-through funds for satellite projects, restricted grants tied to specific programmatic purposes, government contracts with compliance overlays: all of these sit on the core's balance sheet but are not available for core operations. Total cash misleads. The unrestricted position, measured honestly against core operations spend, is the number that tells you whether the institution can survive a funder gap. Every domain core struggles to explain this to its board and funders. The explanation is not complicated; it just requires naming it explicitly and consistently.

Every domain needs graduated controls matched to project scale. A $5,000 wind-down project and a $200,000 research studio sitting inside the same fiscal sponsor cannot be governed with the same overhead. Too much overhead crushes the small project. Too little overhead creates audit risk for the large one. The solution is a layered architecture: a regulatory floor of controls that applies to all projects regardless of size (restricted fund tracking, contract execution, 1099 compliance), and an adaptable layer of controls that scales with project complexity and dollar volume. The class dimension in the general ledger is the technical expression of this layered architecture.

What is unique across domains is culture: funding cycle length, community norms around financial transparency, the balance of government versus philanthropic versus corporate funding, the maturity of governance infrastructure, and the degree to which community members have prior experience with nonprofit compliance. Climate's federal grant culture is different from Cryptography's reactive security funding culture. Civic tech's growing government contract exposure has no parallel in pure research domains. Privacy tech's adversarial political environment creates operational security requirements that do not exist in astronomy software. Commons FinOps must be domain-aware: the regulatory floor is the same everywhere, but the adaptable layer above it has to fit the actual community.

"Commons FinOps" is the right name for the discipline that holds this together because it names both the institutional form and the operational function. The commons side names the governance theory: Ostrom's eight principles, the polycentric architecture, the nested enterprise model, the collective choice mechanisms. The FinOps side names the operational practice: the general ledger, the restricted fund accounting, the audit trail, the reconciliation hierarchy, the treasury posture. Neither side alone is sufficient. Governance theory without operational grounding produces bylaws that look good and books that do not support them. Operational practice without governance theory produces technically compliant institutions that cannot make legitimate decisions and cannot build the trust of their communities over time.

Metagov is the working laboratory for this synthesis. More than $2 million channeled in year one. The operational foundation set for the organization's first independent audit. Five sponsored projects ranging from a conscious organizational wind-down to a $200,000 AI safety research deposit. Fundraising across digital identity standards, interoperability conferences, speculative fiction prizes, and civic AI tools: a portfolio that spans every dimension of the commons governance and OSS funding world in miniature. The lessons from that laboratory, compressed into transferable schema, are what Commons FinOps offers the broader OSS funding ecosystem. The question is no longer whether this discipline is real. The question is whether it can be documented clearly enough to let the next domain core stand up without reinventing the operational infrastructure from scratch.

---

## Section 7: Selected Reading

1. Ostrom, Elinor. *Governing the Commons: The Evolution of Institutions for Collective Action.* Cambridge University Press, 1990. The foundational text. Start with Chapters 1 and 3. Available via many university libraries.

2. Ostrom, Elinor. "Beyond Markets and States: Polycentric Governance of Complex Economic Systems." *American Economic Review* 100, no. 3 (2010): 641–672. Nobel Prize lecture. Free access at [https://www.aeaweb.org/articles?id=10.1257/aer.100.3.641](https://www.aeaweb.org/articles?id=10.1257/aer.100.3.641).

3. NumFOCUS. "Projects Overview." [https://numfocus.org/projects-overview](https://numfocus.org/projects-overview). Practical model of a domain core fiscal sponsor at scale; read for the Comprehensive vs. Grantor-Grantee model distinction.

4. Open Source Endowment Foundation. [https://endowment.dev](https://endowment.dev). The first purpose-built endowment for OSS; the peer model for permanent commons funding.

5. Bioconductor. *2024 Annual Report.* [https://www.bioconductor.org/about/annual-reports/AnnRep2024.pdf](https://www.bioconductor.org/about/annual-reports/AnnRep2024.pdf). Documents the 2024 transition from standalone nonprofit to NumFOCUS fiscal sponsorship: a real-world graduation-in-reverse case study.

6. The Tor Project. "Reports and Financials." [https://www.torproject.org/about/reports/](https://www.torproject.org/about/reports/). Annual audited financials and 990 filings; a transparent model for a mature OSS nonprofit in a privacy-sensitive domain.

7. Signal Foundation. "Signal Foundation formed to support Signal Messenger." [https://signal.org/blog/signal-foundation/](https://signal.org/blog/signal-foundation/). Documents the graduation from fiscal sponsorship under Freedom of the Press Foundation to standalone 501(c)(3).

8. Linux Foundation. "OS-Climate Joins Forces with FINOS." [https://www.linuxfoundation.org/press/os-climate-joins-forces-with-finos-to-enable-industry-wide-open-collaboration-for-climate-and-sustainability-aligned-finance](https://www.linuxfoundation.org/press/os-climate-joins-forces-with-finos-to-enable-industry-wide-open-collaboration-for-climate-and-sustainability-aligned-finance). June 2024. Corporate-member model for climate OSS.

9. Renaissance Philanthropy. "Open Source for Science Fund Launches." [https://www.renaissancephilanthropy.org/insights/open-source-for-science-fund-launches](https://www.renaissancephilanthropy.org/insights/open-source-for-science-fund-launches). May 2026. New multi-donor fund ($20M anchor from Biohub and Wellcome) for scientific OSS.

10. Sané, Andrew. "The Eight Principles, Read from the Operator's Seat." Prepared for the OSS Funding Workshop, UN Open Source Week, June 22, 2026. The narrative companion to this glossary; available at Metagov.

11. OpenSSL. Wikipedia. [https://en.wikipedia.org/wiki/OpenSSL](https://en.wikipedia.org/wiki/OpenSSL). Documents the Heartbleed crisis (2014), the CII emergency response, and the 2024 Foundation/Corporation governance bifurcation.

12. Atlas Computing. [https://atlascomputing.org](https://atlascomputing.org). Problem-first AI safety infrastructure; previously fiscally sponsored under Metagov; now under Renaissance Philanthropy. A documented case study in project transfer.

---

Andrew Ngeseyan · ASN Management LLC · andrew@asnmgt.com
