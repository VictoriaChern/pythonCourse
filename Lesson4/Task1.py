import os

# очищаем консоль
os.system('clear')

def ask_number():
    number = input(f'Введите точность числа пи: ')
    if(not number.lstrip('+ -').isdigit()):
        print('Ошибка: вы ввели не число! Повторите ввод')
        return ask_number()
    return int(number)

def get_pi(d):
    # вычисляем pi используя ряд Нилаканта
    pi = 3.00
    a = 2
    b = 3
    c = 4
    for i in range(1000000):
        pi = pi + 4/(a*b*c)
        a += 2
        b += 2
        c += 2
        pi = pi - 4/(a*b*c)
        a += 2
        b += 2
        c += 2 
    return round(pi, d)

d = ask_number()
print(f'π = {get_pi(d)}')