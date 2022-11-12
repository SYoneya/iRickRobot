from aiogram import types; from main import bot, dp;



@dp.message_handler(lambda message: message.text.casefold() == 'рикролл')
async def rickroll(message: types.Message):
   await bot.copy_message(message.chat.id, -1001882577870, 2, protect_content=True, reply_to_message_id=message.message_id)