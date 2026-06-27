# QA MCP Test Case Generator

> An AI-powered **QA Test Case Generator** built using **Python**, **FastMCP**, **GitHub Models API**, and **Excel Reporting**.

This project demonstrates how the **Model Context Protocol (MCP)** can be used to build AI-powered QA assistants that automatically read software requirements and generate:

- Test Scenarios
- Manual Test Cases
- Requirement Traceability Matrix (RTM)
- Risk Analysis
- Test Data
- Excel Reports

---

# Project Overview

Traditional AI applications directly access files using Python.

This project demonstrates a **real MCP architecture**, where the application communicates with a **Filesystem MCP Server** to retrieve requirement documents.

---

# Project Architecture

```text
                    QA Engineer
                         │
                         ▼
                 main.py (Host)
                         │
                         ▼
                 MCP Client
                         │
                Python STDIO Transport
                         │
                         ▼
             Filesystem MCP Server
                         │
                         ▼
             Requirement Documents
                         │
                         ▼
               GitHub Models API
                         │
                         ▼
          AI Generated QA Artifacts
                         │
                         ▼
             Excel Workbook Output
```

---

# Project Structure

```text
QA_MCP_TestCase_Generator

│
├── main.py
├── mcp_client.py
├── github_models_client.py
├── prompts.py
├── excel_generator.py
├── .env
│
├── mcp_servers
│   └── filesystem_server.py
│
├── requirements
│   ├── LoginRequirement.txt
│   ├── RegistrationRequirement.txt
│   └── PaymentRequirement.txt
│
└── output
```

---

# Features

✔ Filesystem MCP Server

✔ MCP Client

✔ Tool Discovery

✔ Requirement Reader

✔ AI-powered Test Scenario Generation

✔ AI-powered Test Case Generation

✔ AI-powered RTM Generation

✔ AI-powered Risk Analysis

✔ AI-powered Test Data Generation

✔ Excel Workbook Generation

---

# MCP Tools

The Filesystem MCP Server exposes the following tools:

| Tool                      | Description                               |
|-------------------------- |-------------------------------------------|
| list_requirement_files()  | Lists all available requirement files     |
| read_requirement_file()   | Reads a requirement document              |
| generate_test_scenarios() | Generates test scenarios                  |
| generate_test_cases()     | Generates detailed manual test cases      |
| generate_rtm()            | Generates Requirement Traceability Matrix |
| generate_risks()          | Generates QA risk analysis                |
| generate_test_data()      | Generates test data                       |

---

# Technologies Used

- Python 3.12+
- FastMCP
- GitHub Models API
- OpenAI Python SDK
- Pandas
- OpenPyXL
- dotenv

---

# Prerequisites

Install:

- Python 3.12+
- Git
- Visual Studio Code
- GitHub Account

---

# Clone Repository

```bash
git clone https://github.com/<your-username>/qa-mcp-testcase-generator.git

cd qa-mcp-testcase-generator
```

---

# Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install fastmcp

pip install openai

pip install pandas

pip install openpyxl

pip install python-dotenv
```

---

# Configure GitHub Models API

Create a `.env` file in the project root.

Example

```text
GITHUB_TOKEN=your_github_models_api_key
```

---

# Add Requirement Files

Place all requirement documents inside:

```text
requirements/
```

Example:

```text
LoginRequirement.txt

RegistrationRequirement.txt

PaymentRequirement.txt
```

---

# Start the Application

```bash
python main.py
```

---

# Main Menu

```text
====================================================
QA Filesystem MCP Assistant
====================================================

1. Show Available MCP Tools

2. List Requirement Files

3. Read Requirement File

4. Generate Test Scenarios

5. Generate Test Cases

6. Generate RTM

7. Generate Risks

8. Generate Test Data

9. Generate Complete QA Workbook

0. Exit
```

---

# Output

Generated files are saved inside

```text
output/
```

Example

```text
QA_Workbook.xlsx

Scenarios.xlsx

TestCases.xlsx

RTM.xlsx

Risks.xlsx

TestData.xlsx
```

---

# Example Workflow

```
User selects

↓

RegistrationRequirement.txt

↓

Filesystem MCP Server reads file

↓

GitHub Models API analyzes requirement

↓

AI generates

• Test Scenarios

• Test Cases

• RTM

• Risks

• Test Data

↓

Excel Workbook created
```

---

# MCP Concepts Demonstrated

✔ MCP Server

✔ MCP Client

✔ Tool Discovery

✔ Tool Invocation

✔ Python STDIO Transport

✔ AI Integration

✔ Prompt Engineering

✔ Enterprise QA Automation

---

# Future Enhancements

- Jira MCP Server
- Browser MCP Server
- Database MCP Server
- Playwright MCP Server
- API Testing MCP Server
- Complete QA Sprint Agent
- HTML Dashboard
- PDF Report Generation
- Multi-Agent Workflow
- Docker Support

---

# Learning Outcomes

After exploring this project, you'll understand how to:

- Build a custom MCP Server using FastMCP
- Expose custom QA tools
- Connect an MCP Client to a Filesystem MCP Server
- Integrate GitHub Models API with MCP
- Generate AI-powered QA artifacts
- Export AI-generated outputs to Excel
- Design enterprise-ready AI-assisted QA workflows

---

# Contributions

Contributions are welcome!

Feel free to:

- Report bugs
- Suggest improvements
- Raise issues
- Submit Pull Requests

---

# If you found this project helpful...

Please consider giving this repository a ⭐ on GitHub.

It helps others discover the project and motivates future enhancements.

---

# Author

**Neelam Pal**

QA Architect | AI in Testing | MCP | Agentic AI | Test Automation | Quality Engineering

Connect with me on LinkedIn to explore more AI-powered QA projects and tutorials.