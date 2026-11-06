from BasePage import BasePage
import tkinter as tk
from tkinter import ttk

class WelcomePage(BasePage):
    def create_widgets(self):
        center_frame = tk.Frame(self, bg=self.card_bg, bd=2, relief="groove")
        center_frame.place(relx=0.5, rely=0.5, anchor="center", width=480, height=380)

        title_label = tk.Label(
            center_frame,
            text="gonmigel",
            font=("Helvetica", 36, "bold"),
            bg=self.card_bg,
            fg=self.accent_cyan
        )
        title_label.pack(pady=(40, 10))

        subtitle = tk.Label(
            center_frame,
            text="Meet & Chat with new friends worldwide",
            font=("Helvetica", 12),
            bg=self.card_bg,
            fg="#94a3b8"
        )
        subtitle.pack(pady=(0, 40))

        btn_signup = tk.Button(
            center_frame,
            text="Sign Up",
            font=("Helvetica", 14, "bold"),
            bg=self.accent_blue,
            fg="white",
            activebackground="#0369a1",
            activeforeground="white",
            bd=0,
            cursor="hand2",
            command=lambda: self.controller.show_frame("SignUpPage")
        )
        btn_signup.pack(fill="x", padx=60, pady=10, ipady=8)

        btn_login = tk.Button(
            center_frame,
            text="Log In",
            font=("Helvetica", 14, "bold"),
            bg="#334155",
            fg="white",
            activebackground="#475569",
            activeforeground="white",
            bd=0,
            cursor="hand2",
            command=lambda: self.controller.show_frame("LoginPage")
        )
        btn_login.pack(fill="x", padx=60, pady=10, ipady=8)