#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
# ~ import os
# ~ from selenium.webdriver.support.ui import Select

"""
title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100,
используйте метод text_to_be_present_in_element из библиотеки expected_conditions.


"""
link = "http://suninjuly.github.io/explicit_wait2.html"
    
try:
    
    browser = webdriver.Firefox()
    browser.get(link)
 
    # говорим Selenium проверять в течение 15 секунд, пока цена не станет равной $100
    price = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"),'$100')
        )
    # жмем кнопку
    button = browser.find_element_by_id('book')
    button.click()

    # ждем 1 сек
    # ~ time.sleep(1)

    # скроллим страницу вниз
    browser.execute_script("window.scrollBy(0, 300);")


    # функцию calc(), которая рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле.
    def calc(x):
        y = str(math.log(abs(12*math.sin(int(x)))))
        return y
    
    # использовать атрибут .text для найденного элемента.
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    # ввод значения y
    input_y = browser.find_element_by_id("answer")
    input_y.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_id('solve')
    # ~ button = WebDriverWait(browser, 5).until(
        # ~ EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-default"))
    # ~ )
    button.click()

   
    
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
    
finally:
    # успеваем скопировать код за 20 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

