import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod


class BasePage(tk.Frame, ABC):


    def __init__(self, parent, controller, width=900, height=650, title="gonmigel"):
        super().__init__(parent)
        self.controller = controller
        self.width = width
        self.height = height
        self.title = title


        self.bg_color = "#0f172a"
        self.card_bg = "#1e293b"
        self.fg_color = "#f8fafc"
        self.accent_blue = "#0284c7"
        self.accent_cyan = "#06b6d4"
        self.btn_green = "#16a34a"
        self.btn_red = "#dc2626"

        self.configure(bg=self.bg_color)


        self.create_widgets()

    @abstractmethod
    def create_widgets(self):

        pass



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
            cursor="hand2"
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
            cursor="hand2"
        )
        btn_login.pack(fill="x", padx=60, pady=10, ipady=8)



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


        btn_submit = tk.Button(form_frame, text="Log In", font=("Helvetica", 12, "bold"), bg=self.btn_green, fg="white",
                               bd=0, cursor="hand2")
        btn_submit.pack(fill="x", padx=30, ipady=8)


        side_frame = tk.Frame(main_container, bg=self.bg_color)
        side_frame.pack(side="right", fill="both", expand=True, padx=15)

        bubble_card = tk.Frame(side_frame, bg="#0284c7", bd=0)
        bubble_card.place(relx=0.5, rely=0.5, anchor="center", width=280, height=220)

        bubble_text = "gonmigel\nwill never steal\nyour\ndata"
        label_bubble = tk.Label(bubble_card, text=bubble_text, font=("Comic Sans MS", 18, "bold"), bg="#0284c7",
                                fg="white", justify="center")
        label_bubble.pack(expand=True)


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


        btn_signup = tk.Button(card, text="Sign Up & Start Chatting", font=("Helvetica", 12, "bold"),
                               bg=self.accent_blue, fg="white", bd=0, cursor="hand2")
        btn_signup.pack(fill="x", padx=40, pady=(25, 0), ipady=8)

class MainChatPage(BasePage):


    def create_widgets(self):

        video_container = tk.Frame(self, bg=self.bg_color)
        video_container.pack(side="top", fill="both", expand=True, padx=15, pady=15)


        other_cam_frame = tk.Frame(video_container, bg=self.accent_cyan, bd=2, relief="ridge")
        other_cam_frame.pack(side="left", fill="both", expand=True, padx=(0, 8))

        lbl_other = tk.Label(other_cam_frame, text="other person screen", font=("Helvetica", 16, "bold"),
                             bg=self.accent_cyan, fg="#0f172a")
        lbl_other.place(relx=0.5, rely=0.5, anchor="center")


        my_cam_frame = tk.Frame(video_container, bg=self.accent_blue, bd=2, relief="ridge")
        my_cam_frame.pack(side="right", fill="both", expand=True, padx=(8, 0))

        lbl_my = tk.Label(my_cam_frame, text="your screen", font=("Helvetica", 16, "bold"), bg=self.accent_blue,
                          fg="white")
        lbl_my.place(relx=0.5, rely=0.5, anchor="center")


        bottom_panel = tk.Frame(self, bg="#334155", height=220)
        bottom_panel.pack(side="bottom", fill="x")


        controls_frame = tk.Frame(bottom_panel, bg="#334155")
        controls_frame.pack(side="left", fill="y", padx=15, pady=15)


        btn_stop = tk.Button(controls_frame, text="STOP", font=("Helvetica", 12, "bold"), bg=self.btn_red, fg="white",
                             width=10, bd=0, cursor="hand2")
        btn_stop.pack(side="top", pady=5, ipady=6)


        btn_next = tk.Button(controls_frame, text="NEXT", font=("Helvetica", 12, "bold"), bg=self.btn_green, fg="white",
                             width=10, bd=0, cursor="hand2")
        btn_next.pack(side="top", pady=5, ipady=6)


        chat_frame = tk.Frame(bottom_panel, bg="#1e293b")
        chat_frame.pack(side="right", fill="both", expand=True, padx=15, pady=15)


        chat_display = tk.Text(chat_frame, font=("Helvetica", 10), bg="#0f172a", fg="white", bd=0, state="disabled",
                               height=6)
        chat_display.pack(fill="both", expand=True, padx=5, pady=5)


        input_frame = tk.Frame(chat_frame, bg="#1e293b")
        input_frame.pack(fill="x", padx=5, pady=(0, 5))

        chat_entry = tk.Entry(input_frame, font=("Helvetica", 11), bg="#0f172a", fg="white", insertbackground="white",
                              bd=1)
        chat_entry.pack(side="left", fill="x", expand=True, ipady=4)

        btn_send = tk.Button(input_frame, text="Send", font=("Helvetica", 10, "bold"), bg=self.accent_blue, fg="white",
                             bd=0, cursor="hand2")
        btn_send.pack(side="right", padx=(5, 0))

