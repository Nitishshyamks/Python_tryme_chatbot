import traceback
import io
import contextlib

def debug_code(code: str) -> str:
    output = io.StringIO()
    try:
        with contextlib.redirect_stdout(output):
            exec(code, {})
        return f"✅ Output:\n{output.getvalue().strip()}"
    except Exception:
        return f"❌ Traceback:\n{traceback.format_exc()}"
