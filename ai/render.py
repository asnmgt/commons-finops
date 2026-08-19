#!/usr/bin/env python3
"""Render a Commons FinOps template document with your local context.yaml.

Usage:
    python ai/render.py templates/policies/fiscal-policies-and-procedures-manual.md
    python ai/render.py templates/policies/*.md --out rendered/

The render is a pure token substitution: `{{TOKEN}}` → value from context.yaml.
Missing tokens are rendered as `[SET IN CONTEXT.YAML: TOKEN]` so they are
obvious to human reviewers, not silently blank.

No external dependencies beyond PyYAML.
"""

from __future__ import annotations

import argparse
import glob
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with:  pip install pyyaml", file=sys.stderr)
    sys.exit(1)


REPO_ROOT = Path(__file__).resolve().parent.parent

# Token -> yaml path
TOKEN_MAP = {
    "ORG_NAME": ("org", "name"),
    "ORG_LEGAL_NAME": ("org", "legal_name"),
    "ORG_LEGAL_NAME_UPPER": ("org", "legal_name_upper"),
    "ORG_STATE": ("org", "state"),
    "ORG_EIN": ("org", "ein"),
    "ORG_ADDRESS": ("org", "address"),

    "THRESHOLD_DFO_REVIEW": ("thresholds", "dfo_review"),
    "THRESHOLD_BOARD_SECONDARY": ("thresholds", "board_secondary"),
    "THRESHOLD_COMPETITIVE_BIDS": ("thresholds", "competitive_bids"),
    "THRESHOLD_BOARD_EXCEPTION": ("thresholds", "board_exception"),
    "THRESHOLD_DEVIATION": ("thresholds", "deviation"),
    "THRESHOLD_CAPITALIZATION": ("thresholds", "capitalization"),
    "THRESHOLD_SOFTWARE_REVIEW": ("thresholds", "software_review"),
    "THRESHOLD_1099_MIN": ("thresholds", "s1099_min"),
    "THRESHOLD_LINE_ITEM_REVIEW": ("thresholds", "line_item_review"),

    "WINDOW_REIMBURSEMENT": ("windows", "reimbursement"),
    "WINDOW_REIMBURSEMENT_ADJ": ("windows", "reimbursement_adj"),
    "WINDOW_EXPLANATION": ("windows", "explanation"),
    "WINDOW_DFO_APPROVAL": ("windows", "dfo_approval"),
    "WINDOW_MISCODE_FLAG": ("windows", "miscode_flag"),
    "WINDOW_CRYPTO_CONVERSION": ("windows", "crypto_conversion"),
    "WINDOW_CRYPTO_CONVERSION_CAP": ("windows", "crypto_conversion_cap"),

    "PLATFORM_GL": ("platforms", "gl"),
    "PLATFORM_FISCAL_HOST": ("platforms", "fiscal_host"),
    "PLATFORM_CRYPTO_SUB": ("platforms", "crypto_sub"),
    "PLATFORM_CRYPTO_CUSTODIAN": ("platforms", "crypto_custodian"),
    "PLATFORM_CARD_PROCESSOR": ("platforms", "card_processor"),
    "EXTERNAL_ACCOUNTANT": ("platforms", "external_accountant"),

    "HOST_FEE_RATE": ("rates", "host_fee"),

    "PLATFORM_COMMUNITY": ("platforms", "community"),
    "PAYMENT_CADENCE_DAY": ("cadence", "payment_day"),
    "POLICY_EFFECTIVE_DATE": ("policy", "effective_date"),
}


TOKEN_RE = re.compile(r"\{\{([A-Z_0-9]+)\}\}")


def _dig(d: dict[str, Any], path: tuple[str, ...]) -> Any:
    node = d
    for key in path:
        if not isinstance(node, dict):
            return None
        node = node.get(key)
        if node is None:
            return None
    return node


def load_context(path: Path | None = None) -> dict[str, Any]:
    candidates: list[Path]
    if path is not None:
        candidates = [path]
    else:
        candidates = [
            REPO_ROOT / "context.yaml",
            REPO_ROOT / "context.yml",
            REPO_ROOT / "ai" / "context.example.yaml",
        ]

    for c in candidates:
        if c.exists():
            with c.open("r", encoding="utf-8") as f:
                return yaml.safe_load(f) or {}

    raise FileNotFoundError(
        "No context file found. Run `python ai/init.py` or copy "
        "ai/context.example.yaml to context.yaml"
    )


def resolve_token(name: str, ctx: dict[str, Any]) -> str:
    if name == "ORG_LEGAL_NAME_UPPER":
        val = _dig(ctx, TOKEN_MAP[name])
        if val:
            return val
        legal = _dig(ctx, ("org", "legal_name"))
        if legal:
            return str(legal).upper()
        return f"[SET IN CONTEXT.YAML: {name}]"

    if name not in TOKEN_MAP:
        return f"[UNKNOWN TOKEN: {name}]"
    val = _dig(ctx, TOKEN_MAP[name])
    if val in (None, ""):
        return f"[SET IN CONTEXT.YAML: {name}]"
    return str(val)


def render(text: str, ctx: dict[str, Any]) -> str:
    def sub(m: re.Match[str]) -> str:
        return resolve_token(m.group(1), ctx)
    return TOKEN_RE.sub(sub, text)


def render_file(src: Path, dest: Path, ctx: dict[str, Any]) -> None:
    text = src.read_text(encoding="utf-8")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(render(text, ctx), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Render Commons FinOps templates with your context.")
    ap.add_argument("paths", nargs="+", help="Template files or globs to render")
    ap.add_argument("--out", default="rendered", help="Output directory (default: rendered/)")
    ap.add_argument("--context", default=None, help="Path to context.yaml (default: auto-detect)")
    ap.add_argument("--stdout", action="store_true", help="Print rendered content to stdout instead of writing files")
    args = ap.parse_args()

    ctx_path = Path(args.context) if args.context else None
    ctx = load_context(ctx_path)

    out_dir = REPO_ROOT / args.out

    files: list[Path] = []
    for pattern in args.paths:
        matches = glob.glob(pattern) or glob.glob(str(REPO_ROOT / pattern))
        if not matches:
            print(f"WARNING: no files matched: {pattern}", file=sys.stderr)
            continue
        files.extend(Path(m).resolve() for m in matches)

    if not files:
        print("ERROR: no input files found", file=sys.stderr)
        return 1

    unresolved: set[str] = set()

    for src in files:
        text = src.read_text(encoding="utf-8")
        rendered = render(text, ctx)
        for m in TOKEN_RE.finditer(rendered):
            unresolved.add(m.group(1))

        if args.stdout:
            sys.stdout.write(rendered)
        else:
            try:
                rel = src.relative_to(REPO_ROOT)
            except ValueError:
                rel = Path(src.name)
            dest = out_dir / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(rendered, encoding="utf-8")
            print(f"Rendered: {dest.relative_to(REPO_ROOT)}")

    if unresolved:
        print(f"\n{len(unresolved)} unresolved token(s) — check context.yaml:", file=sys.stderr)
        for tok in sorted(unresolved):
            print(f"  - {tok}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
