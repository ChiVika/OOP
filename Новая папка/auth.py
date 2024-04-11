import tkinter as tk
import sqlite3


import tkinter.messagebox as messagebox
class Auth(tk.Tk):
    def __init__(self):
        self.database = sqlite3.connect("Users.db")
        self.cursor = self.database.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS users (
                Id INTEGER PRIMARY KEY,
                Login TEXT,
                Password TEXT
            )"""
        )
        self.database.commit()
        self.database.close()

    def registration(self):
        super().__init__()
        self.title("Регистрация")
        self.geometry("300x330")
        self.resizable(False, False)  # запрет изменения размеров окна
        self.config(bg="#DED2FF")

        self.username_label = tk.Label(self,text="Логин")
        self.username_label.pack()

        self.username_enter = tk.Entry(self)
        self.username_enter.pack()

        self.passwor_label = tk.Label(self,text="Пароль")
        self.passwor_label.pack()

        self.password_enter = tk.Entry(self,show="*")
        self.password_enter.pack()

        self.passwor_label1 = tk.Label(self, text="Повторный пароль")
        self.passwor_label1.pack()

        self.password_enter1 = tk.Entry(self,show="*")
        self.password_enter1.pack()

        self.button = tk.Button(self,text="Зарегистрироваться",command=self.registers)
        self.button.pack()

    def authorization(self):
        super().__init__()
        self.title("Запомни число")
        self.geometry("300x330")
        self.resizable(False, False)  # запрет изменения размеров окна
        self.config(bg="#DED2FF")

        self.username_labelA = tk.Label(self, text="Логин")
        self.username_labelA.pack()

        self.username_enterA = tk.Entry(self)
        self.username_enterA.pack()

        self.passwor_labelA = tk.Label(self, text="Пароль")
        self.passwor_labelA.pack()

        self.password_enterA = tk.Entry(self,show="*")
        self.password_enterA.pack()

        self.button1 = tk.Button(self, text="Войти",command=self.Auth)
        self.button1.pack()

    def registers(self):
        self.database = sqlite3.connect("Users.db")
        self.cursor = self.database.cursor()
        self.user1 = self.username_enter.get()
        self.psw1 = self.password_enter.get()
        self.psw2 = self.password_enter1.get()

        if not self.user1 or not self.psw1 or not self.psw2:
            messagebox.showerror("Ошибка", "Все поля должны быть заполнены!")
            return

        if self.psw1 != self.psw2:
            messagebox.showerror("Ошибка", "Пароли не совпадают!")
            return

        self.cursor.execute("INSERT INTO Users (Login, Password) VALUES (?, ?)", (self.user1, self.psw1))
        self.database.commit()


        # messagebox.showinfo("Успех", "Регистрация прошла успешно!")
        self.database.close()
        self.destroy()
        self.authorization()




    def Auth(self):
        self.database = sqlite3.connect("Users.db")
        self.cursor = self.database.cursor()
        self.user1 = self.username_enterA.get()
        self.psw1 = self.password_enterA.get()

        if not self.user1 or not self.psw1:
            tk.messagebox.showerror("Ошибка", "Все поля должны быть заполнены!")
            return
        # Проверяем, что такой пользователь зарегистрирован
        self.cursor.execute("SELECT * FROM Users WHERE Login=? AND Password=?",(self.user1,self.psw1))
        user = self.cursor.fetchone()
        if not user:
            tk.messagebox.showerror("Ошибка", "Неверный логин или пароль!")
            return
        self.database.close()
        self.destroy()
        # app = App()
        # app.mainloop()








