from tkinter import *

import tkinter.messagebox as mb

"""
#showinfo
#showwarning
def open_error():
    mb.showerror(title = 'Ошибка',
                message = 'Опасность. Ты нажал на кнопку.')

def open_warning():
    mb.showwarning(title = 'Предупреждение',
                   message = "Это предупреждающее сообщение!")

def open_info():
    mb.showinfo(title = "Инфо",
                message = "Вау. Сообщение!")
root = Tk()
root.geometry('200x300')

button_error = Button(width = 8,
                     height = 2,
                     text = 'Ошибка!',
                     command = open_error)

button_warning = Button(width = 8,
                     height = 2,
                     text = 'Ахтунг!',
                     command = open_warning)

button_info = button_error = Button(width = 8,
                     height = 2,
                     text = 'Инфо!',
                     command = open_info)

widgets = [button_warning,
           button_info,
           button_error]
for widget in widgets:
    widget.pack(anchor='n')
"""

class YameteKudasaiError(Exception):
    pass

def add():
    pass

# ValueError
def divide():
    try:
        if 'Yamete kudasai, senpai <3' in text_num1.get(0.0, END).strip():
            raise YameteKudasaiError
        number = int()
        number2 = int(text_num2.get(0.0, END).strip())
        mb.showinfo(title = 'Результат',
                    message = f"{number}/{number2} = {round(number/number2, 2)}")
    except (ZeroDivisionError, ValueError):
        mb.showerror(title = "Ошибка!",
                     message = "Либо деление на 0, либо написал крокозябру в полях!")
        

def minus():
    pass

def multiply():
    pass

root = Tk()
root.geometry('500x500')

label_num1 = Label(width = 12,
                   text = 'Enter number 1:')
text_num1 = Text(width = 20,
                 height = 1)
label_num2 = Label(width = 12,
                   text = 'Enter number 2:')
text_num2 = Text(width = 20,
                 height = 1)
button_add = Button(width = 8,
                    height = 2,
                    text = "Add",
                    command = add)
button_divide = Button(width = 8,
                    height = 2,
                    text = "Divide",
                    command = divide)
button_minus = Button(width = 8,
                    height = 2,
                    text = "Minus",
                    command = minus)
button_multiply = Button(width = 8,
                    height = 2,
                    text = "Multiply",
                    command = multiply)
widgets = [label_num1, text_num1,
           label_num2, text_num2,
           button_add, button_divide,
           button_minus, button_multiply]
for widget in widgets:
    widget.pack(anchor = 'n')

root.mainloop()

"""
ДЗ
1. Почитать о messagebox
2. Дописать задачу с классной работы (add, minus, multiply)
3. На повторение. Написать приложение, которое будет выводить случайное число в messagebox
"""

