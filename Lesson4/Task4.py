import os

# очищаем консоль
os.system('clear')

def remove_digits(s):
    words = s.split(' ')
    result = ''
    for word in words:
        if(not has_digit(word)):
            result += word + ' '
    return result

def has_digit(str):
    for ch in str:
        if(ch.isdigit()):
            return True
    return False


f = open('text.txt','r')
lines = f.readlines()
f.close()
print(lines)
f = open('text.txt', 'w')


for line in lines:
    new_line = remove_digits(line)
    f.write(new_line.strip() + '\n')
    print(new_line)
f.close()