"""agent.py — Claude Agent SDK + Composio.

Connects a Claude agent to Composio's Tool Router MCP server, giving it
access to 1000+ third-party app integrations (GitHub, Gmail, Slack,
Notion, etc.) without wiring up each one individually.

Setup:
    uv add composio claude-agent-sdk
    cp .env.example .env  # then fill in COMPOSIO_API_KEY

Run:
    uv run agent.py
"""

import asyncio
import os

from composio import Composio
from claude_agent_sdk import ClaudeAgentOptions, query
from dotenv import load_dotenv

load_dotenv()

if not os.environ.get("COMPOSIO_API_KEY"):
    raise RuntimeError(
        "COMPOSIO_API_KEY is not set. Copy .env.example to .env and fill it in, "
        "or export it in your shell."
    )

composio = Composio()
USER_ID = "user_9kzsi"

# Create a Composio Tool Router session — this exposes an MCP server that
# proxies to whichever of the 1000+ Composio-supported apps the user has
# connected (GitHub, Gmail, Slack, Notion, etc.).
session = composio.create(user_id=USER_ID)


async def main() -> None:
    options = ClaudeAgentOptions(
        system_prompt="You are a helpful assistant",
        permission_mode="bypassPermissions",
        mcp_servers={
            "composio": {
                "type": session.mcp.type,
                "url": session.mcp.url,
                "headers": session.mcp.headers,
            }
        },
    )

    async for message in query(
        prompt="Star the composiohq/composio repo on GitHub",
        options=options,
    ):
        print(message)


if __name__ == "__main__":
    asyncio.run(main())
