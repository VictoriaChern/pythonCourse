import os

# очищаем консоль
os.system('clear')

def ask_number():
    number = input(f'Введите число: ')
    if(not number.lstrip('+ -').isdigit()):
        print('Ошибка: вы ввели не число! Повторите ввод')
        return ask_number()
    return int(number)

def negafib(number):
    ls = []
    if (number < 0):
        number = -number

    # negativ
    prev = 0
    next = 1
    ls.append(prev)
    ls.append(next)
    for i in range(1, number):
        sum = prev - next
        prev = next
        next = sum
        ls.append(sum)
    ls.reverse()

    # positiv
    prev = 0
    next = 1
    ls.append(next)
    for i in range(1, number):
        sum = prev + next
        prev = next
        next = sum
        ls.append(sum)
    return ls

num = ask_number()
print(negafib(num))
