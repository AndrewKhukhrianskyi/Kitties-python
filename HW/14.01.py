from tkinter import *
from random import choice, randint

# Task 2 & 3 - Создание случайного имени окна
def generate_random_name():
    absurd_list = 'qwertyuiop[]asdfghjkl;zxcvbnm,./1234567890-='
    random_list = ["Окно", "Окошко", "Окошечко", "Окошечечко"]
    if randint(1, 2) == 1:
        index_value = randint(0, len(absurd_list))
        return absurd_list[index_value]
    else:
        return choice(random_list)

root = Tk() # Создает окно
title_name = generate_random_name()
window_x, window_y = 500, 500
root.geometry(f'{window_x}x{window_y}') # Устанавливает размеры окна
root.resizable(False, True) # Позволяет блокировать изменения размера окна

root.title(title_name) # title() позволяет менять название окна
root.mainloop() # Позволяет обрабатывать логику на окне