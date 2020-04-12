import COVID19Py
import telebot
from datetime import datetime, date, time
import time
import math
from telebot import types
import os
import stopcovparse
import stopcov_db

path = os.path.dirname(os.path.abspath(__file__)) + '\\'

from telebot import apihelper

apihelper.proxy = {
  'https': 'socks5h://geek:socks@t.geekclass.ru:7777'
}

covid19 = COVID19Py.COVID19()
#location = covid19.getLocationByCountryCode('US')

bot = telebot.TeleBot('1182477486:AAG-9aBZM13HCxs6P006gDI62rfsM7B61bM')

#latest = covid19.getLatest()
latest = covid19.getLatest()
class ru_update():
    def rus_upd(self):
        return covid19.getLocationByCountryCode("RU")

rus = ru_update()
rus_new = rus.rus_upd()

bad_get_date = rus_new[0]['last_updated']
date_time_list = bad_get_date.split('T')
update_date = date_time_list[0]
update_time = date_time_list[1].split('.')[0]
current_date = date.today().strftime("%Y-%m-%d")
current_time = time.strftime("%H:%M:%S")

illed = rus_new[0]['latest']['confirmed']
deaths = rus_new[0]['latest']['deaths']
#update_date = date_time_list[0]


#fw = open(path + 'cov_temp.csv', 'w')
#fw.writelines((update_date) + ';' + str(illed) + ';' + str(deaths))
#fw.close()

fr = open(path + 'cov_temp.csv', 'r')
frRead = fr.readlines()
old_data = frRead[0].strip().split(';')

d1 = datetime.strptime(update_date, "%Y-%m-%d")
d2 = datetime.strptime(old_data[0], "%Y-%m-%d")

days_gone = int(list(str(d1 - d2))[0])

if days_gone >= 2:
    fw = open(path + 'cov_temp.csv', 'w')
    fw.writelines((update_date) + ';' + str(illed) + ';' + str(deaths))
    fw.close()


population = rus_new[0]['country_population']
old_data_ill = old_data[1]
old_data_death = old_data[2]
fr.close()

day_stat_ill = int(illed) - int(old_data_ill)
day_stat_death = int(deaths) - int(old_data_death)

illed_procent = round((100 - ((population - illed) / population) * 100), 3)

def keyboard():
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text='Обновить данные', callback_data='data')
    markup.add(btn)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    markup = keyboard()
    send_mess = f"<b>Привет {message.from_user.first_name}</b> \nКоличество заболевших в мире:<b> {latest['confirmed']}</b> \nНажмите кнопку для получения данных."
    bot.send_message(message.chat.id, send_mess, parse_mode = 'html', reply_markup = markup)

@bot.callback_query_handler(func=lambda x:True)
def callback_h(data):
    markup = keyboard()
    message = data.message
    if data == data:
        send_mess = f"Всего заражено в России: <b>{illed}</b> \nЗа последние сутки: <b>{day_stat_ill}</b>\nЗаражено: <b>{illed_procent}%</b> населения\nПогибло: <b>{deaths}</b>\n<i>Обновлено {update_date} {update_time}</i>"
        bot.send_message(message.chat.id, send_mess, parse_mode = 'html', reply_markup = markup )

#@bot.message_handler(commands=['Данные','Обновить','data'])
#def rus(message):
#    markup = keyboard()
#    send_mess = f"Всего заражено в России: <b>{illed}</b> \nПогибло: <b>{deaths}</b>\n<i>Обновлено {update_date} {update_time}</i>"
#    bot.send_message(message.chat.id, send_mess, parse_mode = 'html', reply_markup = markup )

print(rus_new)

bot.polling(none_stop=True)
