from tkinter import *
from random import choice

import tkinter.messagebox as mb

def ask_message():
    # yes or no = True or False
    answer = mb.askyesno(title='Сообщение',
                         message='Вы точно нажали на кнопку?')
    if answer: # answer == True
        mb.showinfo(title='Сообщение',
                    message='Вы нажали на кнопку!')
    else:
        mb.showinfo(title='Сообщение',
                    message="КНОПКА НЕ НАЖАТА!")
def change_color():
    answer = mb.askyesno(title='Сообщение',
                         message='Меняем цвет?')
    random_colors = ['red', 'green', 'blue']
    if answer: # answer == True
        window['bg'] = choice(random_colors)
    else:
        mb.showinfo(title='Сообщение',
                    message="КНОПКА НЕ НАЖАТА!")

window = Tk()
window.geometry('100x100')
window.resizable(False, False)

btn = Button(width = 5,
             height = 1,
             text = 'Click!',
             command = ask_message)

btn2 = Button(width = 5,
              height = 1,
              text = 'Click2!',
              command = change_color)

btn.pack(anchor='n')
btn2.pack(anchor='n')

window.mainloop()

'''
HW
1. Почитать о всплывающих окнах (askyesno, askokcancel, askyesnocancel): https://younglinux.info/tkinter/dialogbox
2. Написать приложение, в котором вы будете в 21.
    Условия:
    - Тянем карты от 1 до 6
    - Если игрок закончил тянуть карты - дальше тянет компьютер
    - Карты должны быть случайны
    Запрос о картах задават в формате askyesno
3. На повторение: https://www.codewars.com/kata/5572392fee5b0180480001ae 
'''
