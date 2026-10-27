
import ast
from typing import Any, Dict


def check_python_syntax(code: str) -> Dict[str, Any]:
    """
    Check Python code for syntax errors without executing it.

    Args:
        code: Python source code as a string.

    Returns:
        A dictionary containing the result.
    """
    if not code or not code.strip():
        return {
            "success": False,
            "message": "No Python code was provided."
        }

    try:
        ast.parse(code)

        return {
            "success": True,
            "message": "No Python syntax errors found."
        }

    except SyntaxError as error:
        return {
            "success": False,
            "message": "Python syntax error found.",
            "line": error.lineno,
            "column": error.offset,
            "details": error.msg
        }


def analyze_python_code(code: str) -> Dict[str, Any]:
    """
    Perform a basic static analysis of Python code.
    This function does not execute the supplied code.
    """
    syntax_result = check_python_syntax(code)

    if not syntax_result["success"]:
        return {
            "syntax": syntax_result,
            "analysis": "Analysis stopped because the code has syntax errors."
        }

    try:
        tree = ast.parse(code)

        functions = [
            node.name
            for node in ast.walk(tree)
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        ]

        classes = [
            node.name
            for node in ast.walk(tree)
            if isinstance(node, ast.ClassDef)
        ]

        imports = [
            node.names[0].name
            for node in ast.walk(tree)
            if isinstance(node, (ast.Import, ast.ImportFrom))
            and node.names
        ]

        return {
            "syntax": syntax_result,
            "analysis": {
                "lines_of_code": len(code.splitlines()),
                "functions": functions,
                "classes": classes,
                "imports": imports
            }
        }

    except Exception as error:
        return {
            "syntax": syntax_result,
            "analysis_error": str(error)
        }
