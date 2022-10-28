# Task 1 - Pyramid
import turtle

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
'''

# Task 2 - Tree
from turtle import *

# Рисуем столб
quad_steps = 4
while quad_steps > 0:
    forward(20)
    left(90)
    quad_steps -= 1

penup()
sety(20)
setx(-15)
pendown()

# Рисуем треугольники
triangle_amounts = 2
while triangle_amounts > 0:
    triangle_lines = 3
    while triangle_lines > 0:
        forward(50)
        left(120)
        triangle_lines -= 1
    triangle_amounts -= 1
    sety(50)
exitonclick()
