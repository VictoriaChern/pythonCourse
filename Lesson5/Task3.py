import os

# очищаем консоль
os.system('clear')

def get_tuples(ls1, ls2):
    return list(zip(ls1, map(lambda s: s.upper(), ls2)))

def convert(tuples):
    f_ord = lambda c: ord(c)
    f_map = lambda tuple: (tuple[0], sum(map(f_ord,[c for c in tuple[1]])), tuple[1])
    f_filter = lambda tuple: tuple[1]%tuple[0] == 0

    with_ords = map(f_map, tuples)
    filtered = filter(f_filter, with_ords)

    return list(map(lambda t: (t[1],t[2]), filtered))

langs = ['python', 'c#', 'java', 'javascript']
numbers = list(range(1, len(langs) + 1))

tuples = get_tuples(numbers, langs)
print(f'first function: {tuples}')
print(f'second function: {convert(tuples)}')