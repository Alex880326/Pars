from pymongo import MongoClient
import json

client = MongoClient()
db = client['mydatabase']
collection = db['books']


# вывод первой записи в коллекции
all_docs = collection.find()
first_doc = all_docs[0]


# вывод объекта json
pretty_json = json.dumps(first_doc, indent=4, default=str)
print(pretty_json)



count = collection.count_documents({})
print(f"число записей в бзд =  {count}")

count = collection.count_documents(filter={'price': {'$gte': 50.00}})
print(f"Количество книг, дороже 50 =  {count}")

count = collection.count_documents(filter={'stock': {'$lt': 7}})
print(f"Количество книг, менее 7 =  {count}")

projection = {'_id': 0, 'book_name': 1, 'price': 1}
print("Книги, название которых начинается на (В), стоимостью меньше 14")
for book in collection.find({"book_name": {'$regex': '^B'}, 'price': {'$lte': 14.00}}, projection):
        print(book)


projection = {'_id': 0, 'book_name': 1}
print("Книги, в названиях которых присутствует слово (Hearts)")
for book in collection.find({'book_name': {'$regex': 'Hearts', '$options': 'i'}}, projection):
    print(book)

print(f'Количество книг, стоимостьбю более 40, название которых начинается на  (А), на складе менее 3 штук')
few_books = collection.count_documents({
    '$and': [
        {'price': {'$gte': 40}},
        {'book_name': {'$regex': 'A'}},
        {'stock': {'$lt': 3}}
    ]
})
print(few_books)

pipeline = [
    {"$group": {"_id": None, "total_price": {"$sum": "$price"}}}
]
result = list(collection.aggregate(pipeline))
if result:
    total_price = result[0]["total_price"]
    print(f"Общая стоимость всех книг: {total_price}")

