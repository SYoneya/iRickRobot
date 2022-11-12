from aiogram import Bot, Dispatcher; from config import TOKEN;

bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

async def on_startup(_):
    await bot.send_message(-1001591876770, f'''Сервер: перезапущен. Бот: запущен. К использованию: готов...''')