from aiogram import Bot, Dispatcher, types
from data import config
from aiogram.dispatcher.middlewares import BaseMiddleware
import logging

bot = Bot(
    token=config.TOKEN_API, 
    parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseMiddleware):
    async def update(self, update: types.Update, data: dict):
        if update.callback_query:
            call = update.callback_query
            nonetype = "\u3164"
            logger.info(f"call = {call.data}, {call.from_user.id}, @{call.from_user.username or nonetype}")
        elif update.message:
            msg = update.message
            logger.info(f"message = {msg.text}, {msg.from_user.id}, @{msg.from_user.username or nonetype}")

        await super().on_process_update(update, data)

dp.middleware.setup(LoggingMiddleware())
