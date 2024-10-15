import requests
from dotenv import load_dotenv
import os

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение API-ключа из переменных окружения
API_KEY = os.getenv("COINMARKETCAP_API_KEY")
NEWS_API_URL = "https://pro-api.coinmarketcap.com/v1/content/latest"

# Функция для получения новостей
def get_news():
    headers = {
        "Accepts": "application/json",
        "X-API-KEY": API_KEY
    }
    params = {
        'country': 'us',  # Пример параметра
        'category': 'technology',  # Пример категории
    }
    response = requests.get(NEWS_API_URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        news_list = [f"{article['title']}: {article['description']}" for article in data['articles']]
        return "Текущие новости:\n" + "\n".join(news_list)
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None


