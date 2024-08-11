import time
from selenium.webdriver.common.by import By




class AddUser:
    def __init__(self, driver):
        self.driver = driver
        self.add_user()
    def add_user(self):
        from RunTestCases import GetElementByCSS, PrintResult
        username_filter = GetElementByCSS(self.driver, 'orangehrm-header-container')

        add_user_btn = username_filter.element.find_element(By.CLASS_NAME, 'oxd-button')
        add_user_btn.click()
        print('Navigate to user management and add user')
        PrintResult('Navigate to user management and add user')
        time.sleep(5)
        try:
            "Role"
            user_role = GetElementByCSS(self.driver, 'oxd-select-wrapper')
            user_role.element.click()
            time.sleep(2)
            option_list = self.driver.find_elements(By.CSS_SELECTOR, '.oxd-select-option')
            if len(option_list) == 3:
                option_list[1].click()  #Admin
            print("Role Add Succeed...")
            PrintResult("Role Add Succeed...")


            "USER NAME"
            user_name_input = self.driver.find_element(By.CSS_SELECTOR,
                    'input[placeholder="Type for hints..."]')
            user_name_input.send_keys("Mohit Gaikwad")
            time.sleep(5)
            print("User Name Add succeeed...")
            PrintResult("User Name Add succeeed...")

            "Status"
            user_status = GetElementByCSS(self.driver, 'oxd-input-field-bottom-space', 'Status')
            user_status_input = user_status.element.find_element(By.CLASS_NAME, 'oxd-select-text')
            user_status_input.click()

            option_list = self.driver.find_elements(By.CSS_SELECTOR, '.oxd-select-option')
            option_list[1].click()  # Enable

            print("Status Add Succeed...")
            PrintResult("Status Add Succeed...")

            "USERNAME"
            user_username = GetElementByCSS(self.driver, 'oxd-grid-item', 'Username')
            username = user_username.element.find_element(By.CLASS_NAME, 'oxd-input')
            username.send_keys("Mohit")
            print("Username Add Succeed...")
            PrintResult("Username Add Succeed...")

            "PASSWORD"
            user_password = GetElementByCSS(self.driver, 'oxd-input-group', 'Password')
            password_input = user_password.element.find_element(By.CLASS_NAME, 'oxd-input')
            password_input.send_keys("Qwerty@123")
            print("Password Add Succeeed ... ")
            PrintResult("Password Add Succeeed ... ")


            "CONFIRM PASSWORD"
            user_confirm_password = GetElementByCSS(self.driver, 'oxd-input-group', 'Confirm Password')
            conf_pass = user_confirm_password.element.find_element(By.CLASS_NAME, 'oxd-input')
            conf_pass.send_keys("Qwerty@123")
            print("Confirmed Password Add succeed...")
            PrintResult("Confirmed Password Add succeed...")

            "SUBMIT"
            submit_btn = self.driver.find_element(By.CSS_SELECTOR,
                                        'button[type=submit]')
            submit_btn.click()
            print("Submit Button Clicked...")
            PrintResult("Submit Button Clicked...")

        except Exception as ex:
            print(ex)


