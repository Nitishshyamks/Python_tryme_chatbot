import subprocess
import tempfile

def check_style(code: str) -> str:
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as tmp:
        tmp.write(code)
        tmp_path = tmp.name
    try:
        result = subprocess.run(["flake8", tmp_path], capture_output=True, text=True, timeout=5)
        return result.stdout.strip() or "✅ No PEP8 issues found."
    except Exception as e:
        return f"⚠️ Flake8 failed: {e}"
