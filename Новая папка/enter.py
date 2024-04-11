import tkinter as tk
from game import Game
from game import App
class Enter(tk.Tk):
    def __init__(self,parent, game):
        super().__init__(parent)
        self.game = game
        self.image2 = tk.PhotoImage(file="images/0.png")

    def field_for_input(self):
        self.input_field = tk.Tk()
        self.input_field.title("Запомни число")
        self.input_field.geometry("630x251")
        self.input_field.resizable(False, False)  # запрет изменения размеров окна
        self.input_field.config(bg="#ffffff")

        self.text_box1 = tk.Canvas(self.input_field, width=70, height=70, bg="#E2D8FF",highlightcolor="#8A75C4")
        self.text_box1.place(x=30, y=80)

        self.enter1 = tk.Entry(self.text_box1, bg="#E2D8FF", justify="center", fg="#8A75C4", highlightcolor="#8A75C4")
        self.enter1.config(width=8, bd=0, font=("Arial", 10))
        self.enter1.place(x=8, y=28)

        self.text_box2 = tk.Canvas(self.input_field, width=70, height=70, bg="#E2D8FF",highlightcolor="#8A75C4")
        self.text_box2.place(x=130, y=80)

        self.enter2 = tk.Entry(self.text_box2, bg="#E2D8FF", justify="center", fg="#8A75C4", highlightcolor="#8A75C4")
        self.enter2.config(width=8, bd=0, font=("Arial", 10))
        self.enter2.place(x=8, y=28)

        self.text_box3 = tk.Canvas(self.input_field, width=70, height=70, bg="#E2D8FF",highlightcolor="#8A75C4")
        self.text_box3.place(x=230, y=80)

        self.enter3 = tk.Entry(self.text_box3, bg="#E2D8FF", justify="center", fg="#8A75C4", highlightcolor="#8A75C4")
        self.enter3.config(width=8, bd=0, font=("Arial", 10))
        self.enter3.place(x=8, y=28)

        self.text_box4 = tk.Canvas(self.input_field, width=70, height=70, bg="#E2D8FF",highlightcolor="#8A75C4")
        self.text_box4.place(x=330, y=80)

        self.enter4 = tk.Entry(self.text_box4, bg="#E2D8FF", justify="center", fg="#8A75C4", highlightcolor="#8A75C4")
        self.enter4.config(width=8, bd=0, font=("Arial", 10))
        self.enter4.place(x=8, y=28)

        self.text_box5 = tk.Canvas(self.input_field, width=70, height=70, bg="#E2D8FF",highlightcolor="#8A75C4")
        self.text_box5.place(x=430, y=80)

        self.enter5 = tk.Entry(self.text_box5, bg="#E2D8FF", justify="center", fg="#8A75C4", highlightcolor="#8A75C4")
        self.enter5.config(width=8, bd=0, font=("Arial", 10))
        self.enter5.place(x=8, y=28)

        self.text_box6 = tk.Canvas(self.input_field, width=70, height=70, bg="#E2D8FF",highlightcolor="#8A75C4")
        self.text_box6.place(x=530, y=80)

        self.enter6 = tk.Entry(self.text_box6, bg="#E2D8FF", justify="center", fg="#8A75C4", highlightcolor="#8A75C4")
        self.enter6.config(width=8, bd=0, font=("Arial", 10))
        self.enter6.place(x=8, y=28)

        self.check = tk.Button(self.input_field, text="Проверить",command=self.checking)
        self.check.place(x=280, y=180)

    def checking(self):
        inputs = [self.enter1.get(), self.enter2.get(), self.enter3.get(), self.enter4.get(), self.enter5.get(),
                  self.enter6.get()]
        self.game.checking(inputs)

