
from code_agent_brain import OfflineCodingAgent

agent = OfflineCodingAgent()

print("\n--- CODE GENERATION TEST ---")

answer = agent.generate_code(
    "Write a Python program to find the largest of two numbers."
)

print(answer)

print("\n--- STATIC CODE CHECK TEST ---")

code = """
def multiply(a, b):
    return a * b
"""

print(agent.check_code(code))
