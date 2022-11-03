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
/mute (цифра) (м/ч/д) (причина) - мут
/ban (цифра) (м/ч/д) (причина) - бан
/unmute - размут
/unban - разбан
/admins - список админов
/ping - пинг''')

@dp.message_handler(lambda message: message.text.casefold() == 'помощь' or message.text.casefold() == 'help')
async def help_cmd(message: types.Message):
   await message.reply(f'''/start - приветствие
/help - помощь
/rp - список РП
/mute (цифра) (м/ч/д) (причина) - мут
/ban (цифра) (м/ч/д) (причина) - бан
/unmute - размут
/unban - разбан
/admins - список админов
/ping - пинг''')

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

@dp.message_handler(lambda message: message.text.casefold() == 'рп' or message.text.casefold() == 'rp')
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


    
@dp.message_handler(commands=['выебать'], commands_prefix='!.')
async def выебать(message: types.Message):
   if not message.reply_to_message:
      await message.reply('Ошибка! Нужно в ответ на сообщение.')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''👉👌😬 | {message.from_user.get_mention(as_html=True)} выебал(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['дать'], commands_prefix='!.')
async def дать(message: types.Message):
   if not message.reply_to_message:
      await message.reply('Ошибка! Нужно в ответ на сообщение.')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''🙏🏻 | {message.from_user.get_mention(as_html=True)} дал(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['испугать'], commands_prefix='!.')
async def испугать(message: types.Message):
   if not message.reply_to_message:
      await message.reply('Ошибка! Нужно в ответ на сообщение.')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''😱 | {message.from_user.get_mention(as_html=True)} испугал(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['кастрировать'], commands_prefix='!.')
async def кастрировать(message: types.Message):
   if not message.reply_to_message:
      await message.reply('Ошибка! Нужно в ответ на сообщение.')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''✂️ | {message.from_user.get_mention(as_html=True)} кастрировал(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['лизнуть'], commands_prefix='!.')
async def лизнуть(message: types.Message):
   if not message.reply_to_message:
      await message.reply('Ошибка! Нужно в ответ на сообщение.')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''👅 | {message.from_user.get_mention(as_html=True)} лизнул(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['обнять'], commands_prefix='!.')
async def обнять(message: types.Message):
   if not message.reply_to_message:
      await message.reply('Ошибка! Нужно в ответ на сообщение.')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''🤗 | {message.from_user.get_mention(as_html=True)} обнял(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['отдаться'], commands_prefix='!.')
async def отдаться(message: types.Message):
   if not message.reply_to_message:
      await message.reply('Ошибка! Нужно в ответ на сообщение.')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''💝 | {message.from_user.get_mention(as_html=True)} отдался(-ась) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['отлизать'], commands_prefix='!.')
async def отлизать(message: types.Message):
   if not message.reply_to_message:
      await message.reply('Ошибка! Нужно в ответ на сообщение.')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''👅 | {message.from_user.get_mention(as_html=True)} отлизал(-а) у <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['отравить'], commands_prefix='!.')
async def отравить(message: types.Message):
   if not message.reply_to_message:
      await message.reply('Ошибка! Нужно в ответ на сообщение.')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''💊 | {message.from_user.get_mention(as_html=True)} отравил(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['отсосать'], commands_prefix='!.')
async def отсосать(message: types.Message):
   if not message.reply_to_message:
      await message.reply('Ошибка! Нужно в ответ на сообщение.')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''🥳 | {message.from_user.get_mention(as_html=True)} отсосал(-а) у <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['покормить'], commands_prefix='!.')
async def покормить(message: types.Message):
   if not message.reply_to_message:
      await message.reply('Ошибка! Нужно в ответ на сообщение.')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''🍕 | {message.from_user.get_mention(as_html=True)} покормил(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['послать'], commands_prefix='!.')
async def послать(message: types.Message):
   if not message.reply_to_message:
      await message.reply('Ошибка! Нужно в ответ на сообщение.')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''🖕 | {message.from_user.get_mention(as_html=True)} послал(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['поцеловать'], commands_prefix='!.')
async def поцеловать(message: types.Message):
   if not message.reply_to_message:
      await message.reply('Ошибка! Нужно в ответ на сообщение.')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''😘 | {message.from_user.get_mention(as_html=True)} поцеловал(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['прижать'], commands_prefix='!.')
async def прижать(message: types.Message):
   if not message.reply_to_message:
      await message.reply('Ошибка! Нужно в ответ на сообщение.')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''🤲 | {message.from_user.get_mention(as_html=True)} прижал(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['сжечь'], commands_prefix='!.')
async def сжечь(message: types.Message):
   if not message.reply_to_message:
      await message.reply('Ошибка! Нужно в ответ на сообщение.')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''🔥 | {message.from_user.get_mention(as_html=True)} сжёг(-ожгла) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['трахнуть'], commands_prefix='!.')
async def трахнуть(message: types.Message):
   if not message.reply_to_message:
      await message.reply('Ошибка! Нужно в ответ на сообщение.')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''👉👌 | {message.from_user.get_mention(as_html=True)} трахнул(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['убить'], commands_prefix='!.')
async def убить(message: types.Message):
   if not message.reply_to_message:
      await message.reply('Ошибка! Нужно в ответ на сообщение.')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''🤡🔪 | {message.from_user.get_mention(as_html=True)} убил(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')

@dp.message_handler(commands=['me'], commands_prefix='!.')
async def me_cmd(message: types.Message, command: Command):
   if not command.args:
      await message.reply(f'''Пример ввода: <code>!me полил(-а) цветы</code>''')
      return
   if command.args:
      await message.delete()
      await bot.send_message(message.chat.id, f'''<b>{message.from_user.full_name}</b> {command.args}.''')

@dp.message_handler(commands=['do'], commands_prefix='!.')
async def do_cmd(message: types.Message, command: Command):
   if not command.args:
      await message.reply(f'''Пример ввода: <code>!do Цветы политы</code>''')
      return
   await message.delete()
   await bot.send_message(message.chat.id, f'''{command.args}. (<b>{message.from_user.full_name}</b>)''')
   
   

@dp.message_handler(commands=['мут', 'mute'], commands_prefix='/!.', is_chat_admin=True)
async def mute_cmd(message: types.Message):
   if not message.reply_to_message:
      await message.reply(f'''Ошибка!
