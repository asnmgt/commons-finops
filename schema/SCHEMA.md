# Funding Block v0.1

A machine-readable interface block that a core, a fiscal sponsor, or a project can publish so that funders, auditors, and AI agents can read its funding accountability surface without asking the operator to translate.

The funding block is an optional interface block in the [SciOS Core-Satellite schema](https://scios.tech). It sits next to other optional blocks (agent, conflicts) and extends the four required schema fields. A core can exist without a funding block. It will not be funded by foundations that require one.

This is **v0.1**, drafted at the SciOS Core-Satellite Workshop on June 22, 2026 (UN Open Source Week), and published here as the canonical reference for early adopters.

## What it specifies

| Field | Required | Type | Description |
|---|---|---|---|
| `fiscalHost` | Required | string | The legal entity that holds funds on behalf of the project. Example: `NumFOCUS`, `Open Source Collective`, `Metagov`. |
| `ein` | Required | string | The fiscal host's EIN, in `NN-NNNNNNN` format. For non-US hosts, the equivalent national tax identifier. |
| `ledger` | Required | URL | The public ledger URL. Example: `https://opencollective.com/astropy`. |
| `closeCadence` | Required | enum | One of `monthly` or `quarterly`. The cadence at which the host closes books. |
| `auditStatus` | Required | enum or pattern | One of `none`, `in-preparation`, `review`, `audit`, or `clean-audit-streak-N` where `N` is the number of consecutive years of unqualified audit opinions. |
| `allocationRule` | Required | enum (vocabulary) | One of the named values from the allocation-rule vocabulary below. |
| `classTaxonomy` | Required | list | Must include at minimum the three triple-duty axes: `program`, `funder`, `restriction`. Additional axes permitted. |
| `disbursements` | Optional | URL | Append-only feed of disbursement transactions. JSON or CSV. |
| `restrictedFundsPolicy` | Optional | URL | Link to the host's restricted funds policy document. |
| `inKindPolicy` | Optional | URL | Link to the host's in-kind gift valuation policy. |
| `hostOverhead` | Optional | decimal | The host's indirect overhead rate, as a decimal. Example: `0.15` for 15%. |

## Allocation-rule vocabulary

The `allocationRule` field must be a named value from the following finite vocabulary. Open-text allocation rules make cores impossible to compare across funders.

| Value | Meaning |
|---|---|
| `usage-weighted` | Distribution weighted by downloads, dependents, citations, or other measured usage signal. |
| `criticality-weighted` | Distribution weighted by load-bearing position in the dependency graph, deepest first. |
| `roadmap-voted` | Member-voted allocation via a published funding cycle. AstroPy's Funding Cycle is the canonical reference. |
| `discretionary` | Board, finance committee, or principal investigator decides. Documented but not formulaic. |
| `formula` | Published formula, e.g. NIH-style modular budget caps, or proportional to certain measurable inputs. |
| `pass-through` | The core re-grants from an upstream funder with minimal allocation discretion. |

If your allocation rule doesn't fit cleanly into one of these six, propose a new value via pull request. The vocabulary is open to extension, but values must be named, defined, and contrastable with the existing six.

## The triple-duty class taxonomy

The `classTaxonomy` field is the most operationally consequential part of the funding block. It specifies that every transaction in the ledger is classified on three independent axes:

1. **Program.** What the dollar is being spent on. Not a department or cost center. The mission output. Examples: `canonical-maintenance`, `eval-suite-build`, `satellite-stipend`, `documentation`.
2. **Funder.** Where the dollar came from. Each grant, donation, or revenue stream gets a unique tag for audit-trail purposes.
3. **Restriction.** Whether the dollar is `unrestricted`, `time-restricted`, `purpose-restricted`, or `board-designated`. Drives release timing and reporting obligations.

These three axes never collapse into one. If they collapse, the books lie. Most fiscal hosts today track these axes in their internal accounting system (QuickBooks Online, Sage Intacct, NetSuite) but do not surface them to the public ledger. The funding block's most operationally consequential requirement is that the internal class tags surface to the public feed.

## Validation

A Python reference validator is included at [`validator.py`](./validator.py). It checks any YAML funding block against the v0.1 schema and reports errors and warnings.

```bash
python3 schema/validator.py schema/examples/02-metagov-sample.yaml
```

Four example fixtures live in [`examples/`](./examples):

| File | Purpose |
|---|---|
| [`01-template.yaml`](./examples/01-template.yaml) | The bare template with `<placeholder>` values. Use as a starting point. |
| [`02-metagov-sample.yaml`](./examples/02-metagov-sample.yaml) | A complete, valid example modeled on what a Metagov funding block could look like at publication time. |
| [`03-broken-allocation.yaml`](./examples/03-broken-allocation.yaml) | Intentional failure. Uses an allocation rule outside the named vocabulary, and omits the `restriction` axis from the class taxonomy. The validator catches both. |
| [`04-astropy-partial.yaml`](./examples/04-astropy-partial.yaml) | Modeled on AstroPy's current publishable state. Shows what a "partial core" looks like through the funding-block lens. Four required fields are missing. |

## Versioning

This is **v0.1**, a public draft. Breaking changes will be released as v0.2, v0.3, etc., until a v1.0 is published. The schema follows semantic-ish versioning: minor versions add fields or refine vocabulary; major versions break consumers.

A working group of fiscal hosts and a couple of operating cores is the right body to maintain this schema after v0.1. We're not there yet. Until that body exists, the maintainer of record is Andrew Ngeseyan via this repository. Pull requests and issues welcome.

## Status

- Schema: drafted, v0.1, this document.
- Validator: working ([`validator.py`](./validator.py)).
- Example fixtures: four published.
- Plain-language handbook section explaining the schema: drafted at [`handbook/03-publishing-the-data.md`](../handbook/03-publishing-the-data.md), pending detailed expansion in the first-week build.
- v0.1 working group: not yet convened.
- JSON Schema equivalent for tooling integration: planned, not yet drafted.
- Reference implementations in other languages: planned, not yet drafted.

## Why this matters

A funder evaluating fifty packages individually is doing fifty parallel due-diligence runs. A funder evaluating one core that exposes a funding block is doing one. That's not a marginal speedup. That's an order of magnitude.

The funding block is the surface that makes that speedup real. KYB happens once at the fiscal-host layer. Audit happens once at the host's fiscal year. Class taxonomy is already maintained in the host's internal books. The block doesn't ask hosts to do new work. It asks them to publish work they already do.
