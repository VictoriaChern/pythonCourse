from cgitb import reset
import os

# очищаем консоль
os.system('clear')

def rle_decode(st: str):
    mult = 0
    res = ''
    for ch in st:
        if(ch.isdigit()):
            mult = int(ch)
        else:
            res += ch*mult
    return res

def rle_encode(st: str):
    res = ''
    c = st[0]
    count = 0
    for ch in st:
        if(ch == c):
            count+=1
        else:
            res += str(count) + c
            c = ch
            count = 1
    res += str(count) + c
    return res

def convert_file(f_convert: callable, input_file: str, output_file: str):
    data = ''
    with open(input_file, 'r') as f:
        data = f.read()
        print(f'read data from file {input_file}:\n{data}\n')
    data = f_convert(data)
    with open(output_file, 'w') as f:
        f.write(data)
        print(f'write converted data to file {output_file}:\n{data}\n')

# !!! запускать Task4.py из папки Lesson5 !!!
convert_file(rle_encode,'rle_source.txt','rle_encode_result.txt')
convert_file(rle_decode,'rle_encode_result.txt', 'rle_decode_result.txt')