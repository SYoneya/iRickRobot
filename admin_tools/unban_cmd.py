from aiogram import types; from main import bot, dp;



@dp.message_handler(commands=['разбан', 'unban'], commands_prefix='/!.')
async def unban_cmd(message: types.Message):
   member = await bot.get_chat_member(message.chat.id, message.from_user.id)
   if member.status not in {'administrator', 'creator'}:
      await message.reply(f'''Ты не можешь дать разбан, так как не имеешь прав администратора.''')
      return
   elif not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   admin = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
   if admin.status in {'administrator', 'creator'}:
      await message.reply(f'''Ты не можешь дать разбан администратору.''')
      return
   await bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
   await bot.send_message(message.chat.id, f'''✅ <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> больше не в бане.''', reply_to_message_id=message.message_id)