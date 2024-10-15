from peewee import *
from datetime import datetime

# Подключение к базе данных SQLite
db = SqliteDatabase('user_history.db')

# Определение базовой модели для связи с БД
class BaseModel(Model):
    class Meta:
        database = db

# Модель для хранения истории команд пользователей
class UserHistory(BaseModel):
    user_id = IntegerField()  # ID пользователя
    command = CharField()     # Команда, которую использовал пользователь
    timestamp = DateTimeField(default=datetime.now)  # Время выполнения команды

# Подключение к базе данных и создание таблицы, если её нет
db.connect()
db.create_tables([UserHistory])

# Функция для сохранения действий пользователя
def save_user_action(user_id, command):
    UserHistory.create(user_id=user_id, command=command)

# Функция для получения последних 10 команд пользователя
def get_user_history(user_id):
    # Извлекаем последние 10 записей для данного пользователя
    history = (UserHistory
               .select()
               .where(UserHistory.user_id == user_id)
               .order_by(UserHistory.timestamp.desc())
               .limit(10))
    return history
