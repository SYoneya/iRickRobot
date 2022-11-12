from aiogram import types; from aiogram.dispatcher.filters import Command; from main import bot, dp;



@dp.message_handler(commands=['повысить', 'promote'], commands_prefix='/!.')
async def promote_cmd(message: types.Message, command: Command):
   member = await bot.get_chat_member(message.chat.id, message.from_user.id)
   if member.status not in {'administrator', 'creator'}:
      await message.reply(f'''Ты не можешь повысить, так как не имеешь прав администратора.''')
      return
   elif not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   elif command.args.lower() == '+все':
      await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_manage_chat=True, can_change_info=True, can_delete_messages=True, can_restrict_members=True, can_invite_users=True, can_pin_messages=True, can_manage_video_chats=True, can_promote_members=True)
      await message.reply(f'''+ все права''')
      return
   elif command.args.lower() == '+управление чатом':
      await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_manage_chat=True)