
from turtle import *

'''
# Task 1 - Квадрат из квадратов
line_width = 100
angle = 90

for elem in range(4):
    forward(line_width)
    left(angle)

forward(line_width // 2)
left(90)

forward(line_width)
left(180)

forward(line_width // 2)
left(90)
forward(line_width // 2)
left(180)
forward(line_width)
hideturtle()
exitonclick()

# Task 2 - Спираль
angle = 45
spiral_length = 50
length = 1
penup()
goto(0, 50)
pendown()
left(angle)
forward(spiral_length)
for l in range(spiral_length, - 1, -1):
    left(angle)
    forward(spiral_length)   
    angle += 1
exitonclick()
'''

# Task 3 - Лестница
x_pos, y_pos = 0, 0
speed('slow')
step_length = int(input('Введите длину лестницы: '))
for step in range(step_length + 1):
    forward(20)
    left(90)
    forward(20)
    right(90)
exitonclick()