import math
import random
import sqlite3

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor

import kb #кнопки в боте

BOT_TOKEN = '########:##########################' # тут нужен токен, который можно получить в bot father
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

connection = sqlite3.connect('dictionary.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM Eng_Ru_Dict")
records = cursor.fetchall()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Для генерации вопроса жми: /vopros")


@dp.message_handler(commands=['vopros'])
async def cmd_vopros(message: types.Message):
    
    nomer_voprosa = random.randint(1,7999)
    
    global variant_otveta 
    variant_otveta = random.randint(1,4)
    
    await message.answer(records[nomer_voprosa][1], reply_markup=kb.markup)

    for i in range(4):
       if variant_otveta == i+1 :
           await message.answer(records[nomer_voprosa][2])          #верный ответ
       else:
           await message.answer(records[random.randint(1,7999)][2]) #генерируем неправильный ответ    
    

@dp.message_handler(lambda message: message.text == '1️⃣' or '2️⃣' )
async def cmd_otvet(message: types.Message):
    if variant_otveta == int(message.text[0]):
        await message.reply("Правильно. Далее:/vopros")
    else:
        await message.reply("ОШИБКА. Далее:/vopros")


if __name__ == '__main__':
    executor.start_polling(dp)
