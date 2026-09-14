import asyncio
from typing import Any

from dotenv import load_dotenv

from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ResultMessage,
    create_sdk_mcp_server,
    query,
    tool,
)

load_dotenv()


@tool("add", "Add two numbers together", {"a": float, "b": float})
async def add(args: dict[str, Any]) -> dict[str, Any]:
    result = args["a"] + args["b"]
    return {"content": [{"type": "text", "text": f"Result: {result}"}]}


@tool("multiply", "Multiply two numbers together", {"a": float, "b": float})
async def multiply(args: dict[str, Any]) -> dict[str, Any]:
    result = args["a"] * args["b"]
    return {"content": [{"type": "text", "text": f"Result: {result}"}]}


calculator_server = create_sdk_mcp_server(
    name="calculator",
    version="1.0.0",
    tools=[add, multiply],
)


async def main() -> None:
    prompt = "12.5と7を足して、その結果に3をかけてください。"

    async for message in query(
        prompt=prompt,
        options=ClaudeAgentOptions(
            mcp_servers={"calculator": calculator_server},
            allowed_tools=["mcp__calculator__add", "mcp__calculator__multiply"],
        ),
    ):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if hasattr(block, "text"):
                    print(block.text)
        elif isinstance(message, ResultMessage):
            print(f"--- done ({message.subtype}) ---")
            print(f"cost: ${message.total_cost_usd:.6f}")
            print(f"usage: {message.usage}")


if __name__ == "__main__":
    asyncio.run(main())
