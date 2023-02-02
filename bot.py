import telebot
from main import weather_info

TOKEN = "5941632780:AAFTDrM3q09NqfAorfaAKYgEGFeROuXJe_4"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def welcome_message(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Hi, I'm a Telegram bot to tell you about weather.")
    bot.send_message(chat_id, "Send /weather <city name> to forecast weather data.")

@bot.message_handler(commands=['weather'])
def weather_forecast(message):
    chat_id = message.chat.id
    message_text = message.text
    splitted_message = message_text.split()
    city = splitted_message[-1]
    weather_details = weather_info(city)
    bot.send_message(chat_id, weather_details)

bot.infinity_polling()
