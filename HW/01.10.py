from turtle import *
'''
# Task 1 - Triangle draw
figure = input('Введите название фигуры: ')
if figure == 'Треугольник':
    forward(100)
    left(90)
    forward(50)
    left(115)
    forward(120)
    exitonclick()
else:
    print('Error!')

# Task 2 - Triangle types
triangle_type = input('Введи тип треугольника: ').capitalize()
speed(1)
if triangle_type == 'Прямоугольный':
    forward(100)
    left(90)
    forward(50)
    left(115)
    forward(120)
elif triangle_type == "Тупоугольный":
    forward(100)
    left(45)
    forward(50)
    left(150)
    forward(140)
elif triangle_type == 'Остроугольный':
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)    
else:
    print('Error!')
exitonclick()
'''
# Task 3 - David Star
speed(1)
forward(100)
left(120)
forward(100)
left(120)
forward(100)
penup()
setx(100.00) # setx сдвигает нашу ручку по горизонтали
sety(50.00) # как и setx, только по вертикали
pendown()
forward(100)
right(120)
forward(100)
right(120)
forward(100)
exitonclick()