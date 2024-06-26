import tkinter as tk
import random
from PIL import Image, ImageTk
from auth import Auth
import sqlite3
from statistic import Statistica,AboutGame


class Game(tk.Tk):
    def __init__(self,parent,user_id,username):
        self.parent = parent
        self.textboxes = []
        self.user = Auth()
        self.index = 0
        self.arr = [0]*6
        self.proverka = 1
        self.ind = 0
        self.level = 1
        self.cnt = 0
        self.data_level = 0
        self.check_button_pressed = False
        self.parent.level = tk.Label(self.parent, text=f'Уровень {self.level}')
        self.user_id = user_id
        self.username = username


    def level_up(self):
        self.level += 1
        if self.level > 4:
            self.level = 1
        self.update_level_label()

    def update_level_label(self):
        self.parent.level.config(text=f'Уровень {self.level}')
        return
    def generation(self):
        arr = [0]*6
        for i in range(len(arr)):
            if(self.level == 1):
                arr[i] = random.randint(1,9)
            elif(self.level == 2):
                arr[i] = random.randint(10,99)
            elif self.level == 3:
                arr[i] = random.randint(100,999)
            elif self.level == 4:
                arr[i] = random.randint(1000,9999)
        return arr
    # def show_number(self,textboxes):
    #     self.textboxes = textboxes
    #     arr = self.generation(2)
    #     for i in range(len(arr)):
    #         textboxes[i].create_text(37,37,text=f'{arr[i]}',fill="black")

    def show_number(self, textboxes):
        self.textboxes = textboxes
        self.arr = self.generation()
        self.show_next_number()
        for i in range(len(self.arr)):
            print(self.arr[i])
    def show_next_number(self):
        if self.index < len(self.arr):
            textbox = self.textboxes[self.index]
            textbox.create_text(39, 39, text=f'{self.arr[self.index]}', fill="#8A75C4", font=16)
            self.index += 1
            self.parent.after(1000, self.hide_current_number)
        else:
            self.index = 0
            # self.parent.after(1000, self.level_up)
    def hide_current_number(self):
        if self.index > 0:
            textbox = self.textboxes[self.index - 1]
            textbox.delete("all")
            # self.parent.after(1000, self.show_next_number)
        self.parent.after(1000, self.show_next_number)
    def repeat(self,textboxes):
        self.textboxes = textboxes
        self.show_next_number()
    def field_for_input(self):
        self.input_field = tk.Toplevel()
        self.input_field.title("Ввести числа")
        self.input_field.geometry("630x251+320+150")
        self.input_field.resizable(False, False)  # запрет изменения размеров окна
        self.input_field.config(bg="#ffffff")
        self.input_field.grab_set()


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

        self.check = tk.Button(self.input_field, text="Проверить",command=self.checking,bd=0,foreground="#8A75C4", bg="#ffffff" )
        self.check.config(font=("Arial", 15))
        self.check.place(relx=0.5, rely=0.8,anchor=tk.CENTER)

    def show_modal_window_victory(self,parent):
        self.modal_window = tk.Toplevel(parent)
        self.modal_window.title("Победа")
        self.modal_window.geometry("300x150+480+200")
        self.modal_window.resizable(False, False)  # запрет изменения размеров окна
        self.modal_window.config(bg="#ffffff")
        self.modal_window.grab_set()
        self.label_modal_true = tk.Label(self.modal_window, text="Вы прошли игру",foreground="#8A75C4",bg="#ffffff",bd=0)
        self.label_modal_true.config(font=("Arial", 15))
        self.label_modal_true.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.close_button = tk.Button(self.modal_window, text="Продолжить",foreground="#8A75C4",bg="#ffffff",bd=0,command=self.modal_window.destroy)
        self.close_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    def show_modal_window_true(self,parent):
        # создаем модальное окно
        self.modal_window = tk.Toplevel(parent)
        self.modal_window.title("Уровень пройден")
        self.modal_window.geometry("300x150+480+200")
        self.modal_window.resizable(False, False)  # запрет изменения размеров окна
        self.modal_window.config(bg="#ffffff")
        self.modal_window.grab_set()
        self.label_modal_true = tk.Label(self.modal_window,text="Уровень пройден",foreground="#8A75C4",bg="#ffffff",bd=0)
        self.label_modal_true.config(font=("Arial", 15))
        self.label_modal_true.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.close_button = tk.Button(self.modal_window, text="Продолжить",foreground="#8A75C4",bg="#ffffff",bd=0, command=self.modal_window.destroy)
        self.close_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)


    def show_modal_window_false(self,parent):
        # создаем модальное окно
        self.modal_window = tk.Toplevel(parent)
        self.modal_window.title("Вы проиграли")
        self.modal_window.geometry("300x150+480+200")
        self.modal_window.resizable(False, False)  # запрет изменения размеров окна
        self.modal_window.config(bg="#ffffff")
        self.modal_window.grab_set()
        self.label_modal_false = tk.Label(self.modal_window,text="Вы проиграли",foreground="#8A75C4",bg="#ffffff",bd=0)
        self.label_modal_false.config(font=("Arial", 15))
        self.label_modal_false.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.close_button = tk.Button(self.modal_window, text="Продолжить",foreground="#8A75C4",bg="#ffffff",bd=0, command=self.modal_window.destroy)
        self.close_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    def checking(self):
        print("Checking")
        self.inputs = [self.enter1.get(), self.enter2.get(), self.enter3.get(), self.enter4.get(), self.enter5.get(),
                       self.enter6.get()]
        if not all(x.strip() for x in self.inputs):
            print("We are come in")
            self.label_error = tk.Label(self.input_field, text="Все поля должны быть заполнены", fg="red", bg="#ffffff")
            self.label_error.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            self.input_field.after(2000, self.hide_error_label)
            return

        try:
            self.inputs = [int(x) for x in self.inputs]
        except ValueError:
            print("Error! it is not numbers")
            self.label_error = tk.Label(self.input_field, text="Должны вводится только цифры", fg="red",bg="#ffffff")
            self.label_error.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            self.input_field.after(2000, self.hide_error_label)
            return
        self.inputs = list(map(int, self.inputs))
        flag = 1
        for i in range(len(self.arr)):
            if self.inputs[i] != self.arr[i]:
                flag = 0
                break
        if flag == 1:
            self.cnt += 1
            self.input_field.destroy()
            self.level_up()
            if self.cnt < 4:
                self.show_modal_window_true(self.parent)
            else:
                self.database = sqlite3.connect("Users.db")
                self.cursor = self.database.cursor()
                self.show_modal_window_victory(self.parent)
                self.data_level = self.cnt
                print(self.data_level)
                self.cnt = 0
                self.cursor.execute("INSERT INTO statistic (id_user, level) VALUES (?, ?)",(self.user_id, self.data_level))
                self.database.commit()
                self.database.close()
            self.parent.start.config(state="normal")
            self.parent.repeat.config(state="disabled")
            self.parent.input_field.config(state="disabled")
            print("Успех")


        else:
            self.database = sqlite3.connect("Users.db")
            self.cursor = self.database.cursor()
            self.input_field.destroy()
            self.show_modal_window_false(self.parent)
            self.data_level = self.cnt
            print(self.data_level)
            self.level = 1
            self.update_level_label()
            self.cnt = 0
            self.cursor.execute("INSERT INTO statistic (id_user, level) VALUES (?, ?)", (self.user_id, self.data_level))
            self.database.commit()
            self.database.close()
            self.parent.start.config(state="normal")
            self.parent.repeat.config(state="disabled")
            self.parent.input_field.config(state="disabled")
            print("неудача")
    def hide_error_label(self):
        self.label_error.place_forget()


