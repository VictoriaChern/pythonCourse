import os

os.system('clear')

def askCoordinate(name):
    coordinate = input(f'Введите координату {name}: ')
    if(not coordinate.lstrip('+ -').isdigit()):
        print('Ошибка: вы ввели не число! Повторите ввод')
        return askCoordinate(name)
    coordinate = int(coordinate)
    if(coordinate == 0):
        print(f'Ошибка: {name} не должна быть равна 0! Повторите ввод')
        return askCoordinate(name)
    return coordinate

def getNumberOfFlat(x,y):
    if(x > 0 and y > 0):
        return 1
    elif(x > 0 and y < 0):
        return 2
    elif(x < 0 and y < 0):
        return 3
    else:
        return 4

x = askCoordinate('X')
y = askCoordinate('Y')
flat = getNumberOfFlat(x,y)
print(f'X = {x}; Y = {y} -> {flat}')
