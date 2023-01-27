# Task 1 - Calculator
from tkinter import *
from random import randint

def add():
    number_1, number_2 = randint(1, 100), randint(1, 100)
    print(f'Сгенерированные числа: {number_1} & {number_2}')
    print(f"Результат сложения: {number_1 + number_2}")

def multiply():
    number_1, number_2 = randint(1, 100), randint(1, 100)
    print(f'Сгенерированные числа: {number_1} & {number_2}')
    print(f"Результат умножения: {number_1 * number_2}")

def divide():
    number_1, number_2 = randint(1, 100), randint(1, 100)
    print(f'Сгенерированные числа: {number_1} & {number_2}')
    print(f"Результат деления: {round(number_1 / number_2, 2)}")

def minus():
    number_1, number_2 = randint(1, 100), randint(1, 100)
    print(f'Сгенерированные числа: {number_1} & {number_2}')
    print(f"Результат вычитания: {number_1 - number_2}")

root = Tk()
root.geometry('200x200')
root.title('Не поверишь! Окно.')
root.resizable(False, False)

# Создание кнопки
# Выражение записанное в command ДОЛЖНО БЫТЬ Функцией
# Функция не должна принимать аргументов
button_add = Button(text = '+',
                    width = 30,
                     height = 2,
                     command = add)
button_multiply = Button(width = 30,
                     height = 2,
                     text = '*',
                     command = multiply)
button_divide = Button(width = 30,
                     height = 2,
                     text = '÷',
                     command = divide)
button_minus = Button(width = 30,
                     height = 2,
                     text = '-',
                     command = minus)

widgets = [button_add, button_multiply,
           button_divide, button_minus]
for widget in widgets:
    widget.pack(anchor='n')
root.mainloop()