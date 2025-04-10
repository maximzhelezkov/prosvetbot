from boot import bot, dp, types
from kb.kb import menuikb
from db.dbcon import db
from data.txt import START_MESSAGE


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id, 
        text=START_MESSAGE, 
        reply_markup=menuikb)

    nonetype = "None"
    user_id = message.from_user.id
    username = (message.from_user.username or nonetype)
    db(user_id, username)
    

milky_id = 1984752299 

@dp.message_handler(commands=['source'])
async def source_command(message):
    await bot.send_message(
        chat_id=message.chat.id, 
        text=f"""Код доступен здесь https://github.com/maximzhelezkov/prosvetbot \nРазработка бота: <a href="kiddie113.t.me">Максим</a>
""")

