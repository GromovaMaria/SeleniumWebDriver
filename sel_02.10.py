import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')
user_name.send_keys('standard_user')

password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys('secret_sauce')

login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
login_button.click()

shop = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
shop.click()

time.sleep(2)
basket = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
basket.click()

checkout = driver.find_element(By.XPATH, '//*[@id="checkout"]')
checkout.click()

firstname = driver.find_element(By.XPATH, '//*[@id="first-name"]')
firstname.send_keys('Gala')

lastname = driver.find_element(By.XPATH, '//*[@id="last-name"]')
lastname.send_keys('print')

postalCode = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
postalCode.send_keys('123')

time.sleep(2)
continue1 = driver.find_element(By.XPATH, '//*[@id="continue"]')
continue1.click()

time.sleep(5)
driver.close()
