from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    findbutton = browser.find_element(By.CSS_SELECTOR, "button.btn")
    findbutton.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    def calc(x):
        return str(math.log(abs(12 * math.sin(float(x)))))

    x_element = browser.find_element(By.ID, "input_value")

    x = x_element.text
    y = calc(x)
    result = browser.find_element(By.ID, "answer")
    result.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
