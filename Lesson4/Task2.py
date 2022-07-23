import os

# очищаем консоль
os.system('clear')

def ask_number_list():
    str_list = input('Введите числа через пробел: ').split(' ')
    number_list = []
    for val in str_list:
        if(val.isdigit()):
            number_list.append(int(val))
    return number_list

def get_unique(ls):
    result = []
    for i in range(len(ls)):
        is_unique = True
        for j in range(len(ls)):
            if(i == j):
                continue
            if(ls[i] == ls[j]):
                is_unique = False
                break
        if(is_unique):
            result.append(ls[i])
    return result

numbers = ask_number_list()
print(f'Оригинальный список: {numbers}\n\
Список неповторяющихся элементов: {get_unique(numbers)}')
