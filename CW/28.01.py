from tkinter import *
from random import choice
# Task - Get data
'''
def get_text():
    text = text_field.get(0.0, END)
    print('Result:')
    print(text)

def insert_text():
    text = ['Если волк голоден, он ест',
            'Если Ахмед не идет к горе, то гора идет к Ахмеду',
            'Тише едешь - дальше будешь',
            'Меньше знаешь - крепче спишь',
            "Если ты волк, значит волчата будут волки!"]
    text_field.insert(0.0, choice(text))
    
root = Tk()

root.geometry('200x200')

button = Button(width = 8,
                height = 2,
                text = 'Забрать!',
                command = get_text)
button2 = Button(width = 8,
                height = 2,
                text = 'Вставить!',
                command = insert_text)
entry = Entry(width = 20)
text_field = Text(width = 20,
                  height = 5)
widgets = [entry, text_field,
           button, button2]
for widget in widgets:
    widget.pack(anchor='n')


root.mainloop()
'''
# Топорный подход
def get_data():
    data = []
    text1 = field1.get(0.0, END).strip()
    text2 = field2.get(0.0, END).strip()
    text3 = field3.get(0.0, END).strip()
    data.append(text1)
    data.append(text2)
    data.append(text3)
    print(data)
# Гибкий подход
def get_data_adv():
    data = []
    widgets = [field1, field2, field3]
    for widget in widgets:
        data.append(widget.get(0.0, END).strip())
    print(data)

root = Tk()

root.geometry('200x200')

field1 = Text(width = 20,
              height = 2)
field2 = Text(width = 20,
              height = 2)
field3 = Text(width = 20,
              height = 2)

button = Button(width = 8,
                height = 2,
                text = 'Забрать!',
                command = get_data_adv)


widgets = [field1, field2, field3, button]
for widget in widgets:
    widget.pack(anchor='n')
root.mainloop()
"""
Домашняя работа:
1. Почитать об Entry/Text: https://www.tutorialspoint.com/python/tk_entry.htm
2. Написать приложение, которое будет сохранять введенные данные в текстовом файле
3. Почитать о создании файлов: https://istories.media/workshops/2021/01/29/vvedenie-v-python-chast-11-rabota-s-failami/
"""