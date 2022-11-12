from aiogram import types; import random; from main import bot, dp;



@dp.message_handler(lambda message: message.text.casefold() == 'рикролл')
async def rickroll(message: types.Message):
   await bot.copy_message(message.chat.id, -1001882577870, 2, protect_content=True, reply_to_message_id=message.message_id)

@dp.message_handler(lambda message: message.text.casefold() == 'мем')
async def mem(message: types.Message):
   await bot.copy_message(message.chat.id, -1001882577870, random.randint(4, 39), protect_content=True, reply_to_message_id=message.message_id)



@dp.message_handler(lambda message: message.text.casefold() == 'рик' or message.text.casefold() == 'бот')
async def ping_cmd(message: types.Message):
   await message.reply('✅ На месте!')

@dp.message_handler(lambda message: message.text.casefold() == 'пинг')
async def ping_cmd(message: types.Message):
   await message.reply('ПОНГ')

@dp.message_handler(lambda message: message.text.casefold() == 'пиу')
async def ping_cmd(message: types.Message):
   await message.reply('ПАУ')