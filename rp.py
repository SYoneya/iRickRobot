from aiogram import types; from main import bot, dp;



@dp.message_handler(commands=['выебать'], commands_prefix='/!.')
async def выебать(message: types.Message):
   if not message.reply_to_message:
      await message.reply(f'''Нужно в ответ на сообщение.''')
      return
   args = ' '.join(message.text.split()[1:])
   await bot.send_message(message.chat.id, f'''👉👌😬 | {message.from_user.get_mention(as_html=True)} выебал(-а) <a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.full_name}</a> {args}''')