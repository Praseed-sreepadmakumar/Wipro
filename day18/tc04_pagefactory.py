from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions

from day18.login_pagefactory import loginpage_PageFactory

driver=webdriver.Chrome()
driver.implicitly_wait(10)
wait=WebDriverWait(driver,10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
#time.sleep(5)
loginobj=loginpage_PageFactory(driver)

loginobj.enterusername("Admin")
loginobj.enterpassword("admin123")

loginobj.clicklogin()

