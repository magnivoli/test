from BasePage import BasePage
import tkinter as tk
from tkinter import ttk

class SignUpPage(BasePage):
    def create_widgets(self):
        card = tk.Frame(self, bg=self.card_bg, bd=1, relief="solid")
        card.place(relx=0.5, rely=0.5, anchor="center", width=650, height=520)

        tk.Label(card, text="Create Account", font=("Helvetica", 22, "bold"), bg=self.card_bg, fg=self.fg_color).pack(
            pady=(25, 10))

        fields_frame = tk.Frame(card, bg=self.card_bg)
        fields_frame.pack(fill="x", padx=40)

        tk.Label(fields_frame, text="Username:", font=("Helvetica", 11), bg=self.card_bg, fg="#94a3b8").grid(row=0,
                                                                                                             column=0,
                                                                                                             sticky="w",
                                                                                                             pady=5)
        entry_user = tk.Entry(fields_frame, font=("Helvetica", 11), bg="#0f172a", fg="white", insertbackground="white")
        entry_user.grid(row=0, column=1, sticky="ew", padx=10, ipady=4)

        tk.Label(fields_frame, text="Password:", font=("Helvetica", 11), bg=self.card_bg, fg="#94a3b8").grid(row=1,
                                                                                                             column=0,
                                                                                                             sticky="w",
                                                                                                             pady=5)
        entry_pass = tk.Entry(fields_frame, font=("Helvetica", 11), show="*", bg="#0f172a", fg="white",
                              insertbackground="white")
        entry_pass.grid(row=1, column=1, sticky="ew", padx=10, ipady=4)

        fields_frame.grid_columnconfigure(1, weight=1)

        tk.Label(card, text="What seems interesting to you?", font=("Helvetica", 13, "bold"), bg=self.card_bg,
                 fg=self.accent_cyan).pack(anchor="w", padx=40, pady=(20, 10))

        interests_frame = tk.Frame(card, bg=self.card_bg)
        interests_frame.pack(fill="x", padx=40)

        interests_list = ["relationship", "sports", "gaming", "movies", "study guide", "music", "politics", "idk"]

        for idx, interest in enumerate(interests_list):
            row = idx // 4
            col = idx % 4
            cb = tk.Checkbutton(
                interests_frame,
                text=interest,
                font=("Helvetica", 10),
                bg=self.card_bg,
                fg=self.fg_color,
                selectcolor="#0f172a",
                activebackground=self.card_bg,
                activeforeground=self.accent_cyan
            )
            cb.grid(row=row, column=col, sticky="w", padx=10, pady=8)

        btn_signup = tk.Button(
            card,
            text="Sign Up & Start Chatting",
            font=("Helvetica", 12, "bold"),
            bg=self.accent_blue,
            fg="white",
            bd=0,
            cursor="hand2",
            command=lambda: self.controller.client.send_message(entry_user.get()+  " + "+entry_pass.get())
        )
        btn_signup.pack(fill="x", padx=40, pady=(25, 0), ipady=8)