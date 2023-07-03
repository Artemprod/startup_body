from aiogram.filters.state import State, StatesGroup


class FSMFillForm(StatesGroup):
    QUESTION_PROBLEM = State()
    QUESTION_PRODUCT_STAGE = State()
    QUESTION_PERSONAL_PROBLEMS = State()
    QUESTION_ROLE = State()
    QUESTION_HAVE_PARTNER = State()
    SEND_QUESTIONS = State()


class FSMSendQuestions(StatesGroup):
    QUESTION_SENT = State()
    WAITING_ANSWER = State()
    OBSERVE_ANSWERS = State()
