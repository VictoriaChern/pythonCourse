import os

# очищаем консоль
os.system('clear')

def ask_number_list():
    str_list = input('Введите числа через пробел: ').split(' ')
    number_list = []
    for val in str_list:
        if(isfloat(val)):
            number_list.append(float(val))
    return number_list

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def max_min_dif(numbers):
    new_list = []
    for n in numbers:
        new_list.append(n - int(n))
    max = new_list[0]
    min = new_list[0]
    for i in range(1,len(new_list)):
        if(new_list[i] > max):
            max = new_list[i]
        if(new_list[i] < min):
            min = new_list[i]
    return round(max - min, 3)

def get_afterpoint(fnum):
    strnum = str(fnum)
    return int(strnum[strnum.index('.')+1:])

nums = ask_number_list()
dif = max_min_dif(nums)
print(f'{nums} => {dif} или {get_afterpoint(dif)}')