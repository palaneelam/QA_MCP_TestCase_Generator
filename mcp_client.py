from pathlib import Path

from fastmcp import Client
from fastmcp.client.transports import PythonStdioTransport


def _get_server_path():
    return (
        Path(__file__).parent
        / "mcp_servers"
        / "filesystem_server.py"
    )


async def call_mcp_tool(tool_name, arguments=None):
    server_path = _get_server_path()

    transport = PythonStdioTransport(
        script_path=str(server_path)
    )

    client = Client(transport)

    async with client:
        result = await client.call_tool(
            tool_name,
            arguments or {}
        )

        return result.data


async def show_available_tools():
    server_path = _get_server_path()

    transport = PythonStdioTransport(
        script_path=str(server_path)
    )

    client = Client(transport)

    async with client:
        tools = await client.list_tools()

        print("\nAvailable MCP Tools:")

        for tool in tools:
            print(f"- {tool.name}")


async def list_files_from_mcp():
    return await call_mcp_tool(
        "list_requirement_files"
    )


async def read_requirement_from_mcp(file_name):
    return await call_mcp_tool(
        "read_requirement_file",
        {
            "file_name": file_name
        }
    )


async def generate_scenarios_from_mcp(file_name):
    return await call_mcp_tool(
        "generate_test_scenarios",
        {
            "file_name": file_name
        }
    )


async def generate_test_cases_from_mcp(file_name):
    return await call_mcp_tool(
        "generate_test_cases",
        {
            "file_name": file_name
        }
    )


async def generate_rtm_from_mcp(file_name):
    return await call_mcp_tool(
        "generate_rtm",
        {
            "file_name": file_name
        }
    )


async def generate_risks_from_mcp(file_name):
    return await call_mcp_tool(
        "generate_risks",
        {
            "file_name": file_name
        }
    )


async def generate_test_data_from_mcp(file_name):
    return await call_mcp_tool(
        "generate_test_data",
        {
            "file_name": file_name
        }
    )