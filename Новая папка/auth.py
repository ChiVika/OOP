import tkinter as tk
import sqlite3
from PIL import Image, ImageTk

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
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS statistic (
                Number INTEGER PRIMARY KEY,
                id_user INTEGER,
                level INTEGER,
                FOREIGN KEY (id_user) REFERENCES users(Id)
            )"""
        )
        self.user_id = None
        self.database.commit()
        self.database.close()

    def registration(self):
        super().__init__()
        self.title("Регистрация")
        self.geometry("300x330+450+150")
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


        self.button = tk.Button(self,text="Зарегистрироваться",command=self.registers,fg="#8A75C4",bg="#DED2FF",bd=0)
        self.button.config(font=("Arial",10))
        self.button.place(relx=0.5, rely=0.82,anchor=tk.CENTER)

        self.button1 = tk.Button(self, text="Авторизация",fg="#8A75C4", bg="#DED2FF",bd=0,command=self.Ent)
        self.button1.config(font=("Arial", 8))
        self.button1.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    def authorization(self):
        super().__init__()
        self.title("Запомни число")
        self.geometry("300x330+450+150")
        self.resizable(False, False)  # запрет изменения размеров окна
        self.config(bg="#DED2FF")

        image = Image.open("images/0.png")
        photo = ImageTk.PhotoImage(image)

        self.TitleA = tk.Label(self, text="Авторизация", foreground="#8A75C4", bg="#DED2FF")
        self.TitleA.config(font=("Arial", 15))
        self.TitleA.place(relx=0.5, rely=0.1,anchor=tk.CENTER)

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
        self.imges_enters = tk.PhotoImage(file="images/en.png")
        self.buttonA = tk.Button(self,text="Вход", command=self.Auth,fg="#8A75C4",bg="#DED2FF",bd=0,width=20)
        self.buttonA.config(font=("Arial", 12))
        self.buttonA.place(relx=0.5, rely=0.75,anchor=tk.CENTER)

        self.buttonR = tk.Button(self, text="Регистрация", command=self.reg, fg="#8A75C4", bg="#DED2FF", bd=0)
        self.buttonR.config(font=("Arial", 10))
        self.buttonR.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
    def registers(self):
        self.database = sqlite3.connect("Users.db")
        self.cursor = self.database.cursor()
        self.user1 = self.username_enter.get()
        self.psw1 = self.password_enter.get()
        self.psw2 = self.password_enter1.get()

        if not self.user1 or not self.psw1 or not self.psw2:
            self.label_error = tk.Label(self, text="Все поля должны быть заполнены", fg="red", bg="#DED2FF")
            self.label_error.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
            self.after(2000, self.hide_error_label)
            return

        if self.psw1 != self.psw2:
            self.label_error = tk.Label(self, text="Пароли не совпадают!", fg="red", bg="#DED2FF")
            self.label_error.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
            self.after(2000, self.hide_error_label)
            return
        if len(self.psw1) <= 6:
            self.label_error = tk.Label(self, text="Пароль должен содержать больше 6 символов!", fg="red", bg="#DED2FF")
            self.label_error.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
            self.after(2000, self.hide_error_label)
            return

        self.cursor.execute("INSERT INTO Users (Login, Password) VALUES (?, ?)", (self.user1, self.psw1))
        self.database.commit()


        self.database.close()
        self.destroy()
        self.authorization()




    def Auth(self):
        self.database = sqlite3.connect("Users.db")
        self.cursor = self.database.cursor()
        self.user1 = self.username_enterA.get()
        self.psw1 = self.password_enterA.get()

        if not self.user1 or not self.psw1:
            self.label_error = tk.Label(self, text="Все поля должны быть заполнены!", fg="red", bg="#DED2FF")
            self.label_error.place(relx=0.5,rely=0.6,anchor=tk.CENTER)
            self.after(2000,self.hide_error_label)

            return
        self.cursor.execute("SELECT * FROM Users WHERE Login=? AND Password=?",(self.user1,self.psw1))
        user = self.cursor.fetchone()
        if not user:
            self.label_error = tk.Label(self,text="Неверный логин или пароль!",fg="red",bg="#DED2FF")
            self.label_error.place(relx=0.5,rely=0.6,anchor=tk.CENTER)
            self.after(2000, self.hide_error_label)
            return
        user_id = user[0]
        username = user[1]
        from game import App
        self.database.close()
        self.destroy()
        app = App(user_id,username)
        app.mainloop()
        return user_id,username

    def hide_error_label(self):
        self.label_error.place_forget()

    def Ent(self):
        self.destroy()
        self.authorization()


    def reg(self):
        self.destroy()
        self.registration()









