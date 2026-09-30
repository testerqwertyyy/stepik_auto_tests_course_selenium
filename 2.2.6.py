import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"

# 1. Подготовка абсолютного пути к файлу
# Selenium требует именно АБСОЛЮТНЫЙ путь к файлу, относительный не сработает.
# Этот код создает путь к файлу test.txt в той же папке, где лежит ваш скрипт.
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "test.txt")

# (Опционально) Создадим этот файл автоматически, если его еще нет, чтобы код точно сработал
if not os.path.exists(file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Это тестовый файл для загрузки через Selenium.")

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 2. Заполнение текстовых полей
    # Внимание: в HTML-коде этой страницы у полей нет атрибута id, есть атрибут name.
    # Поэтому надежнее искать их по имени (By.NAME) или через CSS-селектор.
    firstname = browser.find_element(By.NAME, "firstname")
    firstname.send_keys("Тест")

    lastname = browser.find_element(By.NAME, "lastname")
    lastname.send_keys("Тест")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("test@example.com")

    # 3. Загрузка файла
    # Находим элемент input с типом file (у него есть id="file")
    file_input = browser.find_element(By.ID, "file")
    
    # Магия Selenium: чтобы загрузить файл, не нужно кликать на кнопку "Обзор".
    # Достаточно отправить абсолютный путь к файлу как обычный текст!
    file_input.send_keys(file_path)

    # 4. Отправка формы
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Пауза, чтобы увидеть сообщение об успешной отправке
    time.sleep(5)

finally:
    # Гарантированное закрытие браузера
    browser.quit()