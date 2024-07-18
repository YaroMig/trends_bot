from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


btn_get_weather = InlineKeyboardButton(
    text='Узнать температуру воздуха 🌤',
    callback_data='get_weather'
)

keyboard_get_weather = InlineKeyboardBuilder()
keyboard_get_weather.add(btn_get_weather)