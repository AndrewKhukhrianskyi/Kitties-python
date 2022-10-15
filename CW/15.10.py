from turtle import *

steps = 4
horizontal_line = 150
vertical_line = 30
while steps > 0:
    forward(horizontal_line)
    left(90)
    forward(vertical_line)
    left(90)
    forward(horizontal_line)
    left(90)
    forward(vertical_line)
    left(90)
    penup()
    sety(-2)
    horizontal_line += 10
    vertical_line += 10
    pendown()
    steps -= 1
    
    
    
exitonclick()
