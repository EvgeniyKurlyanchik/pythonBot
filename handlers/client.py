import string,json
from create_bot import dp, bot
from aiogram import types, Dispatcher
from keyboards import kb_client
from data_base import sqlite_db

#@dp.message_handler(commands=['start','help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,'Приятного аппетита!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/Pizza_sheef1234_Bot')


# @dp.message_handler(commands=['режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ПНД-ВСК  c 9:00 до 23:00')


# @dp.message_handler(commands=['Адрес'])
async def pizza_address_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Москва ,ул. Мясницкая 1')

# @dp.message_handler(commands=['меню'])
async def pizza_menu_commands(message: types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_client( dp : Dispatcher):
    dp.register_message_handler(command_start, commands =['start','help'])
    dp.register_message_handler(pizza_open_command,commands =['режим_работы'])
    dp.register_message_handler(pizza_address_command,commands =['адрес'])
    dp.register_message_handler(pizza_menu_commands, commands =['меню'])

# @dp.message_handler(commands=['меню'])
# async def pizza_menu_commands(message: types.Message):
#     for ret in cur.execute('Select  *FROM menu').fetchall:
#         await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n Описание: {ret[2]}\n Price {ret[-1]} ')