from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup

from tgbot.models.bot_variables import KEYBOARD


def gen_begin_question_keyboard() -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.button(text=KEYBOARD['begin'], callback_data='begin')
    return kb_builder.as_markup()
