from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/execute_script.html')
    browser.maximize_window()

    x = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")
    answer = browser.find_element(By.XPATH, '//*[@id="answer"]')
    answer.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    robot = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    robot.click()

    radio = browser.find_element(By.XPATH, '//*[@id="robotsRule"]')
    radio.click()

    button = browser.find_element(By.XPATH, '/html/body/div/form/button')
    button.click()

finally:
    time.sleep(5)
    browser.quit()