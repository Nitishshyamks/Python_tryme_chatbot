import requests
from servers.code_analyzer import analyze_code
from servers.lib_suggester import suggest_libraries
from servers.debugger import debug_code
from servers.explainer import explain_code_structure
from servers.suggested_fix import suggest_code_fix
from servers.style_checker import check_style
from servers.doc_searcher import search_docs

# 🔑 Replace this with your actual Groq API key
GROQ_API_KEY = "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"

def build_context_blocks(code_or_prompt: str):
    return [
        {"type": "code", "content": code_or_prompt},
        {"type": "analysis", "content": analyze_code(code_or_prompt)},
        {"type": "library_suggestions", "content": suggest_libraries(code_or_prompt)},
        {"type": "execution_result", "content": debug_code(code_or_prompt)},
        {"type": "code_structure", "content": explain_code_structure(code_or_prompt)},
        {"type": "suggested_fix", "content": suggest_code_fix(code_or_prompt)},
        {"type": "style_feedback", "content": check_style(code_or_prompt)},
        {"type": "documentation", "content": search_docs(code_or_prompt)},
    ]

def call_groq_with_context(prompt: str, context_blocks: list):
    context_string = "\n\n".join(
        f"[{block['type'].upper()}]\n{block['content']}" for block in context_blocks
    )

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful Python code assistant. Use the context blocks to explain bugs, suggest fixes, and recommend libraries."
            )
        },
        {
            "role": "user",
            "content": f"{context_string}\n\n{prompt}"
        }
    ]

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192",  # ✅ New working model
        "messages": messages,
        "temperature": 0.7
    }

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=payload
    )

    if response.status_code != 200:
        print("Groq API Error:", response.status_code, response.text)
        raise Exception("Groq API call failed")

    return response.json()["choices"][0]["message"]["content"]


def mcp_query(user_input: str):
    context = build_context_blocks(user_input)
    return call_groq_with_context(user_input, context)
