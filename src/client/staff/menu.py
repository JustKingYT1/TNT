import tkinter as tk
from .add_menu import AddMenu


class Menu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.font = ('Times New Roman', 16)
        lbl_main = tk.Label(self, text="Добро пожаловать", font=self.font)
        btn_enter = tk.Button(self, text="Ok", font=self.font, command=self.open_add_menu) # TODO Сделать по центру
        btn_close = tk.Button(self, text="Back", font=self.font, command=exit)
        lbl_main.grid(row=0, column=4, columnspan=2, padx=35, ipadx=20)
        lbl_main.place(x=10, y=10, width=100, height=20)
        btn_enter.grid(row=1, columnspan=4, column=1, padx=30, ipadx=20, pady=20)
        btn_close.grid(row=1, column=5, padx=30, ipadx=20, pady=20)

    def open_add_menu(self):
        return AddMenu(self)

