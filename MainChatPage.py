import tkinter as tk
from BasePage import BasePage

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
