from aiogram import types; from main import bot, dp;



@dp.message_handler(lambda message: message.text.casefold() == 'рик' or message.text.casefold() == 'бот')
async def ping_cmd(message: types.Message):
   await message.reply('✅ На месте!')

@dp.message_handler(lambda message: message.text.casefold() == 'пинг')
async def ping_cmd(message: types.Message):
   await message.reply('ПОНГ')

@dp.message_handler(lambda message: message.text.casefold() == 'пиу')
async def ping_cmd(message: types.Message):
   await message.reply('ПАУ')