# Selenium Waits Demonstration Script
# Requirements:
# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

# -------------------------------
# Setup WebDriver
# -------------------------------
driver = webdriver.Chrome()

# -------------------------------
# 1. IMPLICIT WAIT
# -------------------------------
# Applies globally for all element searches
driver.implicitly_wait(10)

print("Implicit wait set to 10 seconds")

# Open demo site
driver.get("https://the-internet.herokuapp.com/dynamic_controls")

# Try locating element (implicit wait will apply)
checkbox = driver.find_element(By.CSS_SELECTOR, "#checkbox input")
print("Element located using implicit wait")

# -------------------------------
# 2. EXPLICIT WAIT (Clickable)
# -------------------------------
wait = WebDriverWait(driver, 15)

# Click Remove button
remove_btn = driver.find_element(By.XPATH, "//button[text()='Remove']")
remove_btn.click()

print("Waiting for Add button to become clickable (Explicit Wait)...")

add_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Add']"))
)

print("Explicit Wait: Add button is clickable now!")

# -------------------------------
# 3. FLUENT WAIT (Polling)
# -------------------------------
print("Starting Fluent Wait (Polling every 2 seconds)...")

fluent_wait = WebDriverWait(
    driver,
    timeout=20,
    poll_frequency=2,   # Poll every 2 seconds
    ignored_exceptions=[NoSuchElementException]
)

message = fluent_wait.until(
    EC.visibility_of_element_located((By.ID, "message"))
)

print("Fluent Wait: Message is visible ->", message.text)

# -------------------------------
# 4. Interaction Confirmation
# -------------------------------
if add_btn.is_enabled():
    print("Element is available for interaction")

# -------------------------------
# Cleanup
# -------------------------------
time.sleep(3)
driver.quit()
