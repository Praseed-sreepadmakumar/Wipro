from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 2: Open the website
driver.get("https://tutorialsninja.com/demo/")
time.sleep(2)

# Step 3: Click "My Account" (Using Class Name)
driver.find_element(By.CLASS_NAME, "dropdown-toggle").click()
time.sleep(1)

# Step 4: Click Login (Using XPath)
driver.find_element(By.XPATH, "//a[text()='Login']").click()
time.sleep(2)

# Step 5: Enter Email (Using ID)
driver.find_element(By.ID, "input-email").send_keys("invalid@email.com")

# Step 6: Enter Password (Using Name)
driver.find_element(By.NAME, "password").send_keys("wrongpassword")

# Step 7: Click Login button (Using CSS Selector)
driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
time.sleep(2)

# Step 8: Validate warning message (Using XPath)
warning_message = driver.find_element(
    By.XPATH, "//div[contains(@class,'alert-danger')]"
).text

print("Displayed Message:", warning_message)

assert "Warning: No match for E-Mail Address and/or Password." in warning_message
print("✅ Validation Successful")

# Step 9: Close browser
driver.quit()
