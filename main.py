import sys
import os
import tkinter as tk

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gui.gui import AppController


class PreviewController(AppController):
    def __init__(self):
        super().__init__()

        self.title("gonmigel - GUI Preview Mode")

        preview_bar = tk.Frame(self, bg="#0284c7", height=45)
        preview_bar.pack(side="top", fill="x", before=self.children[list(self.children.keys())[0]])

        tk.Label(
            preview_bar,
            text="👁️ תצוגה מקדימה של המסכים:",
            font=("Helvetica", 11, "bold"),
            bg="#0284c7",
            fg="white"
        ).pack(side="left", padx=15, pady=8)

        pages = [
            ("1. Welcome Page", "WelcomePage"),
            ("2. Log In Page", "LoginPage"),
            ("3. Sign Up Page", "SignUpPage"),
            ("4. Main Chat Page", "MainChatPage")
        ]

        for btn_text, page_name in pages:
            btn = tk.Button(
                preview_bar,
                text=btn_text,
                font=("Helvetica", 10, "bold"),
                bg="#0f172a",
                fg="white",
                activebackground="#1e293b",
                activeforeground="white",
                bd=0,
                cursor="hand2",
                command=lambda p=page_name: self.show_frame(p)
            )
            btn.pack(side="left", padx=5, pady=6, ipady=3)


if __name__ == "__main__":
    app = PreviewController()
    app.mainloop()