class Start(tk.Tk):
    def __init__(self):
        super().__init__()
        self.auth = Auth()
        self.title("Запомни число")
        self.geometry("300x330+450+150")
        self.resizable(False, False)  # запрет изменения размеров окна
        self.config(bg="#DED2FF")
        self.image2 = tk.PhotoImage(file="images/0.png")
        self.title1 = tk.Label(self,text="Запомни число",foreground="#8A75C4",bg="#DED2FF")
        self.title1.config(font=("Arial", 20))
        self.title1.place(x=50, y=22)

        self.enter = tk.Button(self, text="Вход",foreground="#8A75C4",bg="#DED2FF",bd=0,command=self.Ent)
        self.enter.config(font=("Arial", 13))
        self.enter.place(x=125,y=250)

        # self.Exit_game = tk.Button(self,image=self.image2,command=self.destroy,bg="#DED2FF",bd=0)
        # self.Exit_game.place(x=260, y=10)

        self.regist = tk.Button(self, text="Регистрация",foreground="#8A75C4",bg="#DED2FF",bd=0,command=self.reg)
        self.regist.config(font=("Arial", 8))
        self.regist.place(x=115,y=280)

    def Ent(self):
        self.auth.authorization()
        self.destroy()

    def reg(self):
        self.auth.registration()
        self.destroy()

