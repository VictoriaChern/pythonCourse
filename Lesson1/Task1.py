import os

os.system('clear')

def askDayOfWeek():
    dayOfWeek = input('Введите номер дня недели: ')
    if(not dayOfWeek.isdigit()):
        print('Ошибка: вы ввели не число')
        return askDayOfWeek()
    dayOfWeek = int(dayOfWeek)
    if(dayOfWeek < 1 or dayOfWeek > 7):
        print('Ошибка: день недели должен быть от 1 до 7')
        return askDayOfWeek()
    return dayOfWeek

dayOfWeek = askDayOfWeek()
if(dayOfWeek == 6 or dayOfWeek == 7):
    print(f'{dayOfWeek} -> да')
else:
    print(f'{dayOfWeek} -> нет')