Нужно в ответ на сообщение.''')
      return
   try:
      mute_time = int(message.text.split()[1])
      mute_type = message.text.split()[2]
      mute_reason = ' '.join(message.text.split()[3:])
   except IndexError:
      await message.reply(f'''Ошибка!
Пример ввода: <code>/mute 10 минут</code>''')
      return
   try:
      if mute_type == 'м' or mute_type == 'мин' or mute_type == 'минута' or mute_type == 'минуту' or mute_type == 'минуты' or mute_type == 'минут':
         dnt = datetime.now() + timedelta(minutes=mute_time)
         dntt = dnt.timestamp()
         await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = dntt)
         await bot.send_message(message.chat.id, f'''🔇 <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a>, мут на {mute_time} {mute_type} по причине "{mute_reason}".''')
      elif mute_type == 'ч' or mute_type == 'час' or mute_type == 'часа' or mute_type == 'часов':
         dnt = datetime.now() + timedelta(hours=mute_time)
         dntt = dnt.timestamp()
         await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = dntt)
         await bot.send_message(message.chat.id, f'''🔇 <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a>, мут на {mute_time} {mute_type} по причине "{mute_reason}".''')
      elif mute_type == 'д' or mute_type == 'день' or mute_type == 'дня' or mute_type == 'дней':
         dnt = datetime.now() + timedelta(days=mute_time)
         dntt = dnt.timestamp()
         await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = dntt)
         await bot.send_message(message.chat.id, f'''🔇 <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a>, мут на {mute_time} {mute_type} по причине "{mute_reason}".''')
   except aiogram.utils.exceptions.UserIsAnAdministratorOfTheChat:
      await message.reply(f'''Ошибка!
Нельзя дать мут администратору.''')

@dp.message_handler(commands=['бан', 'ban'], commands_prefix='/!.', is_chat_admin=True)
async def ban_cmd(message: types.Message):
   if not message.reply_to_message:
      await message.reply(f'''Ошибка!
Нужно в ответ на сообщение.''')
      return
   try:
      ban_time = int(message.text.split()[1])
      ban_type = message.text.split()[2]
      ban_reason = ' '.join(message.text.split()[3:])
   except IndexError:
      await message.reply(f'''Ошибка!
Пример ввода: <code>/ban 10 минут</code>''')
      return
   try:
      if ban_type == 'м' or ban_type == 'мин' or ban_type == 'минута' or ban_type == 'минуту' or ban_type == 'минуты' or ban_type == 'минут':
         dnt = datetime.now() + timedelta(minutes=ban_time)
         dntt = dnt.timestamp()
         await bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date = dntt)
         await bot.send_message(message.chat.id, f'''🔴 <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a>, бан на {ban_time} {ban_type} по причине "{ban_reason}".''')
      elif ban_type == 'ч' or ban_type == 'час' or ban_type == 'часа' or ban_type == 'часов':
         dnt = datetime.now() + timedelta(hours=ban_time)
         dntt = dnt.timestamp()
         await bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date = dntt)
         await bot.send_message(message.chat.id, f'''🔴 <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a>, бан на {ban_time} {ban_type} по причине "{ban_reason}".''')
      elif ban_type == 'д' or ban_type == 'день' or ban_type == 'дня' or ban_type == 'дней':
         dnt = datetime.now() + timedelta(days=ban_time)
         dntt = dnt.timestamp()
         await bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id, until_date = dntt)
         await bot.send_message(message.chat.id, f'''🔴 <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a>, бан на {ban_time} {ban_type} по причине "{ban_reason}".''')
   except aiogram.utils.exceptions.UserIsAnAdministratorOfTheChat:
      await message.reply(f'''Ошибка!
