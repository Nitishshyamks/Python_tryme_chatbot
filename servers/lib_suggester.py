def suggest_libraries(code: str) -> str:
    suggestions = []
    if "json" in code:
        suggestions.append("You might need the `json` module.")
    if "requests" in code:
        suggestions.append("Make sure `requests` is installed: `pip install requests`.")
    if "pd." in code or "DataFrame" in code:
        suggestions.append("Looks like you're using Pandas. Install it with `pip install pandas`.")
    return "\n".join(suggestions) or "No external libraries suggested."
