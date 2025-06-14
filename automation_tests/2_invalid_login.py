from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
driver.implicitly_wait(20)

# 2 - Invalid login // login with invalid credentials and ensure a warning is present in the page
username_input = driver.find_element(By.ID, 'user-name')
password_input = driver.find_element(By.ID, 'password')
login_btn = driver.find_element(By.ID, 'login-button')

username_input.send_keys('abc')
password_input.send_keys('abc')
login_btn.click()

error_message = driver.find_element(By.XPATH, "//div[@class='error-message-container error']")

assert error_message.is_displayed(), "Error message is not displayed for invalid login"

driver.quit()
