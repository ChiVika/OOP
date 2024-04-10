import tkinter as tk
import random

class Game(tk.Tk):
    def __init__(self,parent):
        self.parent = parent
        self.textboxes = []
        self.index = 0
        self.arr = [0]*6
        self.proverka = 1
        self.ind = 0
        self.level = 1

    def level_up(self):
        self.level += 1
        if self.level > 4:
            self.level = 1
            self.update_level_label()
        # self.show_number(self.textboxes)
        self.update_level_label()

    def update_level_label(self):
        self.parent.level.config(text=f'Уровень {self.level}')
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
            self.parent.after(1000, self.show_next_number)
        else:
            self.parent.after(1000, self.show_next_number)
    def repeat(self,textboxes):
        self.textboxes = textboxes
        self.show_next_number()
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

    def show_modal_window_true(self,parent):
        # создаем модальное окно
        self.modal_window = tk.Toplevel(parent)
        self.modal_window.title("Уровень пройден")
        self.modal_window.geometry("300x150")
        self.modal_window.resizable(False, False)  # запрет изменения размеров окна
        self.modal_window.config(bg="#ffffff")
        self.modal_window.grab_set()
        self.label_modal_true = tk.Label(self.modal_window,text="Уровень пройден")
        self.label_modal_true.pack()

        self.close_button = tk.Button(self.modal_window, text="Закрыть", command=self.modal_window.destroy)
        self.close_button.pack()

    def show_modal_window_false(self,parent):
        # создаем модальное окно
        self.modal_window = tk.Toplevel(parent)
        self.modal_window.title("Вы проиграли")
        self.modal_window.geometry("300x150")
        self.modal_window.resizable(False, False)  # запрет изменения размеров окна
        self.modal_window.config(bg="#ffffff")
        self.modal_window.grab_set()
        self.label_modal_false = tk.Label(self.modal_window,text="Вы проиграли")
        self.label_modal_false.pack()

        self.close_button = tk.Button(self.modal_window, text="Закрыть", command=self.modal_window.destroy)
        self.close_button.pack()
    def checking(self):
        self.inputs = [self.enter1.get(), self.enter2.get(), self.enter3.get(), self.enter4.get(), self.enter5.get(),
                       self.enter6.get()]
        flag = 1
        for i in range(len(self.arr)):
            if int(self.inputs[i]) != self.arr[i]:
                flag = 0
                break
        if flag == 1:
            self.input_field.destroy()
            self.level_up()
            self.parent.after(1000, self.show_modal_window_true,self.parent)
            print("Успех")
        else:
            self.input_field.destroy()
            self.show_modal_window_false(self.parent)
            self.level = 1
            self.update_level_label()
            print("неудача")



    def input_numbers(self,enters):
        self.enters = enters