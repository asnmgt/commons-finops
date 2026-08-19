#!/usr/bin/env python3
"""Commons FinOps MCP server.

Exposes the rendered policy templates and your local context as MCP
resources and tools that AI assistants (Claude Desktop, Cursor, Continue,
Zed, etc.) can consume.

Resources:
  finops://policies/fiscal-policies-and-procedures-manual
  finops://policies/financial-guidelines-for-sponsored-projects
  finops://policies/expense-classification-guidelines
  finops://context/local
  finops://context/full

Tools:
  render_policy(name)         Render a single policy with your context
  lookup_variable(name)       Return the resolved value of a context variable
  list_policies()             List available policy documents
  search_policies(query)      Case-insensitive substring search across rendered docs

Install:
    pip install mcp pyyaml

Wire up (Claude Desktop):
    Add to ~/Library/Application Support/Claude/claude_desktop_config.json:
    {
      "mcpServers": {
        "commons-finops": {
          "command": "python",
          "args": ["/absolute/path/to/commons-finops/ai/mcp-server/server.py"]
        }
      }
    }

Wire up (Cursor / Continue / Zed):
    See ai/mcp-server/README.md for editor-specific config snippets.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
AI_DIR = REPO_ROOT / "ai"
POLICIES_DIR = REPO_ROOT / "templates" / "policies"

sys.path.insert(0, str(AI_DIR))
try:
    from render import load_context, render, TOKEN_MAP, resolve_token  # noqa: E402
except ImportError as e:
    print(f"ERROR: could not import render.py: {e}", file=sys.stderr)
    sys.exit(1)

# The `mcp` SDK exposes the high-level server class under two different names
# depending on version. Support both so users don't have to pin a version.
try:
    from mcp.server.fastmcp import FastMCP as _Server  # v1.x SDK
except ImportError:
    try:
        from mcp.server.mcpserver import MCPServer as _Server  # v2.x SDK
    except ImportError:
        print(
            "ERROR: The `mcp` package is required. Install with:  pip install mcp",
            file=sys.stderr,
        )
        sys.exit(1)


mcp = _Server("commons-finops")


def _policies() -> dict[str, Path]:
    if not POLICIES_DIR.exists():
        return {}
    return {p.stem: p for p in sorted(POLICIES_DIR.glob("*.md"))}


def _load_ctx() -> dict:
    try:
        return load_context()
    except FileNotFoundError:
        return {}


# ============================================================
# Resources
# ============================================================

@mcp.resource("finops://policies/{name}")
def policy_resource(name: str) -> str:
    """Return the named policy document rendered with your local context."""
    policies = _policies()
    if name not in policies:
        available = ", ".join(policies) or "(none — check templates/policies/)"
        return f"Unknown policy: {name}\nAvailable: {available}"
    text = policies[name].read_text(encoding="utf-8")
    return render(text, _load_ctx())


@mcp.resource("finops://context/local")
def local_context() -> str:
    """Return the free-form `local:` section of context.yaml (chart of accounts, projects, people, notes)."""
    ctx = _load_ctx()
    local = ctx.get("local", {})
    if not local:
        return "No local context set. Edit context.yaml to add chart-of-accounts, projects, people, or notes."
    import yaml
    return yaml.safe_dump(local, sort_keys=False, allow_unicode=True)


@mcp.resource("finops://context/full")
def full_context() -> str:
    """Return the entire context.yaml as YAML (org identity, thresholds, windows, platforms, rates, local)."""
    ctx = _load_ctx()
    if not ctx:
        return "No context.yaml found. Run `python ai/init.py` to create one."
    import yaml
    return yaml.safe_dump(ctx, sort_keys=False, allow_unicode=True)


@mcp.resource("finops://policies")
def policies_index() -> str:
    """Index of available policy documents in this repo."""
    policies = _policies()
    if not policies:
        return "No policies found under templates/policies/."
    lines = ["# Available policy documents", ""]
    for name, path in policies.items():
        first_heading = _first_heading(path)
        lines.append(f"- `finops://policies/{name}` — {first_heading}")
    return "\n".join(lines)


def _first_heading(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        # Skip the leading template-notice blockquote
        if stripped.startswith("#") and not stripped.startswith("##"):
            return stripped.lstrip("#").strip()
        m = re.match(r"^\*\*(.+?)\*\*\s*$", stripped)
        if m:
            return m.group(1)
    return path.stem


# ============================================================
# Tools
# ============================================================

@mcp.tool()
def list_policies() -> list[str]:
    """List available policy documents in this repo."""
    return list(_policies().keys())


@mcp.tool()
def render_policy(name: str) -> str:
    """Render a single policy with your local context. Same output as finops://policies/{name}."""
    policies = _policies()
    if name not in policies:
        raise ValueError(f"Unknown policy: {name}. Available: {list(policies.keys())}")
    text = policies[name].read_text(encoding="utf-8")
    return render(text, _load_ctx())


