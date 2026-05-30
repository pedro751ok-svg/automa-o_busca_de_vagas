import telebot
from dotenv import load_dotenv()
import os

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

def start(text):
  
    chat_id = os.getenv("ID_USUARIO")
    bot.send_message(chat_id,text)