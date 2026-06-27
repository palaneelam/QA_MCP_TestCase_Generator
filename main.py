import asyncio
from mcp_servers.filesystem_server import list_requirement_files, read_requirement_file

from mcp_client import (
    show_available_tools,
    list_files_from_mcp,
    read_requirement_from_mcp,
    generate_scenarios_from_mcp,
    generate_test_cases_from_mcp,
    generate_rtm_from_mcp,
    generate_risks_from_mcp,
    generate_test_data_from_mcp
)

from excel_generator import (
    export_single_sheet,
    export_complete_workbook
)

async def ask_file_name():
    files = list_requirement_files()

    print("\nAvailable Requirement Files:")

    if not files:
        print("No requirement files found.")
        return

    for file in files:
        print(file)

    file_name = input("\nEnter Requirement File Name: ")

    return file_name


async def option_list_files():
    files = await list_files_from_mcp()

    print("\nRequirement Files:")

    for file in files:
        print(f"- {file}")


async def option_read_requirement():
    file_name = await ask_file_name()

    if not file_name:
        return

    requirement = read_requirement_file(file_name)
    print("\nRequirement Content:")
    print(requirement)

async def option_generate_scenarios():
    file_name = await ask_file_name()

    scenarios = await generate_scenarios_from_mcp(
        file_name
    )

    export_single_sheet(
        scenarios,
        "Scenarios.xlsx",
        "Scenarios"
    )


async def option_generate_test_cases():
    file_name = await ask_file_name()

    test_cases = await generate_test_cases_from_mcp(
        file_name
    )

    export_single_sheet(
        test_cases,
        "TestCases.xlsx",
        "TestCases"
    )


async def option_generate_rtm():
    file_name = await ask_file_name()

    rtm = await generate_rtm_from_mcp(
        file_name
    )

    export_single_sheet(
        rtm,
        "RTM.xlsx",
        "RTM"
    )


async def option_generate_risks():
    file_name = await ask_file_name()

    risks = await generate_risks_from_mcp(
        file_name
    )

    export_single_sheet(
        risks,
        "Risks.xlsx",
        "Risks"
    )


async def option_generate_test_data():
    file_name = await ask_file_name()

    test_data = await generate_test_data_from_mcp(
        file_name
    )

    export_single_sheet(
        test_data,
        "TestData.xlsx",
        "TestData"
    )


async def option_generate_complete_workbook():
    file_name = await ask_file_name()

    print("\nGenerating scenarios...")
    scenarios = await generate_scenarios_from_mcp(
        file_name
    )

    print("\nGenerating test cases...")
    test_cases = await generate_test_cases_from_mcp(
        file_name
    )

    print("\nGenerating RTM...")
    rtm = await generate_rtm_from_mcp(
        file_name
    )

    print("\nGenerating risks...")
    risks = await generate_risks_from_mcp(
        file_name
    )

    print("\nGenerating test data...")
    test_data = await generate_test_data_from_mcp(
        file_name
    )

    workbook_data = {
        "Scenarios": scenarios,
        "TestCases": test_cases,
        "RTM": rtm,
        "Risks": risks,
        "TestData": test_data
    }

    export_complete_workbook(
        workbook_data
    )


async def main():
    while True:
        print("\n")
        print("=" * 60)
        print("QA Filesystem MCP Assistant")
        print("=" * 60)

        print("1. Show Available MCP Tools")
        print("2. List Requirement Files")
        print("3. Read Requirement File")
        print("4. Generate Test Scenarios")
        print("5. Generate Test Cases")
        print("6. Generate RTM")
        print("7. Generate Risks")
        print("8. Generate Test Data")
        print("9. Generate Complete QA Workbook")
        print("0. Exit")

        choice = input("\nSelect Option: ")

        if choice == "1":
            await show_available_tools()

        elif choice == "2":
            await option_list_files()

        elif choice == "3":
            await option_read_requirement()

        elif choice == "4":
            await option_generate_scenarios()

        elif choice == "5":
            await option_generate_test_cases()

        elif choice == "6":
            await option_generate_rtm()

        elif choice == "7":
            await option_generate_risks()

        elif choice == "8":
            await option_generate_test_data()

        elif choice == "9":
            await option_generate_complete_workbook()

        elif choice == "0":
            print("\nExiting QA MCP Assistant.")
            break

        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    asyncio.run(main())