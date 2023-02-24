import string

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os, json, string

bot= Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)
async def on_startup(_):
    print('Бот вышел в онлайн')
# **********************************Клиентская часть  *********************************************
@dp.message_handler(commands=['start','help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id,'Приятного аппетита!')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/Pizza_sheef1234_Bot')
@dp.message_handler(commands=['режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ПНД-ВСК  c 9:00 до 23:00')
@dp.message_handler(commands=['Адрес'])
async def pizza_address(message: types.Message):
    await bot.send_message(message.from_user.id, 'Москва ,ул. Мясницкая 1')
# **********************************Админская  часть  *********************************************


# **********************************Общая часть  *********************************************

@dp.message_handler()
async def echo_send(message : types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split('')}\
    .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Мат запрещен')
        await message.delete()





    # if message.text=='Привет':
    #     await message.answer('И тебе привет!!!')
    # await message.reply(message.text)
    # await  bot.send_message(message.from_user.id, message.text)
executor.start_polling(dp, skip_updates=True, on_startup=on_startup())