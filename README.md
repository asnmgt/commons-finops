# Commons FinOps

**A documented financial and operational practice for fiscally sponsored, polycentric, commons-oriented institutions.**

Commons FinOps is the discipline that translates Elinor Ostrom's eight design principles for enduring commons into the operational requirements that fiscal sponsors, foundations, and OSS funding cores must meet to function. It sits at the seam between three rooms that most practitioners treat separately: nonprofit fiscal sponsorship, open source software funding, and digital governance research.

This repository is the working reference set. It is built from operational practice running the financial and operations function of [Metagov](https://metagov.org), a 501(c)(3) fiscal sponsor for digital governance research, where the year one record includes over $2M in fiscal sponsorship funding channeled, the first written onboarding manual delivered, and the operational foundation set for the organization's first independent audit.

## Why this exists

The OSS funding world is in the middle of designing a core and satellite model for sustainable open infrastructure funding. That model is, in effect, a design exercise to implement Ostrom's eighth principle (nested enterprises) for OSS. It will succeed or fail based on whether the operational infrastructure underneath it can actually implement all eight principles in practice.

Most of the conversation in that design world lives at the governance layer. This repository names and documents the operational layer the design depends on: the books, the policies, the audit trails, the intake gates, the monitoring cadence, the conflict resolution paths, the graduated sanctions. The artifacts that turn governance theory into something a funder, an auditor, and a sponsee can each see and trust.

## What's in this repo

| Folder | Contents |
|---|---|
| [`narrative/`](./narrative) | The eight principles read as FinOps requirements, anchored to live ecosystem examples. The talk delivered at the UN Open Source Week funder gathering, June 22, 2026. |
| [`handbook/`](./handbook) | The Financial Operations Handbook for fiscal sponsors and projects. Methodology source covering systems architecture, chart of accounts, fund accounting, reconciliation discipline, intake, grant management, treasury, and sustainability. |
| [`readiness/`](./readiness) | The Foundation Readiness Guide. A two-sided diagnostic for prospective sponsees evaluating whether they're ready to be hosted, and for sponsors evaluating whether to take a project in. |
| [`glossary/`](./glossary) | The Commons Language Glossary. A bilingual reference that translates commons theory and OSS funding vocabulary into FinOps mechanics, with worked examples across AstroPy, Bioconductor, Cryptography, SciPy, Privacy Tech (Tor, Signal), Civic Tech, Climate (Pangeo, OS-Climate), AI safety research, and OSS funding mechanisms. |
| [`case-studies/`](./case-studies) | Year one record of Commons FinOps practice at Metagov. The Atlas Computing transition to Renaissance Philanthropy. The AWS gift reconciliation episode. The endowment proposal. The systems stack. |
| [`templates/`](./templates) | Reserved for templates that operationalize the methodology (intake checklists, chart of accounts shapes, sanctions schedules). Placeholder for now. |

## Who this is for

- **Fiscal sponsor finance and operations leads** building or rebuilding the operational backbone of their organizations
- **Prospective sponsees** evaluating their own readiness to be hosted, or comparing potential homes
- **Foundation program officers** doing serious diligence on potential grantees and fiscal sponsors
- **OSS funding designers** working on core and satellite models, pooled funds, or shared infrastructure for open source ecosystems
- **Digital governance researchers** studying how polycentric institutions actually operate under real funding and compliance pressure
- **AI safety, civic tech, climate tech, privacy tech, and open science communities** organized around shared infrastructure, where the institutional shell matters as much as the code

## The eight principles, in one table

| # | Principle | Operational requirement (FinOps translation) |
|---|---|---|
| 1 | Clearly defined boundaries | Written satellite intake and exit policy, written before anything else |
| 2 | Congruence with local conditions | Layered rule architecture: regulator rules at the account layer, sponsorship choice at the class/project layer |
| 3 | Collective choice arrangements | Sponsorship agreement as protocol for ongoing negotiation; standing channels before scale forces them |
| 4 | Monitoring | Monitoring designed as a service to satellites, not control over them; same screen for monitor and monitored |
| 5 | Graduated sanctions | Written sanctions schedule, drafted before the first sanction is needed |
| 6 | Conflict resolution | Published resolution path; cheap to invoke; faster and lighter than outside counsel |
| 7 | Minimal recognition of rights to organize | Operational maturity as the source of standing to push back on funder and platform over-reach |
| 8 | Nested enterprises | Polycentric governance funded explicitly, including the layer-by-layer monitoring and reporting cost |

The full operational translation lives in [`narrative/eight-principles-from-the-operators-seat.md`](./narrative/eight-principles-from-the-operators-seat.md).

## How to use this repo

1. **For a quick orientation**, read the narrative first. It is the connective tissue.
2. **For methodology**, read the handbook. It is the procedural reference.
3. **For evaluation**, use the readiness guide. It is structured as a checklist you can fill out.
4. **For translation across domains**, use the glossary. Especially helpful when bridging commons theorists, OSS funders, fiscal sponsor practitioners, and traditional nonprofit finance.
5. **For proof of practice**, read the Metagov case study. It shows what a year of doing this work actually looks like, with the numbers, the issues, and the resolutions.

## How to contribute

This is documented practice, not a finished standard. If you operate a fiscal sponsor, a foundation, a sponsored project, or a polycentric institution and you see gaps, errors, or extensions, open an issue or a pull request. The intent is for this practice to compound over many practitioners, not stay locked to one.

See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for the simple intake process.

## About the maintainer

Andrew Ngeseyan is Finance and Operations Director at Metagov and Principal at [ASN Management LLC](https://asnmgt.com). $27M business, 18 years, 16 clean federal and state audits at Community Roots. He runs Commons FinOps as a fractional FinOps practice for fiscal sponsors, foundations, and OSS funding cores.

- Practice: [ASN Management LLC](mailto:andrew@asnmgt.com)
- Currently: Finance and Operations Director, [Metagov Inc.](https://metagov.org)

## License

- Documentation in this repository is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](./LICENSE-docs).
- Any code, templates, or scripts in this repository are licensed under the [MIT License](./LICENSE).

Attribution: Commons FinOps, Andrew Ngeseyan, ASN Management LLC. https://github.com/asnmgt/commons-finops

## Citation

If you cite this work, please use:

> Sané, Andrew. (2026). _Commons FinOps: A Documented Practice for Fiscally Sponsored, Polycentric Institutions._ ASN Management LLC. https://github.com/asnmgt/commons-finops

---

Handle your business.

Andrew Ngeseyan · ASN Management LLC · andrew@asnmgt.com
