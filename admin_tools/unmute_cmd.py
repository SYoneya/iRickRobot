from imports import *;



@dp.message_handler(commands=['размут', 'unmute'], commands_prefix='/!.')
async def unmute_cmd(message: types.Message):
   try:
      member = await bot.get_chat_member(message.chat.id, message.from_user.id)
      if member.status not in {'administrator', 'creator'}:
         await message.reply(f'''Не получится дать размут, т.к. ты не имеешь соответствующие права.''')
         return
      elif not message.reply_to_message:
         await message.reply(f'''Нужно в ответ на сообщение.''')
         return
      admin = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
      if admin.status in {'administrator', 'creator'}:
         await message.reply(f'''Не получится дать размут администратору.''')
         return
      await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages=True, can_send_other_messages=True, can_send_media_messages=True, can_add_web_page_previews=True)
      await bot.send_message(message.chat.id, f'''🔊 <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> больше не в муте.''', reply_to_message_id=message.message_id)
   except aiogram.utils.exceptions.BadRequest:
      await message.reply(f'''Не получится дать размут, т.к. я не имею соответствующие права.''')
      return