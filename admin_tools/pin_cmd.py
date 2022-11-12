from aiogram import types; from main import bot, dp;



@dp.message_handler(commands=['пин', 'pin'], commands_prefix='/!.')
async def pin_cmd(message: types.Message):
   member = await bot.get_chat_member(message.chat.id, message.from_user.id)
   if member.status not in {'administrator', 'creator'}:
      await message.reply(f'''Ты не можешь закрепить, так как не имеешь прав администратора.''')
      return
   elif not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
   await message.reply(f'''📌 Сообщение закреплено.''')