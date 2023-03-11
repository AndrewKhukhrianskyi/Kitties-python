from tkinter import *
'''
def open_window1():
    toplevel_window = Toplevel() # откроется доп окно
    toplevel_window.geometry('100x100')
    toplevel_window.resizable(False, False)

    toplevel_window['bg'] = 'red'

    label = Label(toplevel_window, # Явно указываем окно
                  width = 10,
                  text = 'Доп окно')
    label.pack(anchor = 'n')

def open_window2():
    toplevel_window = Toplevel() # откроется доп окно
    toplevel_window.geometry('100x100')
    toplevel_window.resizable(False, False)

    toplevel_window['bg'] = 'green'

    label = Label(toplevel_window, # Явно указываем окно
                  width = 10,
                  text = 'Доп окно')
    label.pack(anchor = 'n')

def open_window3():
    toplevel_window = Toplevel() # откроется доп окно
    toplevel_window.geometry('100x100')
    toplevel_window.resizable(False, False)

    toplevel_window['bg'] = 'blue'

    label = Label(toplevel_window, # Явно указываем окно
                  width = 10,
                  text = 'Доп окно')
    label.pack(anchor = 'n')

def open_window4():
    toplevel_window = Toplevel() # откроется доп окно
    toplevel_window.geometry('100x100')
    toplevel_window.resizable(False, False)

    toplevel_window['bg'] = 'black'

    label = Label(toplevel_window, # Явно указываем окно
                  width = 10,
                  text = 'Доп окно')
    label.pack(anchor = 'n')

window = Tk()
window.geometry('100x100')
window.resizable(False, False)

btn1 = Button(width = 5,
             height = 1,
             text = 'Red',
             command = open_window1)
btn2 = Button(width = 5,
             height = 1,
             text = 'Green',
             command = open_window2)
btn3 = Button(width = 5,
             height = 1,
             text = 'Blue',
             command = open_window3)
btn4 = Button(width = 5,
             height = 1,
             text = 'Black',
             command = open_window4)

widgets = [btn1, btn2, btn3, btn4]

for widget in widgets:
    widget.pack(anchor='n')


window.mainloop()
'''
def check_digit(number, index1, index2, digit):
    if index1 < index2:
        index1, index2 = index2, index1
    number = str(number)[index1:index2]
    print(number)
    for num in number:
        if int(num) == digit:
            return True
    return False

check_digit(1234567, 1, 0, 1)
