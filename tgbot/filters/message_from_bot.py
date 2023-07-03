from aiogram import Bot
from aiogram.types import Message

from aiogram.filters import BaseFilter


class ReplyFilterBot(BaseFilter):
    async def __call__(self, message: Message, bot: Bot) -> bool:
        try:
            if message.reply_to_message.from_user.id == bot.id:
                return True
        except Exception as e:
            print(e)
