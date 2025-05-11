from fastmcp import Client
import asyncio

client = Client("my_server.py")

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)

if __name__ == "__main__":
    asyncio.run(call_tool("Ford")) 