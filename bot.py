import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8502035128:AAGBoCgSX7eC4bocnT32UAe-WZgYFVrT2vM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton("💡 Info")
    btn2 = KeyboardButton("📁 My Files")
    btn3 = KeyboardButton("⚙️ Help")
    markup.add(btn1, btn2, btn3)

    bot.send_message(
        message.chat.id,
        "Welcome! Niche menu buttons dekho 👇",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: True)
def reply(message):
    if message.text == "💡 Info":
        bot.send_message(message.chat.id, "Info section")
    elif message.text == "📁 My Files":
        bot.send_message(message.chat.id, "Files section")
    elif message.text == "⚙️ Help":
        bot.send_message(message.chat.id, "Help section")
    else:
        bot.send_message(message.chat.id, "Unknown command!")

bot.polling(none_stop=True)
