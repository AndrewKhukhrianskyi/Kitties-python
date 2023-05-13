from webdriver_manager.chrome import ChromeDriverManager
from selenium import *
from selenium import webdriver

from time import sleep
browser = webdriver.Chrome()

browser.get('https://www.google.com/')
sleep(5)
browser.quit()

'''
1. Почитать о селениуме
2. Почитать об XPATH + HTML
3. На сайте https://realpython.com/introduction-to-python-generators/
При помощи инспектора найти упоминания о generator
4. Повторите данный пункт с применением XPATH (пункт 3)
'''
