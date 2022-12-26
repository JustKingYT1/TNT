import tkinter as tk
from api.resolvers import new_channel
import tkinter.messagebox

class AddMenu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add TV Channel")
        self.data_title = tk.StringVar()
        self.abbreviated_title = tk.StringVar()
        self.font = ('Times New Roman', 16)

        lbl_main = tk.Label(self, text="Добавление телеканала\n", font=("Times New Roman", 20))
        lbl_title = tk.Label(self, text="                     Название", font=self.font)
        lbl_abbreviated_title = tk.Label(self, text="Сокращенное название", font=("Times New Roman", 14))
        entry_title = tk.Entry(self, textvariable=self.data_title, font=self.font)
        entry_abbreviated_title = tk.Entry(self, textvariable=self.abbreviated_title, font=self.font)
        btn_back = tk.Button(self, text="Отмена", font=self.font, command=self.destroy)
        btn_enter = tk.Button(self, text="Ок", font=self.font, command=self.add_channel)

        lbl_main.grid(row=0, columnspan=3, column=0)
        lbl_title.grid(row=1, column=0, pady=10, padx=30)
        entry_title.grid(row=1, column=1, columnspan=3, padx=30, pady=10)
        lbl_abbreviated_title.grid(row=2, column=0, pady=10, ipadx=10)
        entry_abbreviated_title.grid(row=2, column=1, columnspan=3, padx=30, pady=10)
        btn_back.grid(row=3, column=0, columnspan=2, pady=10)
        btn_enter.grid(row=3, column=2, pady=10)

    def add_channel(self):
        self.grab_set()
        answer = new_channel(title=self.data_title.get(), abbreviated_title=self.abbreviated_title.get())
        if answer["code"] == 200:
            self.destroy()
            tkinter.messagebox.showinfo(title="Successfully",
                                        message="Телеканал создан успешно")
        else:
            tkinter.messagebox.showerror(title="Wrong data",
                                    message="Данные для создания телеканала введены неверно!")
