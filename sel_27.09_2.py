'''Импорт библиотек'''
import time # Импортируем библиотеку time. Для ипользования пауз time.sleep(5)
from selenium import webdriver # Импортируем библиотеку веб-драйвер
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By # Импортируем библиотеку By

driver = webdriver.Chrome()
driver.get('https://stepik.org/catalog')
driver.maximize_window()
time.sleep(5)

login = driver.find_element(By.XPATH, '//*[@id="ember245"]')
login.click()

user_name = driver.find_element(By.XPATH, '//*[@id="id_login_email"]')
user_name.send_keys('emelina-06@mail.ru')

password = driver.find_element(By.XPATH, '//*[@id="id_login_password"]')
password.send_keys('Qwerty0981!')

button = driver.find_element(By.XPATH, '//*[@id="login_form"]/button')
button.click()

time.sleep(5)
driver.close()