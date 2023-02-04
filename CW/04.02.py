from tkinter import *
from random import choice
def get_data():
    text_data = []
    widgets = [text_field,
               text_field2,
               text_field3]
    
    file = open('saved_text.txt', 'w')
    for widget in widgets:
        text = widget.get(0.0, END)
        text_data.append(text.strip())
    file.write(str(text_data))
    file.close()
    
def change_random_color_label():
    # bg - background (задний фон)
    # fg - foreground (передний фон)
    colors = ['red', 'green', 'blue',
              'black', 'yellow', 'cyan']
    # config - настройка существующих выражений в существующих виджетах
    label.config(bg = choice(colors))
root = Tk()
root.geometry('200x200')

'''
label = Label(width = 10,
              height = 1,
              text = 'Some text',
              bg = 'red')
button = Button(width = 8,
                height = 1,
                text = 'Click!',
                command = change_random_color_label)
'''
name_label = Label(width = 10,
                   height = 1,
                   text = 'Name')
text_field = Text(width = 10,
                  height = 1)

surname_label = Label(width = 10,
                   height = 1,
                   text = 'Surname')
text_field2 = Text(width = 10,
                  height = 1)

age_label = Label(width = 10,
                   height = 1,
                   text = 'Age')
text_field3 = Text(width = 10,
                  height = 1)
button = Button(width = 8,
                height = 1,
                text = 'Click!',
                command = get_data)

widgets = [name_label,
           text_field,
           surname_label,
           text_field2,
           age_label,
           text_field3,
           button]

for widget in widgets:
    widget.pack(anchor='n')
root.mainloop()

'''
HW 04.02

1. Почитать о лейблах (Label)
2. Почитать о файлах (File)
3. Написать приложение, для отчистки, сохранения теста
'''

