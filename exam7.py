from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



chrome_driver_path = "C:\Development\chromedriver.exe"
driver= webdriver.Chrome(chrome_driver_path)
driver.get("http://practice.automationtesting.in/")

myaccountbtn =  driver.find_element_by_id("menu-item-50")
myaccountbtn.click()
time.sleep(5)

emailre_input = driver.find_element_by_id("reg_email")
emailre_input.send_keys("tcaiqb@gmail.com")

passre_input = driver.find_element_by_id("reg_password")
time.sleep(5)

passre_input.send_keys("tcaiA_bc123456")

time.sleep(5)

form = driver.find_element_by_name("register").click()

time.sleep(5)

driver.close()