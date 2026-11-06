import tkinter as tk
from tkinter import ttk
from abc import ABC,abstractmethod

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