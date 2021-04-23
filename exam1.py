#– Open http://practice.automationtesting.in/

from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"

driver= webdriver.Chrome(chrome_driver_path)

driver.get("http://practice.automationtesting.in/")

driver.close()