from turtle import *

from random import choice

d = {1 : 'a', 2 : 'b'}
colors = ['black', 'yellow', 'red', 'green']
print(d[1])

# print(d[3])

# choice выбирает случайный цвет из списка
data = {'line_length' : 100,
        'line_width' : 2,
        'angle' : 45,
        'line_color' : choice(colors)}
# Добавление нового элемента в словарь
# словарь[новый ключ] = новое значение
'''
data['что-либо'] = "Тут лежит что-либо"
print(data)
for part in range(8):
    color(data['line_color'])
    width(data['line_width'])
    forward(data['line_length'])
    left(data['angle'])

hideturtle()
exitonclick()

    
    

