from telebot.types import KeyboardButton,ReplyKeyboardMarkup

def reaction_abaut():
    markub = ReplyKeyboardMarkup(resize_keyboard=True)
    markub.add(KeyboardButton('About 🤖'),
               KeyboardButton('Wikipedia 🔎'),
               KeyboardButton('Exo 🤡')
    )
    return markub
