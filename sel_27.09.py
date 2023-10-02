'''Импорт библиотек'''
import time # Импортируем библиотеку time. Для ипользования пауз time.sleep(5)
from selenium import webdriver # Импортируем библиотеку веб-драйвер
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By # Импортируем библиотеку By

driver = webdriver.Chrome()
driver.get('https://docs.github.com/ru/get-started/quickstart')
driver.maximize_window()

search = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/header/div[1]/div[2]/div[1]/div/div/form/label/span[2]/input')
search.send_keys('Git')
search.send_keys(Keys.RETURN)

time.sleep(5)
driver.close()