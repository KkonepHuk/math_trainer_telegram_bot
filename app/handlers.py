from aiogram import Router, types, F
from aiogram.filters import Command
import app.raiting_module as raiting_module

from app.task_generator import generate_task, get_answers
from app.keyboard import *

router = Router()

#start-хендлер
@router.message(Command('start'))
async def cmd_start(message: types.Message):

    global raiting
    raiting = raiting_module.new_user_raiting(str(message.from_user.id), message.from_user.full_name)

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

    global raiting
    raiting = raiting_module.new_user_raiting(str(message.from_user.id), message.from_user.full_name)

    await message.answer('Вы начали тренировку.\nДля её завершения не забудьте воспользоваться кнопкой "Закончить тренировку"!\nВы также можете нажать "Рейтинг", чтобы следить за своими успехами.', reply_markup=end_keyboard())
    await message.answer(f'Решите пример:\n<b>{task}</b>', parse_mode='HTML', reply_markup=keyboard.as_markup())


@router.message(F.text == 'Закончить тренировку')
async def end_training(message: types.Message):

    try:
        raiting.to_json()
    finally:
        await message.answer('А вы молодец!\nХорошо потрудились!', reply_markup=start_keyboard())

@router.message(F.text == 'Рейтинг')
async def end_training(message: types.Message):
    global raiting
    try:
        raiting.to_json()
        await message.answer(f'Ваш текущий рейтинг: {raiting}')
    except:
        raiting = raiting_module.new_user_raiting(str(message.from_user.id), message.from_user.full_name)
        
        raiting.to_json()
        await message.answer(f'Ваш текущий рейтинг: {raiting}')

@router.message(F.text == 'Лидеры')
async def leaderboard(message: types.Message):
    try:
        raiting.to_json()
    finally:
        await message.answer(f'<b>Наша гордость:</b>\n{raiting_module.show_leaderboard()}', parse_mode='HTML')

@router.callback_query(F.data == 'correct')
async def correct_answer(callback: types.CallbackQuery):
    task, answer = generate_task()
    answers = get_answers(answer)
    keyboard = answers_keyboard(answers, answer)

    raiting.increase_raiting(25)

    await callback.message.answer('Верно!\n+25 к рейтингу')
    await callback.message.answer(f'Решите пример:\n<b>{task}</b>', parse_mode='HTML', reply_markup=keyboard.as_markup())

@router.callback_query(F.data == 'incorrect')
async def incorrect_answer(callback: types.CallbackQuery):
    task, answer = generate_task()
    answers = get_answers(answer)
    keyboard = answers_keyboard(answers, answer)
    await callback.message.answer('Эх, ошибка(\n-25 к рейтингу')

    raiting.decrease_raiting(25)

    await callback.message.answer(f'Решите пример:\n<b>{task}</b>', parse_mode='HTML', reply_markup=keyboard.as_markup())





