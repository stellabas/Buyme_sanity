from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

#loging in:
driver = webdriver.Chrome(executable_path="/Users/stella/Documents/chromedriver")
driver.get("https://buyme.co.il/?modal=login")
driver.find_element_by_xpath("//input[@data-parsley-type='email']").send_keys("basovsky@walla.com")
driver.find_element_by_xpath("//input[@placeholder='סיסמה']").send_keys("12345678Bb")
driver.find_element_by_xpath("//button[@class='ui-btn orange large']").click()

#select  a price of till 200-299
#time.sleep(10)
time.sleep(1)
driver.find_element_by_class_name('chosen-single').click()
driver.find_element_by_xpath("//li[@data-option-array-index='3']").click()

#select an area
driver.find_element_by_xpath(".//span[contains(text(),'אזור')]").click()
driver.find_element_by_xpath("//div[@id='ember679_chosen']//span").click()

print()

#select a category
#select a search point