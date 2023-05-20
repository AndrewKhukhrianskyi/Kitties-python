from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest

'''
browser = webdriver.Chrome() # Устанавливаем драйвер

browser.get('https://clickclickclick.click')# открываем сайт по ссылке


# find_element выполняет поиск элемента на странице сайта
button = browser.find_element(by = By.CLASS_NAME,
                              value='button')
assert button.is_displayed() # True если кнопка есть False если нет
for clicker in range(100):
    button.click() # click тыкает на элемент

sleep(20)
browser.close()# close закрывает сайт

button = browser.find_element(by = By.CLASS_NAME,
                              value='button')
button.click()
achivements = browser.find_element(by = By.ID,
                            value = "achievements")
if achivements.is_displayed():
    print('Все ок!')
else:
    print('Not good!')
'''

@pytest.fixture
def open_browser():
    browser = webdriver.Chrome() # Устанавливаем драйвер
    browser.get('https://clickclickclick.click')# открываем сайт по ссылке
    # .current_url - это ссылка на сайт
    assert 'https://clickclickclick.click' in browser.current_url
    yield browser
    browser.close()

def test_check_button(open_browser):
    browser = open_browser
    button = browser.find_element(by = By.CLASS_NAME,
                                  value='button')
    assert button.is_displayed

'''
1. Почитать о Selenium:
https://www.youtube.com/watch?v=Myl8Br5aRf4&list=PLqGS6O1-DZLp1kgiQNpueIMCHRNzgHa1r
Части 0-1
2. Написать программу, которая будет открывать сайт и проверять, что пользователь на нем
Site: Google.com
3. Почитать о конструкции By в селениуме
4. Переформатировать задачу 2 в тест.
'''
