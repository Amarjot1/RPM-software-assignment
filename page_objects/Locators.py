from lib2to3.pgen2 import driver

from self import self


class Locator (object):
def__init__(self,driver)
    self.driver = driver

    self.employee_name = driver.find_element_by_id('FL:_ctl0:_ctl3')
    self.summary = driver.find_element_by_id('FL:_ctl1:_ctl4')
    self.department = driver.find_element_by_id('FL:_ctl3:_ctl3')
    self.salary = driver.find_element_by_id('FL:_ctl4:_ctl3')
    self.address_lattitude = driver.find_element_by_id('FL_latTxt_5')
    self.address_longitude = driver.find_element_by_id('FL_longTxt_5')
    self.work_location = driver.find_element_by_id('FL:_ctl6:_ctl3')
    self.date_of_joining = driver.find_element_by_id('FL:_ctl8:_ctl3')
    # -- Leaving date of termination
    self.employee_active = driver.find_element_by_xpath("//input[@id='FL__ctl3_9']")





