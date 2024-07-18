from aiogram import types
from aiogram.filters.command import Command
from aiogram import Router
from resources import welcome_message
from resources import keyboard_get_weather


router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        welcome_message,
        reply_markup=keyboard_get_weather.as_markup(resize_keyboard=True)
    )