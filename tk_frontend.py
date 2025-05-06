import tkinter as tk
from tkinter import scrolledtext, messagebox
from mcp_client import mcp_query

# Theme settings
LIGHT_THEME = {
    "bg": "#f9f9f9",
    "fg": "#000000",
    "chat_bg": "#ffffff",
    "bot_bg": "#d0f0c0",
    "entry_bg": "#ffffff",
    "button_bg": "#cce5ff",
    "button_fg": "#003366"
}

DARK_THEME = {
    "bg": "#1e1e1e",
    "fg": "#ffffff",
    "chat_bg": "#2e2e2e",
    "bot_bg": "#264d26",
    "entry_bg": "#3c3c3c",
    "button_bg": "#3a7bd5",
    "button_fg": "#ffffff"
}

current_theme = LIGHT_THEME

def apply_theme(theme):
    window.configure(bg=theme["bg"])
    title_label.config(bg=theme["bg"], fg=theme["fg"])
    chat_box.config(bg=theme["chat_bg"], fg=theme["fg"], insertbackground=theme["fg"])
    user_entry.config(bg=theme["entry_bg"], fg=theme["fg"], insertbackground=theme["fg"])
    send_btn.config(bg=theme["button_bg"], fg=theme["button_fg"])
    toggle_btn.config(bg=theme["button_bg"], fg=theme["button_fg"])
    copy_btn.config(bg=theme["button_bg"], fg=theme["button_fg"])
    input_frame.config(bg=theme["bg"])

def toggle_theme():
    global current_theme
    current_theme = DARK_THEME if current_theme == LIGHT_THEME else LIGHT_THEME
    apply_theme(current_theme)

def send_message():
    user_input = user_entry.get()
    if not user_input.strip():
        return

    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"\n🧑 You:\n{user_input}\n", "user")

    reply = mcp_query(user_input)
    chat_box.insert(tk.END, f"\n🤖 Bot:\n{reply}\n", "bot")

    chat_box.config(state=tk.DISABLED)
    user_entry.delete(0, tk.END)
    chat_box.see(tk.END)

def copy_last_reply():
    try:
        content = chat_box.get("1.0", tk.END).strip().split("🤖 Bot:")[-1].strip()
        if content:
            window.clipboard_clear()
            window.clipboard_append(content)
            messagebox.showinfo("Copied", "Reply copied to clipboard!")
        else:
            raise ValueError
    except:
        messagebox.showwarning("No Reply", "No bot reply found to copy.")

# Window setup
window = tk.Tk()
window.title("TRY ME BOT - ask all your Python Queries")
window.geometry("800x620")
window.resizable(False, False)

# Title
title_label = tk.Label(window, text="TRY ME BOT - ask all your Python Queries",
                       font=("Helvetica", 14, "bold"))
title_label.pack(pady=10)

# Chat display
chat_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=95, height=25, font=("Courier New", 10))
chat_box.pack(padx=10, pady=10)
chat_box.tag_config("user", font=("Courier New", 10, "bold"))
chat_box.tag_config("bot", background=current_theme["bot_bg"], font=("Courier New", 10))
chat_box.config(state=tk.DISABLED)

# Input area
input_frame = tk.Frame(window)
input_frame.pack(pady=10, fill=tk.X, padx=10)

user_entry = tk.Entry(input_frame, font=("Arial", 12), width=65)
user_entry.pack(side=tk.LEFT, padx=(0, 10), pady=5)

send_btn = tk.Button(input_frame, text="SEND", width=10, font=("Arial", 10, "bold"),
                     relief=tk.RIDGE, command=send_message)
send_btn.pack(side=tk.LEFT, padx=(0, 10))

copy_btn = tk.Button(input_frame, text="COPY", width=10, font=("Arial", 10, "bold"),
                     relief=tk.RIDGE, command=copy_last_reply)
copy_btn.pack(side=tk.LEFT, padx=(0, 10))

toggle_btn = tk.Button(input_frame, text="DARK MODE", width=12, font=("Arial", 10, "bold"),
                       relief=tk.RIDGE, command=toggle_theme)
toggle_btn.pack(side=tk.RIGHT)

# Apply theme
apply_theme(current_theme)
window.mainloop()
