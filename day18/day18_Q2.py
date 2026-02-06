from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/iframe")
time.sleep(2)

# Switch to iframe
driver.switch_to.frame("mce_0_ifr")

# Locate TinyMCE editor
text_box = driver.find_element(By.ID, "tinymce")

# Click first (important!)
text_box.click()

# Send text (NO clear())
text_box.send_keys("Hello! This text is entered inside an iframe.")

time.sleep(2)

# Switch back to main page
driver.switch_to.default_content()
print("Switched back to main page")

driver.quit()
