from aiogram import types; from main import bot, dp;



@dp.message_handler(content_types=['pinned_message'])
async def pinned_message(message: types.Message):
    await message.delete()