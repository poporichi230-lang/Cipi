# Cipi

## Composio connector setup

This project wires a [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python)
agent to [Composio](https://composio.dev)'s Tool Router. Composio exposes a single
MCP server that proxies to 1000+ supported apps (GitHub, Gmail, Slack, Notion,
and more), so the agent gets access to whichever apps the Composio user has
connected, without wiring each integration up by hand.

### Setup

```bash
uv add composio claude-agent-sdk
cp .env.example .env
# edit .env and set COMPOSIO_API_KEY
```

### Run

```bash
uv run agent.py
```

`agent.py` creates a Composio Tool Router session for a given `user_id`,
passes its MCP endpoint (`type`, `url`, `headers`) to `ClaudeAgentOptions`,
and then runs a `query(...)` against Claude with that MCP server attached.
Swap the `prompt` in `agent.py` for whatever task you want the agent to run
against the connected apps.

Note: connecting individual apps (GitHub, Gmail, etc.) to your Composio
user happens on Composio's side (via their dashboard/API) — the
`COMPOSIO_API_KEY` alone does not grant access to every app automatically;
each app connection still needs its own auth (OAuth, API key, etc.) set up
through Composio for that `user_id`.
