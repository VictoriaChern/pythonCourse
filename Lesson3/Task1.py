import os
import re

# очищаем консоль
os.system('clear')

def ask_number_list():
    str_list = input('Введите числа через пробел: ').split(' ')
    number_list = []
    for val in str_list:
        if(val.isdigit()):
            number_list.append(int(val))
    return number_list

def sum_odd_numbers(list_numbers):
    sum = 0
    for i,val in enumerate(list_numbers):
        if(not i%2 == 0):
            sum += val
    return sum

numbers = ask_number_list()
print(f'{numbers} -> сумма элементов на нечетной позиции = {sum_odd_numbers(numbers)}')

