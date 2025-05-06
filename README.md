
# 🧠 MCP Python Code Assistant

A modular AI-powered assistant that helps debug, explain, and improve Python code using the **Model Context Protocol (MCP)** pattern.  
It integrates structured tool servers (debugger, analyzer, fixer, etc.) with a GUI built using **Tkinter**, and queries **Groq's LLaMA 3 API** for intelligent responses.

---

## 🚀 Features

- ✅ Run and debug Python code with traceback support
- 🧠 AST-based code explanation
- 🔍 Linting and PEP8 style checking (via Flake8)
- 💡 Suggest code fixes using error hints
- 🔐 Scan for common Python security issues
- 📚 Retrieve Python documentation links
- 🛠️ Modular design with MCP-style context servers
- 🌙 Dark mode + copy support in the GUI
- ⚡ Powered by **Groq LLaMA 3** API

---

## 🏗️ Project Structure

```
mcp_assistant/
│
├── tk_frontend.py              # Tkinter GUI with dark mode + copy
├── mcp_client.py               # MCP client that calls Groq and integrates tool servers
├── requirements.txt            # Required Python packages
│
├── servers/                    # MCP tool servers (each returns a context block)
│   ├── __init__.py
│   ├── code_analyzer.py        # Basic syntax error checking
│   ├── debugger.py             # Executes code and returns output/errors
│   ├── explainer.py            # AST-based code breakdown
│   ├── suggested_fix.py        # Suggests common error fixes
│   ├── style_checker.py        # PEP8 issues via flake8
│   ├── doc_searcher.py         # Finds Python docs for keywords
│   └── lib_suggester.py        # Suggests external libraries
```

---

## 🧪 How It Works

1. You type or paste code into the Tkinter interface.
2. The MCP client gathers structured context from the tool servers.
3. A prompt is built and sent to Groq’s LLaMA 3 (`llama3-70b-8192`) API.
4. The assistant replies with bug analysis, code improvements, and helpful insights.

---

## 🖥️ Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/mcp-assistant.git
cd mcp-assistant
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

Make sure you also install:
```bash
pip install flake8 radon
```

### 3. Run the Assistant
```bash
python tk_frontend.py
```

---

## 🔑 Environment Setup

Create a `.env` file or update `mcp_client.py`:

```python
GROQ_API_KEY = "your-groq-api-key-here"
```

---

## 📦 requirements.txt (example)

```txt
requests
google-generativeai
radon
flake8
```

---

## 🛡️ Security Notes
This tool runs user code using `exec()`. Make sure you:
- Use in a sandboxed or local environment
- Never expose it as a web service without proper isolation

---

## 📜 License

APACHE License

---

## ✨ Roadmap Ideas

- Add voice input
- Integrate Claude or OpenAI toggle
- Add code auto-formatting with Black
- Save and view chat history
