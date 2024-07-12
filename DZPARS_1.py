import requests
import json

query = input('Введите название фильма: ')
page = input('Введите количество выводимых фильмов: ')
url = f"https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit={page}&query={query}"

headers = {
    "Accept": "application/json",
    "X-API-KEY": "WJFMPYY-AAPMS7G-MFD2Z8F-53Q925E"
}

response = requests.get(url, headers=headers)2
data = response.json()

with open('movie_data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Данные в файле: movie_data.json")
