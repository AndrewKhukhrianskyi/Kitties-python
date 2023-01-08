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
    elif lang_type.lower() == 'ru':
        if gamemode.lower() == 'легкая':
            words = ["кот", "утка"]
        elif gamemode.lower() == 'тяжелая':
            words = ["строительство", "виноград"]
        else:
            print('Error. Неправильная команда!')
    elif lang_type.lower() == 'ua':
        if gamemode.lower() == 'легкая':
            words = ["вино", "яблуко"]
        elif gamemode.lower() == 'тяжелая':
            words = ["рівняння", "розповсюдження"]
        else:
            print('Error. Неправильная команда!')
    else:
        print('Error. Неправильная команда!')

    return choice(words)


#print(gen_random_word('en', 'легкая'))

# TODO - написать функцию сравнения проверяемого слова
def check_word(correct_word, lang_type = 'en'):
    def draw_object():
        penup()
        setx(-50)
        sety(-50)
        pendown()
        left(90)
        forward(150)
        right(90)
        forward(70)
        right(90)
        forward(20)
        left(90)
        penup()
        sety(-2)
        pendown()
    def draw_head():
        circle(20)
    def draw_right_leg():
        right(90)
        forward(40)
    def draw_left_leg():
        forward(40)
        left(180)
        forward(40)
    def draw_body():
        right(90)
        forward(100)
        left(180)
        forward(70)
        left(90)
    def draw_left_hand():
        forward(20)
        left(180)
        forward(20)
    def draw_right_hand():
        forward(20)
        right(180)
        forward(20)
        left(90)
        forward(70)
        right(45)
        
    draw_object()
    body_parts = [draw_head,
                  draw_body,
                  draw_left_hand,
                  draw_right_hand,
                  draw_left_leg,
                  draw_right_leg]
    unknown_word = ''
    eng_alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    ru_alphabet = 'йцукенгшщзфывапролдячсмитьхъё'
    ua_alphabet = "йцукенгшщзфівапролдячсмитьбюжєхї'"
    count = 0
    if lang_type == 'en':
        set_alphabet = eng_alphabet
    elif lang_type == 'ru':
        set_alphabet = ru_alphabet
    elif lang_type == 'ua':
        set_alphabet = ua_alphabet
        
    for symbol in correct_word:
        unknown_word += '_' # unknown = '_____'
    while count < 6:
        print(unknown_word)
        letter = input('Введите букву: ').lower()
        if len(letter) != 1 or letter not in set_alphabet:
            print("Введите только одну букву!")
        else:
            find_letter = correct_word.find(letter)
            # Нужно поработать в этом куске кода
            if find_letter == -1:
                body_parts[count]()
                count += 1                
            else:
                unknown_word = list(unknown_word) # ['_', '_'...]
                correct_letter = correct_word.count(letter)
                if correct_letter == 1:
                    unknown_word[find_letter] = correct_word[find_letter]   
                else:
                    letter_index = []
                    for index in range(len(correct_word)):
                        if letter == correct_word[index]:
                            letter_index.append(index)
                            
                    for element in letter_index:
                        unknown_word[element] = letter
                unknown_word = ''.join(unknown_word)
                
        if '_' not in unknown_word:
            print('You Win!')
            return None
    print('You Lose!')
    print(f'Нужно было отгадать слово: {correct_word}')

gamemode = input('Выберите сложность игры (Легкая\Тяжелая): ').lower()
lang_type = input('На каком языке? (UA/EN/RU): ').lower()

win_word = gen_random_word(lang_type, gamemode)
result = check_word(win_word, lang_type)
exitonclick()

    
    

            
