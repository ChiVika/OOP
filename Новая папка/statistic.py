import tkinter as tk
import random
from auth import Auth
import sqlite3


class Statistica(tk.Tk):
    def __init__(self, parent, user_id):
        self.parent = parent
        self.user_id = user_id


    def window_with_statistic(self):
        self.new_window = tk.Toplevel()
        self.new_window.title("Статистика")
        self.new_window.geometry("400x450+420+70")
        self.new_window.resizable(False, False)
        self.new_window.config(bg="#DED2FF")

        self.label_number = tk.Label(self.new_window, text="Номер попытки", foreground="#8A75C4", bg="#DED2FF")
        self.label_number.config(font=("Arial", 14))
        self.label_number.place(x=60, y=50)

        self.label_level = tk.Label(self.new_window, text="Уровень", foreground="#8A75C4", bg="#DED2FF")
        self.label_level.config(font=("Arial", 14))
        self.label_level.place(x=250, y=50)

        self.canvas = tk.Canvas(self.new_window, width=270, height=300,bg="#DED2FF",highlightbackground="#DED2FF")
        self.canvas.place(x=60, y=100)

        self.scrollbar = tk.Scrollbar(self.new_window, orient=tk.VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.database = sqlite3.connect("Users.db")
        self.cursor = self.database.cursor()
        self.cursor.execute("SELECT level FROM statistic WHERE id_user = ?", (self.user_id,))
        rows = self.cursor.fetchall()
        cnt = 0
        for row in rows:
            cnt += 1
            self.canvas.create_text(0, cnt * 30, text="", font=("Arial", 16))
            # self.canvas.create_line(0, cnt*20, 270, cnt*20, fill = "#8A75C4")
            self.canvas.create_text(60, cnt * 30, text=f"{cnt}", font=("Arial", 16),fill="#8A75C4")
            self.canvas.create_text(225, cnt * 30, text=f"{row[0]}", font=("Arial", 16),fill="#8A75C4")
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.database.close()


        


