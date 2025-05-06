import ast

def analyze_code(code: str) -> str:
    try:
        ast.parse(code)
        return "✅ No syntax errors detected."
    except SyntaxError as e:
        return f"❌ Syntax Error: {e}"
