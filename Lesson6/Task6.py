import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def ask_number():
    number = input(f'Введите число: ')
    if(not number.isdigit()):
        print('Ошибка: вы ввели не число! Повторите ввод')
        return ask_number()
    return int(number)

clear()

n = ask_number()
ls = [(-3 if i % 2 == 0 else 3)**(i - 1) for i in range(1, n+1)]
print(ls)
