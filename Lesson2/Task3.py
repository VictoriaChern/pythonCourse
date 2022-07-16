import os

os.system('Clear')

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

def sequence(number):
    result = {}
    for k in range(1,number+1):
        result[k] = (1+1/k)**k
    return result

n = ask_number()
print(f'n = {n}: {sequence(n)}')
