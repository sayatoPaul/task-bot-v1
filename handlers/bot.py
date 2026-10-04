from aiogram import Router
from aiogram.types import FSInputFile
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

# тут команды /start /id и прочие будущие мелочи, не требующие обращения к БД

@router.message(Command('start'))
async def start_handler(message: Message):
    first_name = message.from_user.first_name
    try:
        start_photo = 'https://i.pinimg.com/1200x/b8/d7/a0/b8d7a04e63e7f25ecb9a572ddc9cb464.jpg'
    except:
        start_photo = FSInputFile('start_Mark_photo.jpg')
    await message.answer_photo(
        start_photo,
        caption = f'<b>Привет, {first_name}! </b> \n\nЭто — бот задачник с полноценной базой данных! Да, я это смог наконец-то написать саморучно! ладно, короче, вот команды: \n - `/start` Запустить бота \n - `/id` показывает твой id`шник и имя \n - `/add задача` сохраняет задачу с ID пользователя в бд \n - `/list` показывает только задачи этого пользователя, \n - `/check номер correct/incorrect` пометить что-то верным/неверным, \n - `/delete номер` удалить задачу по номеру.\n\nПоддержки или менеджера здесь нет поэтому звонить и жаловаться вам не кому.',
        parse_mode="HTML")

@router.message(Command('id'))
async def id_handler(message: Message):
    id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username #если есть
    await message.answer(f'Твой ID: {id}\n\nТвое имя: {first_name}\n\nТвой username (если он у тебя вообще есть лох): {username}')