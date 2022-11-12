from aiogram import types; from aiogram.dispatcher.filters import Command; from main import bot, dp;



@dp.message_handler(commands=['разпин', 'unpin'], commands_prefix='/!.')
async def unpin_cmd(message: types.Message, command: Command):
   member = await bot.get_chat_member(message.chat.id, message.from_user.id)
   if member.status not in {'administrator', 'creator'}:
      await message.reply(f'''Ты не можешь открепить, так как не имеешь прав администратора.''')
      return
   elif command.args.lower() == 'все':
      await bot.unpin_all_chat_messages(message.chat.id)
      await message.reply(f'''📌 Все сообщения откреплены.''')
      return
   elif not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   await bot.unpin_chat_message(message.chat.id, message.reply_to_message.message_id)
   await message.reply(f'''📌 Сообщение откреплено.''')