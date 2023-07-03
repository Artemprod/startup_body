import itertools
from asyncio import sleep
from random import randint

from tgbot.filters.message_from_bot import ReplyFilterBot
from tgbot.models.bot_variables import BotAnswers
from tgbot.models.questions import questions as QUESTIONS, questions
from aiogram import Router

from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import default_state
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, StateFilter, Text
from aiogram.fsm.context import FSMContext

from tgbot.models.users import users
from tgbot.states import  FSMSendQuestions

router = Router()



@router.callback_query(Text(text='begin'),
                       )
async def process_send_question(message: Message, state: FSMContext, bot: Bot):
    sent_questions: list = users[message.from_user.id]['sent_questions']

@router.message(StateFilter(FSMSendQuestions.QUESTION_SENT), )
async def process_send_question(message: Message, state: FSMContext, bot: Bot):
    print(message)
    await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    sent_questions: list = users[message.from_user.id]['sent_questions']
    if len(sent_questions) == 30:
        await state.set_state(FSMSendQuestions.OBSERVE_ANSWERS)
    number_of_question = randint(0, len(questions.keys()))
    if number_of_question in sent_questions:
        number_of_question = randint(0, len(questions.keys()))
    question_to_send = (f'{BotAnswers.QUESTION_TO_SEND_QUESTION.value} {questions[number_of_question]["question"]}\n\n'
                        f'{BotAnswers.QUESTION_TO_SEND_USEFULNESS.value} {questions[number_of_question]["usefulness"]}\n'
                        f'{BotAnswers.QUESTION_TO_SEND_METRIC.value} {questions[number_of_question]["metric"]}\n'
                        f'{BotAnswers.QUESTION_TO_SEND_CATEGORY.value} {questions[number_of_question]["category"]}\n'
                        f'{BotAnswers.QUESTION_TO_SEND_STAGE.value} {questions[number_of_question]["stage"]}')
    sent_questions.append(number_of_question)

    await state.update_data(number_of_question=number_of_question)
    await bot.send_message(chat_id=message.chat.id, text=question_to_send,)
    await bot.send_chat_action(chat_id=message.chat.id, action='typing')
    await sleep(1)
    await bot.send_message(chat_id=message.chat.id, text='Жду ответ',)
    await state.update_data(answer=message.text)
    users[message.from_user.id]['answers'] = await state.get_data()
    await state.set_state(FSMSendQuestions.QUESTION_SENT)



@router.message(StateFilter(FSMSendQuestions.WAITING_ANSWER))
async def process_write_answer(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(answer=message.text)
    users[message.from_user.id]['answers'] = await state.get_data()
    await state.set_state(FSMSendQuestions.QUESTION_SENT)


@router.message(StateFilter(FSMSendQuestions.OBSERVE_ANSWERS))
async def process_send_question_1(message: Message, state: FSMContext, bot: Bot):
    user_answers = users[message.from_user.id]['answers']
    await message.answer(user_answers)
    await state.set_state(FSMSendQuestions.QUESTION_SENT)
