import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

clear()
ls = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
print(f'Список строк: {ls}')
str = input('Введите строку для поиска: ')
ls = list(filter(lambda t: t[1] == str, enumerate(ls)))
print(ls[1][0] if len(ls)>1 else -1)
