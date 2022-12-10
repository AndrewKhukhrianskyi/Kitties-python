from turtle import *
from random import choice
# choice в случайном порядке выбирает выражение из списка

# get_random_word()
# Вытаскивает случайное слово из списка
# lang_type - выбор языка (русский, английский)
# gamemode - сложность игры (Легкая, тяжелая)
def gen_random_word(lang_type, gamemode):
    words = []
    if lang_type.lower() == 'en':
        if gamemode.lower() == 'легкая':
            words = ['cat', 'dog', 'night',
                     'day', 'cup', 'cap',
                     'snow', 'apple', 'egg']
        elif gamemode.lower() == 'тяжелая':
            words = ['elephant', 'difference',
                    'starship', 'telephone',
                    'rainbow', 'leggins',
                    'knight', 'crossbow',
                    'quartermaster']
        else:
            print('Error. Неправильная команда!')
    # TODO - написать логику функции для русского (ru) и украинского языков (ua)


    return choice(words)


print(gen_random_word('en', 'легкая'))

# TODO - написать функцию сравнения проверяемого слова
def check_word(correct_word):
    ...

            
