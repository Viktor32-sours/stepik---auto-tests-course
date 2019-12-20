import pytest
from selenium import webdriver
import time
import math


# создаем список ссылок
link_list = [
   "https://stepik.org/lesson/236895/step/1",
   "https://stepik.org/lesson/236896/step/1",
   "https://stepik.org/lesson/236897/step/1",
   "https://stepik.org/lesson/236898/step/1",
   "https://stepik.org/lesson/236899/step/1",
   "https://stepik.org/lesson/236903/step/1",
   "https://stepik.org/lesson/236904/step/1",
   "https://stepik.org/lesson/236905/step/1",
]


""" @pytest.mark.parametrize('language', ["ru", "en-gb"])
    def test_guest_should_see_login_link(browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
"""
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    #browser = webdriver.Chrome()
    browser = webdriver.Firefox()  
    yield browser
    print("\nquit browser..")
    browser.quit()
    
    
# @pytest.mark.xfail
@pytest.mark.parametrize('url', link_list)
def test_find_word_on_window(browser, url):
    # ~ browser = webdriver.Firefox()
    # ~ url = 'https://stepik.org/lesson/236895/step/1'
    browser.implicitly_wait(15)
    browser.get(url)

    # вычисления значения
    answer = str(math.log(int(time.time())))
    
    # ~ # поиск области для ввода
    browser.implicitly_wait(15)
    text_area = browser.find_element_by_css_selector(".textarea").send_keys(answer)
    # ~ text_area.send_keys("123")

   
    print(answer)


    # отправка сообщения
    browser.implicitly_wait(15)
    button = browser.find_element_by_css_selector(".submit-submission").click()
    
    # ~ time.sleep(60)
    # проверка корректности сообщения
    browser.implicitly_wait(15)
    elem = browser.find_element_by_css_selector(".smart-hints__hint")

    assert elem.text == "Correct!", f"Некорректный ответ на {url}]"
    
