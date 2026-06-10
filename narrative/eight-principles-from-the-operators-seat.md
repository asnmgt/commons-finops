# The Eight Principles, Read from the Operator's Seat
## A Commons FinOps narrative for the OSS Funding Workshop, June 22, 2026

**By Andrew Ngeseyan · ASN Management LLC · Finance and Operations Director, Metagov**

---

## The frame

Elinor Ostrom gave us eight design principles for commons that endure. They are usually read as governance theory. Rules of legitimacy, structures of authority, conditions for cooperation. That reading is correct, and it is incomplete.

Read from the operator's seat, which is the seat I sit in as the person responsible for the financial and operational backbone of a fiscally sponsored research network, the eight principles are not governance abstractions. They are operational requirements. Each one specifies a concrete capability the financial and operational infrastructure must support, or the commons cannot endure regardless of what its bylaws say.

The proposed core and satellite model for sustainable OSS funding is a polycentric institutional design. It will succeed or fail based on whether the operational infrastructure underneath it can actually implement the eight principles. Most of the conversation in this room will focus on the design layer: what the schema looks like, what governance bodies exist, what protocols cores and satellites adopt. My contribution is to name the operational layer the design depends on, and to ground that naming in what is actually happening at Metagov right now.

I will read each principle as a FinOps requirement. For each one, I will point to where it lives in our books today, where it gets tested, and where the schema your group is designing has to land if it is going to be more than language.

A note on terms. I use "Commons FinOps" through this narrative. It is what I do. It is the discipline of running the books, the controls, the intake, and the treasury for an institution whose job is to hold and steward funds for a community of projects that share infrastructure but not legal form. It is fiscal sponsorship with the polycentric design fully named.

---

## 1. Clearly defined boundaries

A commons institution cannot endure if no one can tell who is in and who is out, or where the resource starts and ends. In the OSS funding context, the question is: **what does it mean to be a satellite of a core?**

From the operator's seat, this is not philosophical. It is a question with cash flow consequences. When a project's status as a satellite changes, money moves differently. Funder restrictions apply or do not. Reporting obligations attach or detach. Audit boundaries shift. A satellite that is informally part of a core has none of these consequences. A satellite that is formally a satellite has all of them.

Metagov is operating this boundary rule explicitly right now. The fiscal sponsorship policy adopted by the board this year says that, for at least the rest of 2026, we will only accept project leads who are personally known to our Research Directors. That is Ostrom's first principle in production. It is not a soft preference. It is a written intake gate that selects for trust and information density before money or legal exposure crosses the boundary.

Our current sponsee pipeline reads the same way. Five projects are in active development: The Wind Down with Camille Acey, Relational Design Lab with LXCast, Open Machine with Ven Gist and Exeunt, North East Los Angeles Computer Club with Michael Appuhn, and Civic AI Tools with Nathan Storey. Every one of those project leads is personally known to one or more of our Research Directors. The funding outlook ranges from a trickle of individual donations to a $200,000 deposit ready to land. The boundary rule is the same across all of them.

Here is the operational consequence. Open Machine has $200,000 ready to be deposited. Once Metagov accepts that intake, the cash sits on our balance sheet, it is restricted to that project, and our 990 has to reflect it. It is not Metagov's money to spend. It is Open Machine's money, held in trust, under our tax exemption. If the boundary between "satellite of Metagov" and "not a satellite of Metagov" is fuzzy, we cannot answer the IRS, we cannot answer our CPA at EisnerAmper or our auditor when the time comes, and we cannot answer the funder.

The schema your working group is designing has to specify boundary criteria that are machine determinable, not subjectively interpreted, because they will be tested. They will be tested by the IRS during 990 review. By foundation grant compliance officers. By auditors during fund balance reconciliation. By sponsees themselves when they want to know what they are signing up for.

Concretely, the schema needs:

- Written intake criteria for satellite status
- A defined moment of satellite recognition. Signed agreement, formal acceptance, board ratification
- A defined moment of satellite exit. Sunset, ejection, graduation to its own 501(c)(3)
- Treatment of edge cases. Paused projects, dormant satellites, satellites with no current funding

