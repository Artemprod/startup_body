import itertools
from time import sleep

from tgbot.models.questions import questions as QUESTIONS, questions
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message
from aiogram.fsm.state import default_state

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, StateFilter, Text

from aiogram.fsm.context import FSMContext

from tgbot.states import FSMFillForm

router = Router()



@router.message(Text(text=['поехали', 'погнали', 'да']))
async def send_questions(message: Message):
    stop = 0
    for number, question in itertools.cycle(questions.items()):
        if stop == 1:
            break
        q = (f'<b>Вопрос:</b> {question["question"]}\n\n'
             f'<b>Полезность:</b> {question["usefulness"]}\n'
             f'<b>Метрика:</b> {question["metric"]}\n'
             f'<b>Категория:</b> {question["category"]}\n'

             f'<b>Стадия:</b> {question["stage"]}')

        await message.answer(f'{number} \n{q}', parse_mode='HTML')
        sleep(24 * 60 * 60)






# Этот хэндлер будет срабатывать, если введено корректное имя
# и переводить в состояние ожидания ввода возраста
@router.message(StateFilter(FSMFillForm.QUESTION_PROBLEM))
async def process_name_sent(message: Message, state: FSMContext):
    print()
    # Cохраняем введенное имя в хранилище по ключу "name"
    await state.update_data(name=message.text)
    await message.answer(text='Спасибо!\n\nА теперь введите ваш возраст')
    # Устанавливаем состояние ожидания ввода возраста
    await state.set_state(FSMFillForm.QUESTION_HAVE_PARTNER)

@router.message(StateFilter(FSMFillForm.QUESTION_HAVE_PARTNER))
async def process_name_sent(message: Message, state: FSMContext):
    # Cохраняем введенное имя в хранилище по ключу "name"
    await state.update_data(name=message.text)
    await message.answer(text='Спасибо!\n\nА теперь введите ваш возраст')
    # Устанавливаем состояние ожидания ввода возраста
    await state.set_state(FSMFillForm.QUESTION_PRODUCT_STAGE)

@router.message(StateFilter(FSMFillForm.QUESTION_PRODUCT_STAGE), F.text.isalpha())
async def process_name_sent(message: Message, state: FSMContext):
    # Cохраняем введенное имя в хранилище по ключу "name"
    await state.update_data(name=message.text)
    await message.answer(text='Спасибо!\n\nА теперь введите ваш возраст')
    # Устанавливаем состояние ожидания ввода возраста
    await state.set_state(FSMFillForm.QUESTION_ROLE)

@router.message(StateFilter(FSMFillForm.QUESTION_ROLE), F.text.isalpha())
async def process_name_sent(message: Message, state: FSMContext):
    # Cохраняем введенное имя в хранилище по ключу "name"
    await state.update_data(name=message.text)
    await message.answer(text='Спасибо!\n\nА теперь введите ваш возраст')
    # Устанавливаем состояние ожидания ввода возраста
    await state.set_state(FSMFillForm.QUESTION_PERSONAL_PROBLEMS)

@router.message(StateFilter(FSMFillForm.QUESTION_ROLE), F.text.isalpha())
async def process_name_sent(message: Message, state: FSMContext):
    # Cохраняем введенное имя в хранилище по ключу "name"
    await state.update_data(name=message.text)
    await message.answer(text='Спасибо!\n\nА теперь введите ваш возраст')
    # Устанавливаем состояние ожидания ввода возраста
    await state.set_state(FSMFillForm.SEND_QUESTIONS)

@router.message(StateFilter(FSMFillForm.QUESTION_ROLE), F.text.isalpha())
async def process_name_sent(message: Message, state: FSMContext):
    # Cохраняем введенное имя в хранилище по ключу "name"
    await state.update_data(name=message.text)
    await message.answer(text=f'{QUESTIONS[1]}')
    # Устанавливаем состояние ожидания ввода возраста
