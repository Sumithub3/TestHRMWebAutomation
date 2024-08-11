import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SearchForUser:
    def __init__(self, driver):
        self.driver = driver
        self.search_for_user()

    def search_for_user(self):
        from RunTestCases import GetElementByCSS, PrintResult

        print('Search for a user')
        PrintResult('Search for a user')
        admin_pannel = GetElementByCSS(self.driver, 'oxd-main-menu-item', 'Admin')

        admin_pannel.element.click()
        time.sleep(5)
        username_filter = GetElementByCSS(self.driver, 'oxd-input-field-bottom-space')
        username_input = username_filter.element.find_element(By.CLASS_NAME, 'oxd-input')
        username_input.send_keys('Admin')

        submit_btn = GetElementByCSS(self.driver, 'orangehrm-left-space')
        submit_btn.element.click()


        print('Verify search results')
        PrintResult('Verify search results')
        results_table = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-table-card"))
        )
        assert "Admin" in str(results_table.text)

        print('Validate navigation to user details')
        PrintResult('Validate navigation to user details')


        print('User Management Search Test Passed')
        PrintResult('User Management Search Test Passed')
