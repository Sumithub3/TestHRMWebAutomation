import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginHRM:
    def __init__(self, driver):
        self.driver = driver
        self.login_HRM()
    def login_HRM(self):
        from RunTestCases import PrintResult

        try:

            self.driver.get("https://opensource-demo.orangehrmlive.com")
            time.sleep(10)
            username = self.driver.find_element(By.NAME, "username")
            password = self.driver.find_element(By.NAME, "password")
            username.send_keys("Admin")
            password.send_keys("admin123")

            self.driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()

            user_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "oxd-topbar-header-breadcrumb-module"))
            )
            time.sleep(5)
            assert "Dashboard" in user_element.text
            print("Login Test Passed...")
            PrintResult("Login Test Passed...")
            time.sleep(5)

        except Exception as ex:
            print(ex)
