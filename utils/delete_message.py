from aiogram import Bot
from config import TOKEN


bot = Bot(token=TOKEN)


async def delete_message(chat_id, messages_id):
    """
    Функция для удаления нескольких сообщений в чате.

    Аргументы:
        chat_id (int): ID чата, в котором нужно удалить сообщения.
        messages_id (list): Список ID сообщений для удаления.
    """
    for message_id in messages_id:
        await bot.delete_message(chat_id, message_id)