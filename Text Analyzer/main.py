from config import *

from tkinter import *

import re
import tkinter.messagebox as mb

'''
Main -  это основной файл, который запускает
основной код приложения
'''

# Функции
def clear_data():
    fields = [regex_text_field,
              text_field,
              result_text_field]
    question = mb.askyesno(title = 'Вопрос',
                           message = "Очистить поля?")
    if question:
        for field in fields:
            field.delete(0.0, END)
        mb.showinfo(title = "Результат!",
                    message = "Данные стерты!")

def find_elements():
    regex = regex_text_field.get(0.0, END).strip()
    text = text_field.get(0.0, END).strip()


    result = re.findall(rf'{regex}', text)
    result_text_field.insert(0.0, str(result))

    mb.showinfo(title='Результат',
                message = 'Данные найдены!')

    
# UI
window = Tk()

window.resizable(RESIZABLE_WINDOW_STATUS[0],
                 RESIZABLE_WINDOW_STATUS[1])
window.title(TITLE)
window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')

regex_label = Label(text = 'Введите регулярное выражение ниже:',
                    width = LABEL_WIDTH)
regex_text_field = Text(width = REGEX_TEXT_WIDTH,
                        height = REGEX_TEXT_HEIGHT)

text_label = Label(text = 'Введите текст ниже:',
                   width = LABEL_WIDTH)

text_field = Text(width = TEXT_FIELD_WIDTH,
                  height = TEXT_FIELD_HEIGHT)

result_label = Label(text = 'Результат:',
                     width = LABEL_WIDTH)

result_text_field = Text(width = TEXT_FIELD_WIDTH,
                         height = TEXT_FIELD_HEIGHT)

clear_button = Button(width = BUTTON_WIDTH,
                      height = BUTTON_HEIGHT,
                      text = 'Clear!',
                      command = clear_data)

find_button = Button(width = BUTTON_WIDTH,
                      height = BUTTON_HEIGHT,
                      text = 'Find!',
                      command = find_elements)
widgets = [regex_label, regex_text_field,
           text_label, text_field, result_label,
           result_text_field, clear_button,
           find_button]

for widget in widgets:
    widget.pack(anchor='n')
window.mainloop()

'''
TODO
1. Найти баги,
2. Реализовать подсчет элементов текста
3. Реализовать подсчет гласных, согласных букв
4. Структурировать вывод в поле результата
Пример:
Кол-во гласных: ...
Кол-во согласных: ...
'''
