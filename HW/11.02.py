from tkinter import *
from random import randint
import tkinter.messagebox as mb
'''
# Task 1 - Калькулятор за 300
def divide():
    try:
        number = int(text_num1.get(0.0, END).strip())
        number2 = int(text_num2.get(0.0, END).strip())
        mb.showinfo(title = 'Результат',
                    message = f"{number}/{number2} = {round(number/number2, 2)}")
    except (ZeroDivisionError, ValueError):
        mb.showerror(title = "Ошибка!",
                     message = "Либо деление на 0, либо написал крокозябру в полях!")
        

def minus():
    try:
        number = int(text_num1.get(0.0, END).strip())
        number2 = int(text_num2.get(0.0, END).strip())
        mb.showinfo(title = 'Результат',
                    message = f"{number} - {number2} = {round(number-number2, 2)}")
    except ValueError:
        mb.showerror(title = "Ошибка!",
                     message = "Написал крокозябру в полях!")

def multiply():
    try:
        number = int(text_num1.get(0.0, END).strip())
        number2 = int(text_num2.get(0.0, END).strip())
        mb.showinfo(title = 'Результат',
                    message = f"{number} х {number2} = {round(number*number2, 2)}")
    except ValueError:
        mb.showerror(title = "Ошибка!",
                     message = "Написал крокозябру в полях!")


def add():
    try:
        number = int(text_num1.get(0.0, END).strip())
        number2 = int(text_num2.get(0.0, END).strip())
        mb.showinfo(title = 'Результат',
                    message = f"{number} + {number2} = {round(number+number2, 2)}")
    except ValueError:
        mb.showerror(title = "Ошибка!",
                     message = "Написал крокозябру в полях!")

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
'''
# Task 2 - Random number app
def generate_random_number():
    number = str(randint(1, 100))
    mb.showinfo(title='Инфо',
                message=f'Рандомное число: {number}')

root = Tk()

root.geometry("100x100")
root.resizable(False, False)

button = Button(width = 8,
                height = 2,
                text = 'Рандом!',
                command = generate_random_number)

button.pack(anchor='n')
root.mainloop()