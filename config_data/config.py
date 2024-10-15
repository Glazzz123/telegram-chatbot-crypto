from dotenv import load_dotenv
import os

# Загрузка переменных окружения из файла .env
load_dotenv()


def load_config():
    tg_bot_token = os.getenv('TOKEN')
    coinmarketcap_api_key = os.getenv('COINMARKETCAP_API_KEY')

    if not tg_bot_token:
        raise ValueError("Токен Telegram-бота (TOKEN) не найден в .env файле!")
    if not coinmarketcap_api_key:
        raise ValueError("API-ключ CoinMarketCap (COINMARKETCAP_API_KEY) не найден в .env файле!")

    return {
        'tg_bot_token': tg_bot_token,  # Токен бота из .env
        'coinmarketcap_api_key': coinmarketcap_api_key  # API-ключ CoinMarketCap из .env
    }


























