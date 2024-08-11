import sys
import time
import subprocess

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from test_add_new_user import AddUser
from test_api import GetRequest
from test_login import LoginHRM
from test_user_management_search import SearchForUser

file_name = f"Test_Result_{str(time.asctime()).replace(' ', '_').replace(':', '-')}"




def install_package(package_name):
    """Install a Python package using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package_name}: {e}")

def check_and_install_packages():
    """Check for required packages and install them if not present."""
    try:
        import selenium
    except ImportError:
        print("Selenium not found. Installing...")
        install_package('selenium')

    try:
        import chromedriver_autoinstaller
    except ImportError:
        print("chromedriver-autoinstaller not found. Installing...")
        install_package('chromedriver-autoinstaller')



class ExcecuteTestCases:
    def __init__(self):
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)


        print("::::::::::::  Test Scenario 1: User Login - is in Progress...  ::::::::::::::::::::")
        PrintResult("::::::::::::  Test Scenario 1: User Login - is in Progress...  ::::::::::::::::::::")
        LoginHRM(self.driver) #Login
        time.sleep(2)

        print("::::::::::::  Test Scenario 2: User Management Search - is in Progress...  ::::::::::::::::::::")
        PrintResult("::::::::::::  Test Scenario 2: User Management Search - is in Progress...  ::::::::::::::::::::")
        SearchForUser(self.driver) #Search
        time.sleep(2)

        print("::::::::::::  Test Scenario 3: Add to new user - is in Progress...  ::::::::::::::::::::")
        PrintResult("::::::::::::  Test Scenario 3: Add to new user - is in Progress...  ::::::::::::::::::::")
        AddUser(self.driver)  # Add User
        time.sleep(2)

        print("::::::::::::  Test Scenario 4: API Testing - is in Progress...  ::::::::::::::::::::")
        PrintResult("::::::::::::  Test Scenario 4: API Testing - is in Progress...  ::::::::::::::::::::")
        GetRequest(self.driver) #API

        print(":::::::::: All TestCases Executed Successfully... :::::::::::::::::")
        PrintResult(":::::::::: All TestCases Executed Successfully... :::::::::::::::::")

class PrintResult:
    def __init__(self, data):
        self.set_file_name()
        self.write_result_data(data)

    def write_result_data(self, data):
        with open(f"TestResult\{file_name}.txt", "a") as file:
            file.write(f"{data} \n")


class GetElementByCSS:
    def __init__(self, driver, class_name, text=""):
        self.driver = driver
        self.element = self.get_element(class_name, text)
        self.result_Data = ""
    def get_element(self, class_name, text=""):
        if class_name and text:
            element_list = self.driver.find_elements(By.XPATH,
                                               f"//*[contains(@class, '{class_name}') ]")
            element = None
            for elm in element_list:
                if text in elm.text:
                    element = elm
                    break
        if not text:
            element = self.driver.find_element(By.XPATH,
                f"//*[contains(@class, '{class_name}') ]")
        return element


if __name__ == '__main__':
    check_and_install_packages()
    ExcecuteTestCases()