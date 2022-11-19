from turtle import *
from random import randint
'''
# .items()
d = {1 : 'a', 2 : 'b', 3 : 'c'}
for key, value in d.items():
    print(f'KEY: {key}')
    print(f'VALUE: {value}')

# .values(), .keys()
# При работе с этими методами нужно ЯВНО говорить, что мы получаем список (вложить выражение в list())
k = list(d.keys())
print(k)

v = list(d.values())
print(v)

data = {'amount_lines' : randint(5, 10),
        'angle' : randint(45, 90),
        'line_length' : randint(50, 100)}

for k, v in data.items():
    print(f'{k} = {v}')
    choice = randint(1, 2)
    if choice == 1:
        left(data['angle'])
    else:
        forward(data['line_length'])
'''

# Функции стоит вызывать по их имени и имя функции должно быть глаголом
def draw_square():
    for line in range(4):
        forward(50)
        left(90)
        
def draw_triangle():
    ...
# Для работы функции нужно вызвать ее по имени
draw_square()
draw_triangle()



