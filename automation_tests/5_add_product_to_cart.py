from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
driver.implicitly_wait(20)

# 5 - Add product to cart // add a product to the cart and ensure it's there
username_input = driver.find_element(By.ID, 'user-name')
password_input = driver.find_element(By.ID, 'password')
login_btn = driver.find_element(By.ID, 'login-button')
username_input.send_keys('standard_user')
password_input.send_keys('secret_sauce')
login_btn.click()
add_cart_btn = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
add_cart_btn.click()
cart_icon = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
cart_icon.click()
remove_cart_btn = driver.find_element(By.ID, 'remove-sauce-labs-backpack')
remove_cart_btn.is_displayed()