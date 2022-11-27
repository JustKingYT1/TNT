import tkinter as tk
from api.resolvers import check_login


class Menu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.font = ('Arial Bold', 30)

        lbl_main = tk.Label(self, text="Меню", font=self.font)
        btn_enter = tk.Button(self, text="", font=self.font, command=self.destroy)

        lbl_main.grid(row=0, columnspan=2, column=1)
        btn_enter.grid(row=0, column=3)
