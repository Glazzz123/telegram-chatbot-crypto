import requests
from dotenv import load_dotenv
import os

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение API-ключа из переменных окружения
API_KEY = os.getenv("COINMARKETCAP_API_KEY")

# Функция для получения топ-50 криптовалют
def get_top_50_cryptos():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": API_KEY,
    }
    params = {
        'start': '1',
        'limit': '50',
        'convert': 'USD'
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        return format_crypto_data(data)
    except Exception as e:
        return f"Ошибка: {str(e)}"


# Функция для получения данных о росте и падении криптовалют
def get_growth_decline():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": API_KEY,
    }
    params = {
        'start': '1',
        'limit': '10',
        'sort': 'percent_change_24h',
        'sort_dir': 'desc',
        'convert': 'USD'
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        return format_crypto_data(data)
    except Exception as e:
        return f"Ошибка: {str(e)}"


# Функция для получения трендовых криптовалют
def get_trending_cryptos():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/trending/most-visited"
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": API_KEY,
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return format_crypto_data(data)
    except Exception as e:
        return f"Ошибка: {str(e)}"


# Функция для получения предстоящих криптовалют
def get_upcoming_cryptos():
    url = "https://pro-api.coinmarketcap.com/v1/blockchain/statistics/latest"
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": API_KEY,
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return format_crypto_data(data)
    except Exception as e:
        return f"Ошибка: {str(e)}"


# Функция для форматирования данных о криптовалютах
def format_crypto_data(data):
    formatted_data = ""
    for crypto in data['data']:
        formatted_data += f"{crypto['name']} ({crypto['symbol']}): {crypto['quote']['USD']['price']}$\n"
    return formatted_data



