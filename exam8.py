# Login Form
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



chrome_driver_path = "C:\Development\chromedriver.exe"
driver= webdriver.Chrome(chrome_driver_path)
driver.get("https://the-internet.herokuapp.com")

form_auth = driver.find_element_by_xpath("//a[contains(text(),'Form Authentication')]")
form_auth.click()

user_input = driver.find_element_by_id("username")
user_input.send_keys("tomsmith")

time.sleep(5)

pass_input =  driver.find_element_by_id("password")
pass_input.send_keys("SuperSecretPassword!")
time.sleep(5)

login_btn = driver.find_element_by_xpath("//form[@id='login']/button/i").click()


driver.close()