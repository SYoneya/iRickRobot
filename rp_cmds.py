from aiogram import types; from aiogram.dispatcher.filters import Command; from main import bot, dp;



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