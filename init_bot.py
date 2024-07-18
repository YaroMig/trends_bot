from aiogram import Bot, Dispatcher
from handlers import commands_handler, users_handler
import logging 
from config import TOKEN


logging.basicConfig(level=logging.INFO)


async def main():
    """
    Основная функция запуска бота.
    """
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_routers(
        commands_handler.router,
        users_handler.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot) 