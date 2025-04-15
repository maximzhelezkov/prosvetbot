from aiogram import executor
import logging
from boot import dp, bot  
from data import config
from handlers import handlers
from kb import kb, cb
from db import dbcon
from data import config, txt


logging.basicConfig(level=logging.INFO)
    
# async def start_bot(_):
#     print("Бот запущен")
#     await bot.send_message(
#         config.chat_log_id, 
#         "Бот запущен ✅")

# async def stop_bot(_):
#     print("Бот офнут")
#     await bot.send_message(config.chat_log_id, "Бот выключен ❌")

        # on_shutdown=stop_bot, 
        # on_startup=start_bot

if __name__ == "__main__":
    executor.start_polling(
        dp, 
        skip_updates=True)