from aiogram import types, Router
from aiogram.filters import Command  # Новый синтаксис для фильтров
from services.news_services import get_news  # Импорт функции для взаимодействия с API

router = Router()  # Создаем роутер для регистрации обработчиков

# Функция для разделения сообщения на части
def split_message(message, max_length=4096):
    return [message[i:i + max_length] for i in range(0, len(message), max_length)]

# Обработчик для команды "Новости"
@router.message(Command(commands=["news"]))

async def news_handler(message: types.Message):
    await message.answer("Вы выбрали раздел 'Новости'")

    # Вызов функции для получения новостей
    news = get_news()

    # Отправка пользователю новостей, если они есть
    if news:
        # Проверяем длину сообщения
        if len(news) > 4096:
            for part in split_message(news):
                await message.answer(part)  # Отправляем каждую часть по очереди
        else:
            await message.answer(news)
    else:
        await message.answer("Не удалось получить новости. Попробуйте позже.")



