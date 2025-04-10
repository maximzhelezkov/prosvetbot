from boot import bot, dp, types
from aiogram.types import CallbackQuery
from data.txt import START_MESSAGE,MENU_MESSAGE, NOT_YET, MENUB1_MESSAGE, MENUB4_MESSAGE, MENUB5_MESSAGE
from kb.kb import menuikb, menub5ikb, menuikb1
import logging
import asyncio
import sqlite3

# MENU_MESSAGE = START_MESSAGE

# @dp.callback_query_handler(lambda cb: cb.data == 'backtomenu')
# async def callback_rus(call: CallbackQuery):     
#     nonetype = "\u3164"
#     logging.info(f"call = {call.data}, {call.from_user.id}, @{call.from_user.username or nonetype}")
#     await bot.answer_callback_query(call.id)
#     await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=MENU_MESSAGE, reply_markup=menuikb)


@dp.callback_query_handler(lambda cb: cb.data == 'menub1')
async def callback_menub1(call: CallbackQuery):     
    nonetype = "\u3164"
    logging.info(f"call = {call.data}, {call.from_user.id}, @{call.from_user.username or nonetype}")
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=MENUB1_MESSAGE, reply_markup=menuikb1)

@dp.callback_query_handler(lambda cb: cb.data == 'back1')
async def callback_back(call: CallbackQuery):
    nonetype = "\u3164"
    logging.info(f"call = {call.data}, {call.from_user.id}, @{call.from_user.username or nonetype}")
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text=START_MESSAGE, reply_markup=menuikb)

@dp.callback_query_handler(lambda cb: cb.data == 'menub5')
async def callback_menub5(call: CallbackQuery):     
    nonetype = "\u3164"
    logging.info(f"call = {call.data}, {call.from_user.id}, @{call.from_user.username or nonetype}")
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=MENUB5_MESSAGE, reply_markup=menub5ikb, disable_web_page_preview=True)

@dp.callback_query_handler(lambda cb: cb.data == 'menub51')
async def callback_menub51(call: CallbackQuery):     
    nonetype = "\u3164"
    logging.info(f"call = {call.data}, {call.from_user.id}, @{call.from_user.username or nonetype}")
    await bot.answer_callback_query(call.id)
    await bot.send_location(chat_id=call.message.chat.id, latitude=55.788208, longitude=37.582715)
    
 

@dp.callback_query_handler(lambda cb: cb.data == 'menub4')
async def callback_menub4(call: CallbackQuery):     
    nonetype = "\u3164"
    logging.info(f"call = {call.data}, {call.from_user.id}, @{call.from_user.username or nonetype}")
    await bot.answer_callback_query(call.id)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=MENUB4_MESSAGE)#, reply_markup=menuikb4)
