from imports import *;



@dp.message_handler(commands=['разбан', 'unban'], commands_prefix='/!.')
async def unban_cmd(message: types.Message):
   try:
      member = await bot.get_chat_member(message.chat.id, message.from_user.id)
      if member.status not in {'administrator', 'creator'}:
         await message.reply(f'''Не получится дать разбан, т.к. ты не имеешь соответствующие права.''')
         return
      elif not message.reply_to_message:
         await message.reply(f'''Нужно в ответ на сообщение.''')
         return
      admin = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
      if admin.status in {'administrator', 'creator'}:
         await message.reply(f'''Не получится дать разбан администратору.''')
         return
      await bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
      await bot.send_message(message.chat.id, f'''✅ <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> больше не в бане.''', reply_to_message_id=message.message_id)
   except aiogram.utils.exceptions.BadRequest:
      await message.reply(f'''Не получится дать разбан, т.к. я не имею соответствующие права.''')
      return