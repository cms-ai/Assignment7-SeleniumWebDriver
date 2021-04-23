# Login Form
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver= webdriver.Chrome(chrome_driver_path)
driver.get("https://itmscoaching.herokuapp.com/form")

firstName = driver.find_element_by_id("first-name").send_keys("Binh")
time.sleep(2)

lastName = driver.find_element_by_id("last-name").send_keys("Nguyen")
time.sleep(2)

jobTitle = driver.find_element_by_id("job-title").send_keys("Tester")
time.sleep(2)

highLevel = driver.find_element_by_id("radio-button-3").click()
time.sleep(2)
gender = driver.find_element_by_id("checkbox-2").click()
time.sleep(2)

yearExp = driver.find_element_by_css_selector("#select-menu [value='3']").click()
time.sleep(2)

date =  driver.find_element_by_id("datepicker")
date.click()
date.send_keys("07/20/2011")
time.sleep(2)
submit_btn = driver.find_element_by_xpath("//a[contains(@href, '/thanks')]")
submit_btn.click()



# driver.close()