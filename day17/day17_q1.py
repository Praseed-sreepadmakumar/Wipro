from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# 1. Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# 2. Open Register page
driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")

# 3. Fill text boxes
driver.find_element(By.ID, "input-firstname").send_keys("Praseed")
driver.find_element(By.ID, "input-lastname").send_keys("Sreepadmakumar")
driver.find_element(By.ID, "input-email").send_keys("praseed123@test.com")
driver.find_element(By.ID, "input-telephone").send_keys("9876543210")
driver.find_element(By.ID, "input-password").send_keys("Test@123")
driver.find_element(By.ID, "input-confirm").send_keys("Test@123")

# 4. Select radio button (Yes for Newsletter)
driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']").click()

# 5. Select checkbox (Privacy Policy)
driver.find_element(By.NAME, "agree").click()

# 7. Submit the form
driver.find_element(By.XPATH, "//input[@value='Continue']").click()

# 8. Verify confirmation message
confirmation_text = driver.find_element(By.TAG_NAME, "h1").text

if "Your Account Has Been Created!" in confirmation_text:
    print("Test Passed: Account created successfully")
else:
    print("Test Failed")

# 9. Close browser
time.sleep(3)
driver.quit()
