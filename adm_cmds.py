import aiogram; from aiogram import types; from aiogram.dispatcher.filters import Command; from datetime import datetime, timedelta; from main import bot, dp;



@dp.message_handler(commands=['мут', 'mute'], commands_prefix='/!.')
async def mute_cmd(message: types.Message):
    try:
        member = await bot.get_chat_member(message.chat.id, message.from_id)
        if member.status not in {'administrator', 'creator'}:
            await message.reply(f'''Ты не можешь дать мут, так как не имеешь прав администратора.''')
            return
        elif not message.reply_to_message:
            await message.reply(f'''Нужно в ответ на сообщение.''')
            return
        admin = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        if admin.status in {'administrator', 'creator'}:
            await message.reply(f'''Ты не можешь дать мут администратору.''')
            return
        mute_time = int(message.text.split()[1])
        mute_type = message.text.split()[2]
        mute_reason = ' '.join(message.text.split()[3:])
    except IndexError:
        await message.reply(f'''Пример ввода: <code>/mute 10 минут флуд</code>''')
        return
    except ValueError:
        await message.reply(f'''Пример ввода: <code>/mute 10 минут флуд</code>''')
        return
    if mute_type == mute_type == 'минута' or mute_type == 'минуту' or mute_type == 'минуты' or mute_type == 'минут':
        dnt = datetime.now() + timedelta(minutes=mute_time)
        dntt = dnt.timestamp()
        await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = dntt)
        await bot.send_message(message.chat.id, f'''🔇 <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> получил(-а) мут на {mute_time} {mute_type} по причине "{mute_reason}".''', reply_to_message_id=message.message_id)
    elif mute_type == 'час' or mute_type == 'часа' or mute_type == 'часов':
        dnt = datetime.now() + timedelta(hours=mute_time)
        dntt = dnt.timestamp()
        await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = dntt)
        await bot.send_message(message.chat.id, f'''🔇 <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> получил(-а) мут на {mute_time} {mute_type} по причине "{mute_reason}".''', reply_to_message_id=message.message_id)
    elif mute_type == 'день' or mute_type == 'дня' or mute_type == 'дней':
        dnt = datetime.now() + timedelta(days=mute_time)
        dntt = dnt.timestamp()
        await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = dntt)
        await bot.send_message(message.chat.id, f'''🔇 <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> получил(-а) мут на {mute_time} {mute_type} по причине "{mute_reason}".''', reply_to_message_id=message.message_id)

@dp.message_handler(commands=['бан', 'ban'], commands_prefix='/!.')
async def ban_cmd(message: types.Message):
    try:
        member = await bot.get_chat_member(message.chat.id, message.from_id)
        if member.status not in {'administrator', 'creator'}:
            await message.reply(f'''Ты не можешь дать бан, так как не имеешь прав администратора.''')
            return
        elif not message.reply_to_message:
            await message.reply(f'''Нужно в ответ на сообщение.''')
            return
        admin = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        if admin.status in {'administrator', 'creator'}:
            await message.reply(f'''Ты не можешь дать бан администратору.''')
            return
        ban_time = int(message.text.split()[1])
        ban_type = message.text.split()[2]
        ban_reason = ' '.join(message.text.split()[3:])
    except IndexError:
        await message.reply(f'''Пример ввода: <code>/ban 4 часа спам</code>''')
        return
    except ValueError:
        await message.reply(f'''Пример ввода: <code>/ban 4 часа спам</code>''')
        return
    if ban_type == 'минута' or ban_type == 'минуту' or ban_type == 'минуты' or ban_type == 'минут':
        dnt = datetime.now() + timedelta(minutes=ban_time)
        dntt = dnt.timestamp()
        await bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date = dntt)
        await bot.send_message(message.chat.id, f'''🔴 <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> получил(-а) бан на {ban_time} {ban_type} по причине "{ban_reason}".''', reply_to_message_id=message.message_id)
    elif ban_type == 'час' or ban_type == 'часа' or ban_type == 'часов':
        dnt = datetime.now() + timedelta(hours=ban_time)
        dntt = dnt.timestamp()
        await bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date = dntt)
        await bot.send_message(message.chat.id, f'''🔴 <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> получил(-а) бан на {ban_time} {ban_type} по причине "{ban_reason}".''', reply_to_message_id=message.message_id)
    elif ban_type == 'день' or ban_type == 'дня' or ban_type == 'дней':
        dnt = datetime.now() + timedelta(days=ban_time)
        dntt = dnt.timestamp()
        await bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date = dntt)
        await bot.send_message(message.chat.id, f'''🔴 <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a>получил(-а) бан на {ban_time} {ban_type} по причине "{ban_reason}".''', reply_to_message_id=message.message_id)



@dp.message_handler(commands=['размут', 'unmute'], commands_prefix='/!.')
async def unmute_cmd(message: types.Message):
   member = await bot.get_chat_member(message.chat.id, message.from_user.id)
   if member.status not in {'administrator', 'creator'}:
      await message.reply(f'''Ты не можешь дать размут, так как не имеешь прав администратора.''')
      return
   elif not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   admin = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
   if admin.status in {'administrator', 'creator'}:
      await message.reply(f'''Ты не можешь дать размут администратору.''')
      return
   await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages=True, can_send_other_messages=True)
   await bot.send_message(message.chat.id, f'''🔊 <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> больше не в муте.''', reply_to_message_id=message.message_id)

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



@dp.message_handler(commands=['админы', 'кто админ', 'admins'], commands_prefix='/!.')
async def admins_cmd(message: types.Message):
   try:
      chat_admins = await bot.get_chat_administrators(message.chat.id)
      lst = [f'''"id": "{admin.user.id}",
"full_name": "{admin.user.full_name}",
"username": "{admin.user.username}"''' for admin in chat_admins]
      await message.reply('\n\n'.join(lst))
   except aiogram.utils.exceptions.BadRequest:
      await message.reply(f'''Нужно использовать в чате.''')
        


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



@dp.message_handler(commands=['повысить', 'promote'], commands_prefix='/!.')
async def promote_cmd(message: types.Message, command: Command):
   member = await bot.get_chat_member(message.chat.id, message.from_user.id)
   if member.status not in {'administrator', 'creator'}:
      await message.reply(f'''Ты не можешь повысить, так как не имеешь прав администратора.''')
      return
   elif not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   elif command.args.lower() == 'все':
      await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_manage_chat=True)
      return
   elif command.args.lower() == '+управление чатом':
      await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_manage_chat=True)
   
@dp.message_handler(commands=['понизить', 'demote'], commands_prefix='/!.')
async def demote_cmd(message: types.Message, command: Command):
   member = await bot.get_chat_member(message.chat.id, message.from_user.id)
   if member.status not in {'administrator', 'creator'}:
      await message.reply(f'''Ты не можешь понизить, так как не имеешь прав администратора.''')
      return
   elif not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   elif command.args.lower() == 'все':
      await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_manage_chat=False)
      return
   elif command.args.lower() == '-управление чатом':
      await bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_manage_chat=False)