class AppController(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("gonmigel - Video & Chat Application")


        window_width = 950
        window_height = 680
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int((screen_width / 2) - (window_width / 2))
        center_y = int((screen_height / 2) - (window_height / 2))

        self.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        self.resizable(True, True)


        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}


        for PageClass in (WelcomePage, LoginPage, SignUpPage, MainChatPage):
            page_name = PageClass.__name__
            frame = PageClass(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")


        self.show_frame("WelcomePage")

    def show_frame(self, page_name):

        frame = self.frames[page_name]
        frame.tkraise()


import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod


class BasePage(tk.Frame, ABC):
    def __init__(self, parent, controller, width=900, height=650, title="gonmigel"):
        super().__init__(parent)
        self.controller = controller
        self.width = width
        self.height = height
        self.title = title

        self.bg_color = "#0f172a"
        self.card_bg = "#1e293b"
        self.fg_color = "#f8fafc"
        self.accent_blue = "#0284c7"
        self.accent_cyan = "#06b6d4"
        self.btn_green = "#16a34a"
        self.btn_red = "#dc2626"

        self.configure(bg=self.bg_color)
        self.create_widgets()

    @abstractmethod
    def create_widgets(self):
        pass


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
            command=lambda: self.controller.show_frame("MainChatPage")
        )
        btn_signup.pack(fill="x", padx=40, pady=(25, 0), ipady=8)


class MainChatPage(BasePage):
    def create_widgets(self):
        video_container = tk.Frame(self, bg=self.bg_color)
        video_container.pack(side="top", fill="both", expand=True, padx=15, pady=15)

        other_cam_frame = tk.Frame(video_container, bg=self.accent_cyan, bd=2, relief="ridge")
        other_cam_frame.pack(side="left", fill="both", expand=True, padx=(0, 8))

        lbl_other = tk.Label(other_cam_frame, text="other person screen", font=("Helvetica", 16, "bold"),
                             bg=self.accent_cyan, fg="#0f172a")
        lbl_other.place(relx=0.5, rely=0.5, anchor="center")

        my_cam_frame = tk.Frame(video_container, bg=self.accent_blue, bd=2, relief="ridge")
        my_cam_frame.pack(side="right", fill="both", expand=True, padx=(8, 0))

        lbl_my = tk.Label(my_cam_frame, text="your screen", font=("Helvetica", 16, "bold"), bg=self.accent_blue,
                          fg="white")
        lbl_my.place(relx=0.5, rely=0.5, anchor="center")

        bottom_panel = tk.Frame(self, bg="#334155", height=220)
        bottom_panel.pack(side="bottom", fill="x")

        controls_frame = tk.Frame(bottom_panel, bg="#334155")
        controls_frame.pack(side="left", fill="y", padx=15, pady=15)

        btn_stop = tk.Button(controls_frame, text="STOP", font=("Helvetica", 12, "bold"), bg=self.btn_red, fg="white",
                             width=10, bd=0, cursor="hand2")
        btn_stop.pack(side="top", pady=5, ipady=6)

        btn_next = tk.Button(controls_frame, text="NEXT", font=("Helvetica", 12, "bold"), bg=self.btn_green, fg="white",
                             width=10, bd=0, cursor="hand2")
        btn_next.pack(side="top", pady=5, ipady=6)

        chat_frame = tk.Frame(bottom_panel, bg="#1e293b")
        chat_frame.pack(side="right", fill="both", expand=True, padx=15, pady=15)

        chat_display = tk.Text(chat_frame, font=("Helvetica", 10), bg="#0f172a", fg="white", bd=0, state="disabled",
                               height=6)
        chat_display.pack(fill="both", expand=True, padx=5, pady=5)

        input_frame = tk.Frame(chat_frame, bg="#1e293b")
        input_frame.pack(fill="x", padx=5, pady=(0, 5))

        chat_entry = tk.Entry(input_frame, font=("Helvetica", 11), bg="#0f172a", fg="white", insertbackground="white",
                              bd=1)
        chat_entry.pack(side="left", fill="x", expand=True, ipady=4)

        btn_send = tk.Button(input_frame, text="Send", font=("Helvetica", 10, "bold"), bg=self.accent_blue, fg="white",
                             bd=0, cursor="hand2")
        btn_send.pack(side="right", padx=(5, 0))


class AppController(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("gonmigel - Video & Chat Application")

        window_width = 950
        window_height = 680
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int((screen_width / 2) - (window_width / 2))
        center_y = int((screen_height / 2) - (window_height / 2))

        self.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        self.resizable(True, True)

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for PageClass in (WelcomePage, LoginPage, SignUpPage, MainChatPage):
            page_name = PageClass.__name__
            frame = PageClass(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("WelcomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
if __name__ == "__main__":
    app = AppController()
    app.mainloop()