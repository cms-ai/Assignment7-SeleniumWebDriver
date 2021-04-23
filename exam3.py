#Set size of browser window
from selenium import webdriver
import  time

chrome_driver_path = "C:\Development\chromedriver.exe"

driver= webdriver.Chrome(chrome_driver_path)
driver.set_window_size(1300, 700)
driver.get("http://practice.automationtesting.in/")

time.sleep(5)

driver.close()