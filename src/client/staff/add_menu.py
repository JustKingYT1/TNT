import tkinter as tk


class AddMenu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.font = ('Times New Roman', 16)

        lbl_main = tk.Label(self, text="Меню", font=self.font)
        btn_enter = tk.Button(self, text="add staff", font=self.font, command=self.destroy)

        lbl_main.grid(row=0, columnspan=2, column=1)
        btn_enter.grid(row=0, column=3)
