from turtle import *
'''
# Task 1 - N-angle
speed('slowest')
COORDS = ((50, 50), (80, 60),
          (90, 40), (30, -20),
          (0,0), (-10, 20), 
          (-10, -10), (30, -40),
          (60, -40), (10, -5),
          (-50, -70), (-30, -80),
          (20, -10))
for coord in COORDS:
    x, y = coord 
    goto(x,y)
hideturtle()
exitonclick()
'''
# Task 2 - Olympic flag
circles = 5
x, y = 100, 0

while circles > 2:
    circle(50)
    penup()
    goto(x, y)
    pendown()
    x += 100
    circles -= 1

x = 125
y -= 100
penup()
goto(x - 75, y)
pendown()

while circles > 0:
    circle(50)
    penup()
    x += 25
    circles -= 1
    goto(x, y)
    pendown()
    
exitonclick()