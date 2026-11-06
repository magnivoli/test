from BasePage import BasePage
import tkinter as tk
from tkinter import ttk

class LoginPage(BasePage):
    def create_widgets(self):
        main_container = tk.Frame(self, bg=self.bg_color)
        main_container.place(relx=0.5, rely=0.5, anchor="center", width=750, height=400)

        form_frame = tk.Frame(main_container, bg=self.card_bg, bd=1, relief="solid")
        form_frame.pack(side="left", fill="both", expand=True, padx=15)

        tk.Label(form_frame, text="Welcome Back", font=("Helvetica", 22, "bold"), bg=self.card_bg,
                 fg=self.fg_color).pack(anchor="w", padx=30, pady=(30, 20))

        tk.Label(form_frame, text="Username", font=("Helvetica", 11), bg=self.card_bg, fg="#94a3b8").pack(anchor="w",
                                                                                                          padx=30)
        entry_user = tk.Entry(form_frame, font=("Helvetica", 12), bg="#0f172a", fg="white", insertbackground="white",
                              bd=1)
        entry_user.pack(fill="x", padx=30, pady=(5, 15), ipady=6)

        tk.Label(form_frame, text="Password", font=("Helvetica", 11), bg=self.card_bg, fg="#94a3b8").pack(anchor="w",
                                                                                                          padx=30)
        entry_pass = tk.Entry(form_frame, font=("Helvetica", 12), show="*", bg="#0f172a", fg="white",
                              insertbackground="white", bd=1)
        entry_pass.pack(fill="x", padx=30, pady=(5, 25), ipady=6)

        btn_submit = tk.Button(
            form_frame,
            text="Log In",
            font=("Helvetica", 12, "bold"),
            bg=self.btn_green,
            fg="white",
            bd=0,
            cursor="hand2",
            command=lambda: self.controller.show_frame("MainChatPage")
        )
        btn_submit.pack(fill="x", padx=30, ipady=8)

        side_frame = tk.Frame(main_container, bg=self.bg_color)
        side_frame.pack(side="right", fill="both", expand=True, padx=15)

        bubble_card = tk.Frame(side_frame, bg="#0284c7", bd=0)
        bubble_card.place(relx=0.5, rely=0.5, anchor="center", width=280, height=220)

        bubble_text = "gonmigel\nwill never steal\nyour\npassword"
        label_bubble = tk.Label(bubble_card, text=bubble_text, font=("Comic Sans MS", 18, "bold"), bg="#0284c7",
                                fg="white", justify="center")
        label_bubble.pack(expand=True)