import ast

def explain_code_structure(code: str) -> str:
    try:
        tree = ast.parse(code)
        lines = []

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                lines.append(f"🧠 Function `{node.name}` defined with {len(node.args.args)} argument(s)")
            elif isinstance(node, ast.If):
                lines.append("🔀 Conditional branch detected (if statement)")
            elif isinstance(node, ast.For):
                lines.append("🔁 Loop detected (for loop)")
            elif isinstance(node, ast.While):
                lines.append("🔁 Loop detected (while loop)")
            elif isinstance(node, ast.Assign):
                lines.append("📝 Variable assignment")

        return "\n".join(lines) or "ℹ️ No major structures detected."
    except Exception as e:
        return f"Error parsing code: {e}"
