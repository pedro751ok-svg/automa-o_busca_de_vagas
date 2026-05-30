import telebot
from database.db import Vagas,session
bot = telebot.TeleBot("8601886664:AAHGnVMlXmeOPMiG8vpvrQAjodv2ELKa1tc")

def start(text):
  
    chat_id = "6410990747"
    bot.send_message(chat_id,text)