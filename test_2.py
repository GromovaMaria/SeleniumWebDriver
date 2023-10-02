import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'

driver.get(base_url)
driver.maximize_window()

login_standard_user = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')
user_name.send_keys(login_standard_user)
print("Input Login")
password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys('secret_sauce')
print("Input Password")
button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]')
button_login.click()
print("Click Login Button")

warring_text = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
value_warring_text = warring_text.text

assert value_warring_text == 'Epic sadface: Username and password do not match any user in this service'
print('Good test')
time.sleep(3)
driver.refresh()

time.sleep(50)
driver.close()


