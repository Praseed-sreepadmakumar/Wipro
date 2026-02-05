from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# 2. Open alerts test page
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# -----------------------------
# ALERT BOX
# -----------------------------
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

alert = driver.switch_to.alert
print("Alert Message:", alert.text)
alert.accept()

# Verify result
result = driver.find_element(By.ID, "result").text
print("Result:", result)

# -----------------------------
# CONFIRMATION BOX
# -----------------------------
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()

confirm_alert = driver.switch_to.alert
print("Confirm Message:", confirm_alert.text)
confirm_alert.dismiss()

# Verify result
result = driver.find_element(By.ID, "result").text
print("Result:", result)

# -----------------------------
# PROMPT BOX
# -----------------------------
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()

prompt_alert = driver.switch_to.alert
print("Prompt Message:", prompt_alert.text)

prompt_alert.send_keys("Selenium Test")
prompt_alert.accept()

# Verify result
result = driver.find_element(By.ID, "result").text
print("Result:", result)

# -----------------------------
# Close browser
# -----------------------------
time.sleep(3)
driver.quit()
