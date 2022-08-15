from time import sleep
from telegram import ForceReply
from telegram.ext import (
    Filters,
    CommandHandler,
    MessageHandler,
    ConversationHandler
)
from settings import SETTINGS
import random

def start_command_callback(update, context):
    candies = SETTINGS['candies']
    context.user_data['total_count'] = candies
    update.message.reply_text(f'Началась Игра!\n\
        На столе лежит {candies} конфета')
    update.message.reply_text('Бросаем жребий...')
    sleep(1)
    rand = random.randint(0,1)
    if (rand == 0):
        update.message.reply_text('Ты ходишь первым!')
        return player_turn(update, context)
    update.message.reply_text('Я хожу первым!')
    return bot_turn(update, context)

def player_turn_callback(update, context):
    number = update.message.text
    total_count = context.user_data['total_count']
    max_count = SETTINGS['max_count']
    if(not number.isdigit()):
        update.message.reply_text("Ошибка: вы ввели не число! Повторите ввод")
        return EXPECT_PLAYER_ANSWER
    number = int(number)
    if(number > max_count):
        update.message.reply_text(f'Ошибка: за один ход можно забрать не более чем {max_count} конфет')
        return EXPECT_PLAYER_ANSWER
    if (number > total_count):
        update.message.reply_text(f'Ошибка: вы не можете взять больше чем {total_count} конфет')
        return EXPECT_PLAYER_ANSWER
    if (number <= 0):
        update.message.reply_text('Ошибка: количество конфет должно быть больше нуля')
        return EXPECT_PLAYER_ANSWER

    total_count -= number
    update.message.reply_text(f'На столе осталось {total_count} конфет')
    context.user_data['total_count'] = total_count
    if (total_count == 0):
        update.message.reply_text('Вы проиграли 😢, Бот победил!')
        return ConversationHandler.END
    return bot_turn(update, context)

def player_turn(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
        text='Твой ход. Сколько конфет вы хотите взять?', reply_markup=ForceReply())
    return EXPECT_PLAYER_ANSWER

def bot_turn(update, context):
    update.message.reply_text('Мой ход...')
    total_count = context.user_data['total_count']
    max_count = SETTINGS['max_count']
    limit = max_count if max_count < total_count else total_count
    number = random.randint(1, limit)
    update.message.reply_text(f'Я забираю {number} конфет')
    total_count -= number
    update.message.reply_text(f'На столе осталось {total_count} конфет')
    context.user_data['total_count'] = total_count
    if (total_count == 0):
        update.message.reply_text('Я проиграл, Вы победили! 🥳🥳🥳')
        return ConversationHandler.END
    return player_turn(update, context)

def cancel_callback(update, context):
    update.message.reply_text('Игра прервана')
    return ConversationHandler.END

EXPECT_PLAYER_ANSWER = 0 

GAME_HANDLER = ConversationHandler(
    entry_points=[CommandHandler('start', start_command_callback)],
    states={
        EXPECT_PLAYER_ANSWER : [MessageHandler(Filters.text & (~Filters.command), player_turn_callback)]
    },
    fallbacks=[CommandHandler('cancel', cancel_callback)]
)