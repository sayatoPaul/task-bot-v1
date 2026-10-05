from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from database import develop_get

router = Router()

# личные команды для интереса

@router.message(Command('develop_tools'))
async def develop_handler(message: Message):
    get = develop_get()
    await message.answer(f'Команда администратора №1\n\n{get}')

# А это веточка test-new

@router.message(Command('test'))
async def develop_handler(message: Message):
    await message.answer(f'Скибиди-до скибиди-ду')