'''
# input(), print()
print('Hello')
print(2 + 5)
print('a' + 'b')
#print('a' + 3)
print('a' * 3)

input('Enter something: ')

# Variable - это ящик, в который можно сохранить значения
name = input('Enter name: ')
print('Your name is ' + name)

# Bad practice (Не надо делать)
имя = input('Введи имя: ')
print(имя)

# Filters: int(), float(), str()
number = int(input('Number: '))
print(number * 2)

number = float(input('Number: '))
print(number * 2)

from turtle import *

forward(90)
left(90)

forward(90)
left(90)

forward(90)
left(90)

forward(90)
left(90)

# > (Больше), < (Меньше), >= (Больше либо равно),
# <= (Меньше либо равно), == (Равно), != (Не равно)

print(5 > 2)
print(2 < 3)
print(10 != 10)
print(2 >= 5)
print(2 <= 2)

# if - если
# if работает если результат = True
if 5 > 2:
    print("Пять больше двух")

number = int(input('Введите число: '))
if number > 0:
    print('+')

# else - Иначе (во всех остальных случаях)
number = int(input('Введите число: '))
if number > 0:
    print('+')
else:
    print('Результат либо 0 либо отрицательное число')

# elif - else if - Также если
number = int(input('Введите число: '))
if number > 0:
    print('+')
elif number == 0:
    print('0')
else:
    print('-')
'''
from turtle import *

length = int(input('Введите длину: '))
angle = int(input('Введите угол: '))
# and\or - И\ИЛИ
if length <= 0 or angle <= 0:
    print("Длина или угол меньше 0")
else:
    forward(length)
    left(angle)

length = int(input('Введите длину: '))
angle = int(input('Введите угол: '))
# and\or - И\ИЛИ
if length <= 0 or angle <= 0:
    print("Длина или угол меньше 0")
else:
    forward(length)
    left(angle)

length = int(input('Введите длину: '))
angle = int(input('Введите угол: '))
# and\or - И\ИЛИ
if length <= 0 or angle <= 10:
    print("Длина или угол меньше 0")
else:
    forward(length)
    left(angle)

length = int(input('Введите длину: '))
angle = int(input('Введите угол: '))
# and\or - И\ИЛИ
if length <= 0 or angle <= 0:
    print("Длина или угол меньше 0")
else:
    forward(length)
    left(angle)
    
length = int(input('Введите длину: '))
angle = int(input('Введите угол: '))
# and\or - И\ИЛИ
if length <= 0 or angle <= 0:
    print("Длина или угол меньше 0")
else:
    forward(length)
    left(angle)

