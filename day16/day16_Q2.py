from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Open browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 2: Navigate to TutorialsNinja demo site
driver.get("https://tutorialsninja.com/demo/")
time.sleep(2)
print("Home Page Title:", driver.title)

# Step 3: Navigate to another page on the same site (Login page)
my_account = driver.find_element(By.LINK_TEXT, "My Account")
my_account.click()

login = driver.find_element(By.LINK_TEXT, "Login")
login.click()
time.sleep(2)
print("Login Page Title:", driver.title)

# Step 4: Browser navigation actions

# Back
driver.back()
time.sleep(2)
print("After Back - Page Title:", driver.title)

# Forward
driver.forward()
time.sleep(2)
print("After Forward - Page Title:", driver.title)

# Refresh
driver.refresh()
time.sleep(2)
print("After Refresh - Page Title:", driver.title)

# Step 5: Close browser
driver.quit()
