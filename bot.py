import logging, random; from aiogram import types, executor; from main import bot, dp, on_startup; from rp_cmds import *; from adm_cmds import *;

logging.basicConfig(level=logging.INFO)



@dp.message_handler(commands=['start'], commands_prefix='/')
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



@dp.message_handler(content_types=['new_chat_members'])
async def new_chat_members(message: types.Message):
    await bot.send_message(message.chat.id, f'''{message.new_chat_members[0].full_name} вступил(-а) в чат.''')
    await message.delete()

@dp.message_handler(content_types=['pinned_message'])
async def pinned_message(message: types.Message):
   await message.delete()



@dp.message_handler(lambda message: message.text.casefold() == 'рикролл')
async def rickroll(message: types.Message):
   await bot.copy_message(message.chat.id, -1001882577870, 2, protect_content=True, reply_to_message_id=message.message_id)

@dp.message_handler(lambda message: message.text.casefold() == 'мем')
async def mem(message: types.Message):
   await bot.copy_message(message.chat.id, -1001882577870, random.randint(4, 39), protect_content=True, reply_to_message_id=message.message_id)



@dp.message_handler(lambda message: message.text.casefold() == 'рик' or message.text.casefold() == 'бот')
async def ping_cmd(message: types.Message):
   await message.reply('✅ На месте!')

@dp.message_handler(lambda message: message.text.casefold() == 'пинг')
async def ping_cmd(message: types.Message):
   await message.reply('ПОНГ')

@dp.message_handler(lambda message: message.text.casefold() == 'пиу')
async def ping_cmd(message: types.Message):
   await message.reply('ПАУ')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
