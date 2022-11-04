from turtle import *

# Task 1.
'''
step = 0

while True:
    if step == -1:
        break

    forward_line = int(input('Line: '))
    angle = int(input('Angle: '))
    rotation = input("Rotation: (Left or Right)")

    if rotation == 'Left':
        left(angle)
    elif rotation == 'Right':
        right(angle)

    forward(forward_line)

    step = int(input('Again? -1 - No, Something - Yes'))
exitonclick()
'''

# Task 2.
coords = [[0, 0], [100, 0], [100, 100], [0, 100], [0, 0]]
hideturtle()
for coord in coords:
    x, y = coord # Распаковываем список на два отдельных числа
    goto(x, y)
exitonclick()