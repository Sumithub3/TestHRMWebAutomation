import requests



class GetRequest:
    def __init__(self, driver):
        self.driver = driver
        self.api_data = self.get_api_result()
        # self.print_data()
    def get_api_result(self):
        from RunTestCases import PrintResult


        url = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/users?limit=50&offset=0&sortField=u.userName&sortOrder=ASC"

        session = requests.Session()

        for cookie in self.driver.get_cookies():
            session.cookies.set(cookie['name'], cookie['value'])

        PrintResult("Sending request to the API endpoint")
        response = session.get(url)

        assert response.status_code == 200
        print("API Status Code Test Passed...")
        PrintResult("API Status Code Test Passed...")

        response_json = response.json()
        required_keys = {"userName", "userRole", "status"}
        assert all(key in response_json['data'][0] for key in required_keys)
        print("API Response Structure Test Passed")
        PrintResult("API Response Structure Test Passed")

        print("API Data Validation Passed")
        PrintResult("API Data Validation Passed")
        return response_json
    def print_data(self):
        print(self.api_data)
