"""import aiogram; from aiogram import types; from datetime import datetime, timedelta; from main import bot, dp;



@dp.message_handler(commands=['бан', 'ban'], commands_prefix='/!.')
async def ban_cmd(message: types.Message):
    try:
        member = await bot.get_chat_member(message.chat.id, message.from_user.id)
        if member.status not in {'administrator', 'creator'}:
            await message.reply(f'''Не получится дать бан, т.к. ты не имеешь соответствующие права.''')
            return
        elif not message.reply_to_message:
            await message.reply(f'''Нужно в ответ на сообщение.''')
            return
        admin = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        if admin.status in {'administrator', 'creator'}:
            await message.reply(f'''Не получится дать бан администратору.''')
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
    try:
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
    except aiogram.utils.exceptions.BadRequest:
        await message.reply(f'''Не получится дать бан, т.к. я не имею соответствующие права.''')
        return"""