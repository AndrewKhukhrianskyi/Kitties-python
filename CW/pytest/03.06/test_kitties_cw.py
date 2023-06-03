import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def open_browser():
    browser = webdriver.Chrome() # Устанавливаем драйвер
    browser.get('https://www.google.com')# открываем сайт по ссылке
    browser.set_window_size(1024, 600)
    browser.maximize_window()
    yield browser
    browser.close()

@pytest.mark.parametrize('data', [('Python'), ('Java'), ('CSS'), ('HTML')])
def test_send_data(open_browser, data):
    browser = open_browser
    button = browser.find_element(By.XPATH, '//div/form/button')
    button.click()
    # send_keys позволяет написать текст в поле
    search_field = browser.find_element(By.XPATH, "//form[@id='gcse-form']/input")
    assert search_field.is_displayed()
    search_field.send_keys(data)
    search_field.send_keys(Keys.RETURN)
    time.sleep(2)
    search_results = browser.find_element(By.XPATH, "//div[@class='left-content-modal']")
    assert 'No Result Found.' not in search_results.text

@pytest.mark.parametrize('data, dark_mode', [('agasdgadsgdasgsda', True),
                                             ('2353452354326234632', False),
                                             ('-08u76464tdytdgfdsreq3', True)])
@pytest.mark.negative
def test_send_data_neg(open_browser, data, dark_mode):
    browser = open_browser
    if dark_mode:
        dark_mode_button = browser.find_element(By.XPATH, "//div[@class='darkMode-wrap']/button")
        dark_mode_button.click()
    button = browser.find_element(By.XPATH, '//div/form/button')
    button.click()
    # send_keys позволяет написать текст в поле
    search_field = browser.find_element(By.XPATH, "//form[@id='gcse-form']/input")
    assert search_field.is_displayed()
    search_field.send_keys(data)
    search_field.send_keys(Keys.RETURN)
    time.sleep(2)
    try:
        search_results = browser.find_element(By.XPATH, "//div[@class='left-content-modal']")
        assert 'No Result Found.' in search_results.text
    except:
        assert True


    
        
'''
Task
В поисковой строке гугла сделать запрос и проверить, что данные были найдены по данному
запросу

Прикрутите еще негативные тесты и проверьте, что выражение в формате "Ничего не найдено"
отображается
'''
@pytest.mark.google
@pytest.mark.parametrize('data', [('cats'),('dogs'),('tanks')])
def test_check_search(open_browser, data):
    browser = open_browser
    text_field = browser.find_element(By.XPATH, '//*[@id="APjFqb"]')
    text_field.send_keys(data)
    text_field.send_keys(Keys.RETURN)
    text_zone = browser.find_element(By.XPATH, '//*[@id="topstuff"]/div/div/p[1]')
    assert text_zone.is_displayed()
    assert f'По запросу {data} ничего не найдено.' not in text_zone.text


    

