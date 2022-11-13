from imports import *;



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