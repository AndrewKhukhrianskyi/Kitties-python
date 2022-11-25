from turtle import *

# Task 1 - Patterns

def draw_square(line_length):
    for elem in range(4):
        forward(line_length)
        left(90)

def draw_triangle(line_list, angle_list):
    value = line_list[0] if len(line_list) == 1 else None
    if value is not None:
        forward(value)
        for angle in angle_list:
            left(angle)
            forward(value)
    else:
        for par in range(len(line_list)):
            left(angle_list[par])
            forward(line_list[par])
        

def draw_circle(radius):
    circle(radius)

#draw_square(50)
#draw_triangle([50], [120, 120])
#draw_circle(50)

#exitonclick()

# Task 2 - Draw Smile

draw_circle(100)
up()
goto(-50, 100)
down()
draw_circle(10)

up()
goto(50, 100)
down()
draw_circle(10)

up()
goto(25, 40)
down()
left(180)
forward(50)

hideturtle()
exitonclick()