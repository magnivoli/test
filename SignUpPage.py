import tkinter as tk
from tkinter import messagebox
import json
from BasePage import BasePage

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
        self.entry_user = tk.Entry(fields_frame, font=("Helvetica", 11), bg="#0f172a", fg="white", insertbackground="white")
        self.entry_user.grid(row=0, column=1, sticky="ew", padx=10, ipady=4)

        tk.Label(fields_frame, text="Password:", font=("Helvetica", 11), bg=self.card_bg, fg="#94a3b8").grid(row=1,
                                                                                                             column=0,
                                                                                                             sticky="w",
                                                                                                             pady=5)
        self.entry_pass = tk.Entry(fields_frame, font=("Helvetica", 11), show="*", bg="#0f172a", fg="white",
                              insertbackground="white")
        self.entry_pass.grid(row=1, column=1, sticky="ew", padx=10, ipady=4)

        fields_frame.grid_columnconfigure(1, weight=1)

        tk.Label(card, text="What seems interesting to you?", font=("Helvetica", 13, "bold"), bg=self.card_bg,
                 fg=self.accent_cyan).pack(anchor="w", padx=40, pady=(20, 10))

        interests_frame = tk.Frame(card, bg=self.card_bg)
        interests_frame.pack(fill="x", padx=40)

        interests_list = ["relationship", "sports", "gaming", "movies", "study guide", "music", "politics", "idk"]

        self.interest_vars = {}
        for idx, interest in enumerate(interests_list):
            row = idx // 4
            col = idx % 4
            var = tk.BooleanVar()
            self.interest_vars[interest] = var
            cb = tk.Checkbutton(
                interests_frame,
                text=interest,
                font=("Helvetica", 10),
                bg=self.card_bg,
                fg=self.fg_color,
                selectcolor="#0f172a",
                activebackground=self.card_bg,
                activeforeground=self.accent_cyan,
                variable=var
            )
            cb.grid(row=row, column=col, sticky="w", padx=10, pady=8)

        self.btn_signup = tk.Button(
            card,
            text="Sign Up & Start Chatting",
            font=("Helvetica", 12, "bold"),
            bg=self.accent_blue,
            fg="white",
            bd=0,
            cursor="hand2",
            command=self.handle_signup_click
        )
        self.btn_signup.pack(fill="x", padx=40, pady=(25, 0), ipady=8)

    def handle_signup_click(self):
        username = self.entry_user.get()
        password = self.entry_pass.get()
        selected_interests = [interest for interest, var in self.interest_vars.items() if var.get()]

        signup_data = {
            "action": "register",
            "username": username,
            "password": password,
            "interests": selected_interests
        }

        if hasattr(self.controller, 'client') and self.controller.client:
            self.controller.client.set_callback(self.on_server_response)
            self.controller.client.send_message(json.dumps(signup_data))

    def on_server_response(self, response):
        self.after(0, lambda: self.process_response(response))

    def process_response(self, response):
        status = response.get("status")
        message = response.get("message")

        if status == "success":
            messagebox.showinfo("Success", message)
            self.controller.show_frame("MainChatPage")
        else:
            messagebox.showerror("Error", message)