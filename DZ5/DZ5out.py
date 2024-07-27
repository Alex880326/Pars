from pymongo import MongoClient
import json

client = MongoClient()
db = client['mydatabase']
collection = db['Economics']


# вывод первой записи в коллекции
all_docs = collection.find()
first_doc = all_docs[0]


# вывод объекта json
pretty_json = json.dumps(first_doc, indent=4, default=str)
print(pretty_json)



count = collection.count_documents({})
print(f"число записей в бзд =  {count}")
