from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


driver = webdriver.Chrome(executable_path="/Users/stella/Documents/chromedriver")
driver.get("https://buyme.co.il")
time.sleep(3)
driver.maximize_window()
time.sleep(2)

#knisa/harshama
driver.find_element_by_class_name("seperator-link").click()

#leharshama
driver.find_element_by_xpath("//span[@class='text-btn']").click()
#harshama
driver.find_element_by_xpath("//input[@placeholder='שם פרטי']").send_keys("dudu")
driver.find_element_by_xpath("//input[@placeholder='מייל']").send_keys("sus@walla.com")
driver.find_element_by_xpath("//input[@placeholder='סיסמה']").send_keys("12345678Aa")
driver.find_element_by_xpath("//input[@placeholder='אימות סיסמה']").send_keys("12345678Aa")
driver.execute_script("arguments[0].click();",driver.find_element_by_class_name("fa-check"))
driver.find_element_by_xpath("//button[@class='ui-btn orange large']").click()





