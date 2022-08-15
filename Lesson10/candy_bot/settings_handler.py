from telegram.ext import (
    Filters,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    CallbackQueryHandler
)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ForceReply
from settings import SETTINGS


def settings_callback(update, context):
    update_options = [
        [
            InlineKeyboardButton("Всего 🍬", callback_data='candies'),
            InlineKeyboardButton("🍬 за ход", callback_data='max_count'),
        ]
    ]
    markup = InlineKeyboardMarkup(update_options)
    update.message.reply_text('Какие настройки вы хотите изменить?', reply_markup=markup)
    return EXPECT_BUTTON_CLICK

def setting_button_click_callback(update, context):
    query = update.callback_query
    query.answer(f'button click {query.data} recieved')
    if query.data == 'candies':
        query.edit_message_text(f'Вы выбрали изменить общее количество конфет')
        context.bot.send_message(chat_id=update.effective_chat.id,
                                text='Введите общее количество конфет', reply_markup=ForceReply())
        return EXPECT_CANDIES
    if query.data == 'max_count':
        query.edit_message_text(f'Вы выбрали изменить максимальное количество конфет за ход')
        context.bot.send_message(chat_id=update.effective_chat.id,
                                text='Введите количество конфет за ход', reply_markup=ForceReply())
        return EXPECT_MAX_COUNT

def set_candies_callback(update, context):
    candies = update.message.text
    if(not candies.isdigit()):
        update.message.reply_text("Ошибка: вы ввели не число! Повторите ввод")
        return EXPECT_CANDIES
    SETTINGS['candies'] = int(candies)
    update.message.reply_text('Изменения сохранены')
    return ConversationHandler.END

def set_max_count_callback(update, context):
    max_count = update.message.text
    if(not max_count.isdigit()):
        update.message.reply_text("Ошибка: вы ввели не число! Повторите ввод")
        return EXPECT_MAX_COUNT
    SETTINGS['max_count'] = int(max_count)
    update.message.reply_text('Изменения сохранены')
    return ConversationHandler.END

def cancel_callback(update, context):
    update.message.reply_text('Okay')
    return ConversationHandler.END

EXPECT_BUTTON_CLICK, EXPECT_CANDIES, EXPECT_MAX_COUNT = range(3)

SETTINGS_HANDLER = ConversationHandler(
    entry_points=[CommandHandler('settings', settings_callback)],
    states={
        EXPECT_BUTTON_CLICK: [CallbackQueryHandler(setting_button_click_callback)],
        EXPECT_CANDIES: [MessageHandler(Filters.text & (~Filters.command), set_candies_callback)],
        EXPECT_MAX_COUNT: [MessageHandler(Filters.text & (~Filters.command), set_max_count_callback)]
    },
    fallbacks=[CommandHandler('cancel', cancel_callback)]
)