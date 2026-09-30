from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    alert1 = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
    alert1.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    def calc(x):
        return str(math.log(abs(12 * math.sin(float(x)))))

    x_element = browser.find_element(
        By.XPATH, "/html/body/form/div/div/div/label/span[2]"
    )
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
