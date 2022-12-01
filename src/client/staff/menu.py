import tkinter as tk
from .add_menu import AddMenu


class Menu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.font = ('Times New Roman', 16)
        lbl_main = tk.Label(self, text="Добро пожаловать", font=self.font)
        btn_enter = tk.Button(self, text="Ok", font=self.font, command=self.open_add_menu)
        btn_close = tk.Button(self, text="Back", font=self.font, command=self.close_menu)

        lbl_main.grid(row=0, columnspan=3, column=1)
        btn_enter.grid(row=1, columnspan=4, column=1, padx=30, ipadx=20, pady=20)
        btn_close.grid(row=1, column=5, padx=30, ipadx=20, pady=20)

    def open_add_menu(self):
        return AddMenu(self)

    @staticmethod
    def close_menu():
        return exit()