Нельзя дать бан администратору.''')

@dp.message_handler(commands=['размут', 'unmute'], commands_prefix='/!.')
async def unmute_cmd(message: types.Message):
    try:
        member = await bot.get_chat_member(message.chat.id, message.from_id)
        if member.status not in {"administrator", "creator"}:
            await message.reply(f'''Ты не можешь дать размут, так как не имеешь прав администратора.''')
            return
        if not message.reply_to_message:
            await message.reply(f'''Нужно в ответ на сообщение.''')
            return
        await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True, can_add_web_page_previews=True)
        await bot.send_message(message.chat.id, f'''✅ <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> больше не в муте.''')
    except aiogram.utils.exceptions.ChatAdminRequired:
        await message.reply(f'''Ты не можешь дать размут администратору.''')
    except aiogram.utils.exceptions.CantRestrictChatOwner:
        await message.reply(f'''Ты не можешь дать размут основателю.''')

@dp.message_handler(commands=['разбан', 'unban'], commands_prefix='/!.')
async def unban_cmd(message: types.Message):
    try:
        member = await bot.get_chat_member(message.chat.id, message.from_id)
        if member.status not in {"administrator", "creator"}:
            await message.reply(f'''Ты не можешь дать разбан, так как не имеешь прав администратора.''')
            return
        if not message.reply_to_message:
            await message.reply(f'''Нужно в ответ на сообщение.''')
            return
        await bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        await bot.send_message(message.chat.id, f'''✅ <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> больше не в бане.''')
    except aiogram.utils.exceptions.UserIsAnAdministratorOfTheChat:
        await message.reply(f'''Ты не можешь дать разбан администратору.''')
    except aiogram.utils.exceptions.CantRestrictChatOwner:
        await message.reply(f'''Ты не можешь дать разбан основателю.''')

@dp.message_handler(commands=['админы', 'кто админ', 'admins'], commands_prefix='/!.')
async def admins_cmd(message: types.Message):
   try:
      chat_admins = await bot.get_chat_administrators(message.chat.id)
      lst = [f'''"id": "{admin.user.id}",
"first_name": "{admin.user.first_name}",
"last_name": "{admin.user.last_name}",
"username": "{admin.user.username}"''' for admin in chat_admins]
      await message.reply('\n\n'.join(lst))
   except aiogram.utils.exceptions.BadRequest:
      await message.reply(f'''Ошибка!
Нужно использовать в чате.''')

@dp.message_handler(lambda message: message.text.casefold() == 'админы' or message.text.casefold() == 'кто админ' or message.text.casefold() == 'admins')
async def admins_cmd(message: types.Message):
   try:
      chat_admins = await bot.get_chat_administrators(message.chat.id)
      lst = [f'''"id": "{admin.user.id}",
"first_name": "{admin.user.first_name}",
"last_name": "{admin.user.last_name}",
"username": "{admin.user.username}"''' for admin in chat_admins]
      await message.reply('\n\n'.join(lst))
   except aiogram.utils.exceptions.BadRequest:
      await message.reply(f'''Ошибка!
Нужно использовать в чате.''')



@dp.message_handler(content_types=['new_chat_members'])
async def ncm(message: types.Message):
   await message.delete()
   await bot.send_message(message.chat.id, f'''{message.new_chat_members[0].full_name} вступил(-а) в чат.''')

@dp.message_handler(content_types=['left_chat_member'])
async def lcm(message: types.Message):
   await message.delete()
   await bot.send_message(message.chat.id, f'''{message.left_chat_member.full_name} покинул(-а) чат.''')



@dp.message_handler(commands=['рик', 'rick', 'бот', 'bot'], commands_prefix='/!.')
async def ping_cmd(message: types.Message):
   await message.reply('✅ На месте!')

@dp.message_handler(lambda message: message.text.casefold() == 'рик' or message.text.casefold() == 'rick' or message.text.casefold() == 'бот' or message.text.casefold() == 'bot')
async def ping_cmd(message: types.Message):
   await message.reply('✅ На месте!')

@dp.message_handler(commands=['пинг', 'ping'], commands_prefix='/!.')
async def ping_cmd(message: types.Message):
   await message.reply('ПОНГ')

@dp.message_handler(lambda message: message.text.casefold() == 'пинг' or message.text.casefold() == 'ping')
async def ping_cmd(message: types.Message):
   await message.reply('ПОНГ')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
