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

        self.Title = tk.Label(self,text="Регистрация",foreground="#8A75C4",bg="#DED2FF")
        self.Title.config(font=("Arial", 15))
        self.Title.place(x=87,y=20)

        self.username_label = tk.Label(self,text="Логин",foreground="#8A75C4",bg="#DED2FF")
        self.username_label.config(font=("Arial", 10))
        self.username_label.place(x=48,y=70)

        self.username_enter = tk.Entry(self,bd=0,fg="#7362A2")
        self.username_enter.config(width=30,font=("Arial", 10))
        self.username_enter.place(x=50,y=95)

        self.passwor_label = tk.Label(self,text="Пароль",foreground="#8A75C4",bg="#DED2FF")
        self.passwor_label.config(font=("Arial", 10))
        self.passwor_label.place(x=48,y=130)

        self.password_enter = tk.Entry(self,show="*",bd=0,fg="#7362A2")
        self.password_enter.config(width=30, font=("Arial", 10))
        self.password_enter.place(x=50,y=155)

        self.passwor_label1 = tk.Label(self, text="Повторный пароль",foreground="#8A75C4",bg="#DED2FF")
        self.passwor_label1.config(font=("Arial", 10))
        self.passwor_label1.place(x=48,y=190)

        self.password_enter1 = tk.Entry(self,show="*",bd=0,fg="#7362A2")
        self.password_enter1.config(width=30, font=("Arial", 10))
        self.password_enter1.place(x=50,y=215)


        self.button = tk.Button(self,text="Зарегистрироваться",command=self.registers)
        self.button.place(x=87,y=270)

    def authorization(self):
        super().__init__()
        self.title("Запомни число")
        self.geometry("300x330")
        self.resizable(False, False)  # запрет изменения размеров окна
        self.config(bg="#DED2FF")

        self.TitleA = tk.Label(self, text="Авторизация", foreground="#8A75C4", bg="#DED2FF")
        self.TitleA.config(font=("Arial", 15))
        self.TitleA.place(x=87, y=20)

        self.username_labelA = tk.Label(self, text="Логин", foreground="#8A75C4", bg="#DED2FF")
        self.username_labelA.config(font=("Arial", 10))
        self.username_labelA.place(x=48, y=70)

        self.username_enterA = tk.Entry(self, bd=0, fg="#7362A2")
        self.username_enterA.config(width=30, font=("Arial", 10))
        self.username_enterA.place(x=50, y=95)

        self.passwor_labelA = tk.Label(self, text="Пароль", foreground="#8A75C4", bg="#DED2FF")
        self.passwor_labelA.config(font=("Arial", 10))
        self.passwor_labelA.place(x=48, y=130)

        self.password_enterA = tk.Entry(self, show="*", bd=0, fg="#7362A2")
        self.password_enterA.config(width=30, font=("Arial", 10))
        self.password_enterA.place(x=50, y=155)

        self.buttonA = tk.Button(self, text="Войти", command=self.Auth)
        self.buttonA.place(x=127, y=270)

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
        from game import App
        self.database.close()
        self.destroy()
        app = App()
        app.mainloop()








