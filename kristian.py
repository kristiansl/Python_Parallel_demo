from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium import webdriver
import time, unittest, sys, saucehelper, copy
import wd.parallel
import os

class parallel(unittest.TestCase):
	SAUCE_USERNAME = 'kristianmeiersl'
	SAUCE_ACCESS_KEY = '69c9ea29-59c8-4b3a-9909-18b1b05343f6'
 
	def setUp(self):
	# self.wd = WebDriver()
	# self.wd.implicitly_wait(60)
 
		desired_capabilities=[]
 
		browser = copy.copy(webdriver.DesiredCapabilities.CHROME)
		browser['platform'] = 'Linux'
		browser['name'] = 'Zebra on Sauce 1/2'
		browser['tags'] = "Parallel"
		browser['build'] = "9999"
		
		desired_capabilities += [browser]
 
		browser = copy.copy(webdriver.DesiredCapabilities.CHROME)
		browser['platform'] = 'Windows XP'
		browser['name'] = 'Zebra on Sauce 2/2'
		browser['tags'] = "Parallel"
		browser['build'] = "9999"
		
		desired_capabilities += [browser]
 
		self.drivers = wd.parallel.Remote(
		desired_capabilities=desired_capabilities,
		command_executor="http://" + parallel.SAUCE_USERNAME + ":" + parallel.SAUCE_ACCESS_KEY + "@ondemand.saucelabs.com:80/wd/hub"
	 
		)
 
	@wd.parallel.multiply
	def test_parallel(self):
 
		self.driver.get("https://ec2-54-169-136-199.ap-southeast-1.compute.amazonaws.com/dashboard/")
		self.driver.find_element_by_id("textfield-1025-inputEl").clear()
		self.driver.find_element_by_id("textfield-1025-inputEl").send_keys("vgr843@zebra.com")
		self.driver.find_element_by_id("textfield-1026-inputEl").clear()
		self.driver.find_element_by_id("textfield-1026-inputEl").send_keys("symbol")
		self.driver.find_element_by_id("button-1030-btnInnerEl").click()

		wait = WebDriverWait(self.driver, 20)
		condition = EC.text_to_be_present_in_element((By.ID, "displayfield-1051-inputEl"), "Rameswara")
		wait.until(condition)

 		self.driver.find_element_by_id("splitbutton-1052-btnWrap").click()
 		self.driver.find_element_by_id("menuitem-1054-itemEl").click()
		self.driver.find_element_by_id("button-1006-btnInnerEl").click()
 
		print self.driver.session_id
 
	@wd.parallel.multiply
	def tearDown(self):
 
		status = sys.exc_info() == (None, None, None)
		saucehelper.reportStatus(status, self.driver.session_id, parallel.SAUCE_USERNAME, parallel.SAUCE_ACCESS_KEY)
		self.driver.quit()
 
if __name__ == '__main__':
 unittest.main()