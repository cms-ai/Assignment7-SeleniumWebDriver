#- Maximize browser window
from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"

driver= webdriver.Chrome(chrome_driver_path)
driver.maximize_window()

driver.get("http://practice.automationtesting.in/")
driver.close()