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
    if len(regex) == 0:
        mb.showerror(title="Ошибка!",
                     message="Регулярное выражение не может быть пустым!")
    else:
        text = text_field.get(0.0, END).strip()


        result = re.findall(rf'{regex}', text)
        result_text_field.insert(0.0, str(result))

        mb.showinfo(title='Результат',
                    message = 'Данные найдены!')

def get_statements():
    letters = False
    numbers = False
    symbols = False

    if letters_var.get() == 1: # letters_var == True (1)
        letters = True
        
    if numbers_var.get() == 1:
        numbers = True
        
    if symbols_var.get() == 1:
        symbols = True

    analyze_text(letters, numbers, symbols)

    
def analyze_text(letters, numbers,
                 symbols, language_status='en'):
    text = text_field.get(0.0, END).strip().lower()
    result = []
    result_text = ''
    if language_status == 'en':
        if letters == True:
            vowels = 'aeouiy'
            consonants = 'qwrtpsdfghjklzxcvbnm'
    # Работа с гласными буквами будет тут
            vowels_count = 0
            for vowel in vowels:
                vowels_count += text.count(vowel)
            result.append(vowels_count)
    # Работа с согласными буквами будет тут
            consonants_count = 0
            for consonant in consonants:
                consonants_count += text.count(consonant)
            result.append(consonants_count)
        else:
            result.append('IGNORED!')
            result.append('IGNORED!')
    # Подсчет всех символов будет тут
        if symbols == True:
            result.append(len(text))
        else:
            result.append('IGNORED!')
    # Часто встречаемая буква будет тут
        if letters == True:
            letters_dictionary = {}
            for letter in LANGUAGE_EN:
                # словарь[ключ] = значение
                letters_dictionary[letter] = text.count(letter)
                # {буква: сколько раз повторяется}
            maximum_value = max(letters_dictionary.values())
            # Редко встречаемая буква будет тут
            minimum_values = list(letters_dictionary.values())
            minimum_values.sort()
            for minimum_value in minimum_values:
                if minimum_value != 0:
                    break
                
            letters_dictionary = dict(zip(letters_dictionary.values(), letters_dictionary.keys()))
            result.append(f'{letters_dictionary[maximum_value]}({maximum_value})')
            result.append(f'{letters_dictionary[minimum_value]}({minimum_value})')
        else:
            result.append('INGORED!')
            result.append('IGNORED!')
        
    for field in range(len(ANALYZE_TEXT_LIST)): # range(0,8)
        try:
            result_text += f'{ANALYZE_TEXT_LIST[field]} {result[field]}\n'
        except IndexError:
            result_text += f'{ANALYZE_TEXT_LIST[field]} No results!\n'
    
    
    result_text_field.insert(0.0, result_text)
            
        
    
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
statistics_button = Button(width = BUTTON_WIDTH,
                           height = BUTTON_HEIGHT,
                           text = 'Statistic!',
                           command = get_statements)
letters_var = IntVar()
letters_checkbutton = Checkbutton(text='Letters!',
                                  var=letters_var)
numbers_var = IntVar()
numbers_checkbutton = Checkbutton(text='Numbers!',
                                  var=numbers_var)

symbols_var = IntVar()
symbols_checkbutton = Checkbutton(text='Symbols!',
                                  var=symbols_var)
widgets = [regex_label, regex_text_field,
           text_label, text_field, result_label,
           result_text_field, clear_button,
           find_button, statistics_button,
           letters_checkbutton, numbers_checkbutton,
           symbols_checkbutton]

for widget in widgets:
    widget.pack(anchor='n')
window.mainloop()

'''
TODO
1. Найти баги,
2. Структурировать вывод в поле результата
Пример:
Кол-во гласных: ...
Кол-во согласных: ...
'''
