import tkinter as tk
import tkinter.messagebox
from log_form import LoginForm

font = ('Arial Bold', 30)


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btn = tk.Button(text="Login", font=font,
                             command=self.open_login)
        self.btn.pack(pady=20, padx=50)
        self.open_login()

    def open_login(self):
        login_form = LoginForm(self)
        post = login_form.open()
        if post:
            print("Login ok")
        else:
            tk.messagebox.showerror(title="Wrong login",
                                          message="Логин или пароль не верны")
            self.open_login()


if __name__ == '__main__':
    root = MainWindow()
    root.title("Наша база")
    root.geometry('800x600')
    root.mainloop()
