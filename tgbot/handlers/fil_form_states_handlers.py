from asyncio import sleep
from random import randint

from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.fsm.state import default_state

from tgbot.handlers.send_question_handler import process_send_question
from tgbot.keyboards.inline_keyboard import gen_begin_question_keyboard
from tgbot.models.bot_variables import BotAnswers
from tgbot.models.questions import questions
from tgbot.models.users import users

from tgbot.states import FSMFillForm, FSMSendQuestions

router: Router = Router()


@router.message(Command(commands='fillform'), StateFilter(default_state))
async def process_start_filling_form(message: Message, state: FSMContext):
    await message.answer(f'{BotAnswers.QUESTION_PROBLEM.value}')
    await state.set_state(FSMFillForm.QUESTION_PROBLEM)

@router.message(StateFilter(FSMFillForm.QUESTION_PROBLEM),)
async def process_state_fill_problem(message: Message, state: FSMContext,bot:Bot):
    await state.update_data(problem=message.text)
    await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    await sleep(1)
    await message.answer(f'{BotAnswers.QUESTION_ROLE.value}')
    await state.set_state(FSMFillForm.QUESTION_ROLE)

@router.message(StateFilter(FSMFillForm.QUESTION_ROLE),)
async def process_state_fill_problem(message: Message, state: FSMContext,bot:Bot):
    await state.update_data(role=message.text)
    await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    await sleep(1)
    await message.answer(f'{BotAnswers.QUESTION_PERSONAL_PROBLEMS.value}')
    await state.set_state(FSMFillForm.QUESTION_PERSONAL_PROBLEMS)

@router.message(StateFilter(FSMFillForm.QUESTION_PERSONAL_PROBLEMS),)
async def process_state_fill_problem(message: Message, state: FSMContext,bot:Bot):
    await state.update_data(personal_problem=message.text)
    await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    await sleep(1)
    await message.answer(f'{BotAnswers.QUESTION_PRODUCT_STAGE.value}')
    await state.set_state(FSMFillForm.QUESTION_PRODUCT_STAGE)

@router.message(StateFilter(FSMFillForm.QUESTION_PRODUCT_STAGE),)
async def process_state_fill_problem(message: Message, state: FSMContext,bot:Bot):
    await state.update_data(satge=message.text)
    await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    await sleep(1)
    await message.answer(f'{BotAnswers.QUESTION_HAVE_PARTNER.value}')
    await state.set_state(FSMFillForm.QUESTION_HAVE_PARTNER)

@router.message(StateFilter(FSMFillForm.QUESTION_HAVE_PARTNER),)
async def process_state_fill_problem(message: Message, state: FSMContext,bot:Bot):
    await state.update_data(partner=message.text)
    users['personal_info'] = await state.get_data()
    print(users)
    await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    await sleep(1)
    await message.answer(f'{BotAnswers.EXIT_FROM_FILL_FORM_FSM_DATA_SAVED.value}',
                         )
    await state.set_state(FSMSendQuestions.QUESTION_SENT)
    await process_send_question(message, state, bot,)

