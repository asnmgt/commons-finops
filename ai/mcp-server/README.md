# Commons FinOps MCP Server

An [MCP](https://modelcontextprotocol.io) server that exposes the Commons FinOps policy templates and your local context to any MCP-compatible AI assistant — Claude Desktop, Cursor, Continue, Zed, Windsurf, and others.

## Why this exists

The templates in `templates/policies/` are org-agnostic. Your organization is not. The MCP server closes that gap: it renders each template with the values from your `context.yaml` on the fly and serves them as first-class resources your AI can address by URI.

That way, when someone in your ops team asks the AI "does a $28,000 contractor engagement need three bids?", the AI answers using **your** thresholds — not the template defaults, and not whatever the model happens to have memorized about fiscal policy in general.

## Install

```bash
pip install mcp pyyaml
```

The server auto-detects whether you have the v1.x SDK (`mcp.server.fastmcp.FastMCP`) or the v2.x SDK (`mcp.server.mcpserver.MCPServer`) and uses whichever is present. No version pin required.

If you have not yet set up your local context, run:

```bash
python ai/init.py
```

That will interactively write `context.yaml` at the repo root. It is git-ignored automatically.

## Wire up your assistant

### Claude Desktop

Edit `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "commons-finops": {
      "command": "python",
      "args": ["/absolute/path/to/commons-finops/ai/mcp-server/server.py"]
    }
  }
}
```

Restart Claude Desktop. In a new conversation, you should see the `commons-finops` server listed under Attach → Add from server.

### Cursor

Edit `~/.cursor/mcp.json` (or the workspace `.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "commons-finops": {
      "command": "python",
      "args": ["/absolute/path/to/commons-finops/ai/mcp-server/server.py"]
    }
  }
}
```

### Continue (VS Code / JetBrains)

Add to your Continue config `~/.continue/config.json`:

```json
{
  "experimental": {
    "modelContextProtocolServers": [
      {
        "transport": {
          "type": "stdio",
          "command": "python",
          "args": ["/absolute/path/to/commons-finops/ai/mcp-server/server.py"]
        }
      }
    ]
  }
}
```

### Zed

In your `~/.config/zed/settings.json`:

```json
{
  "context_servers": {
    "commons-finops": {
      "command": {
        "path": "python",
        "args": ["/absolute/path/to/commons-finops/ai/mcp-server/server.py"]
      }
    }
  }
}
```

### Other MCP clients

Any MCP-compatible client can attach to this server over stdio. The command is `python ai/mcp-server/server.py`. No environment variables are required; the server reads `context.yaml` from the repo root by convention.

## What the server exposes

### Resources (addressable, cacheable)

| URI | Content |
|---|---|
| `finops://policies` | Index of every policy doc in `templates/policies/` |
| `finops://policies/fiscal-policies-and-procedures-manual` | Manual, rendered with your context |
| `finops://policies/financial-guidelines-for-sponsored-projects` | Sponsee-facing guidelines, rendered |
| `finops://policies/expense-classification-guidelines` | Coding guidelines, rendered |
| `finops://context/local` | Your `local:` block — chart of accounts, projects, people, notes |
| `finops://context/full` | The full `context.yaml` as YAML |

### Tools (callable actions)

| Tool | Purpose |
|---|---|
| `list_policies()` | Enumerate policy documents |
| `render_policy(name)` | Render a policy with your context (same as the resource) |
| `lookup_variable(name)` | Return a single resolved token (`THRESHOLD_DFO_REVIEW`, `ORG_NAME`, etc.) |
| `list_variables()` | Dump every token and its resolved value |
| `search_policies(query, context_lines=2)` | Substring search across all rendered policies |

### Prompts (turnkey workflows)

Both are invoked as slash-commands or attachments depending on your client.

| Prompt | Args | Effect |
|---|---|---|
| `classify_expense` | `description`, `amount`, `vendor` | Ask the AI to classify a spend, cite the guideline section, and return the GL code + approval chain |
| `approval_check` | `amount`, `description` | Ask the AI to list every approver required at that dollar amount, cross-referencing your thresholds |

## What "local context" means

The `local:` section of `context.yaml` is free-form. Anything you put there becomes available to the AI via `finops://context/local` alongside the standard policies. Common uses:

- **`chart_of_accounts`** — map your account codes to descriptions so the AI recommends codes that actually exist in your GL.
- **`projects`** — list your sponsored projects and their class codes so the AI can identify which one an expense belongs to.
- **`people`** — name your DFO, ED, and Board President so the AI can suggest the right escalation.
- **`notes`** — anything else the AI should treat as authoritative for your org.

The server does not send your `context.yaml` anywhere. It reads the file locally and returns rendered text to the AI client, over the same stdio channel MCP uses for everything else.

## Debugging

Run the server directly to check startup:

```bash
python ai/mcp-server/server.py
```

Because MCP servers speak stdio, you will see no output until a client connects. To sanity-check the render pipeline outside MCP:

```bash
python ai/render.py 'templates/policies/*.md' --out rendered/
```

The rendered docs land in `rendered/` (git-ignored).

## Extending

- **New policy docs.** Drop any `.md` file into `templates/policies/`. The server picks it up automatically.
- **New tokens.** Add them to `TOKEN_MAP` in `ai/render.py`. They then work everywhere: `render.py`, the MCP server, and any file that uses `{{TOKEN}}`.
- **New tools or resources.** Edit `server.py` — the `FastMCP` decorators make this straightforward. PRs welcome.
