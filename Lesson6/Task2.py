from functools import reduce
import os
import random

# очищаем консоль
os.system('clear')

ls = random.sample(range(100), 10)
print(list(ls))
sum = str(reduce(lambda x,y: x + y,\
    map(lambda x: x[1],\
        filter(lambda x: x[0]%2 != 0, enumerate(ls)))))
print(f'Сумма чисел списка стоящих на нечетной позиции: {sum}')