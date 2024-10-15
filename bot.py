import asyncio  # Импортируем asyncio
import logging  # Импортируем logging
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot
from config_data import load_config  # Импорт функции load_config

from handlers.base_handlers import router as base_router
from handlers.other_handlers import router as other_router
from handlers.exchanges_handlers import router as exchanges_router
from handlers.product_handlers import router as product_router
from handlers.news_handlers import router as news_router

# Загрузка конфигурации (токен и API ключи) из .env через config.py
config = load_config()

# Инициализация бота с токеном из файла .env
bot = Bot(token=config['tg_bot_token'])
dp = Dispatcher(storage=MemoryStorage())

# Регистрируем обработчики
dp.include_router(base_router)
dp.include_router(other_router)
dp.include_router(exchanges_router)
dp.include_router(product_router)
dp.include_router(news_router)


async def on_startup():
    print("Бот запущен")


async def on_shutdown():
    print("Бот остановлен")


async def main():
    logging.info("Бот успешно запущен и готов к работе")
    await dp.start_polling(bot)


# Запускаем основную функцию через asyncio с обработкой ошибок
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # Настройка логирования

    try:
        asyncio.run(main())  # Попытка запустить бота
    except Exception as e:
        logging.error(f"Не удалось запустить бота! Ошибка: {e}")  # Логируем ошибку









