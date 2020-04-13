import COVID19Py
import telebot
from telebot import types
from datetime import datetime, date, time, timedelta
from helpers import dbHelper
from telebot import apihelper
import config
import strings
from stopcovparse import update_db

apihelper.proxy = {
  'https': config.proxy
}

bot = telebot.TeleBot(config.token)

dateToday = date.today().strftime("%Y-%m-%d")
prevDay = date.today() - timedelta(days=1)
prevDay = prevDay.strftime('%Y-%m-%d')


covid19 = COVID19Py.COVID19()
latest_world_info = covid19.getLatest()
latest_world_actual = latest_world_info['confirmed']

rus_new = covid19.getLocationByCountryCode("RU")
population = rus_new[0]['country_population']

def illed_procent(illed):
    return round((100 - ((population - int(illed)) / population) * 100), 3)


def keyboard():
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='Обновить данные', callback_data='update')
    markup.add(btn)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    markup = keyboard()
    send_mess = strings.start_msg(message.from_user.first_name, latest_world_actual)
    bot.send_message(message.chat.id, send_mess, parse_mode = 'html', reply_markup = markup)

@bot.callback_query_handler(func=lambda x:True)
def callback_h(update):
    markup = keyboard()
    message = update.message
    #update_db()
    all_data = dbHelper.return_full_day(dateToday)
    illed = all_data[0][1]
    day_stat_ill = all_data[0][2]
    res = all_data[0][3]
    deaths = all_data[0][4]
    il_proc = illed_procent(illed)
    if update == update:
        send_mess = strings.full_msg(illed, day_stat_ill, res, deaths, il_proc)
        bot.send_message(message.chat.id, send_mess, parse_mode = 'html', reply_markup = markup )

#print(strings.start_msg)

bot.polling(none_stop=True)
