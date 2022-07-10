import os
import math

os.system('clear')

def askNumberOfFlat():
    numberOfFlat = input(f'Введите номер четверти: ')
    if(not numberOfFlat.isdigit()):
        print('Ошибка: вы ввели не число! Повторите ввод')
        return askNumberOfFlat()
    numberOfFlat = int(numberOfFlat)
    if(numberOfFlat < 1 or numberOfFlat > 4):
        print(f'Ошибка: {numberOfFlat} должна быть от 1 до 4! Повторите ввод')
        return askNumberOfFlat()
    return numberOfFlat

def diap(numberOfFlat):
    if(numberOfFlat == 1):
        return f'X: [0, {math.inf}]; Y: [0, {math.inf}]'
    elif(numberOfFlat == 2):
        return f'X: [0, {math.inf}]; Y: [0, {-math.inf}]'
    elif(numberOfFlat == 3):
        return f'X: [0, {-math.inf}]; Y: [0, {-math.inf}]'
    elif(numberOfFlat == 4):
        return f'X: [0, {-math.inf}]; Y: [0, {math.inf}]'
    else:
        return 'Неверно задан номер плоскости (должно быть от 1 до 4)'



i = askNumberOfFlat()
print(diap(i))
        