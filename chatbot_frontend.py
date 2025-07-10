import tkinter as tk
from tkinter import scrolledtext, font
from enhanced_chatbot import process_user_input

class ChatbotGUI:
    def __init__(self, master):
        """Initialize the chatbot GUI"""
        self.master = master
        self.setup_ui()
        
        # Display welcome message
        self.display_message("Chatbot", "Hello! I'm your chatbot assistant. Type 'help' for options.", True)

    def setup_ui(self):
        """Set up all UI components"""
        # Window configuration
        self.master.title("Rule-Based Chatbot")
        self.master.geometry("700x800")
        self.master.configure(bg="#f0f0f0")
        
        # Colors and fonts
        self.colors = {
            "bot_bg": "#e3f2fd",
            "user_bg": "#bbdefb",
            "accent": "#1976d2",
            "text": "#333333"
        }
        
        self.fonts = {
            "title": font.Font(family="Arial", size=16, weight="bold"),
            "chat": font.Font(family="Arial", size=12),
            "button": font.Font(family="Arial", size=12, weight="bold")
        }
        
        # Create UI components
        self.create_header()
        self.create_chat_area()
        self.create_input_area()

    def create_header(self):
        """Create the header section"""
        header = tk.Frame(self.master, bg=self.colors["accent"], height=70)
        header.pack(fill=tk.X)
        
        tk.Label(
            header,
            text="Python Chatbot",
            font=self.fonts["title"],
            bg=self.colors["accent"],
            fg="white",
            pady=15
        ).pack()

    def create_chat_area(self):
        """Create the chat display area"""
        self.chat_display = scrolledtext.ScrolledText(
            self.master,
            wrap=tk.WORD,
            width=80,
            height=30,
            font=self.fonts["chat"],
            bg="white",
            padx=15,
            pady=15,
            state='disabled'
        )
        self.chat_display.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Configure message tags
        self.chat_display.tag_config("bot", background=self.colors["bot_bg"], lmargin1=15, lmargin2=15, spacing3=5)
        self.chat_display.tag_config("user", background=self.colors["user_bg"], lmargin1=15, lmargin2=15, spacing3=5)
        self.chat_display.tag_config("sender", foreground=self.colors["accent"], font=(self.fonts["chat"].actual("family"), self.fonts["chat"].actual("size"), "bold"))

    def create_input_area(self):
        """Create the input area"""
        input_frame = tk.Frame(self.master, bg="#f0f0f0", padx=10, pady=10)
        input_frame.pack(fill=tk.X)
        
        self.user_input = tk.Entry(
            input_frame,
            font=self.fonts["chat"],
            width=60,
            relief=tk.GROOVE,
            borderwidth=2
        )
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.user_input.bind("<Return>", self.send_message)
        
        tk.Button(
            input_frame,
            text="Send",
            command=self.send_message,
            bg=self.colors["accent"],
            fg="white",
            font=self.fonts["button"],
            relief=tk.FLAT,
            padx=20
        ).pack(side=tk.RIGHT)

    def send_message(self, event=None):
        """Handle sending messages"""
        user_text = self.user_input.get().strip()
        if not user_text:
            return
            
        self.display_message("You", user_text, False)
        self.user_input.delete(0, tk.END)
        
        response, should_exit = process_user_input(user_text)
        self.display_message("Chatbot", response, True)
        
        if should_exit:
            self.master.after(1500, self.master.destroy)

    def display_message(self, sender, message, is_bot):
        """Display a message in the chat"""
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, f"{sender}: ", "sender")
        self.chat_display.insert(tk.END, f"{message}\n\n", "bot" if is_bot else "user")
        self.chat_display.see(tk.END)
        self.chat_display.config(state='disabled')

# Main application entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()