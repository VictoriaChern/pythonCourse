import os

# очищаем консоль
os.system('clear')

def delete_from_text(word, txt):
    words = txt.split()
    ls = list(filter(lambda w: word not in w, words))
    return ' '.join(ls)


text = input('Введите текст: ')
delete_word = input('Введите текст для удаления: ')
print(delete_from_text(delete_word,text))
