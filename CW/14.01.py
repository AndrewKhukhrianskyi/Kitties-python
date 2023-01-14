from tkinter import *
from random import randint

def generate_numbers():
    number_1 = randint(100, 500)
    number_2 = randint(100, 500)
    return number_1, number_2
root = Tk() # Создает окно
window_x, window_y = generate_numbers()
root.geometry(f'{window_x}x{window_y}') # Устанавливает размеры окна
root.resizable(False, True) # Позволяет блокировать изменения размера окна

root.title('Бабиджон') # title() позволяет менять название окна
root.mainloop() # Позволяет обрабатывать логику на окне

# Task 1 - distance
def find_distance(speed, time, river_speed):
    speed -= river_speed
    print(speed * time)

find_distance(10, 2, 2)

"""
1. Почитать о Tkinter
2. Пройти шаги создания окна
3 (*). Написать программу, которая будет создавать случайное имя окна
4. Модифицируйте задачу 3 для создания осмысленных названий.
"""


