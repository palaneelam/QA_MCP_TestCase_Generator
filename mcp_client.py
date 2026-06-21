from fastmcp import Client
from fastmcp.client.transports import PythonStdioTransport

async def get_requirement_from_mcp(file_name):
    transport = PythonStdioTransport(
        script_path="mcp_servers/filesystem_server.py"
    )

    client = Client(transport)

    async with client:

        tools = await client.list_tools()

        print("\nAvailable MCP Tools:")

        for tool in tools:
            print(tool.name)

        result = await client.call_tool(
            "read_requirement_file",
            {
                "file_name": file_name
            }
        )

        return result.data