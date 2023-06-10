import asyncio
from aiogram import Bot, Dispatcher
from config import load_config
from tgbot.handlers import command_handlers, send_question_handler
from aiogram.fsm.storage.memory import MemoryStorage

async def main() -> None:
    storage: MemoryStorage = MemoryStorage()
    config = load_config('.env')
    bot: Bot = Bot(token=config.token)

    dp: Dispatcher = Dispatcher()
    dp.include_router(command_handlers.router)
    dp.include_router(send_question_handler.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())