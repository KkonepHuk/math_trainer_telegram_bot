import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
    