from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# =========================================
# VARIABLES (DEFINED FIRST)
# =========================================
url = "https://tutorialsninja.com/demo/"
wait_time = 2

valid_first_name = "Praseed"
valid_last_name = "Sreepad"
email = f"test{int(time.time())}@mail.com"
telephone = "9876543210"

address_1 = "Test Address Line 1"
city = "Bangalore"
postcode = "560001"

password = "test1234"

# =========================================
# PART 1: Launch Application
# =========================================
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(wait_time)

# Verify page title
assert driver.title == "Your Store"
print("Page title verified")

# My Account → Register
driver.find_element(By.XPATH, "//span[text()='My Account']").click()
driver.find_element(By.LINK_TEXT, "Register").click()
time.sleep(wait_time)


# Verify Register page using URL + form element
assert "route=account/register" in driver.current_url
assert driver.find_element(By.ID, "input-firstname").is_displayed()
print("Register Account page opened")

# Click Continue without agreeing Privacy Policy
driver.find_element(By.XPATH, "//input[@value='Continue']").click()
time.sleep(wait_time)

# Verify warning message
warning_msg = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
assert "Warning: You must agree to the Privacy Policy!" in warning_msg
print("Privacy policy warning validated")

# =========================================
# PART 2: Your Personal Details
# =========================================
first_name_field = driver.find_element(By.ID, "input-firstname")
last_name_field = driver.find_element(By.ID, "input-lastname")

# First Name length validation (33 chars)
first_name_field.send_keys("A" * 33)
driver.find_element(By.XPATH, "//input[@value='Continue']").click()
time.sleep(wait_time)

assert driver.find_elements(By.ID, "error-firstname")
print("First Name length validation passed")

first_name_field.clear()
first_name_field.send_keys(valid_first_name)

# Last Name length validation (33 chars)
last_name_field.send_keys("B" * 33)
driver.find_element(By.XPATH, "//input[@value='Continue']").click()
time.sleep(wait_time)

assert driver.find_elements(By.ID, "error-lastname")
print("Last Name length validation passed")

last_name_field.clear()
last_name_field.send_keys(valid_last_name)

# Email & Telephone
driver.find_element(By.ID, "input-email").send_keys(email)
driver.find_element(By.ID, "input-telephone").send_keys(telephone)

# =========================================
# PART 3: Your Address
# =========================================
driver.find_element(By.ID, "input-address-1").send_keys(address_1)
driver.find_element(By.ID, "input-city").send_keys(city)
driver.find_element(By.ID, "input-postcode").send_keys(postcode)

Select(driver.find_element(By.ID, "input-country")).select_by_visible_text("India")
time.sleep(wait_time)
Select(driver.find_element(By.ID, "input-zone")).select_by_index(1)

# =========================================
# PART 4: Password
# =========================================
driver.find_element(By.ID, "input-password").send_keys(password)
driver.find_element(By.ID, "input-confirm").send_keys(password)

# =========================================
# PART 5: Newsletter & Submit
# =========================================
driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']").click()
driver.find_element(By.NAME, "agree").click()
driver.find_element(By.XPATH, "//input[@value='Continue']").click()
time.sleep(wait_time)

# Verify success message
success_heading = driver.find_element(By.TAG_NAME, "h1").text
assert "Your Account Has Been Created!" in success_heading
print("Account successfully created")

# Continue to My Account
driver.find_element(By.LINK_TEXT, "Continue").click()
time.sleep(wait_time)

# View Order History
driver.find_element(By.LINK_TEXT, "View your order history").click()
print("Order history page opened")

# =========================================
# CLOSE BROWSER
# =========================================
time.sleep(3)
driver.quit()
