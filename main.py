from imports import *;



bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

async def on_startup(_):
    await bot.send_message(-1001343770601, f'''Żyję!''')