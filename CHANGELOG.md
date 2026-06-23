# Changelog

All notable changes to Commons FinOps are recorded here. Format: [Keep a Changelog](https://keepachangelog.com). Versions follow semantic-ish versioning for the published schema; documentation evolves continuously.

## [v0.1] — 2026-06-23

First numbered release. Drafted at the SciOS Core-Satellite Workshop, UN Open Source Week, June 22, 2026, and published here as the canonical reference for early adopters.

### Added
- **`schema/` directory.** The machine-readable funding-block v0.1 spec.
  - `SCHEMA.md`: human-readable specification.
  - `funding-block-v0.1.yaml`: canonical schema reference.
  - `validator.py`: working Python validator.
  - `examples/`: four worked fixtures (template, valid sample, intentional failure, real-world partial).
- **`handbook/00-overview.md`**: new operator-facing table of contents structured as five plain-language sections (operating the books, compliance gates, publishing the data, fiscal sponsor operations, working with funders).
- **`CHANGELOG.md`** (this file).

### Changed
- **README.md** rewritten for operator-first plain language. Automation now framed as a first-class concern. Ostrom moved to "Why this works at the theory layer" near the end.
- **`narrative/` renamed to `foundation/`.** Ostrom theory layer kept as the philosophical foundation, no longer the front door.

### Pending (first-week build)
- Plain-language expansion of handbook sections 01 through 05.
- JSON Schema equivalent of `funding-block-v0.1.yaml` for standard tooling.
- Reference implementations of the validator in JavaScript and Go.
- v0.1 working group convening.

## Earlier history (pre-v0.1)

- 2026-06-10: Initial repository publication. README, ABOUT, ENGAGE, narrative, handbook, readiness, glossary, case-studies, templates scaffolding.
- 2026-06: Iterative cleanup including author name corrections (Sané → Ngeseyan), phone-number removal from public docs, audit-status accuracy corrections (Metagov: audit in preparation, not yet completed), citation surname fix.
