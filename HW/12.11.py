from turtle import *
from math import sqrt

"""
# Task 1 - Polygon in polygon
data = {'amount_lines' : 7, 
        'line_length' : 100,
        'angle' : 45}

forward(data['line_length'])
for line in range(data['amount_lines']):
    left(data['angle'])
    forward(data['line_length'])

left(data['angle'])

up()
goto(25, 50)
down()

forward(data['line_length'] // 2)
for line in range(data['amount_lines']):
    left(data['angle'])
    forward(data['line_length'] // 2)

exitonclick()
"""
# Task 2 - Circle radius
pi = 3.14
square = int(input('Enter Square: '))
# Округляем до двух знаков после запятой
radius = square / 3.14
circle(sqrt(radius))
exitonclick()
