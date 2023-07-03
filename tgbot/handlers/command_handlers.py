import asyncio
from copy import deepcopy
from datetime import datetime
from time import sleep

from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.fsm.state import default_state
from tgbot.models.bot_variables import BotAnswers
from tgbot.models.users import users, template
from tgbot.states import FSMFillForm

router = Router()


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message,state:FSMContext):
    bot = Bot.get_current()
    if message.from_user.id not in users:
        users[message.from_user.id] = deepcopy(template)
    await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    await asyncio.sleep(1)
    await message.answer(f'{BotAnswers.GREETINGS.value}',
                         parse_mode="HTML")

    await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    await asyncio.sleep(5)
    await message.answer(f'{BotAnswers.QUESTION_PROBLEM.value}')
    await state.set_state(FSMFillForm.QUESTION_PROBLEM)


# Этот хэндлер будет срабатывать на команду "/help"
@router.message(Command(commands='help'), StateFilter(default_state))
async def process_help_command(message: Message):
    await message.answer(f'{BotAnswers.HELP.value}', parse_mode="HTML")


@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(text=f'{BotAnswers.EXIT_FROM_FILL_FORM_FSM.value}')
    # Сбрасываем состояние
    await state.clear()


