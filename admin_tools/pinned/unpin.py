from imports import *;



@dp.message_handler(commands=['разпин', 'unpin'], commands_prefix='/!.')
async def unpin_cmd(message: types.Message, command: Command):
   try:
      member = await bot.get_chat_member(message.chat.id, message.from_user.id)
      if member.status not in {'administrator', 'creator'}:
         await message.reply(f'''Не получится открепить, т.к. ты не имеешь соответсвующие права.''')
         return
      elif not command.args:
         await bot.unpin_chat_message(message.chat.id, message.reply_to_message.message_id)
         await message.reply(f'''📌 Сообщение откреплено.''')
         return
      elif command.args.casefold() == 'все':
         await bot.unpin_all_chat_messages(message.chat.id)
         await message.reply(f'''📌 Все сообщения откреплены.''')
         return
      elif not message.reply_to_message:
         await message.reply(f'''Нужно в ответ на сообщение.''')
         return
   except aiogram.utils.exceptions.BadRequest:
      await message.reply(f'''Не получится открепить, т.к. я не имею соответствующие права.''')
      return