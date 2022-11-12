from aiogram import types; from aiogram.dispatcher.filters import Command; from main import bot, dp;



@dp.message_handler(commands=['понизить', 'demote'], commands_prefix='/!.')
async def demote_cmd(message: types.Message, command: Command):
   member = await bot.get_chat_member(message.chat.id, message.from_user.id)
   if member.status not in {'administrator', 'creator'}:
      await message.reply(f'''Ты не можешь понизить, так как не имеешь прав администратора.''')
      return
   elif not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   elif command.args.lower() == '-все':
      await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_manage_chat=False)
      await message.reply(f'''-все права''')
      return
   elif command.args.lower() == '-управление чатом':
      await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_manage_chat=False)