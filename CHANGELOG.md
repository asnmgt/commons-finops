# Changelog

All notable changes to Commons FinOps are recorded here. Format: [Keep a Changelog](https://keepachangelog.com). Versions follow semantic-ish versioning for the published schema; documentation evolves continuously.

## [unreleased]

### Added
- **`templates/policies/`**: three org-agnostic policy templates adapted from live fiscal-sponsor practice.
  - `fiscal-policies-and-procedures-manual.md`: full nonprofit fiscal-policy manual (accounting, internal controls, revenue, expenses, assets, digital assets, fiscal sponsorship annex).
  - `financial-guidelines-for-sponsored-projects.md`: sponsee-facing companion doc — what counts as an in-books expense, how to code it, approval matrix, worked examples.
  - `expense-classification-guidelines.md`: five-principles + hard-rules coding guide with a decision-tree quick reference.
  All three are token-templated: `{{ORG_NAME}}`, `{{THRESHOLD_DFO_REVIEW}}`, `{{PLATFORM_FISCAL_HOST}}`, etc. Every token is documented at the bottom of each doc and mapped to `ai/context.example.yaml`.
- **`ai/`**: local-context + AI-assistant plugin infrastructure.
  - `context.example.yaml`: reference schema for org identity, approval thresholds, time windows, platform bindings, rates, and a free-form `local:` block for chart-of-accounts and project metadata.
  - `init.py`: interactive setup CLI that writes `context.yaml` at the repo root and adds it to `.gitignore`.
  - `render.py`: token-substitution renderer. Missing tokens render as `[SET IN CONTEXT.YAML: TOKEN]` so gaps are visible, not silent.
  - `mcp-server/`: [Model Context Protocol](https://modelcontextprotocol.io) server exposing rendered policies and local context as resources and tools. Wires up to Claude Desktop, Cursor, Continue, Zed, Windsurf, and any MCP-compatible client with a short JSON config snippet. Includes turnkey prompts for `classify_expense` and `approval_check`.

### Changed
- **`.gitignore`**: added `context.yaml`, `context.yml`, `rendered/`, and `__pycache__/` so private organizational values and generated output stay out of version control.
- **README.md**: added a top-level section pointing readers to `templates/policies/` and `ai/` alongside the existing handbook, schema, and foundation layers.

## [v0.1] 2026-06-23

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
