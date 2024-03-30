from telebot.types import Message

from loader import bot
from keyboards import *

@bot.message_handler(commands=['start'])
def reaction_start(message:Message):
    chat_id = message.chat.id
    bot.send_message(chat_id,f'Assalomu alekom{message.from_user.full_name}')

