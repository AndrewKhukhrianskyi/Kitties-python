# Список
arr = [1,2,3]
print(arr)
arr.append(4)
print(arr)
# Кортеж
tup = (1,2,3,4,1,2,3,1)

# .count() - подсчет кол-ва повторений кортежа
# .index() - поиск элемента по выражению
# count()
print(tup.count(1))
# index()
print(tup.index(4))

# Свойства:
"""
1. Обращение по индексу (порядку)
2. Работа со срезами
3. Работа с методами кортежа
"""

from turtle import *

# Константы - постоянные переменные
# которые не меняются в процессе
# работы кода
COORDS = (0, 0)
'''
penup()
x, y = COORDS # x=0, y=0
goto(x,y)
pendown()
for elem in range(4):
    forward(100)
    left(90)
exitonclick()
'''

# Task 1 - N-угольник

speed('slowest')
COORDS = ((50, 50), (80, 60),
          (90, 40), (30, -20),
          (0,0), )
for coord in COORDS:
    x, y = coord # 0, 0
    goto(x,y)

exitonclick()
    


