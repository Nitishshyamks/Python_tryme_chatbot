import ast

def suggest_code_fix(code: str) -> str:
    try:
        ast.parse(code)
        return "✅ Code looks fine. No fixes needed."
    except SyntaxError as e:
        msg = str(e)
        if "unexpected EOF" in msg or "unexpected indent" in msg:
            return "💡 Suggestion: Check for missing colons or improper indentation."
        elif "expected ':'" in msg:
            return "💡 Suggestion: Did you forget a colon after a function or if/else?"
        elif "invalid syntax" in msg:
            return "💡 Suggestion: There may be a typo. Check brackets, quotes, or operators."
        else:
            return f"⚠️ Suggestion based on error: {msg}"
    except Exception as e:
        return f"⚠️ Couldn't analyze fix: {e}"
