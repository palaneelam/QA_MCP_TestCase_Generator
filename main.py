import asyncio

from mcp_client import (get_requirement_from_mcp)

from prompts import (build_testcase_prompt)

# from github_models_client import (generate_test_cases)
from github_model_client import generate_test_cases

from excel_generator import (export_to_excel)

async def main():

    print("\n")
    print("=" * 50)
    print("QA MCP Test Case Generator")
    print("=" * 50)

    file_name = input(
        "\nEnter Requirement File: "
    )

    print(
        "\nReading via MCP..."
    )

    requirement = (
        await get_requirement_from_mcp(
            file_name
        )
    )

    print(
        "\nGenerating Prompt..."
    )

    prompt = build_testcase_prompt(
        requirement
    )

    print(
        "\nCalling GitHub Models..."
    )

    test_cases = (
        generate_test_cases(
            prompt
        )
    )

    print(
        "\nGenerated Test Cases:"
    )

    print(
        test_cases
    )
    print(test_cases)
    export_to_excel(test_cases)


if __name__ == "__main__":
    asyncio.run(main())