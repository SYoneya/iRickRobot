import aiogram, logging; from aiogram import Bot, Dispatcher, types, executor; from aiogram.dispatcher.filters import Command; from datetime import datetime, timedelta;
from config import TOKEN;

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

async def on_startup(_):
    print('Bot was started!')
    await bot.send_message(-1001591876770, f'''Бот обновлён и запущен.''')



@dp.message_handler(commands=['start'], commands_prefix='/!.')
async def start_cmd(message: types.Message):
    await message.reply(f'''Привет!
Я Рик - чат-менеджер.
Помощь: /help''')

@dp.message_handler(commands=['помощь', 'help'], commands_prefix='/!.')
async def help_cmd(message: types.Message):
   await message.reply(f'''/start - приветствие
/help - помощь
/rp - список РП
/mute (цифра) (минут/часов/дней) (причина) - мут
/ban (цифра) (минут/часов/дней) (причина) - бан
/unmute - размут
/unban - разбан
/pin - закрепить
/unpin - открепить (/unpin все - открепить все)
/admins - список админов''')

@dp.message_handler(commands=['рп', 'rp'], commands_prefix='/!.')
async def rp_cmd(message: types.Message):
    await message.reply(f'''1. !выебать (реплика)
2. !дать (реплика)
3. !испугать (реплика)
4. !кастрировать (реплика)
5. !лизнуть (реплика)
6. !обнять (реплика)
7. !отдаться (реплика)
8. !отлизать (реплика)
9. !отравить (реплика)
10. !отсосать (реплика)
11. !покормить (реплика)
12. !послать (реплика)
13. !поцеловать (реплика)
14. !прижать (реплика)
15. !сжечь (реплика)
16. !трахнуть (реплика)
17. !убить (реплика)
18. !do (реплика)
19. !me (реплика)''')


 
@dp.message_handler(commands=['выебать'], commands_prefix='/!.')
async def выебать(message: types.Message):
   if not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''👉👌😬 | {message.from_user.get_mention(as_html=True)} выебал(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['дать'], commands_prefix='/!.')
async def дать(message: types.Message):
   if not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''🙏🏻 | {message.from_user.get_mention(as_html=True)} дал(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['испугать'], commands_prefix='/!.')
async def испугать(message: types.Message):
   if not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''😱 | {message.from_user.get_mention(as_html=True)} испугал(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['кастрировать'], commands_prefix='/!.')
async def кастрировать(message: types.Message):
   if not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''✂️ | {message.from_user.get_mention(as_html=True)} кастрировал(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['лизнуть'], commands_prefix='/!.')
async def лизнуть(message: types.Message):
   if not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''👅 | {message.from_user.get_mention(as_html=True)} лизнул(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['обнять'], commands_prefix='/!.')
async def обнять(message: types.Message):
   if not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''🤗 | {message.from_user.get_mention(as_html=True)} обнял(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['отдаться'], commands_prefix='/!.')
async def отдаться(message: types.Message):
   if not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''💝 | {message.from_user.get_mention(as_html=True)} отдался(-ась) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['отлизать'], commands_prefix='/!.')
async def отлизать(message: types.Message):
   if not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''👅 | {message.from_user.get_mention(as_html=True)} отлизал(-а) у <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['отравить'], commands_prefix='/!.')
async def отравить(message: types.Message):
   if not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''💊 | {message.from_user.get_mention(as_html=True)} отравил(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['отсосать'], commands_prefix='/!.')
async def отсосать(message: types.Message):
   if not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''🥳 | {message.from_user.get_mention(as_html=True)} отсосал(-а) у <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['покормить'], commands_prefix='/!.')
async def покормить(message: types.Message):
   if not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''🍕 | {message.from_user.get_mention(as_html=True)} покормил(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['послать'], commands_prefix='/!.')
async def послать(message: types.Message):
   if not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''🖕 | {message.from_user.get_mention(as_html=True)} послал(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['поцеловать'], commands_prefix='/!.')
async def поцеловать(message: types.Message):
   if not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''😘 | {message.from_user.get_mention(as_html=True)} поцеловал(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['прижать'], commands_prefix='/!.')
async def прижать(message: types.Message):
   if not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''🤲 | {message.from_user.get_mention(as_html=True)} прижал(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['сжечь'], commands_prefix='/!.')
async def сжечь(message: types.Message):
   if not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''🔥 | {message.from_user.get_mention(as_html=True)} сжёг(-ожгла) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['трахнуть'], commands_prefix='/!.')
async def трахнуть(message: types.Message):
   if not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''👉👌 | {message.from_user.get_mention(as_html=True)} трахнул(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['убить'], commands_prefix='/!.')
async def убить(message: types.Message):
   if not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''🤡🔪 | {message.from_user.get_mention(as_html=True)} убил(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['do'], commands_prefix='/!.')
