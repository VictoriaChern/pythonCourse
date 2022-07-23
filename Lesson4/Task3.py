import os

# очищаем консоль
os.system('clear')

def ask_number():
    number = input(f'Введите натуральное число N: ')
    if(not number.isdigit()):
        print('Ошибка: вы ввели не число! Повторите ввод')
        return ask_number()
    number = int(number)
    if(number <= 0):
        print(f'Ошибка! Число должно быть больше 0')
        return ask_number()
    return number

def prime_factor(N):
    prime_numbers = []
    for i in range(2,N):
        is_simple = True
        for j in range(2,i):
            if(i == j):
                continue
            if(i%j == 0):
                is_simple = False
                break
        if(is_simple):
            prime_numbers.append(i)
    result = []
    for i in prime_numbers:
        if(N % i == 0):
            result.append(i)
    return result

N = ask_number()
print(f'N = {N} -> {prime_factor(N)}')