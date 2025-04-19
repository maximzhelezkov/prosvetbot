from aiogram import Bot, Dispatcher, types
from data import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=config.TOKEN_API, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)
