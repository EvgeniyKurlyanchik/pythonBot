from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/режим_работы')
b2 = KeyboardButton('/Адрес')
b3 = KeyboardButton('/меню')
# b4 = KeyboardButton('Поделится номером', request_contact=True)
# b5 = KeyboardButton('Геолокация', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard= True)
kb_client.insert(b1).insert(b2).insert(b3)
# kb_client.insert(b1).insert(b2).insert(b3).insert(b4).insert(b5)