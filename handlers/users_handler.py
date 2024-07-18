from aiogram import types
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from utils import get_weather_data
from utils import delete_message
from handlers.commands_handler import cmd_start
from aiogram import Bot
from config import TOKEN


router = Router()
bot = Bot(token=TOKEN)


class GeographicData(StatesGroup):
    latitude = State()
    longitude = State()


@router.callback_query(F.data == "get_weather")
async def get_weather(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer('Введите широту')
    await state.set_state(GeographicData.latitude)


@router.message(GeographicData.latitude)
async def input_latitude(message: types.Message, state: FSMContext):
    chat_id = message.from_user.id
    messages_id = [message.message_id, message.message_id - 1]
    await delete_message(chat_id, messages_id)
    await state.update_data(latitude=message.text)
    await message.answer('Введите долготу')
    await state.set_state(GeographicData.longitude)


@router.message(GeographicData.longitude)
async def input_longitude(message: types.Message, state: FSMContext):
    chat_id = message.from_user.id 
    messages_id = [message.message_id, message.message_id - 1]
    await delete_message(chat_id, messages_id)
    await state.update_data(longitude=message.text)

    user_data = await state.get_data()
    latitude = user_data['latitude']
    longitude = user_data['longitude']

    air_temperature = await get_weather_data(latitude, longitude)

    await message.answer(
        f'''Текущая температура воздуха по координатам:n
Широта: <b>{latitude}</b>
Долгота: <b>{longitude}</b>

<b>Составляет {air_temperature} градуса по Цельсию.</b>''',
        parse_mode='HTML'
    )

    await cmd_start(message)