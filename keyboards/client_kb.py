from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/режим_работы')
b2 = KeyboardButton('/Адрес')
b3 = KeyboardButton('/меню')

kb_client = ReplyKeyboardMarkup(resize_keyboard= True)
kb_client.insert(b1).insert(b2).insert(b3)
