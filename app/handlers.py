from aiogram import Router, types, F
from aiogram.filters import Command
import random

from app.task_generator import generate_task, get_answers
from app.keyboard import *

router = Router()

#start-хендлер
@router.message(Command('start'))
async def cmd_start(message: types.Message):
    keyboard = start_keyboard()
    await message.answer(f'Добро пожаловать в <b>MATH TRAINER</b>, {message.from_user.first_name}!\nНачните тренировать свои математические навыки, нажав на кнопку!',
                         parse_mode='HTML',
                         reply_markup=keyboard
    )


@router.message(F.text == 'Начать тренировку!')
async def start_training(message: types.Message):
    task, answer = generate_task()
    answers = get_answers(answer)
    keyboard = answers_keyboard(answers, answer)
    await message.answer('Вы начали тренировку.\nДля её завершения воспользуйтесь кнопкой "Закончить тренировку".\nВы также можете нажать "Рейтинг", чтобы следить за своими успехами.', reply_markup=end_keyboard())
    await message.answer(f'Решите пример:\n<b>{task}</b>', parse_mode='HTML', reply_markup=keyboard.as_markup())

@router.message(F.text == 'Закончить тренировку')
async def end_training(message: types.Message):
    await message.answer('А вы молодец!\nХорошо потрудились!', reply_markup=start_keyboard())

@router.message(F.text == 'Рейтинг')
async def end_training(message: types.Message):
    await message.answer('Извините, система рейтинга находится в разработке') 

@router.callback_query(F.data == 'correct')
async def correct_answer(callback: types.CallbackQuery):
    task, answer = generate_task()
    answers = get_answers(answer)
    keyboard = answers_keyboard(answers, answer)
    await callback.message.answer('Верно!\n+25 к рейтингу')
    await callback.message.answer(f'Решите пример:\n<b>{task}</b>', parse_mode='HTML', reply_markup=keyboard.as_markup())

@router.callback_query(F.data == 'incorrect')
async def incorrect_answer(callback: types.CallbackQuery):
    task, answer = generate_task()
    answers = get_answers(answer)
    keyboard = answers_keyboard(answers, answer)
    await callback.message.answer('Эх, ошибка(\n-25 к рейтингу')
    await callback.message.answer(f'Решите пример:\n<b>{task}</b>', parse_mode='HTML', reply_markup=keyboard.as_markup())




