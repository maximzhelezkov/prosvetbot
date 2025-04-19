from boot import bot, dp, types
from kb.kb import menuikb, adminikb, startikb
from db.dbcon import db
from data.txt import START_MESSAGE, START_MESSAGE2
import data.config
from data.txt import ADMIN_PANEL_MESSAGE

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    if len(message.get_args()) > 0 and message.get_args() == "new":
        await bot.send_message(
            chat_id=message.chat.id, 
            text="", 
            reply_markup=startikb)
    else:
        await bot.send_message(
        chat_id=message.chat.id, 
        text=START_MESSAGE2) 
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
async def source_command(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id, 
        text=f"""Код доступен здесь https://github.com/maximzhelezkov/prosvetbot \nРазработка бота: <a href="kiddie113.t.me">Максим</a>
""")
    
@dp.message_handler(commands=['admin'])
async def admin_command(message: types.Message):
    user_id = message.from_user.id
    if user_id in data.config.admin_id:
        await bot.send_message(chat_id=message.chat.id, 
                               text=ADMIN_PANEL_MESSAGE, 
                               reply_markup=adminikb)        
    