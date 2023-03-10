from imports import *;



@dp.message_handler(lambda message: message.text.casefold() == 'рик' or message.text.casefold() == 'бот')
async def ping_cmd(message: types.Message):
    await message.reply('✅ На месте!')
    
@dp.message_handler(commands=['start'], commands_prefix='/')
async def start_cmd(message: types.Message):
    await message.reply('Привет!')



if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=False, on_startup=on_startup)