import os

# очищаем консоль
os.system('clear')

def ask_number():
    number = input(f'Введите число: ')
    if(not number.lstrip('+ -').isdigit()):
        print('Ошибка: вы ввели не число! Повторите ввод')
        return ask_number()
    return int(number)

def to_binary(number):
    result = ''
    while(number != 0):
        result += str(number%2)
        number = int(number/2)
    return result[::-1]

num = ask_number()
print(f'{num} -> {to_binary(num)}')