The first principle, in the operator's translation, is this: **write the satellite intake and exit policy before you write anything else.** Metagov did that. We will keep that gate narrow until the operational machinery can handle a wider one.

---

## 2. Congruence between rules and local conditions

Ostrom found that successful commons institutions tailored their rules to local conditions. Climate, scale, resource type, community composition. Copy-pasted rulebooks from one commons to another usually failed.

In FinOps terms: **the fiscal and operational rules a core applies must fit the actual cadence and structure of the satellites it sponsors.** Astronomy software has different funding cycles than bioinformatics tools. AI safety research has different grant compliance requirements than civic tech platforms. A single fiscal sponsorship rulebook applied identically across all satellites will either oversimplify, fail to protect the core, and produce findings at audit, or it will overcomplicate, strangle the satellites, and produce attrition.

Metagov's current portfolio illustrates the range. The Wind Down operates at under $10,000 per year. Open Machine arrives with $200,000 in hand and a research studio orientation. Civic AI Tools is courting grants and potentially government contracts, which carry an entirely different compliance overlay. Treating these four shapes of work with one rulebook would either fail the smallest project (too much overhead) or fail the largest one (not enough controls).

The operational implication is that the schema needs a layered rule architecture. Some rules are core-wide. Audit readiness standards, restricted fund treatment, 1099 contractor classification. These come from regulation and do not flex. Other rules are domain specific. Reporting cadence, milestone definitions, allowable cost interpretations. These adapt to the satellite's actual work. Schema design must distinguish which is which, and the chart of accounts must be built to support both at the same time.

A practical example. Metagov runs QuickBooks Online as the system of record, with classes for each sponsored project. The class dimension lets one transaction post to both the right account (what kind of activity) and the right project (which satellite). The same general ledger structure supports a $10,000 per year project and a $200,000 deposit without separate books, because the chart of accounts was designed to hold both at the account layer and the class layer. The regulator's rules sit at the account layer. The satellite's local conditions sit at the class layer. They do not collide.

The second principle, translated: **separate the rules that come from regulators (non negotiable) from the rules that come from sponsorship choice (adaptable). Confusing the two is the most common operational failure mode I see.**

---

## 3. Collective choice arrangements

Most individuals affected by the operational rules can participate in modifying them. Top down rule setting alienates the people who have to comply and produces compliance theater instead of compliance.

For the operator, the question is: **do satellites have a real voice in how cores set rules, or are the rules imposed?**

I have seen both versions. When satellites have voice, a quarterly policy review where representatives can flag friction, a written grievance procedure, an annual sponsorship terms renegotiation, compliance is genuine. When satellites have no voice, the rules degrade into a compliance fiction that survives until the first audit finding or the first major funder asking questions, at which point the structural rot becomes visible.

Metagov is small enough today that collective choice happens in standing relationships. Liz, the Research Directors, and I work directly with project leads. When the fiscal sponsorship policy was being written this year, that policy was shaped by what we had learned running Atlas Computing, the Grant Innovation Lab, Public AI, and others. The Atlas transition to Renaissance Philanthropy in particular taught us about transfer agreements, signature blocks, and inherited representations. Those lessons went straight into the next version of the intake template. The satellites we had at the time effectively wrote the policy by living it.

That works at five projects. It does not work at fifty. The schema needs explicit collective choice mechanisms for the moment scale outruns standing relationships. How do satellites propose rule changes. How do cores respond. What is the appeal process when sponsees disagree with core decisions. Who is at the table when policies are written.

These mechanisms must be lightweight enough to actually use and structured enough to produce decisions. A standing policy review session with a documented agenda costs almost nothing. Skipping it costs the legitimacy of every rule it would have ratified.

The third principle, translated: **the sponsorship agreement is not just a document. It is the protocol for ongoing negotiation. Build the negotiation channels into the operational structure before scale forces you to.**

---

## 4. Monitoring

Monitors are accountable to the resource users themselves, or are users. External monitoring imposed from above without legitimacy fails.

This is the principle where the FinOps function lives in pure form. **Monitoring is what FinOps does for a living.** Reconciliations, audits, restricted fund tracking, period end close, variance analysis. These are all monitoring activities. They produce the visibility that lets the commons institution see itself.

