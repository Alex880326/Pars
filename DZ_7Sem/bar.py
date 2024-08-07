from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import csv


def scroll_to_bottom(driver):
    """Прокрутка страницы до самого конца."""
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Прокручиваем вниз
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Ждем, пока загрузится новая часть страницы
        time.sleep(2)
        try:
            next_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Показать еще')]")  # Замените текст на нужный
            next_button.click()
            time.sleep(2)  # Подождем немного, чтобы страница загрузилась
        except Exception as e:
            print("Больше страниц нет или произошла ошибка:", e)
            break
        # Получаем новую высоту
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        # Проверяем, достигли ли мы конца страницы
        if new_height == last_height:
            break  # Выходим из цикла, если высота не изменилась
        last_height = new_height


def main():
    """Основная функция."""
    user_agent = (
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    )
    url = 'https://byruthub.org/action/'
    chrome_option = Options()
    chrome_option.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(options=chrome_option)

    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        time.sleep(5)

        scroll_to_bottom(driver)

        # data = get_video_data(driver)

        # save_to_json(data)
        # save_to_csv(data)

    except Exception as er:
        print(f'Error: {er}')
    finally:
        driver.quit()


if __name__ == '__main__':
    main()