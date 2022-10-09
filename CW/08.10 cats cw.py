from turtle import *
from time import sleep
# Infinite (Бесконечный цикл)
#while True:
#    print('aaa')

# Loop Conditions (Условия цикла)
count = 5
while count > 0:
    sleep(1) # через 1 секунду код продолжит работать
    print(count)
    count -= 1

# Цикл может обрабатывать множество условий
count = 10
while count % 2 == 0 and count > 0:
    print(count)
    count -= 1

# Можно один цикл вложить внутрь другого
count = 5
while count > 0:
    number = 0
    while number < 5:
        print(f'Number: {number}')
        number += 1
    print(f'Count: {count}')  
    count -= 1

# Task - Loop spiral
length = 100 # длина линии
angle = 90 # угол
left(45)
while length > 0:
    forward(length)
    length -= 10
    left(angle)