A concrete instance from our books. A major charitable gift from Amazon Web Services arrived structured as two separate annual purchase orders of roughly $75,000 each, supporting CSLib work fiscally sponsored under Atlas Computing. The Open Collective platform showed three entries that, read naively, looked like $225,000 in receipts. The general ledger told a different story. Two of those three entries were internal Mercury to platform reconciliation postings. Only $75,000 had actually arrived. The transfer to Renaissance Philanthropy at closeout was sized against the $75,000 on hand, not the pledge. Monitoring caught what casual reading would have missed.

That is the kind of thing monitoring is supposed to do. Not catch bad actors. Catch the seam between two systems, the place where the same event looks different from two different angles, and resolve which angle is authoritative.

But Ostrom's insight goes further. Monitoring is not just an act of measurement. It is an act of legitimacy. The monitors must be trusted by the monitored. In commercial finance, this is rarely a problem because auditors are external, professional, and regulated. In commons institutions, monitoring legitimacy is harder. Sponsees must trust that the core's monitoring is fair, that data is not being used against them, that the cadence is not punitive, that errors get corrected without penalty.

Metagov runs its monitoring as a service to satellites. Project leads get per project statements of activity from the general ledger, cut by class. They see what came in, what was spent, what remains, what is committed versus available. They see the same numbers I see. That is the legitimacy move. The monitor and the monitored are looking at the same screen.

The schema needs to specify not just what gets monitored, but who monitors, to whom they report, how their independence is protected, and what recourse a satellite has if it disagrees with a monitoring finding.

The fourth principle, translated: **the monitoring function is the most important operational function the core performs, and it must be designed as a service to satellites, not a control over them.**

---

## 5. Graduated sanctions

Violations are punished with graduated sanctions. First offenses get light responses. Repeated or severe ones escalate. Binary punishment, banned or not, destroys community trust.

This is, in my experience, the single hardest principle to implement well. Most fiscal sponsors I have worked with either over tolerate (no consequences, drift compounds, the next audit produces findings) or over react (one mistake triggers termination, satellites learn to hide problems instead of surfacing them).

The middle path requires a documented sanctioning schedule. **A graduated sanctions framework, written before the first sanction is ever needed.** Something like:

- Missed reporting deadline, first instance: written reminder, no other consequence
- Missed reporting deadline, third instance in twelve months: satellite leadership called into a review meeting, written corrective plan required
- Misuse of restricted funds, modest amount, self reported: course correction, no public sanction
- Misuse of restricted funds, material amount, discovered through audit: formal review, funder notification consideration, possible termination
- Pattern of misuse across multiple events: termination, funder notification, recovery action

These are not just rules. They are commitments. To satellites that they will be treated fairly. To funders that the commons institution can self police. To the auditor that there is a controls framework. Without graduated sanctions in writing, sanction decisions become political, ad hoc, and unjust.

A practical note that does not always make it into governance theory. The audit firm will ask. Any auditor approaching Metagov's first independent audit will have standard questions about how findings get raised, escalated, and resolved. If the answer is "we figure it out case by case," the auditor will look harder. If the answer is "here is the schedule, here is the log," the auditor moves on. Graduated sanctions are not just a fairness mechanism. They are an audit readiness mechanism.

The fifth principle, translated: **write the sanctions schedule before you have to sanction anyone. Once a violation is in front of you, the temptation to handle it case by case is overwhelming, and the precedent you set becomes the rule.**

---

## 6. Conflict resolution mechanisms

Low cost, accessible arenas for resolving disputes among users, or between users and officials.

In FinOps terms: **what happens when a satellite disputes a core's accounting decision?** When a funder's reporting interpretation conflicts with a satellite's understanding? When two satellites disagree about which can claim a shared piece of grant funding? When the core makes an allocation decision a satellite considers unfair?

Formal courts and outside counsel are too expensive for these disputes. Most commons institutions need internal mechanisms. A designated mediator. A peer review panel. A defined escalation path. The operational requirement is that these mechanisms exist, are known, and are cheap to invoke.

