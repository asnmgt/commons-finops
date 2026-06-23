"""
Commons FinOps funding-block validator (v0.1).

Checks a YAML funding block against the v0.1 proposed schema.

Usage:
    python3 validator.py <file.yaml> [<file.yaml> ...]

Exit codes:
    0  all files valid
    1  one or more files had errors
    2  parse error or usage error

This is a reference implementation. A v0.1 JSON Schema equivalent is in
funding-block-v0.1.yaml for use with standard JSON Schema tooling.
"""
import sys
import re

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


# ---------- v0.1 SCHEMA RULES ----------
ALLOCATION_VOCAB = {
    "usage-weighted",
    "criticality-weighted",
    "roadmap-voted",
    "discretionary",
    "formula",
    "pass-through",
}

CLOSE_CADENCE = {"monthly", "quarterly"}

AUDIT_STATUS_LITERAL = {"none", "in-preparation", "review", "audit"}
AUDIT_STREAK_RE = re.compile(r"^clean-audit-streak-(\d+)$")

TRIPLE_DUTY = ["program", "funder", "restriction"]

EIN_RE = re.compile(r"^\d{2}-\d{7}$")
URL_RE = re.compile(r"^https?://[^\s<>]+$")

REQUIRED = [
    "fiscalHost",
    "ein",
    "ledger",
    "closeCadence",
    "auditStatus",
    "allocationRule",
    "classTaxonomy",
]

OPTIONAL = [
    "disbursements",
    "restrictedFundsPolicy",
    "inKindPolicy",
    "hostOverhead",
]

KNOWN = set(REQUIRED + OPTIONAL)


def looks_placeholder(v):
    """Detect <angle-bracket> placeholders so template YAML doesn't false-flag."""
    return isinstance(v, str) and v.strip().startswith("<") and v.strip().endswith(">")


def validate(doc):
    """Return (errors, warnings) for a parsed YAML document."""
    errors, warnings = [], []

    if not isinstance(doc, dict) or "funding" not in doc:
        return ["Top-level must be a mapping with a 'funding:' key."], []

    fb = doc["funding"]
    if not isinstance(fb, dict):
        return ["'funding' must be a mapping."], []

    # 1. Required fields present
    for k in REQUIRED:
        if k not in fb:
            errors.append(f"Missing required field: {k}")

    # 2. Unknown fields (warning, not error: schema is ignore-unknown)
    for k in fb:
        if k not in KNOWN:
            warnings.append(f"Unknown field (consumers will ignore): {k}")

    # 3. Type and format checks
    def is_str(k):
        return isinstance(fb.get(k), str)

    if "fiscalHost" in fb and not is_str("fiscalHost"):
        errors.append("fiscalHost must be a string.")

    if "ein" in fb:
        v = fb["ein"]
        if not is_str("ein"):
            errors.append("ein must be a string.")
        elif not looks_placeholder(v) and not EIN_RE.match(v):
            errors.append(f"ein must match pattern NN-NNNNNNN (got: {v!r})")

    for url_field in ["ledger", "disbursements", "restrictedFundsPolicy", "inKindPolicy"]:
        if url_field in fb:
            v = fb[url_field]
            if not is_str(url_field):
                errors.append(f"{url_field} must be a string.")
            elif not looks_placeholder(v) and not URL_RE.match(v):
                errors.append(f"{url_field} must be an http(s) URL (got: {v!r})")

    if "closeCadence" in fb:
        v = fb["closeCadence"]
        if v not in CLOSE_CADENCE:
            errors.append(
                f"closeCadence must be one of {sorted(CLOSE_CADENCE)} (got: {v!r})"
            )

    if "auditStatus" in fb:
        v = fb["auditStatus"]
        valid = v in AUDIT_STATUS_LITERAL or (
            isinstance(v, str) and AUDIT_STREAK_RE.match(v)
        )
        if not valid:
            errors.append(
                f"auditStatus must be one of {sorted(AUDIT_STATUS_LITERAL)} "
                f"or match 'clean-audit-streak-N' (got: {v!r})"
            )

    if "allocationRule" in fb:
        v = fb["allocationRule"]
        if looks_placeholder(v):
            warnings.append("allocationRule is a placeholder; fill in before publishing.")
        elif v not in ALLOCATION_VOCAB:
            errors.append(
                f"allocationRule must be in the named vocabulary "
                f"{sorted(ALLOCATION_VOCAB)} (got: {v!r})"
            )

    # 4. Triple-duty class taxonomy. NON-NEGOTIABLE.
    if "classTaxonomy" in fb:
        v = fb["classTaxonomy"]
        if not isinstance(v, list):
            errors.append("classTaxonomy must be a list.")
        else:
            missing = [d for d in TRIPLE_DUTY if d not in v]
            extras = [d for d in v if d not in TRIPLE_DUTY]
            if missing:
                errors.append(
                    f"classTaxonomy must include the triple-duty axes "
                    f"{TRIPLE_DUTY}. Missing: {missing}"
                )
            if extras:
                warnings.append(
                    f"classTaxonomy has extra axes beyond triple-duty: {extras}. "
                    f"Permitted, but most consumers will only read the three core axes."
                )

    if "hostOverhead" in fb:
        v = fb["hostOverhead"]
        if not isinstance(v, (int, float)):
            errors.append("hostOverhead must be a number (decimal).")
        elif not (0 <= v <= 1):
            errors.append(
                f"hostOverhead must be between 0 and 1 (got: {v}). "
                f"Use 0.15 for 15%, not 15."
            )

    return errors, warnings


def main(paths):
    rc = 0
    for path in paths:
        try:
            with open(path) as f:
                doc = yaml.safe_load(f)
        except FileNotFoundError:
            print(f"[NOT FOUND] {path}")
            rc = max(rc, 2)
            continue
        except yaml.YAMLError as e:
            print(f"[PARSE ERROR] {path}")
            print(f"  {e}")
            rc = max(rc, 2)
            continue

        errors, warnings = validate(doc)
        print(f"\n=== {path} ===")
        if not errors and not warnings:
            print("  VALID. No errors, no warnings.")
            continue
        if errors:
            print(f"  ERRORS ({len(errors)}):")
            for e in errors:
                print(f"    - {e}")
            rc = max(rc, 1)
        if warnings:
            print(f"  WARNINGS ({len(warnings)}):")
            for w in warnings:
                print(f"    - {w}")
    return rc


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
