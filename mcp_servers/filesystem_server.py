from fastmcp import FastMCP
from pathlib import Path

mcp = FastMCP("QA Filesystem Server")

# REQUIREMENTS_FOLDER = "requirements"
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

REQUIREMENTS_FOLDER = BASE_DIR / "requirements"


@mcp.tool()
def list_requirement_files():
    """
    Return all available requirement files.
    """

    files = []

    for file in Path(REQUIREMENTS_FOLDER).glob("*.txt"):
        files.append(file.name)

    return files


@mcp.tool()
def read_requirement_file(file_name: str):
    """
    Read requirement file content.
    """
    file_path = REQUIREMENTS_FOLDER / file_name
    # file_path = Path(REQUIREMENTS_FOLDER) / file_name

    if not file_path.exists():
        return f"File not found: {file_name}"

    return file_path.read_text(
        encoding="utf-8"
    )


if __name__ == "__main__":
    print("Server Started")
    print("Requirements Folder:", REQUIREMENTS_FOLDER)
    mcp.run()