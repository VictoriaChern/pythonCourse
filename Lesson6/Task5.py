import os
import math
import random

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

clear()
ls = random.sample(range(50), random.randint(4,8))
center = math.ceil(len(ls)/2)
left = ls[:center]
right = ls[center:]
right.reverse()

result = list(map(lambda tuple: tuple[0]*tuple[1], zip(left,right)))
print(f'{ls} => {result}')