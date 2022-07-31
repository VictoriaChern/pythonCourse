import os
import math

os.system('clear')

def askCoordinates():
    coordinates = list(map(lambda s: int(s),\
    filter(lambda s: s.isdigit(),\
        input('Введите координаты через пробел: ').split(' '))))
    if(len(coordinates) != 4):
        print('Ошибка: координат должно быть четыре! Повторите ввод')
        return askCoordinates()
    return coordinates

ls = askCoordinates()
distance =round(math.sqrt(math.pow(ls[2]-ls[0],2) + math.pow(ls[3]-ls[1],2)),2)
print(f'A ({ls[0]},{ls[1]}); B({ls[2]},{ls[3]}) -> {distance}')
