from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import Message
from aiogram.utils.markdown import link
from config import *
from database import *

bot = Bot(token=token)
dp = Dispatcher(bot)

# logging.basicConfig(level=logging.DEBUG)

button_start = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="бебрик")],
    ], resize_keyboard=True)


@dp.message_handler(commands=["start"])
async def inline_echo(message: Message):
    user_id = message.from_user.id
    user_id = str(user_id)
    user_list = []
    s = select([user_tg_table])
    r = conn.execute(s)

    for row in r:
        for id in row:
            user_list.append(id)
    chek_user = False
    for name in user_list:
        if name == user_id:
            chek_user = True
            break
        else:
            chek_user = False
    
    if chek_user == True:
        await message.answer("ты уже тут был")
    else:
        await message.answer("ты первый раз")
        ins = user_tg_table.insert().values(
                id = user_id
        )
        r = conn.execute(ins)

        s = select([user_tg_table])
        r = conn.execute(s)
        for row in r:
            for id in row:
                user_list.append(id)
        

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)