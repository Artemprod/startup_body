import asyncio
from aiogram import Bot, Dispatcher
from config import load_config
from tgbot.handlers import command_handlers, send_question_handler, fil_form_states_handlers
from aiogram.fsm.storage.memory import MemoryStorage

from tgbot.keyboards.set_menu import set_main_menu


async def main() -> None:
    storage: MemoryStorage = MemoryStorage()
    config = load_config('.env')
    bot: Bot = Bot(token=config.token, parse_mode='HTML')

    dp: Dispatcher = Dispatcher(storage=storage)
    dp.include_router(command_handlers.router)
    dp.include_router(fil_form_states_handlers.router)
    dp.include_router(send_question_handler.router)

    await set_main_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())