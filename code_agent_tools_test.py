
from code_agent_tools import (
    check_python_syntax,
    analyze_python_code
)

print("TEST 1: Valid Python code")

valid_code = """
def add(a, b):
    return a + b

print(add(5, 3))
"""

print(check_python_syntax(valid_code))

print("\nTEST 2: Invalid Python code")

invalid_code = """
if 5 > 2
    print("Hello")
"""

print(check_python_syntax(invalid_code))

print("\nTEST 3: Basic code analysis")

print(analyze_python_code(valid_code))
