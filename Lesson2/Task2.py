import os
from tkinter import N

os.system('clear')

def ask_number():
    number = input(f'Введите число: ')
    if(not number.lstrip('+-').isdigit()):
        print('Ошибка: вы ввели не число! Повторите ввод')
        return ask_number()
    number = int(number)
    if (number <= 0):
        print('Ошибка: число должно быть больше 0! Повторите ввод')
        return ask_number()
    return number

def set_mult(number):
    mult = 1
    result = []
    for i in range(1, number+1):
        mult *= i
        result.append(mult)
    return result

N = ask_number()
print(f'N = {N} -> {set_mult(N)}')
