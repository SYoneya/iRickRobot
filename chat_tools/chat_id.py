from imports import *;



@dp.message_handler(commands='chatid', commands_prefix='/!.')
async def chatid(message: types.Message):
    await message.reply(f'''{message.chat.id}''')