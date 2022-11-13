import aiogram; from aiogram import types; from main import bot, dp;



@dp.message_handler(commands=['пин', 'pin'], commands_prefix='/!.')
async def pin_cmd(message: types.Message):
   try:
      member = await bot.get_chat_member(message.chat.id, message.from_user.id)
      if member.status not in {'administrator', 'creator'}:
         await message.reply(f'''Не получится закрепить, т.к. ты не имеешь соответствующие права.''')
         return
      elif not message.reply_to_message:
         await message.reply(f'''Нужно в ответ на сообщение.''')
         return
      await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
      await message.reply(f'''📌 Сообщение закреплено.''')
   except aiogram.utils.exceptions.BadRequest:
      await message.reply(f'''Не получится закрепить, т.к. я не имею соответствующие права.''')
      return