def search_docs(code: str) -> str:
    docs = []
    if "open(" in code:
        docs.append("📘 open(): https://docs.python.org/3/library/functions.html#open")
    if "json" in code:
        docs.append("📘 json module: https://docs.python.org/3/library/json.html")
    if "requests" in code:
        docs.append("📘 requests: https://docs.python-requests.org/en/latest/")
    if "re." in code:
        docs.append("📘 re (regex): https://docs.python.org/3/library/re.html")
    if "pandas" in code or "pd." in code:
        docs.append("📘 pandas: https://pandas.pydata.org/docs/")
    return "\n".join(docs) or "ℹ️ No specific documentation found."
