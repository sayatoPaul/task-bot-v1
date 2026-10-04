import asyncio
from aiogram import Bot, Dispatcher
from database import create_table

from config import TOKEN 
# все не требующее ДБ
from handlers.bot import router as bot_router  
# вся дата
from handlers.data import router as data_router
# все девелоп
from handlers.develop import router as develop_router

bot = Bot(token=TOKEN)
dp = Dispatcher()

create_table()

# все не требующее ДБ
dp.include_router(bot_router)
# вся дата
dp.include_router(data_router)
# все девелоп
dp.include_router(develop_router)

async def main():
    print('Запущено')
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())        