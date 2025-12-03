import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8502035128:AAGBoCgSX7eC4bocnT32UAe-WZgYFVrT2vM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Bot is running!")

bot.polling(none_stop=True)￼Enter