class App(tk.Tk):
    def __init__(self,user_id,username):
        super().__init__()
        self.Game = Game(self, user_id,username)
        self.user_id = user_id
        self.username = username
        self.st = Statistica(self,user_id,username)
        self.about_game = AboutGame(self)
        self.title("Запомни число")
        self.geometry("869x508+200+50")
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
        self.repeat.config(font=("Arial", 8),state="disabled")

        self.image4 = tk.PhotoImage(file="images/Input.png")
        self.input_field = tk.Button(self,image=self.image4, command=self.new_window,bg="#ffffff",bd=0)
        self.input_field.place(x=332.5, y=400)
        self.input_field.config(font=("Arial", 8), state="disabled")

    def unblock_repeat(self):
        self.repeat.config(state="normal")  # разблокируем кнопку repeat
    def unblock_enter(self):
        self.input_field.config(state="normal")  # разблокируем кнопку repeat

    def unblock_start(self):
        self.start.config(state="normal")  # разблокируем кнопку repeat
    def start_game(self):
        self.start.config(state="disabled")
        self.repeat.config(state="disabled")  # блокируем кнопку repeat
        self.input_field.config(state="disabled")
        self.Game.show_number([self.text_box1, self.text_box2, self.text_box3, self.text_box4, self.text_box5, self.text_box6])
        self.after(12000, self.unblock_repeat)  # ждем 1 секунду и разблокируем кнопку repeat
        self.after(12000, self.unblock_enter)


    def repeat(self):
        self.Game.repeat([self.text_box1, self.text_box2, self.text_box3, self.text_box4, self.text_box5, self.text_box6])
        self.input_field.config(state="disabled")
        self.repeat.config(state="disabled")
        self.after(12000, self.unblock_enter)

    def new_window(self):
        self.Game.field_for_input()
        # self.unblock_start()


    def create_new_window(self):
        from auth import Auth
        new_frame = tk.Frame(self, width=200, height=600, bg="#E2D8FF")
        new_frame.place(x=0, y=0)
        self.username1 = tk.Label(new_frame,text=self.username,bg="#E2D8FF",bd=0,foreground="#8A75C4")
        self.username1.config(font=("Arial", 15))
        self.username1.place(relx=0.5, rely=0.03, anchor=tk.CENTER)

        self.exit = tk.Button(new_frame,image=self.image2,command=new_frame.destroy, bg="#E2D8FF",bd=0)
        self.exit.place(x=160, y=12)

        self.statistic = tk.Button(new_frame, text="Статистика",bg="#E2D8FF",bd=0,foreground="#8A75C4",command=lambda: [self.window_statistic(), new_frame.destroy()])
        self.statistic.config(font=("Arial", 15))
        self.statistic.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        self.abouts = tk.Button(new_frame, text="Об игре", bg="#E2D8FF", bd=0, foreground="#8A75C4",command=lambda: [self.about(), new_frame.destroy()])
        self.abouts.config(font=("Arial", 15))
        self.abouts.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.Enter_from_game = tk.Button(new_frame, text="выход", bg="#E2D8FF", bd=0, foreground="#8A75C4",command=self.enter_from_close)
        self.Enter_from_game.config(font=("Arial", 15))
        self.Enter_from_game.place(relx=0.5, rely=0.8, anchor=tk.CENTER)


    def window_statistic(self):
        self.st.window_with_statistic()
    def enter_from_close(self):
        self.destroy()
        start_window = Start()
        start_window.mainloop()
    def about(self):
        self.about_game.main_window()









