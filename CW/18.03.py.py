from tkinter import *
from random import randint

import tkinter.messagebox as mb

window = Tk()
window.geometry('300x200')
window.resizable(False, False)

def check():
    if int_var.get() == 1: # get() достает число
        msg_1()
    if int_var2.get() == 1:
        msg_2()
    
'''
1. Генерировать два случайных числа
2. Для msg_1 генерировать два случайных числа от -100 до -1
3. Для msg_2 от 0 до 100
4. Сделать проверку (игрок победил\проиграл или ничья)
'''
def msg_1():
    player_number = randint(-100, -1)
    pc_number = randint(-100, -1)
    if player_number > pc_number:
        mb.showinfo(title = 'Победа!',
                    message = f"Результат: Player - {player_number}, PC - {pc_number}")
    elif player_number == pc_number:
        mb.showinfo(title = 'DRAW!',
                    message = f"Результат: Player - {player_number}, PC - {pc_number}")
    else:
        mb.showinfo(title = 'Game Over!',
                    message = f"Результат: Player - {player_number}, PC - {pc_number}")

def msg_2():
    player_number = randint(0, 100)
    pc_number = randint(0, 100)
    if player_number > pc_number:
        mb.showinfo(title = 'Победа!',
                    message = f"Результат: Player - {player_number}, PC - {pc_number}")
    elif player_number == pc_number:
        mb.showinfo(title = 'DRAW!',
                    message = f"Результат: Player - {player_number}, PC - {pc_number}")
    else:
        mb.showinfo(title = 'Game Over!',
                    message = f"Результат: Player - {player_number}, PC - {pc_number}")

int_var = IntVar() # Это поле нужно для подключения радиокнопок
int_var2 = IntVar()
button = Button(text = 'Click!',
                width = 8,
                height = 1,
                command = check)
rb_1 = Checkbutton(variable = int_var,
                   text = 'Больше\меньше с отрицательными числами')
rb_2 = Checkbutton(variable = int_var2,
                   text = 'Больше\меньше с положительными числами')
widgets = [button, rb_1, rb_2]

for widget in widgets:
    widget.pack(anchor='n')

window.mainloop()

'''
HW
1. О Radiobutton & Checkbutton почитать: https://metanit.com/python/tkinter/2.9.php
2. Написать приложение, которое будет переводить текст в числа по порядку в алфавите.
Через радиокнопки нужно будет шифровать и расшифровывать текст
3. Почитать о регулярных выражениях: https://en.wikipedia.org/wiki/Regular_expression
'''

