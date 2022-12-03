#try:
#    print(2 + 'dog')
# Для обработки нескольких ошибок нужно создавать кортеж
#except (ZeroDivisionError, TypeError):
#    print('Либо деление на ноль либо к слову прибавляется число!')

# Можно придумывать свои ошибки!
#class DanyaNotFoundError(Exception):
#    pass

#name = input('Enter name: ')
#if name == 'Danya':
    # raise вызывает 0ошибку
#    raise DanyaNotFoundError

# finally отработает в любом случае вне зависимости от исхода
#try:
 #   print('hello' + 2)
#except:
 #   print('Error')
#finally:
 #   print('End of program!')
from turtle import *
from random import randint

def draw_figure(amount_lines, length):
    try:
        for line in range(amount_lines):
            forward(length)
            left(randint(30,90))
    except TypeError:
        print('Один из параметров не является числом! Ошибка!')
    exitonclick()

#draw_figure(6, 100)
draw_figure('dsdsdsds', 50)
    


