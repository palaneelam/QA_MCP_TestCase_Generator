def scenario_prompt(requirement):
    return f"""
You are a Senior QA Engineer.

Generate test scenarios from the requirement.

Return ONLY valid JSON in this format:

{{
  "scenarios": [
    {{
      "Scenario_ID": "TS001",
      "Scenario_Type": "Positive",
      "Scenario": "Verify user can login with valid credentials"
    }}
  ]
}}

Requirement:
{requirement}
"""


def test_case_prompt(requirement):
    return f"""
You are a Senior QA Engineer.

Generate detailed manual test cases.

Return ONLY valid JSON in this format:

{{
  "test_cases": [
    {{
      "TC_ID": "TC001",
      "Scenario": "Valid login",
      "Precondition": "User account exists",
      "Steps": "1. Open login page\\n2. Enter valid username\\n3. Enter valid password\\n4. Click Login",
      "Expected_Result": "User should login successfully",
      "Priority": "High"
    }}
  ]
}}

Requirement:
{requirement}
"""


def rtm_prompt(requirement):
    return f"""
You are a QA Lead.

Create Requirement Traceability Matrix.

Return ONLY valid JSON in this format:

{{
  "rtm": [
    {{
      "Requirement_ID": "REQ001",
      "Requirement": "User should login with valid credentials",
      "Test_Scenario_ID": "TS001",
      "Test_Case_ID": "TC001",
      "Coverage_Status": "Covered"
    }}
  ]
}}

Requirement:
{requirement}
"""


def risk_prompt(requirement):
    return f"""
You are a QA Lead.

Identify QA risks from the requirement.

Return ONLY valid JSON in this format:

{{
  "risks": [
    {{
      "Risk_ID": "R001",
      "Risk_Type": "Business Risk",
      "Risk_Description": "User may not be able to complete payment",
      "Impact": "High",
      "Mitigation": "Perform payment validation and failure scenario testing"
    }}
  ]
}}

Requirement:
{requirement}
"""


def test_data_prompt(requirement):
    return f"""
You are a QA Test Data Specialist.

Generate test data from the requirement.

Return ONLY valid JSON in this format:

{{
  "test_data": [
    {{
      "Data_ID": "TD001",
      "Data_Type": "Valid",
      "Field": "Email",
      "Value": "testuser@example.com",
      "Purpose": "Valid email registration"
    }}
  ]
}}

Requirement:
{requirement}
"""