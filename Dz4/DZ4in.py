import pymongo
import json

# Подключение к базе данных MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

# Создание коллекции
collection = db["forex"]

# Чтение данных из JSON файла
with open('finance.yahoo.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Добавление данных в коллекцию
collection.insert_many(data)

print("Данные успешно добавлены в базу данных MongoDB!")
