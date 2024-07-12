import requests
from bs4 import BeautifulSoup
import json
import time

def parse_books(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        books = soup.find_all('article', class_='product_pod')

        all_books = []
        

        for book in books:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            in_stock = book.find('p', class_='instock availability').text.strip()

            book_info = {
                "Название": title,
                "Цена": price,
                "Наличие": in_stock
            }

            all_books.append(book_info)

            print(f"Название: {title}")
            print(f"Цена: {price}")
            print(f"В наличии: {in_stock}")
            print("------------------")

        with open('books_info.json', 'a', encoding='utf-8') as f:
            json.dump(all_books, f, indent=2, ensure_ascii=False)

        next_button = soup.find('li', class_='next')
        if next_button:
            next_page = next_button.a['href']
            time.sleep(1)
            next_url = url.split('/index.html')[0] + '/' + next_page
            parse_books(next_url)
        else:
            print("Парсинг завершен")

    else:
        print("Ошибка при получении страницы")

url = "https://books.toscrape.com/"
parse_books(url)
