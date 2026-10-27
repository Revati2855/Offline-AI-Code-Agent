
from llama_cpp import Llama

from code_agent_prompts import SYSTEM_PROMPT
from code_agent_tools import (
    check_python_syntax,
    analyze_python_code
)


MODEL_PATH = (
    "local_models/"
    "qwen2.5-coder-1.5b-instruct-q4_k_m.gguf"
)


class OfflineCodingAgent:
    def __init__(self):
        print("Loading local coding model...")

        self.llm = Llama(
            model_path=MODEL_PATH,
            n_ctx=4096,
            n_threads=4,
            verbose=False
        )

        print("Coding model loaded!")

    def ask_ai(self, task, code=""):
        prompt = f"""
Task:
{task}

User's code:
{code if code else "No code provided."}

Instructions:
- Answer the user's actual request directly.
- When generating code, put the complete program
  inside a properly formatted Python code block.
- Use correct indentation and line breaks.
- Keep explanations simple and beginner-friendly.
- Avoid repeating the same information.
- Do not add unnecessary sections or examples.
- Finish your answer completely.
- Never claim code was executed or tested unless it was.
"""

        response = self.llm.create_chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=900,
            temperature=0.1
        )

        return response["choices"][0]["message"]["content"]

    def generate_code(self, request):
        task = f"""
Generate a complete Python program for this request:

{request}

Requirements:
1. Provide the complete code in one Python code block.
2. Use proper Python indentation.
3. Include comments where useful.
4. Explain the program briefly after the code.
5. Keep the answer focused on the request.
"""

        return self.ask_ai(task=task)

    def explain_code(self, code):
        task = """
Explain the supplied Python code step by step.

Describe:
1. What the program does.
2. Important variables and functions.
3. How the program works.
4. An example output, if it can be determined.

Use simple language and do not unnecessarily rewrite the code.
"""

        return self.ask_ai(task=task, code=code)

    def debug_code(self, code):
        syntax_result = check_python_syntax(code)

        if not syntax_result["success"]:
            tool_result = (
                "The Python syntax checker found an error:\n"
                f"{syntax_result}"
            )
        else:
            tool_result = (
                "The Python syntax checker found no syntax errors.\n"
                "Static analysis results:\n"
                f"{analyze_python_code(code)}"
            )

        task = f"""
Review and debug the supplied Python code.

Results from the static analysis tool:
{tool_result}

Instructions:
1. Explain any identified syntax error or likely programming issue.
2. Provide corrected code in a properly formatted Python code block.
3. Explain the important correction briefly.
4. If no clear error is found, say so and suggest possible checks.
5. Do not claim the program was executed or tested.
"""

        return self.ask_ai(task=task, code=code)

    def check_code(self, code):
        return analyze_python_code(code)
