from functools import reduce
import os
import random

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

clear()
ls = random.sample(range(100), 10)
print(list(ls))
sum = str(reduce(lambda x,y: x + y,\
    map(lambda x: x[1],\
        filter(lambda x: x[0]%2 != 0, enumerate(ls)))))
print(f'Сумма чисел списка стоящих на нечетной позиции: {sum}')