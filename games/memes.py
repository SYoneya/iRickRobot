from imports import *;



@dp.message_handler(lambda message: message.text.casefold() == 'рикролл')
async def rickroll(message: types.Message):
   await bot.copy_message(message.chat.id, -1001882577870, 2, protect_content=True, reply_to_message_id=message.message_id)

@dp.message_handler(lambda message: message.text.casefold() == 'мем')
async def mem(message: types.Message):
   await bot.copy_message(message.chat.id, -1001882577870, random.randint(4, 39), protect_content=True, reply_to_message_id=message.message_id)