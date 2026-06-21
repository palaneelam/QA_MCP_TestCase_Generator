def build_testcase_prompt(requirement):

    return f"""
    You are a Senior QA Engineer.
    
    Generate test cases.
    
    Return ONLY JSON.
    
    Example:
    
    [
      {{
        "TC_ID":"TC001",
        "Scenario":"Valid Login",
        "Precondition":"User exists",
        "Steps":"Enter username and password",
        "Expected_Result":"Login successful",
        "Priority":"High"
      }}
    ]
    
    Requirement:
    
    {requirement}
    """