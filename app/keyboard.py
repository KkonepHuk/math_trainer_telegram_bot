from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram import types

def start_keyboard():
    kb = [
        [types.KeyboardButton(text="Начать тренировку!")],
        [types.KeyboardButton(text="Рейтинг"), types.KeyboardButton(text="Лидеры")]
    ]
    start = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )

    return start

def end_keyboard():
    kb = [
        [types.KeyboardButton(text="Закончить тренировку")],
        [types.KeyboardButton(text="Рейтинг"), types.KeyboardButton(text="Лидеры")]
    ]
    end = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )

    return end

def answers_keyboard(answers, answer):
    keyboard = InlineKeyboardBuilder()
    for i in answers:
        callback = 'incorrect'
        if i == answer:
            callback = 'correct'
        keyboard.add(types.InlineKeyboardButton(text=str(i), callback_data=callback))
    
    return keyboard
