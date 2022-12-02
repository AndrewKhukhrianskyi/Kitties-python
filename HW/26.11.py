# Task 1 - Draw Circle
from turtle import *

def draw_circle(radius = 50):
    circle(radius)

# Task 2 - Draw flower in the pot
def draw_flower_pot():
    def draw_square(line_length = 100):
        for line in range(4):
            forward(line_length)
            left(90)
    draw_square()
    left(90)
    forward(100)
    right(90)
    up()
    goto(-50, 100)
    down()
    for line in range(2):
        forward(200)
        left(90)
        forward(20)
        left(90)
    
    left(90)
    forward(20)
    right(90)
    forward(100)
    left(90)
    forward(50)
    right(90)

    up()
    goto(25, 170)
    down()
    draw_square(50)
    up()
    goto(50, 190)
    down()
    circle(10)
    hideturtle()


draw_flower_pot()
exitonclick()