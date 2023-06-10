
from aiogram.filters.state import State, StatesGroup


class FSMFillForm(StatesGroup):
    # Создаем экземпляры класса State, последовательно
    # перечисляя возможные состояния, в которых будет находиться
    # бот в разные моменты взаимодейтсвия с пользователем
    GREETINGS = State()
    QUESTION_PROBLEM = State()
    QUESTION_PRODUCT_STAGE = State()
    QUESTION_PERSONAL_PROBLEMS = State()
    QUESTION_ROLE = State()
    QUESTION_HAVE_PARTNER = State()
    SEND_QUESTIONS = State()