Metagov uses outside counsel sparingly. Karl Mill at Mill Law Center handles agreements and complex transfers. The Atlas to Renaissance Philanthropy transfer document went through counsel because the executed PDF had inconsistencies in entity naming and a blank signatory line that needed to be fixed before close. That kind of issue is what counsel is for. It is not what conflict resolution is for. The day to day questions of "is this allowable under your restriction" or "did the platform charge this to the right class" need a cheaper, faster path.

The cost of a missing conflict resolution mechanism is that disputes either get suppressed and accumulate as silent resentment, or escalated externally and become public, expensive, and relationship destroying. Neither is acceptable for a commons institution trying to compound trust over time.

The sixth principle, translated: **publish your conflict resolution path before you need it, and make invoking it cheap enough that satellites will actually use it.**

---

## 7. Minimal recognition of rights to organize

The right of users to devise their own institutions is not challenged by external governmental authorities. Without this, every internal rule is contestable from above and the institution lacks autonomy.

In OSS funding context, this principle is mostly external. It applies to how funders relate to cores. Do funders respect the core's authority to write its own policies, or do funders unilaterally impose terms? **This is the funder externality problem, named explicitly.**

From the operator's seat, funder over reach is a real and growing pressure. Funders increasingly want to dictate not just what their money is spent on but how the recipient organization is governed. Board composition, audit firm choice, executive compensation, board giving requirements. Some of this is legitimate. Donor restrictions are protected by law. Some of it is mission creep that violates the seventh principle.

There is also a less obvious version of this principle that came into focus for us this year. Last week Liz was warned in person by a democracy funder of latent risks to Metagov itself because of the way we organize in public. The example given was a hypothetical third party who once signed up for Metagov Slack, then later did something that triggered investigation, and the legal disclosure obligations that could follow might bankrupt us. Our infrastructure choices, Slack and Google, are themselves a recognition of rights question. The platforms we use participate in the rule setting whether we invite them to or not. Our planned response is to evaluate self hosted alternatives for communication, knowledge management, and research, possibly as the core offering of a paid membership program. That is Ostrom's seventh principle expressed through procurement.

The core and satellite model gives cores a stronger position vis a vis funders precisely because cores represent collective bargaining power. A core can negotiate funder terms on behalf of multiple satellites in ways individual projects cannot. But this only works if the core has the operational maturity, the books, the policies, the audit history, the governance documentation, to negotiate as a peer.

The seventh principle, translated: **the operational maturity of the core is what gives it standing to push back on funder over reach and platform over reach. Without books a funder respects, there is no leverage.**

---

## 8. Nested enterprises

For larger systems, governance activities are organized in multiple layers of nested enterprises. Smaller units handle local decisions. Larger units coordinate across them.

**The eighth principle is the architectural blueprint of the entire core and satellite proposal.** This is not coincidence. The workshop is, in effect, a design exercise to implement Ostrom's eighth principle for the OSS funding world.

From the operator's seat, nested enterprises generate specific operational requirements:

- Each nested layer needs its own financial books and its own monitoring function
- Cross layer transactions, satellite to core, core to ecosystem coordinator, require defined accounting treatment
- Authority boundaries must be explicit so decisions made at one level are not contested at another
- Reporting flows up cleanly and resources flow down cleanly, with both audit trails intact

Metagov itself is now a nested system in development. The five sponsees sit inside Metagov. Metagov sits inside a wider ecosystem of funders, peer fiscal sponsors, and the One Project core relationship that runs through 2028. Liz's "win^n" or BLOOM^n framework, the idea that the right institutional form for technologists coordinating on interoperability standards looks like a nonprofit under member governance with a cooperative of technologists and a marketplace of interoperable tools inside, is itself a third nested layer being designed in real time. The 2027 South America Regional Interop Conference, the Asia Regional Conference funded by the Toda Foundation, the Systems Worthy of Your Speech identity standards project, and the Protopian Prize working group all sit as semi nested enterprises with their own working groups, their own funder relationships, and their own reporting cadences that ultimately roll up to Metagov's 990.

The nested enterprise model is operationally heavier than centralized governance. It has more interfaces, more handoffs, more places where information must travel cleanly. This is the cost of polycentricity. It is worth paying because the alternatives, centralization or fragmentation, fail for the reasons Ostrom documented across forty years of empirical work. But the operational cost is real, and it has to be funded.

