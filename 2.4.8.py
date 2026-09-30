from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    findbutton = browser.find_element(By.ID, "book")
    price = browser.find_element(By.ID, "price")
    price_element = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    findbutton.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(float(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    result = browser.find_element(By.ID, "answer")
    result.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.ID, "solve")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
