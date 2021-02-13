from selenium import webdriver
from selenium.webdriver.common.by import By
#from sys import argv
import time
#link = argv
link= "http://suninjuly.github.io/registration1.html"

#лажа полная, можно не проверять

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, "form-control.first.input:required")
    input1.send_keys("New")
    input2 = browser.find_element(By.CSS_SELECTOR, "input:required")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "input:required")
    input3.send_keys("Smolensk")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()