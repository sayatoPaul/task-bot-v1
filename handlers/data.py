from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from database import add_task, show_list, delete_task, check_task

router = Router()

# тут команды /add /list /delete /check

@router.message(Command('add'))
async def add_handler(message: Message):
    user_id = message.from_user.id
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        await message.answer('Пиши в нормальном формате але.\n\n`/add задача`')
    task = parts[1]
    try:
        add_task(user_id, task)
        await message.answer('Ваша задача была успешна добавлена!')
    except Exception as e:
        await message.answer(f'Ошибка! Что-то пошло не так. {e}')

@router.message(Command('list'))
async def list_handler(message: Message):
    user_id = message.from_user.id
    tasks = show_list(user_id)

    if not tasks:
        await message.answer('У тебя нет задач!')
        return

    text = ''
    
    for i, task in enumerate(tasks, 1):
        if task[3] == 1:
            status = '✅'
        else:
            status = '🚫'
        text += f'{status}| {i}. {task[2]}\n'

    await message.answer(f'<b>Твои задачи:</b>\n\n{text}', parse_mode="HTML") 

@router.message(Command('delete'))
async def delete_handler(message: Message):
    parts = message.text.split()

    # проверка что тип написал не просто команду и номер
    if len(parts) < 2:
        await message.answer('Ну ты тупой! Введи в формате `/delete номер`')
        return

    # проверяем что второе значение это номер и присваем это переменной
    try:
        num = int(parts[1])
    except ValueError:
        await message.answer('Введи номер!')
        return

    user_id = message.from_user.id
    tasks = show_list(user_id)

    # проверяем что корректное число
    if num < 1 or num > len(tasks):
        await message.answer('Ну ты внатуре тупой')
        return

    real_num = tasks[num - 1][0] # мы обращаемся КО ВСЕМ ЗАДАЧАМ которые есть у этого типа. Число которое дал тип МИНУСУЕМ - 1 тк это пайтон и тут с 0 начинается. Мы получаем какую то ВСЮЮЮЮ СТРОЧКУ. но мне надо только лишь ПЕРВУЮ ЧАСТЬ (ТО ЕСТЬ ID - РЕАЛЬНЫЙ). поэтому еще [0] чтобы первую самую часть.
    try:
        delete_task(real_num, user_id) # отправляем данные 
        await message.answer(f'Да! Задача под  id {num} удалена')
    except:
        await message.answer('Something went wrong.... Idk what it is actually')

@router.message(Command('check'))
async def check_handler(message: Message):
    parts = message.text.split()

    if len(parts) < 3:
        await message.answer('Ну ты реально глупый или притворяешься? Давай пиши нормально `/check номер correct/incorrect`')
        return

    try:
        num = int(parts[1])
    except:
        await message.answer('Введи корректно номер! `/check номер correct/incorrect`')
        return

    user_id = message.from_user.id
    tasks = show_list(user_id)

    if num < 1 or num > len(tasks):
        await message.answer('Глупый реально')
        return

    try:
        check = parts[2]
        if check == 'correct':
                check = 1
        elif check == 'incorrect':
                check = 0
        else:
            await message.answer('Введи correct/incorrect...')
            return
    except:
        await message.answer('Глупенький...')
        return

    real_num = tasks[num-1][0]
    check_task(check, real_num, user_id)
    await message.answer('Успешно!') 