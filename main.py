import telebot
from currency_request import get_usd_to_rub
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("BOT_API_KEY")

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=["start", "help"])

def send_welcome(message):
    bot.reply_to(message, "Добрый день. Как вас зовут?")


@bot.message_handler(func = lambda message: True)
def return_current_rate(message):
    rate = get_usd_to_rub()
    bot.reply_to(message, f"Рад знакомству, {message.text}! Курс доллара сегодня {rate}р")

bot.polling()
