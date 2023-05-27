import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


'''
By.
1. LINK_TEXT
2. LINK
3. CLASS
4. ID
5. XPATH

Example:
By.CLASS
'''

@pytest.fixture
def open_browser():
    browser = webdriver.Chrome() # Устанавливаем драйвер
    browser.get('https://theuselessweb.com/')# открываем сайт по ссылке
    browser.set_window_size(1024, 600)
    browser.maximize_window()
    yield browser
    browser.close()

# find_element ищет элемент на веб-сайте
# click тыкает на элемент
'''
def test_check_deutsch(open_browser):
    browser = open_browser
    time.sleep(3)
    action = webdriver.ActionChains(browser)
    language_button = browser.find_element(By.XPATH, '//li/button')
    
    action.move_to_element(language_button)
    
    language_list_element = browser.find_element(By.XPATH, "//ul[@id='language-dropdown-submenu']/li[2]")
    language_list_element.click()
    
    time.sleep(2)
    assert browser.current_url in 'https://blog.hubspot.de/?hubs_content=blog.hubspot.com%2F&hubs_content-cta=null'
'''
@pytest.mark.metka
def test_main_page(open_browser):
    browser = open_browser
    time.sleep(3)
    main_button = browser.find_element(By.CLASS_NAME, '-desktop')
    main_button.click()
    assert 'https://blog.hubspot.com' in browser.current_url
    
@pytest.mark.metka2
def test_not_on_page(open_browser):
    browser = open_browser
    button = browser.find_element(By.ID, 'button')
    button.click()
    assert 'https://theuselessweb.com/' not in browser.current_url
    
'''
1. Почитать о селениуме и конструкции By
https://selenium-python.readthedocs.io/locating-elements.html
2. Написать программу, которая будет открывать ссылку сайта

3. Модифицировать программу 2, написав тест, который будет это проверять
4. Освежить в памяти XPATH: https://ru.wikipedia.org/wiki/XPath
5.(*) Пофиксить код теста test_not_in_page
'''

    

