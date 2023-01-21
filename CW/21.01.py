from tkinter import *
from random import choice

def pushed():
    random_words = ['Ты нажал!',
                    '*издает нажимательные звуки*',
                    'Очередное нажатие!',
                    'Вау. Нажал.']
    print(choice(random_words))

root = Tk()
root.geometry('400x400')
root.title('Не поверишь! Окно.')
root.resizable(False, False)

# Создание кнопки
# Выражение записанное в command ДОЛЖНО БЫТЬ Функцией
# Функция не должна принимать аргументов
button_main = Button(text = 'Нажми!',
                     command = pushed)
button_main_2 = Button(width = 15,
                     height = 2,
                     text = 'Нажми!',
                     command = pushed)
button_main_3 = Button(width = 15,
                     height = 2,
                     text = 'Нажми!',
                     command = pushed)
button_main_4 = Button(width = 15,
                     height = 2,
                     text = 'Нажми!',
                     command = pushed)
button_main_5 = Button(width = 15,
                     height = 2,
                     text = 'Нажми!',
                     command = pushed)
# команда .pack
# anchor позволяет прикреплять кнопки
'''
n - север (вверху)
s - юг (внизу)
w - запад (слева)
e - восток (справа)
'''
# команда .grid
# row - строчка, column - колонка
# Порядок паковки ВАЖЕН!
# Паковать можно ТОЛЬКО одним способом
'''
button_main.grid(column = 3,
                 row = 2)
button_main_2.grid(column = 0,
                   row = 3)
button_main_3.grid(column = 3,
                   row = 4)
button_main_4.grid(column = 0,
                   row = 5)
button_main_5.grid(column = 3,
                   row = 6)
'''
button_main.place(width = 50,
             height = 200,
             bordermode = INSIDE,
             x = 50,
             y = 0)
root.mainloop()

"""
1. Почитать о виджетах
2. Почитать о кнопке Button() и паковках
3. Написать программу-калькулятор где будут складываться\умножаться\делится\отниматся числа в функции
"""

