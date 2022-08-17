from telegram import Bot
from telegram.ext import Updater, CommandHandler
from settings import TOKEN
from game_handler import GAME_HANDLER

def info_callback(update, context):
    update.message.reply_text('''Игра "Быки и коровы".
Бот загадывает слово из определенного количества букв. Допустим, четырех.
Ваша задача - угадать слово,называя слова из того же количества букв (добавьте проверку). 
Если буква из вашего слова есть в загаданном - это корова.
Если еще и позиция совпадает - это бык.
Пример: 
загаданное слово: чаты. 
Игрок: тьма - 2 коровы
Игрок : чума - 1 бык, 1 корова''')

bot = Bot(token = TOKEN)
updater = Updater(token = TOKEN)
dispatcher = updater.dispatcher

handlers = {
    'start'    : GAME_HANDLER,
    'info'     : CommandHandler('info', info_callback)
}

for key, value in handlers.items():
    dispatcher.add_handler(value)
    print(f'Добавлен обработчик {key}')

print('Бот запущен!')
updater.start_polling()
updater.idle()