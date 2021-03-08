from idlelib import browser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.3\\plugins\\python-ce\\helpers\\python-skeletons\\chromedriver.exe")

# -- Go to Employee registration page of ACME Corpoaration
driver.get("https://rpmsoftware.com/hiring/2020/integration-test/form-edit.html")

# -- Employee details

driver.find_element_by_id('FL:_ctl0:_ctl3').send_keys('Isabel Britt')
driver.find_element_by_id('FL:_ctl1:_ctl4').send_keys('This is a test Employee Summary.')
select = Select(driver.find_element_by_id('FL:_ctl3:_ctl3'))
select.select_by_value('1')
driver.find_element_by_id('FL:_ctl4:_ctl3').send_keys('$50,000.00')
driver.find_element_by_id('FL_latTxt_5').send_keys('Lat: 34.833850\xb0')
driver.find_element_by_id('FL_longTxt_5').send_keys('Long: 106.748580\xb0')
select = Select(driver.find_element_by_id('FL:_ctl6:_ctl3'))
#-- Leaving Date of Termination Blank
select.select_by_value('6')
driver.find_element_by_id('FL:_ctl8:_ctl3').send_keys("01042018")
driver.find_element_by_xpath("//input[@id='FL__ctl3_9']").click()
#--driver.execute_script("window.scrollTo(0,1080)")
driver.find_element_by_xpath("//input[@class='forMeasurement TableCell--input TableCell--input-value form-control']").send_keys('47')
select = Select(driver.find_element_by_css_selector("select[class='forMeasurement TableCell--input TableCell--input-select form-control ml-1']"))
select.select_by_value('3')
driver.find_element_by_xpath("(((//select[@class='forMeasurement TableCell--input TableCell--input-select form-control ml-1'])[2])//preceding::input)[12]").send_keys('21')
select = Select(driver.find_element_by_xpath("((//select[@class='forMeasurement TableCell--input TableCell--input-select form-control ml-1'])[2])"))
select.select_by_value('3')
driver.find_element_by_xpath("(//input[@class='TableCell--input form-control'])[1]").send_keys('Brown')
driver.find_element_by_xpath("(//input[@class='TableCell--input form-control'])[2]").send_keys('Ford')
driver.find_element_by_xpath("(//input[@class='TableCell--input form-control'])[3]").send_keys('Taurus')
driver.find_element_by_xpath("(//input[@class='TableCell--input form-control'])[4]").send_keys('2018')
driver.find_element_by_xpath("(//input[@class='TableCell--input form-control'])[5]").send_keys('SEL')
driver.find_element_by_xpath("(//input[@class='TableCell--input form-control'])[6]").send_keys('Black')
driver.find_element_by_xpath("(//input[@class='TableCell--input form-control'])[7]").send_keys('TEST-0001')
driver.find_element_by_xpath("(//input[@class='TableCell--input form-control'])[8]").send_keys('Ford')
driver.find_element_by_xpath("(//input[@class='TableCell--input form-control'])[9]").send_keys('F150')
driver.find_element_by_xpath("(//input[@class='TableCell--input form-control'])[10]").send_keys('2015')
driver.find_element_by_xpath("(//input[@class='TableCell--input form-control'])[11]").send_keys('XLT')
driver.find_element_by_xpath("(//input[@class='TableCell--input form-control'])[12]").send_keys('Red')
driver.find_element_by_xpath("(//input[@class='TableCell--input form-control'])[13]").send_keys('TEST-0002')

driver.find_element_by_xpath("//button[@id='submit_form']").click()

#-- even not filling full information gives me further car details

#-- Validating
assert driver.current_url in "https://rpmsoftware.com/hiring/2020/integration-test/form.html"

assert "47in" in driver.find_element_by_xpath("(//div[@class='TableCell--input-container'])[6]").text

#-- Optional task
#-- a. The employee nsme is displayed as a header on the page

element = driver.find_element_by_xpath("//h1[@class='border-bottom border-gray pb-2']").text
assert element == 'Isabel Britt'
driver.quit()








