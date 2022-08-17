from telegram.ext import (
    Filters,
    CommandHandler,
    MessageHandler,
    ConversationHandler
)
from settings import WORDS
import random

def start_command_callback(update, context):
    rand = random.randint(0,len(WORDS))
    secret_word = WORDS[rand]
    context.user_data['secret_word'] = secret_word
    update.message.reply_text(f'Началась Игра!\n\
        Я загадал слово из {len(secret_word)} букв. Отгадай его!')
    update.message.reply_text('Твой ход')
    return EXPECT_PLAYER_ANSWER

def player_turn_callback(update, context):
    answer = update.message.text.lower()
    secret_word = context.user_data['secret_word']
    len_secret_word = len(secret_word)
    if(not validate_player_answer(answer, len_secret_word)):
        update.message.reply_text(f'Ошибка: слово должно состоять из {len_secret_word} букв')
        return EXPECT_PLAYER_ANSWER
    bulls = 0
    cows = 0
    for i,a in enumerate(secret_word):
        for j,b in enumerate(answer):
            if(a == b and i == j):
                bulls += 1
            elif(a == b):
                cows += 1
    update.message.reply_text(f'{answer}: {bulls} быков, {cows} коров')
    if(len_secret_word == bulls):
        update.message.reply_text(f'Поздравляем!🥳 Вы отгадали! Это слово - "{secret_word}"')
        return ConversationHandler.END
    update.message.reply_text('Следующий ход')
    return EXPECT_PLAYER_ANSWER

def validate_player_answer(answer, length):
    if(len(answer) != length):
        return False
    if(not answer.isalpha()):
        return False
    return True

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