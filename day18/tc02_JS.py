from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.get("https://www.amazon.in")
#driver.execute_script("alert('Hello Amazon')")
#driver.execute_script("window.ScrollBy(0,900)")
time.sleep(5)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")