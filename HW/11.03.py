# Task 2 - Repeat

def computer_to_phone(numbers):
    pad = {
        "7":"1",
        "8":"2",
        "9":"3",
        "4":"4",
        "5":"5",
        "6":"6",
        "1":"7",
        "2":"8",
        "3":"9",
        "0":"0"
    }
    return "".join([pad[number] for number in numbers])

#print(computer_to_phone('0123456789'))

# Task 2 - BlackJack
from tkinter import *
from random import randint

import tkinter.messagebox as mb

def draw_card():
    count_player = 0
    count_pc = 0
    while True:
        choice = mb.askyesno(title="Вопрос",
                         message='Тянем карту?')
        if choice:
            count_player += randint(1, 6)
            mb.showinfo(title="Карты",
                        message=f"Результат: {count_player}")
            
        else:
            break
    count_pc = randint(1, 21)

    if count_player > count_pc:
        mb.showinfo(title='Результат',
                    message="Вы победили!")
    elif count_player == count_pc:
        mb.showinfo(title='Результат',
                    message="Ничья!")
    elif count_player < count_pc or count_player > 21:
        mb.showinfo(title='Результат',
                    message="Вы проиграли!")
    mb.showinfo(title="Счет",
                message=f"Игрок: {count_player}, РС: {count_pc}")
        



window = Tk()

window.geometry('100x100')
window.resizable(False, False)

start_btn = Button(text='Start!',
                   width=8,
                   height=1,
                   command=draw_card)

start_btn.pack(anchor='n')
window.mainloop()