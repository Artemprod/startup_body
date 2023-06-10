import asyncio
from aiogram import Bot, Dispatcher
from config import load_config
from tgbot.handlers import command_handlers
from aiogram.fsm.storage.memory import MemoryStorage

async def main() -> None:
    storage: MemoryStorage = MemoryStorage()
    config = load_config('.env')
    bot: Bot = Bot(token=config.token)

    dp: Dispatcher = Dispatcher()
    dp.include_router(command_handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())