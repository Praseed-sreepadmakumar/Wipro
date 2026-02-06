import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ===============================
# CONFIG
# ===============================
BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
VALID_USER = "Admin"
VALID_PASS = "admin123"

# ===============================
# DRIVER FACTORY
# ===============================
def get_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver

# ===============================
# BASE PAGE (Reusable)
# ===============================
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

# ===============================
# LOGIN PAGE OBJECT
# ===============================
class LoginPage(BasePage):

    # Locators
    username_field = (By.CSS_SELECTOR, "input[name='username']")
    password_field = (By.CSS_SELECTOR, "input[name='password']")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    error_message = (By.CSS_SELECTOR, ".oxd-alert-content-text")

    # Actions
    def open(self):
        self.driver.get(BASE_URL)

    def login(self, user, pwd):
        self.enter_text(self.username_field, user)
        self.enter_text(self.password_field, pwd)
        self.click(self.login_button)

    def get_error(self):
        return self.get_text(self.error_message)

# ===============================
# DASHBOARD PAGE OBJECT
# ===============================
class DashboardPage(BasePage):
    # Locator for an element on successful login (e.g., breadcrumb title)
    dashboard_title = (By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb h6")

    def is_displayed(self):
        return "dashboard" in self.wait.until(EC.visibility_of_element_located(self.dashboard_title)).text.lower()

# ===============================
# TEST CASES (pytest)
# ===============================
def test_valid_login():
    driver = get_driver()
    login_page = LoginPage(driver)
    login_page.open()

    login_page.login(VALID_USER, VALID_PASS)

    dashboard = DashboardPage(driver)
    assert dashboard.is_displayed(), "Dashboard did not appear – login might have failed"
    print("Login was successful and dashboard is displayed.")
    driver.quit()

def test_invalid_login():
    driver = get_driver()
    login_page = LoginPage(driver)
    login_page.open()

    login_page.login("wrongUser", "wrongPass")
    err = login_page.get_error()
    print("Error displayed:", err)

    assert "invalid" in err.lower(), "Expected invalid credentials error"
    driver.quit()
