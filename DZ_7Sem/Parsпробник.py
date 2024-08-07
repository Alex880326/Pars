from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import csv

user_agent = (
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
)

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument(f'user-agent={user_agent}')
chrome_option.add_argument('start-minimized')

driver = webdriver.Chrome(options=chrome_option)
url = 'https://byruthub.org/action/'

try:
    driver.get(url)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    game_data = []

    while True:
        game_titles_xpath = "//*[@class='short_title']/a"
        size_xpath = "//span[@class='size']"
        year_release_xpath = "//span[@class='short_year']"
        loaded_xpath = "//span[@class='views']/text()" # Берем текст после значка загрузок

        game_titles = driver.find_elements(By.XPATH, game_titles_xpath)
        game_sizes = driver.find_elements(By.XPATH, size_xpath)
        game_years = driver.find_elements(By.XPATH, year_release_xpath)
        game_loads = driver.find_elements(By.XPATH, loaded_xpath)

        for title_element, size_element, year_element, load_element in zip(game_titles, game_sizes, game_years, game_loads):
            title = title_element.text
            size = size_element.text
            year = year_element.text
            loads = load_element.text
            
            game_data.append({
                'title': title,
                'size': size,
                'year': year,
                'loads': loads
            })  # Сохраняем все данные как словарь

        print(game_data)

        # Попробуем найти кнопку "Далее" и кликнуть по ней
        try:
            next_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Показать еще')]")  # Замените текст на нужный
            next_button.click()
            time.sleep(2)  # Подождем немного, чтобы страница загрузилась
        except Exception as e:
            print("Больше страниц нет или произошла ошибка:", e)
            break

  


except Exception as e:
    print(f'Произошла ошибка: {e}')
finally:
    driver.quit()
