import sys; from aiogram import Bot, Dispatcher; from config import *;

bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

sys.path.insert(0, 'C:\Users\yoney\Documents\Projects\Python\iRickRobot\admin_tools')

async def on_startup(_):
    await bot.send_message(-1001591876770, f'''Бот обновлен и запущен!''')