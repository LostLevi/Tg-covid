import COVID19Py
import telebot
from telebot import types
from datetime import datetime, date, time
from helpers import dbHelper
from telebot import apihelper
import config
import strings

apihelper.proxy = {
  'https': config.proxy
}

bot = telebot.TeleBot(config.token)

covid19 = COVID19Py.COVID19()
latest_world_info = covid19.getLatest()


def keyboard():
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='Обновить данные', callback_data='update')
    markup.add(btn)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    markup = keyboard()
    send_mess = strings.start_msg(message.from_user.first_name)
    bot.send_message(message.chat.id, send_mess, parse_mode = 'html', reply_markup = markup)

@bot.callback_query_handler(func=lambda x:True)
def callback_h(update):
    markup = keyboard()
    message = update.message
    if update == update:
        send_mess = "Фыр"
        bot.send_message(message.chat.id, send_mess, parse_mode = 'html', reply_markup = markup )

#print(strings.start_msg)

bot.polling(none_stop=True)
