# Task 1 - Spirograph (Basic)
from turtle import *
'''
bgcolor('black') # Закрашиваем фон
pensize(2) # размер ручки
speed(100)

steps = int(input('Enter steps: '))

while steps > 0:
    color('red')
    circle(100)
    left(60)
    steps -= 1

hideturtle() # убираем "черепашку" (убираем стрелочку)
exitonclick()

import turtle
# Task 2 - Шахматная доска       
sc = turtle.Turtle()
pen = turtle.Turtle()
    
# set turtle object speed
pen.speed(100)
    
# loops for board
for i in range(8):
    
    # not ready to draw
    pen.up()
    
    # set position for every row
    pen.setpos(0, 30 * i)
    
    # ready to draw
    pen.down()
    
    # row
    for j in range(8):
        # conditions for alternative color
        if (i + j)% 2 == 0:
            col ='black'
        
        else:
            col ='white'
    
    # fill with given color
    pen.fillcolor(col)
    
    # start filling with colour
    pen.begin_fill()
    
    # call method
    for i in range(4):
        pen.forward(30)
        pen.left(90)
    pen.forward(30)
    # stop filling
    pen.end_fill()
    
# hide the turtle
pen.hideturtle()
exitonclick()
'''
import turtle
# Task 3 - Heart
wn = turtle.Screen()
wn.setup(width=400, height=400)
red = turtle.Turtle()

def curve():
    steps = 200
    while steps > 0:
        red.right(1)
        red.forward(1)
        steps -= 1

def heart():
    red.fillcolor('red')
    red.begin_fill()
    red.left(140)
    red.forward(113)
    curve()
    red.left(120)
    curve()
    red.forward(112)
    red.end_fill()

heart()
red.ht()
turtle.done()