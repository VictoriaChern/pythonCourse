def ask_number():
    number = input('Введите число: ')
    if(not isfloat(number)):
        print("Вы ввели не число, повторите ввод:")
        return ask_number()
    return number

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def sum_numbers(number):
    sum = 0
    for i in range(len(number)):
        s = number[i]
        if(s.isdigit()):
            sum += int(s)
    return sum

number = ask_number()
print(f'{number} -> {sum_numbers(number)}')




