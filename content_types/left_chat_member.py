from imports import *;



@dp.message_handler(content_types=['left_chat_member'])
async def left_chat_member(message: types.Message):
    await message.delete()