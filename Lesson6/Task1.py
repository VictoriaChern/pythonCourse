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
ls = ['aaa','aaa1', 'bbb2', 'ccc3', 'ddd4', 'eee5', '67']
print(f'Список строк: {ls}')
n = ask_number()
fl = list(filter(lambda s: str(n) in s, ls))
res = 'есть' if len(fl) != 0 else 'отсутствует'
print(f'В заданном списке строк число {n} {res}')

