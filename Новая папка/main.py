import tkinter as tk
import random
from game import Game


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.Game = Game(self)
        self.title("Запомни число")
        self.geometry("869x508")
        self.resizable(False, False)  # запрет изменения размеров окна
        self.config(bg="#ffffff")



        image1 = tk.PhotoImage(file="images/menu.png")
        self.image2 = tk.PhotoImage(file="images/0.png")
        self.image3 = tk.PhotoImage(file="images/start1.png")


        self.button1 = tk.Button(self,image=image1,command=self.create_new_window,bg="#ffffff",bd=0)
        self.button1.place(x=92,y=42)
        self.button1.image = image1

        self.label1 = tk.Label(text="Запомни число",foreground="#8A75C4",bg="#ffffff")
        self.label1.config(font=("Arial", 35))
        self.label1.place(x=264,y=22)

        self.level = tk.Label(self,text="Уровень "+ str(self.Game.level), foreground="#8A75C4",bg="#ffffff")
        self.level.place(x=383,y=100)
        self.level.config(font=("Arial", 15))

        self.text_box1 = tk.Canvas(self,width=74,height=74,bg="#E2D8FF")
        self.text_box1.place(x=92,y=176)

        self.text_box2 = tk.Canvas(self,width=74,height=74,bg="#E2D8FF")
        self.text_box2.place(x=213,y=176)

        self.text_box3 = tk.Canvas(self,width=74,height=74,bg="#E2D8FF")
        self.text_box3.place(x=334,y=176)

        self.text_box4 = tk.Canvas(self,width=74,height=74,bg="#E2D8FF")
        self.text_box4.place(x=455,y=176)

        self.text_box5 = tk.Canvas(self,width=74,height=74,bg="#E2D8FF")
        self.text_box5.place(x=576,y=176)

        self.text_box6 = tk.Canvas(self,width=74,height=74,bg="#E2D8FF")
        self.text_box6.place(x=697,y=176)

        self.start = tk.Button(self,image=self.image3,command=self.start_game, bd=0, bg="#ffffff")
        self.start.place(x=332.5,y=300)

        self.repeat = tk.Button(self, text="Повторить", command=self.repeat, bd=0, bg="#ffffff",foreground="#8A75C4")
        self.repeat.place(x=403.5, y=350)
        self.repeat.config(font=("Arial", 8))

        self.image4 = tk.PhotoImage(file="images/Input.png")
        self.input_field = tk.Button(self,image=self.image4, command=self.new_window,bg="#ffffff",bd=0)
        self.input_field.place(x=332.5, y=400)

    def start_game(self):
        self.Game.show_number([self.text_box1, self.text_box2, self.text_box3, self.text_box4, self.text_box5, self.text_box6])
        # self.start.config(state="disabled")

    def repeat(self):
        self.Game.repeat([self.text_box1, self.text_box2, self.text_box3, self.text_box4, self.text_box5, self.text_box6])
        # self.repeat.config(state="disabled")

    def new_window(self):
        self.Game.field_for_input()



    def create_new_window(self):
        new_frame = tk.Frame(self, width=200, height=600, bg="#E2D8FF")
        new_frame.place(x=0, y=0)
        self.username = tk.Label(new_frame,text="username",bg="#E2D8FF",bd=0,foreground="#8A75C4")
        self.username.config(font=("Arial", 15))
        self.username.place(x=50, y=4)

        self.exit = tk.Button(new_frame,image=self.image2,command=new_frame.destroy, bg="#E2D8FF",bd=0)
        self.exit.place(x=160, y=10)

        self.statistic = tk.Button(new_frame, text="Статистика",bg="#E2D8FF",bd=0,foreground="#8A75C4")
        self.statistic.config(font=("Arial", 10))
        self.statistic.place(x=55, y=100)



if __name__ == "__main__":
    app = App()
    app.mainloop()

