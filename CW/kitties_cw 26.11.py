from turtle import *
from random import randint

def calculate_radius():
    return randint(5, 20) # return достает значение из функции

def draw_circle(radius):
    circle(radius)
    exitonclick()

def generate_lines():
    return randint(20,100), randint(20, 100), randint(20, 100)
# все выражения достанутся в форме кортежа


# Выражения по умолчанию - выражения, которые не меняются при объявлении функции
def draw_square(line = 50):
    for elem in range(4):
        forward(line)
        left(90)
    exitonclick()

#draw_square() # Квадрат нарисуется с длиной линии = 50 см
#draw_square(100)

def find_line(square):
    return square // 4

def draw_square1(line):
    for elem in range(4):
        forward(line)
        left(90)
    exitonclick()




def draw_flower(amount_of_circles, shift_list): # [[0, 1], [0, 2]]
    def draw_circle1(radius):
        circle(radius)
    for circ in range(amount_of_circles):
        draw_circle1(50)
        up()
        goto(shift_list[circ][0], shift_list[circ][1])
        down()

draw_flower(6, [[50, 100], [20, 20], [30, 50], [100, -50], [40, 50], [-50, 0]])
    

