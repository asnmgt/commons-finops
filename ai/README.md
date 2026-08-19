# AI plugin

This folder makes the Commons FinOps policies usable by AI assistants against **your** organization's context — not the template defaults.

## Contents

| File | Purpose |
|---|---|
| [`context.example.yaml`](./context.example.yaml) | Reference schema for your local context. Documents every placeholder token used across `templates/policies/`. |
| [`init.py`](./init.py) | Interactive setup CLI. Prompts for the highest-value fields and writes `context.yaml` at the repo root (git-ignored). |
| [`render.py`](./render.py) | Renders any template file with your context. `{{TOKEN}}` → value from `context.yaml`. Missing tokens render as `[SET IN CONTEXT.YAML: TOKEN]` so they're obvious. |
| [`mcp-server/`](./mcp-server) | Model Context Protocol server. Exposes rendered policies + your local context as resources and tools to Claude Desktop, Cursor, Continue, Zed, and any other MCP client. See [`mcp-server/README.md`](./mcp-server/README.md). |

## Quick start

```bash
# 1. Install dependencies (only needed once)
pip install pyyaml mcp

# 2. Set up your local context (interactive)
python ai/init.py

# 3a. Render policies to plain markdown you can share:
python ai/render.py 'templates/policies/*.md'
# Output lands in rendered/  (git-ignored)

# 3b. Or wire the MCP server up to your AI assistant:
# See ai/mcp-server/README.md for Claude Desktop, Cursor, Continue, Zed configs.
```

## How context is resolved

The templates under `templates/policies/` use placeholder tokens like `{{ORG_NAME}}`, `{{THRESHOLD_DFO_REVIEW}}`, and `{{PLATFORM_FISCAL_HOST}}`. Both `render.py` and the MCP server read from `context.yaml` at the repo root. Precedence for locating context:

1. Explicit `--context <path>` argument (render.py only)
2. `context.yaml` at the repo root
3. `context.yml` at the repo root
4. `ai/context.example.yaml` (fallback — never a good idea in production)

`context.yaml` is added to `.gitignore` by `init.py`, so your organization's thresholds and internal notes do not get committed to a public fork.

## What lives where

- **Template documents:** [`../templates/policies/`](../templates/policies/) — org-agnostic, versioned in the repo, safe to edit and PR upstream.
- **Your organization's values:** `context.yaml` at the repo root — private to your machine or your private fork.
- **Rendered output:** `rendered/` at the repo root — regenerable, git-ignored.
