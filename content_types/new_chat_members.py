from aiogram import types; from main import bot, dp;



@dp.message_handler(content_types=['new_chat_members'])
async def new_chat_members(message: types.Message):
    await bot.send_message(message.chat.id, f'''{message.new_chat_members[0].full_name} вступил(-а) в чат.''')
    await message.delete()