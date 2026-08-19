# Commons FinOps

**An open-source FinOps standard for fiscal sponsors, cores, and the projects they host. Grounded in Ostrom's eight design principles for commons governance.**

If you fund open source, run a fiscal sponsor, host research software, or operate a public-goods grant program, this repository is for you. It's the working manual for how to publish funding accountability that funders, auditors, and AI agents can all read the same way.

## What this is

Commons FinOps is three things in one repo:

1. **An operations and finance handbook.** Plain-language guidance anchored in real compliance frameworks: nonprofit GAAP (FASB ASC 958), federal Uniform Guidance (2 CFR 200), OFAC sanctions, 1099/W-8/W-9, restricted fund accounting, and clean monthly close discipline. Written by an operator, for operators.

2. **A machine-readable funding-accountability standard.** The `funding-block v0.1` schema lives in [`schema/`](./schema). It's the data interface that lets a funder evaluate one core covering fifty packages instead of running due diligence on fifty packages individually. YAML schema, working validator, and example fixtures included.

3. **A theoretical foundation, kept in its place.** Elinor Ostrom's eight principles for enduring commons are what makes the operational standard hold together over time. They live in [`foundation/`](./foundation). They're the why. The handbook and schema are the what and how.

## What this solves

Funders today move money to fiscal sponsors, who hold restricted funds on behalf of grantees and disburse them. The bookkeeping discipline at the sponsor layer is the thing that determines whether everything downstream is real or theater. **Most of that discipline is invisible from the outside.** It lives in QuickBooks files, in monthly reconciliations, in audit workpapers that nobody publishes. As a result:

- Funders can't compare cores. Every conversation with a new fiscal host starts from zero.
- AI agents can't read funding accountability. The data is there; it just isn't surfaced.
- Auditors keep finding the same problems in new organizations because nobody publishes a how-to.
- Operators reinvent the wheel at every shop because the standard hasn't been written down.

Commons FinOps publishes the standard so the next operator can inherit the work instead of paying the reinvention tax. The schema makes that work machine-readable so funders and agents can read it without asking the operator to translate.

## Automation is a first-class concern

Funders are signaling clearly that **automation is now a requirement, not a luxury**. Sponsors that can't expose ledgers, transaction tags, and audit status in machine-readable form will lose ground to sponsors that can. The handbook calls out, at every section, which steps can be automated, which require human review, and which audit trails need to survive the automation. Automation is not the opposite of compliance. It is the only way to make compliance scale.

## What's in here

| Path | Contents |
|---|---|
| [`README.md`](./README.md) | You are here. |
| [`handbook/`](./handbook) | The operations and finance handbook. Five plain-language sections covering the books, compliance gates, publishing data, fiscal sponsor operations, and working with funders. |
| [`schema/`](./schema) | `funding-block v0.1`: the machine-readable spec. YAML schema, working Python validator, four worked example fixtures (template, filled-in sample, intentional-failure, real-world partial). |
| [`foundation/`](./foundation) | Ostrom's eight principles as the theoretical foundation. The narrative as delivered at UN Open Source Week, June 22, 2026. The spoken cut. |
| [`readiness/`](./readiness) | The Foundation Readiness Guide. A two-sided diagnostic for projects evaluating whether they're ready to be hosted, and for sponsors evaluating whether to take a project on. |
| [`glossary/`](./glossary) | The Commons Language Glossary. Translates commons theory, OSS funding vocabulary, and traditional nonprofit finance into a single working vocabulary. |
| [`case-studies/`](./case-studies) | Year-one record of Commons FinOps practice at Metagov. The Atlas Computing transition. The AWS gift reconciliation episode ($75K real receipt, $225K apparent value, fully traced). The endowment proposal. The systems stack. |
| [`templates/`](./templates) | Operational templates: funding-block YAML template, monthly close checklist, audit-readiness checklist, sponsee onboarding checklist. |
| [`templates/policies/`](./templates/policies) | Four ready-to-adopt policy templates: Fiscal Policies & Procedures Manual, Financial Guidelines for Sponsored Projects, Expense Classification Guidelines, and Fiscal Project Onboarding Guide. Fully org-agnostic — token-templated with `{{ORG_NAME}}`, `{{THRESHOLD_DFO_REVIEW}}`, etc. |
| [`ai/`](./ai) | Local-context configuration + Model Context Protocol server that renders these templates against your organization's values and serves them to Claude Desktop, Cursor, Continue, Zed, and other MCP-compatible AI assistants. |
| [`ABOUT.md`](./ABOUT.md) | Author background, project history, scope. |
| [`ENGAGE.md`](./ENGAGE.md) | How to engage. Tiers, pricing, contact. |
| [`CHANGELOG.md`](./CHANGELOG.md) | Version history. |

