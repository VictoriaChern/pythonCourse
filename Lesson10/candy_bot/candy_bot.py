from telegram import Bot
from telegram.ext import Updater, CommandHandler
from settings import SETTINGS
from game_handler import GAME_HANDLER
from settings_handler import SETTINGS_HANDLER

def info_callback(update, context):
    update.message.reply_text(f'''На столе лежит конфет - {SETTINGS['candies']}.
Играем мы с тобой делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем {SETTINGS['max_count']} конфет.
Тот, кто берет последнюю конфету - проиграл.''')

bot = Bot(token=SETTINGS['token'])
updater = Updater(token=SETTINGS['token'])
dispatcher = updater.dispatcher

handlers = {
    'start'    : GAME_HANDLER,
    'settings' : SETTINGS_HANDLER,
    'info'     : CommandHandler('info', info_callback)
}

for key, value in handlers.items():
    dispatcher.add_handler(value)
    print(f'Добавлен обработчик {key}')

print('Бот запущен!')
updater.start_polling()
updater.idle()