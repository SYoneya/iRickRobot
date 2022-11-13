from imports import *;



@dp.message_handler(commands=['start'], commands_prefix='/')
async def start_cmd(message: types.Message):
    await message.reply('Привет!', reply_markup=kb1)



if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=False, on_startup=on_startup)