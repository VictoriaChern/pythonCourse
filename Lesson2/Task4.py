import os
import time
import random

os.system("Clear")

def ask_number(name):
    number = input(f'Введите {name}: ')
    if(not number.lstrip('+ -').isdigit()):
        print('Ошибка: вы ввели не число! Повторите ввод')
        return ask_number(name)
    return int(number)


def rand_int(min, max):
    t = time.time()
    t = t - float(str(t).split('.')[0])
    r = min + t * (max - min)
    return int(r)

min = ask_number('MIN')
max = ask_number('MAX')
result = rand_int(min, max)
print(f'Случайное число в диапазоне от {min} до {max}: {result}')