@mcp.tool()
def lookup_variable(name: str) -> str:
    """Look up a single context variable by token name (e.g. THRESHOLD_DFO_REVIEW, ORG_NAME).

    Returns the value from context.yaml, or `[SET IN CONTEXT.YAML: NAME]` if unset.
    """
    ctx = _load_ctx()
    token = name.strip().strip("{}").upper()
    return resolve_token(token, ctx)


@mcp.tool()
def list_variables() -> dict[str, str]:
    """Return a dictionary of every known token and its resolved value."""
    ctx = _load_ctx()
    return {tok: resolve_token(tok, ctx) for tok in TOKEN_MAP}


@mcp.tool()
def search_policies(query: str, context_lines: int = 2) -> str:
    """Case-insensitive substring search across all rendered policy documents.

    Returns matching lines with `context_lines` lines of surrounding context.
    """
    if not query.strip():
        return "Empty query."
    q = query.lower()
    ctx = _load_ctx()
    results: list[str] = []
    for name, path in _policies().items():
        rendered = render(path.read_text(encoding="utf-8"), ctx).splitlines()
        hits = [i for i, line in enumerate(rendered) if q in line.lower()]
        if not hits:
            continue
        results.append(f"\n## {name}\n")
        seen: set[int] = set()
        for i in hits:
            lo = max(0, i - context_lines)
            hi = min(len(rendered), i + context_lines + 1)
            for j in range(lo, hi):
                if j in seen:
                    continue
                seen.add(j)
                marker = ">>> " if j == i else "    "
                results.append(f"{marker}L{j+1}: {rendered[j]}")
            results.append("---")
    return "\n".join(results) if results else f"No matches for `{query}`."


# ============================================================
# Prompts (helpful defaults users can invoke)
# ============================================================

@mcp.prompt()
def classify_expense(description: str, amount: str = "", vendor: str = "") -> str:
    """Ask the AI to classify a spend using the Expense Classification Guidelines."""
    return f"""You have access to the Commons FinOps policy documents via the `finops://` resources.

Please classify this expense using the rules in `finops://policies/expense-classification-guidelines`:

- **Description:** {description}
- **Amount:** {amount or "(not specified)"}
- **Vendor:** {vendor or "(not specified)"}

Steps:
1. Read `finops://policies/expense-classification-guidelines`.
2. Read `finops://context/local` for any org-specific chart of accounts or projects that apply.
3. Return: (a) whether this is a project or core expense, (b) the recommended GL code, (c) any approval or documentation required per `finops://policies/fiscal-policies-and-procedures-manual`, and (d) any flags or questions to verify before recording."""


@mcp.prompt()
def approval_check(amount: str, description: str = "") -> str:
    """Ask the AI which approvals are required for a given spend amount."""
    return f"""Using `finops://policies/fiscal-policies-and-procedures-manual`, tell me the full approval chain required for this spend:

- **Amount:** {amount}
- **Description:** {description or "(not specified)"}

Cross-reference the thresholds in `finops://context/full` (thresholds section) with the policy sections, and list every approver who must sign before the money moves, plus any documentation minimums (competitive bids, board resolution, etc.)."""


if __name__ == "__main__":
    mcp.run()
