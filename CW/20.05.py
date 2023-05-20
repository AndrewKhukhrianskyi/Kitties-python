from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

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

