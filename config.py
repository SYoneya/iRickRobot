TOKEN = '5449016317:AAHly8zYgBWSUVKY3vEQvpYvTOMsIlAmAdQ'

async def on_startup(_):
    print('Bot was started!')
    await bot.send_message(-1001591876770, f'''Бот обновлён и запущен.''')
