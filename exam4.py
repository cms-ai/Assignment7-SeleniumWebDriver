#Print it's Page title.

from selenium import webdriver
import time
chrome_driver_path = "C:\Development\chromedriver.exe"

driver= webdriver.Chrome(chrome_driver_path)
driver.get("http://practice.automationtesting.in/")

get_title = driver.title

print(get_title)

time.sleep(5)

driver.close()