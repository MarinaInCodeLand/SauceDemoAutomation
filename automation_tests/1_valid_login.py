from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
driver.implicitly_wait(20)

# 1 - Valid login // login and ensure the cart icon is displayed
username_input = driver.find_element(By.ID, 'user-name')
password_input = driver.find_element(By.ID, 'password')
login_btn = driver.find_element(By.ID, 'login-button')
username_input.send_keys('standard_user')
password_input.send_keys('secret_sauce')
login_btn.click()

cart_icon = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')

# assert
assert cart_icon.is_displayed(), "Cart icon is NOT displayed after login"

driver.quit()  
