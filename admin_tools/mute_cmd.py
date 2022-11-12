from aiogram import types; from datetime import datetime, timedelta; from main import bot, dp;



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