import sys
import os
from pathlib import Path

from fastmcp import FastMCP

BASE_DIR = Path(__file__).resolve().parent.parent

if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from github_model_client import call_github_models_json
from prompts import (
    scenario_prompt,
    test_case_prompt,
    rtm_prompt,
    risk_prompt,
    test_data_prompt
)

mcp = FastMCP("QA Filesystem MCP Server")

REQUIREMENTS_FOLDER = BASE_DIR / "requirements"


def _read_requirement(file_name: str):
    file_path = REQUIREMENTS_FOLDER / file_name

    if not file_path.exists():
        return f"File not found: {file_name}"

    return file_path.read_text(encoding="utf-8")

@mcp.tool()
def list_requirement_files() -> list[str]:
    requirements_dir = "requirements"

    if not os.path.exists(requirements_dir):
        return []

    return [
        file
        for file in os.listdir(requirements_dir)
        if file.endswith(".txt")
    ]

""" @mcp.tool()
def list_requirement_files():
    files = []

    for file in REQUIREMENTS_FOLDER.glob("*.txt"):
        files.append(file.name)

    return files """


@mcp.tool()
def read_requirement_file(file_name: str):
    return _read_requirement(file_name)


@mcp.tool()
def generate_test_scenarios(file_name: str):
    requirement = _read_requirement(file_name)
    result = call_github_models_json(scenario_prompt(requirement))
    return result.get("scenarios", result)


@mcp.tool()
def generate_test_cases(file_name: str):
    requirement = _read_requirement(file_name)
    result = call_github_models_json(test_case_prompt(requirement))
    return result.get("test_cases", result)


@mcp.tool()
def generate_rtm(file_name: str):
    requirement = _read_requirement(file_name)
    result = call_github_models_json(rtm_prompt(requirement))
    return result.get("rtm", result)


@mcp.tool()
def generate_risks(file_name: str):
    requirement = _read_requirement(file_name)
    result = call_github_models_json(risk_prompt(requirement))
    return result.get("risks", result)


@mcp.tool()
def generate_test_data(file_name: str):
    requirement = _read_requirement(file_name)
    result = call_github_models_json(test_data_prompt(requirement))
    return result.get("test_data", result)


if __name__ == "__main__":
    mcp.run()