## Who this is for

- **Fiscal sponsor finance and operations leads** building or rebuilding the operational backbone of their organizations.
- **Foundations and grantmakers** who want to publish a funding-accountability requirement that grantees can actually meet, or who want to evaluate a sponsor before committing.
- **Open source funding designers** working on core-and-satellite models, pooled funds, or shared infrastructure for OSS ecosystems.
- **Project leads and prospective sponsees** evaluating their own operational readiness, or comparing potential fiscal hosts.
- **AI safety, civic tech, climate, privacy, and open science communities** organized around shared infrastructure, where the institutional shell matters as much as the code.

## How to start

1. **If you want the front door,** read this README and the handbook overview at [`handbook/00-overview.md`](./handbook/00-overview.md).
2. **If you want to see the machine-readable standard,** open [`schema/SCHEMA.md`](./schema/SCHEMA.md) and the YAML examples in [`schema/examples/`](./schema/examples).
3. **If you want to evaluate your own readiness,** start with [`readiness/foundation-readiness-guide.md`](./readiness/foundation-readiness-guide.md).
4. **If you want ready-to-adopt policies,** open [`templates/policies/`](./templates/policies). Four templates cover the fiscal policies manual, sponsee-facing guidelines, expense coding, and prospective-project onboarding.
5. **If you want your AI assistant to answer questions using your organization's policies and thresholds,** set up the [AI plugin](./ai) (`python ai/init.py`, then wire the [MCP server](./ai/mcp-server) into Claude Desktop, Cursor, Continue, or Zed).

## AI plugin: your policies, your assistant

The policy templates in [`templates/policies/`](./templates/policies) are org-agnostic on purpose — every threshold, platform name, and identifier is a token like `{{THRESHOLD_DFO_REVIEW}}` or `{{PLATFORM_FISCAL_HOST}}`. The [`ai/`](./ai) folder resolves those tokens against your local `context.yaml` and exposes the rendered documents to any AI assistant that speaks the [Model Context Protocol](https://modelcontextprotocol.io).

```bash
# One-time setup
pip install pyyaml mcp
python ai/init.py

# Wire the MCP server into your assistant
# (see ai/mcp-server/README.md for Claude Desktop, Cursor, Continue, Zed configs)
```

Once connected, your AI can answer *"does a $28,000 contractor engagement need three bids?"* by reading your board-adopted thresholds, not the model's memorized generalities. See [`ai/README.md`](./ai/README.md) for the full walkthrough.

## More entry points

- **If you want the theoretical foundation,** read [`foundation/eight-principles-from-the-operators-seat.md`](./foundation/eight-principles-from-the-operators-seat.md).
- **If you want to engage,** see [`ENGAGE.md`](./ENGAGE.md).

## Why this works at the theory layer

Ostrom's research showed that commons sustained over generations all share eight design principles. The operating standard in this handbook is what it takes to actually implement those principles in a modern fiscal sponsor or OSS funding core. The principles aren't decoration. They're the load-bearing structure. They live in [`foundation/`](./foundation) so the operating layer can be read first, and the theory can be read by anyone who wants to know why this particular set of operational requirements and not some other set.

## License

Docs: CC BY 4.0 ([`LICENSE-docs`](./LICENSE-docs)). Code and schemas: MIT ([`LICENSE`](./LICENSE)).

## Author

Andrew Ngeseyan. Finance & Operations Director, [Metagov](https://metagov.org). ASN Management LLC. andrew@asnmgt.com.
