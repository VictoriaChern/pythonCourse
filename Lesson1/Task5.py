import os
import math

os.system('clear')

def askCoordinate(name):
    coordinate = input(f'Введите координату {name}: ')
    if(not coordinate.lstrip('+ -').isdigit()):
        print('Ошибка: вы ввели не число! Повторите ввод')
        return askCoordinate(name)
    return int(coordinate)

def askPoint(name):
    x = askCoordinate(f'x точки {name}')
    y = askCoordinate(f'y точки {name}')
    return [x,y]

def getDistance(a,b):
    if(len(a) != 2 or len(b) != 2):
        print('Ошибка! Точка должна содержать 2 координаты!')
        return 0
    return math.sqrt(math.pow(b[0]-a[0],2) + math.pow(b[1]-a[1],2))

a = askPoint('A')
b = askPoint('B')
distance = round(getDistance(a,b), 2)
print(f'A ({a[0]},{a[1]}); B({b[0]},{b[1]}) -> {distance}')