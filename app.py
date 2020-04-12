import COVID19Py
import telebot
from telebot import types
from datetime import datetime, date, time
from helper import dbHelper
from telebot import apihelper
import config

apihelper.proxy = {
  'https': config.proxy
}

bot = telebot.TeleBot(config.token)
