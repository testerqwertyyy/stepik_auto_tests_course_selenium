from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1_text = browser.find_element(By.ID, "num1").text
    num2_text = browser.find_element(By.ID, "num2").text

    sum = int(num1_text) + int(num2_text)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(sum))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
   
    time.sleep(10)
   
    browser.quit()


