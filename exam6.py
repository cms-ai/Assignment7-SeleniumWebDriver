#Print Page source.
from selenium import webdriver
import time
chrome_driver_path = "C:\Development\chromedriver.exe"

driver= webdriver.Chrome(chrome_driver_path)
driver.get("http://practice.automationtesting.in/")
driver.set_window_size(1300, 700)

sourse_page = driver.page_source

print(sourse_page)

time.sleep(5)

driver.close()