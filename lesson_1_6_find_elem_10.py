#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from selenium import webdriver
import time

try:
    # ссылка на сайт с успешной регистрацией
    link = "http://suninjuly.github.io/registration1.html"

    # ссылка на сайт с ошибкой при регистрации
    # link = "http://suninjuly.github.io/registration2.html"
    
    browser = webdriver.Firefox()
    # ~ browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector("body > div.container > form > div.first_block > div.form-group.first_class > input")
    input1.send_keys("Viktor")
    input2 = browser.find_element_by_css_selector("body > div.container > form > div.first_block > div.form-group.second_class > input")
    input2.send_keys("Kucherov")
    input3 = browser.find_element_by_css_selector("body > div.container > form > div.first_block > div.form-group.third_class > input")
    input3.send_keys("mail@mail.ru")

    
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


# ~ except Exception as error:
    # ~ print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()# не забываем оставить пустую строку в конце файла
