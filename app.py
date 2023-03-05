import telebot

from telebot.types import Message
from classes import sqlite3_client

bot = telebot.TeleBot("5784165981:AAELedr0F2jYbaGCHb1VIWdUKkuObazjT84")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    is_premium = message.from_user.is_premium
    sqlite3_client.save_user_info(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        username=username,
        is_premium=is_premium
    )
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()

