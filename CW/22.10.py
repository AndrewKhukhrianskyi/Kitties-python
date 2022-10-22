# Task 1 - Pyramid
from turtle import *

'''
bottom_brick = 10
top_brick = 1
brick_length = 35
brick_width = 25
turtle.speed('fastest')
for x_pos in range(bottom_brick - top_brick + 2):
    for y_pos in range(bottom_brick - x_pos + 1):
        turtle.setposition((y_pos + x_pos / 2) * brick_length, x_pos * brick_width)
        turtle.fillcolor('orange') 
        turtle.begin_fill()
        turtle.forward(brick_length)
        turtle.left(90)
        turtle.forward(brick_width)
        turtle.left(90)
        turtle.forward(brick_length)
        turtle.left(90)
        turtle.forward(brick_width)
        turtle.left(90)
        turtle.end_fill()
turtle.done()

# for - переборщик
word = input('Введите слово: ')
# Переменной для цикла
# symbol - переменная, которая работает в цикле и сохраняет последний результат
for symbol in word:
    print(symbol)
# for - индексатор
# range(start,stop,step) - создает ряд чисел от start до step
for number in range(1, 10):
    print(number)
# Неявные элементы

for number in range(5): # range(0,5)
    print(number)
    
# Конструкция else в for
for number in range(10):
    if number > 11:
        print(True)
else:
    print("Закончилась работа цикла...")
    print("И мы попали сюда...")
'''
# Циклы можно вкладывать друг в друга (не больше двух циклов)
for number in range(10):
    print("Число из 1-ГО цикла:", number)
    for number2 in range(10):
        print("Числа из 2-ГО цикла:", number2)

# Задача: Нарисовать мишень
radius = 50
for circ in range(4):
    circle(radius)
    radius //= 2
exitonclick()

