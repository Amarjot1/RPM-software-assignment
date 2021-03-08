from lib2to3.pgen2 import driver

from TestBase.EnvironmentSetup import EnvironmentSetup


class RegistrationPage(EnvironmentSetup):
  def test_RegistrationFlow(self):
    driver = self.driver
    self.driver.get("https://rpmsoftware.com/hiring/2020/integration-test/form-edit.html")











