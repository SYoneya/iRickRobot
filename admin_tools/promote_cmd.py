import aiogram; from aiogram import types; from aiogram.dispatcher.filters import Command; from main import bot, dp;



@dp.message_handler(commands=['повысить', 'promote'], commands_prefix='/!.')
async def promote_cmd(message: types.Message, command: Command):
   try:
      member = await bot.get_chat_member(message.chat.id, message.from_user.id)
      if member.status not in {'administrator', 'creator'}:
         await message.reply(f'''Не получится дать повышение, т.к. ты не имеешь соответствующие права.''')
         return
      elif not message.reply_to_message:
         await message.reply(f'''Нужно в ответ на сообщение.''')
         return
      admin = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
      if admin.status in {'administrator', 'creator'}:
         await message.reply(f'''Не получится дать повышение администратору.''')
         return
      elif command.args == '0':
         await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, is_anonymous=True)
         await message.reply(f'''✅ анонимность''')
         return
      elif command.args == '1':
         await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_manage_chat=True)
         await message.reply(f'''✅ управление чатом''')
         return
      elif command.args == '2':
         await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_change_info=True)
         await message.reply(f'''✅ изменение профиля группы''')
         return
      elif command.args == '3':
         await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_delete_messages=True)
         await message.reply(f'''✅ удаление сообщений''')
         return
      elif command.args == '4':
         await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_restrict_members=True)
         await message.reply(f'''✅ блокировка пользователей''')
         return
      elif command.args == '5':
         await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_invite_users=True)
         await message.reply(f'''✅ добавление участников''')
         return
      elif command.args == '6':
         await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_pin_messages=True)
         await message.reply(f'''✅ закрепление сообщений''')
         return
      elif command.args == '7':
         await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_manage_video_chats=True)
         await message.reply(f'''✅ управление видеочатами''')
         return
      elif command.args == '8':
         await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_promote_members=True)
         await message.reply(f'''✅ выбор администраторов''')
         return
      elif command.args == '9':
         await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_change_info=True, can_delete_messages=True, can_restrict_members=True, can_invite_users=True, can_pin_messages=True, can_manage_video_chats=True, can_promote_members=True)
         await message.reply(f'''✅ измение профиля группы
✅ удаление сообщений
✅ блокировка пользователей
✅ добавление участников
✅ закрепление сообщений
✅ управление видеочатами
✅ выбор администраторов
❌ анонимность''')
         return
      elif command.args == '10':
         await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_change_info=True, can_delete_messages=True, can_restrict_members=True, can_invite_users=True, can_pin_messages=True, can_manage_video_chats=True, can_promote_members=True, is_anonymous=True)
         await message.reply(f'''✅ измение профиля группы
✅ удаление сообщений
✅ блокировка пользователей
✅ добавление участников
✅ закрепление сообщений
✅ управление видеочатами
✅ выбор администраторов
✅ анонимность''')
         return
   except aiogram.utils.exceptions.BadRequest:
      await message.reply(f'''Не получится дать повышение, т.к. я не имею соответствующие права.''')