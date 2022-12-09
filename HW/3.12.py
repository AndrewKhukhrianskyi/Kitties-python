from turtle import *

# Task 1 - Check Error
def draw_circle():
    try:
        radius = int(input('Введите ваш радиус: '))
        circle(radius)
    except ValueError:
        print("Радиус не является числом!")

#draw_circle()
#exitonclick()

# Task 2 - Draw star
def draw_star():
    try:
        amount_lines = 5
        line_length = int(input('Длина линии: '))
        for line in range(amount_lines):
            forward(line_length)
            right(144)
    except ValueError:
        print("Кол-во линий не явлется числом!")

draw_star()
exitonclick()