A specific consequence I will name. If Metagov takes accounting in house this year, which is on the table for our team kickoff conversations, that saves the organization roughly $3,500 a month in outsourced bookkeeping. That savings is not a luxury. It is the funding for the operational layer Ostrom's eighth principle requires. The work of running per project books, restricted fund tracking, and clean nested reporting has to be paid for somehow. Either a core funder pays for it directly, or the sponsor builds the capacity to do it in house at a lower cost than the market rate. Both routes are valid. Hand waving is not.

The eighth principle, translated: **polycentric governance is operationally expensive. Build that cost into the funding model from day one, or watch the structure collapse under its own administrative weight.**

---

## The seam the schema must hold

If I had to name the single operational seam where the schema will succeed or fail, it would be this. **The schema must connect the user governance layer, where Ostrom's empirical work lives, with the funder rule setting layer, where Ostrom's empirical work is silent.**

Classic Ostromian commons were governed by the people who used them. The OSS funding world introduces a second class of rule setters, funders, who shape outcomes without participating in the commons themselves. This is the genuinely new design challenge.

The fiscal sponsorship structure I run at Metagov holds this seam imperfectly. Some funders accept our governance and trust us to set rules. Others impose their own and treat us as a pass through. Most do something in between, on a per grant basis, in ways that are hard to predict and harder to systematize. EisnerAmper, our CPA, treats us as a single legal entity with consolidated obligations regardless of how the funders behave. The IRS does the same. Our chart of accounts has to absorb the variance.

A successful core and satellite schema must give cores a defensible position in this negotiation. That position comes from operational legitimacy. The books, the policies, the audit history, the documented adherence to the eight principles. Without that, cores are renting their legitimacy from funders. With it, they are negotiating from their own ground.

---

## What I would push the working group to specify

If I have one ask of the technical and social and governance working groups coming out of June 22, it is to specify the **minimum operational dataset** that any institution must produce to qualify as a core. Not a governance bylaw template, though those are useful, but a list of operational artifacts every core must be able to produce on demand:

- A written sponsee intake and exit policy
- A written sanctions schedule with graduated levels
- A written conflict resolution procedure
- A monitoring cadence (what gets reviewed when, by whom)
- A documented chart of accounts that distinguishes restricted from unrestricted funds at the satellite level
- An audit history, most recent two years minimum, clean opinions preferred
- A board composition and governance document
- A funder due diligence packet, a one page summary plus the supporting evidence
- A treasury policy that covers fiat and digital assets if relevant, with named custodians and signing thresholds
- A documented system of record, with the project platform identified as a subset of the ledger and not a substitute for it

These artifacts are the operational expression of Ostrom's eight principles. They are also the things funders ask for when they are doing serious diligence. Specifying them at the schema level gives the ecosystem something testable. An institution either has the dataset or it does not, and only those that do should be funded as cores.

This is the Commons FinOps contribution to the schema. The schema can be elegant or inelegant. Either way it has to land in books, policies, and audit trails to be real. I would like to make sure that landing is in the design, not retrofitted onto it.

---

## Closing

The work the workshop is starting is the most interesting operational design problem in nonprofit finance today. The eight principles give us a tested framework. The fiscal sponsorship structures already operating across the OSS ecosystem, Metagov among them, give us a starting set of working examples. The remaining work is to compress what those structures have learned into a transferable schema that lets new cores stand up cleanly instead of reinventing the operational infrastructure each time.

Metagov is in the middle of that work. We channeled more than $2 million in fiscal sponsorship funding in year one, built the first written onboarding manual, set the operational foundation for our first independent audit, closed the Atlas Computing transition cleanly, and stood up the systems that let us hold $200,000 of restricted Open Machine cash with the same controls we use for a $3,500 wind down grant. The five sponsees in our current pipeline, and the funder relationships behind them, are not theoretical examples. They are the live test cases for whether Commons FinOps is a real discipline or just language.

I think it is a real discipline. I think it can be transferred. I think this room is the right room to start that transfer. I look forward to being useful in the work.

Handle your business.

— Andrew Ngeseyan
Finance and Operations Director, Metagov
ASN Management LLC
andrew@asnmgt.com