async def do_cmd(message: types.Message, command: Command):
   if not command.args:
      await message.reply(f'''Пример ввода: <code>!do Цветы политы</code>''')
      return
   await bot.send_message(message.chat.id, f'''{command.args}. (<b>{message.from_user.full_name}</b>)''')
   await message.delete()

@dp.message_handler(commands=['me'], commands_prefix='/!.')
async def me_cmd(message: types.Message, command: Command):
   if not command.args:
      await message.reply(f'''Пример ввода: <code>!me полил(-а) цветы</code>''')
      return
   if command.args:
      await bot.send_message(message.chat.id, f'''<b>{message.from_user.full_name}</b> {command.args}.''')
      await message.delete()


   
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
        await bot.send_message(message.chat.id, f'''🔇 <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a>, мут на {mute_time} {mute_type} по причине "{mute_reason}".''')
    elif mute_type == 'час' or mute_type == 'часа' or mute_type == 'часов':
        dnt = datetime.now() + timedelta(hours=mute_time)
        dntt = dnt.timestamp()
        await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = dntt)
        await bot.send_message(message.chat.id, f'''🔇 <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a>, мут на {mute_time} {mute_type} по причине "{mute_reason}".''')
    elif mute_type == 'день' or mute_type == 'дня' or mute_type == 'дней':
        dnt = datetime.now() + timedelta(days=mute_time)
        dntt = dnt.timestamp()
        await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = dntt)
        await bot.send_message(message.chat.id, f'''🔇 <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a>, мут на {mute_time} {mute_type} по причине "{mute_reason}".''')

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
        await bot.send_message(message.chat.id, f'''🔴 <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a>, бан на {ban_time} {ban_type} по причине "{ban_reason}".''')
    elif ban_type == 'час' or ban_type == 'часа' or ban_type == 'часов':
        dnt = datetime.now() + timedelta(hours=ban_time)
        dntt = dnt.timestamp()
        await bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date = dntt)
        await bot.send_message(message.chat.id, f'''🔴 <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a>, бан на {ban_time} {ban_type} по причине "{ban_reason}".''')
    elif ban_type == 'день' or ban_type == 'дня' or ban_type == 'дней':
        dnt = datetime.now() + timedelta(days=ban_time)
        dntt = dnt.timestamp()
        await bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date = dntt)
        await bot.send_message(message.chat.id, f'''🔴 <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a>, бан на {ban_time} {ban_type} по причине "{ban_reason}".''')

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
    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True, can_add_web_page_previews=True)
    await bot.send_message(message.chat.id, f'''🔊 <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> больше не в муте.''')

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
    await bot.send_message(message.chat.id, f'''✅ <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> больше не в бане.''')

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
    if member.status in {'member'}:
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
    if member.status in {'member'}:
        await message.reply(f'''Ты не можешь открепить, так как не имеешь прав администратора.''')
        return
    elif command.args == 'ВСЕ' or command.args == 'ВСе' or command.args == 'Все' or command.args == 'все' or command.args == 'всЕ' or command.args == 'вСЕ' or command.args == 'вСе':
        await bot.unpin_all_chat_messages(message.chat.id)
        await message.reply(f'''📌 Все сообщения откреплены.''')
        return
    elif not message.reply_to_message:
        await message.reply(f'''Нужно в ответ на сообщение.''')
        return
    await bot.unpin_chat_message(message.chat.id, message.reply_to_message.message_id)
    await message.reply(f'''📌 Сообщение откреплено.''')



@dp.message_handler(content_types=['new_chat_members'])
async def new_chat_members(message: types.Message):
    await bot.send_message(message.chat.id, f'''{message.new_chat_members[0].full_name} вступил(-а) в чат.''')
    await message.delete()

@dp.message_handler(content_types=['left_chat_member'])
async def left_chat_member(message: types.Message):
    await bot.send_message(message.chat.id, f'''{message.left_chat_member.full_name} покинул(-а) чат.''')
    await message.delete()
    
@dp.message_handler(content_types=['new_chat_title', 'new_chat_photo', 'delete_chat_photo', 'message_auto_delete_timer_changed', 'pinned_message', 'video_chat_scheduled', 'video_chat_started', 'video_chat_ended'])
async def other_types(message: types.Message):
    await message.delete()



@dp.message_handler(lambda message: message.text.casefold() == 'рик' or message.text.casefold() == 'rick' or message.text.casefold() == 'бот' or message.text.casefold() == 'bot')
async def ping_cmd(message: types.Message):
   await message.reply('✅ На месте!')

@dp.message_handler(lambda message: message.text.casefold() == 'рикролл')
async def rickroll(message: types.Message):
   await bot.forward_message(message.chat.id, -1001882577870, 2)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
