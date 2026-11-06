from BasePage import BasePage
import tkinter as tk
from tkinter import ttk
from WelcomePage import WelcomePage
from LoginPage import LoginPage
from SignUpPage import SignUpPage
from MainChatPage import MainChatPage
from client import Client

class AppController(tk.Tk):
    client = None

    def __init__(self):
        super().__init__()
        self.title("gonmigel - Video & Chat Application")

        self.client = Client()

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
