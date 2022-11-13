from imports import *;



bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

async def on_startup(_):
    await bot.send_message(-1001591876770, f'''Бот обновлен и запущен.''')

@dp.message_handler(lambda message: message.text.casefold() == 'рик' or message.text.casefold() == 'бот')
async def ping_cmd(message: types.Message):
    await message.reply('✅ На месте!', reply_markup=kb1)