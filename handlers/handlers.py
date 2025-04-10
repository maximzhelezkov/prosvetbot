from boot import bot, dp, types
from kb.kb import menuikb
from db.dbcon import db
from data.txt import START_MESSAGE
from data.config import admin_id
import sqlite3
from aiogram.types import ChatInviteLink
import asyncio


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=START_MESSAGE, reply_markup=menuikb)

    nonetype = "None"
    user_id = message.from_user.id
    username = (message.from_user.username or nonetype)
    db(user_id, username)
    

milky_id = 1984752299 



