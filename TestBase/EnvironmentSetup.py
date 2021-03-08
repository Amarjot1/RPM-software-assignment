from selenium.webdriver.chrome import webdriver


class EnvironmentSetup:
    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.3\\plugins\\python-ce\\helpers\\python-skeletons\\chromedriver.exe")

    def setup(self):
        pass

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
