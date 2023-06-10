import itertools
from datetime import datetime
from time import sleep

from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.state import default_state
from tgbot.models.bot_variables import BotAnswers, BotStates
from tgbot.models.users import users
from tgbot.models.questions import questions

router = Router()


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message,state: FSMContext):
    if message.from_user.id not in users:
        # Если пользователь только запустил бота и его нет в словаре'
        # 'users - добавляем его в словарь
        users[message.from_user.id] = {
            'name': message.from_user.first_name,
            'registration_date': datetime.now(),
            'product_info': None,
            'difficulty': None,
            'questions': None,
            'answers': None,
            'state': BotStates.GREETINGS.QUESTION_PROBLEM,
        }

    await message.answer(f'{BotAnswers.GREETINGS.value}'
                         'Чтобы получить справку и список доступных '
                         'команд - отправьте команду /help', parse_mode="HTML")

    # await message.answer(f'{BotAnswers.QUESTION_PROBLEM.value}'
    #                      ,
    #                      parse_mode="HTML")




# Этот хэндлер будет срабатывать на команду "/help"
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(f'{BotAnswers.HELP.value}', parse_mode="HTML")


@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(text='Вы вышли из машины состояний\n\n'
                              'Чтобы снова перейти к заполнению анкеты - '
                              'отправьте команду /fillform')
    # Сбрасываем состояние
    await state.clear()
