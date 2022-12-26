import tkinter as tk
from tkinter import END
from tkinter import ttk
from director.add_menu import AddMenu
from director.del_menu import DelMenu
from director.upd_menu import UpdMenu
from client.api.resolvers import data_for_table_tv_channels


class Menu(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Hello Director!")
        self.font = ('Times New Roman', 16)
        data_channels = data_for_table_tv_channels()
        btn_add = tk.Button(self, text="Создать телеканал", font=("Times New Roman", 11), command=self.open_add_menu)
        btn_upd = tk.Button(self, text="Обновить телеканал", font=("Times New Roman", 11), command=self.open_upd_menu)
        btn_del = tk.Button(self, text="Удалить телеканал", font=("Times New Roman", 11), command=self.open_del_menu)
        btn_exit = tk.Button(self, text="Выйти из аккаунта", font=("Times New Roman", 11), command=exit)
        columns = ("title", "abbreviated_title")
        tree = ttk.Treeview(self, columns=columns, show="headings")
        tree.heading("title", text="Название")
        tree.heading("abbreviated_title", text="Сокращенное название")
        for channel in data_channels:
            tree.insert("", END, values=channel)

        tree.grid(row=0, column=0, rowspan=6, pady=10, padx=10)
        btn_add.grid(row=1, column=1, padx=2)
        btn_upd.grid(row=2, column=1, padx=2)
        btn_del.grid(row=3, column=1, padx=2)
        btn_exit.grid(row=4, column=1, padx=2)

    def open_add_menu(self):
        return AddMenu(self)

    def open_upd_menu(self):
        return UpdMenu(self)

    def open_del_menu(self):
        return DelMenu(self)

