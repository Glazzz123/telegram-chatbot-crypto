import requests
from dotenv import load_dotenv
import os

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение API-ключа из переменных окружения
API_KEY = os.getenv("COINMARKETCAP_API_KEY")

# URL для API
AIRDROPS_API_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/airdrops"
EVENTS_API_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/categories"
ICO_API_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/category"

# Функция для получения информации о текущих airdrops
def get_airdrops():
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": API_KEY
    }
    response = requests.get(AIRDROPS_API_URL, headers=headers)

    if response.status_code == 200:
        data = response.json()
        airdrops_list = [f"{airdrop['name']}: {airdrop['details']}" for airdrop in data['data']]
        return "Текущие airdrops:\n" + "\n".join(airdrops_list)
    else:
        print(f"Error: {response.status_code}, {response.text}")  # Логирование ошибки
        return "Не удалось получить данные об аирдропах"

# Функция для получения календаря мероприятий (категории криптовалют)
def get_events_calendar():
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": API_KEY
    }
    response = requests.get(EVENTS_API_URL, headers=headers)

    if response.status_code == 200:
        data = response.json()
        categories_list = [f"{category['name']}: {category['description']}" for category in data['data']]
        return "Категории криптовалют:\n" + "\n".join(categories_list)
    else:
        return "Не удалось получить данные о мероприятиях"


# Функция для получения календаря ICO (категория криптовалют)
def get_ico_calendar():
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": API_KEY
    }
    response = requests.get(ICO_API_URL, headers=headers)

    if response.status_code == 200:
        data = response.json()
        ico_list = [f"{ico['name']}: {ico['description']}" for ico in data['data']]
        return "Календарь ICO:\n" + "\n".join(ico_list)
    else:
        return "Не удалось получить данные о ICO"


