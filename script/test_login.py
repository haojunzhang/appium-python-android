import unittest
from script.common.driver import get_driver

class LoginTest(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		self.driver = get_driver()
	
	@classmethod
	def tearDownClass(self):
		self.driver.quit()
	
	def clear_all_input(self):
		eEmail = self.driver.find_element_by_id("idv.haojun.calculatorrecorder:id/etLoginEmail")
		eEmail.clear()
		ePassword = self.driver.find_element_by_id("idv.haojun.calculatorrecorder:id/etLoginPassword")
		ePassword.clear()
	
	def is_login_page(self):
		eEmail = self.driver.find_element_by_id("idv.haojun.calculatorrecorder:id/etLoginEmail")
		return eEmail.is_displayed()
	
	def is_main_page(self):
		eAdd = self.driver.find_element_by_id("idv.haojun.calculatorrecorder:id/ivMainAdd")
		return eAdd.is_displayed()
	
	def test_is_login_page(self):
		self.assertTrue(self.is_login_page())

	def test_email_is_empty(self):
		self.clear_all_input()

		ePassword = self.driver.find_element_by_id("idv.haojun.calculatorrecorder:id/etLoginPassword")
		ePassword.send_keys("123456789")

		eLogin = self.driver.find_element_by_id("idv.haojun.calculatorrecorder:id/tvLoginLogin")
		eLogin.click()

		eMessage = self.driver.find_element_by_id("android:id/message")
		self.assertTrue(eMessage.is_displayed())

		if eMessage.is_displayed():
			eCancel = self.driver.find_element_by_id("android:id/button2")
			eCancel.click()

	def test_password_is_empty(self):
		self.clear_all_input()

		eEmail = self.driver.find_element_by_id("idv.haojun.calculatorrecorder:id/etLoginEmail")
		eEmail.send_keys("aaa@aa.aa")

		eLogin = self.driver.find_element_by_id("idv.haojun.calculatorrecorder:id/tvLoginLogin")
		eLogin.click()

		eMessage = self.driver.find_element_by_id("android:id/message")
		self.assertTrue(eMessage.is_displayed())

		if eMessage.is_displayed():
			eCancel = self.driver.find_element_by_id("android:id/button2")
			eCancel.click()

	def test_email_is_valid(self):
		self.clear_all_input()

		eEmail = self.driver.find_element_by_id("idv.haojun.calculatorrecorder:id/etLoginEmail")
		eEmail.send_keys("aaa@@aa.aa")

		ePassword = self.driver.find_element_by_id("idv.haojun.calculatorrecorder:id/etLoginPassword")
		ePassword.send_keys("123456789")

		eLogin = self.driver.find_element_by_id("idv.haojun.calculatorrecorder:id/tvLoginLogin")
		eLogin.click()

		eMessage = self.driver.find_element_by_id("android:id/message")
		self.assertTrue(eMessage.is_displayed())

		if eMessage.is_displayed():
			eCancel = self.driver.find_element_by_id("android:id/button2")
			eCancel.click()

	def test_password_is_valid(self):
		self.clear_all_input()

		eEmail = self.driver.find_element_by_id("idv.haojun.calculatorrecorder:id/etLoginEmail")
		eEmail.send_keys("aaa@aa.aa")

		ePassword = self.driver.find_element_by_id("idv.haojun.calculatorrecorder:id/etLoginPassword")
		ePassword.send_keys("00")

		eLogin = self.driver.find_element_by_id("idv.haojun.calculatorrecorder:id/tvLoginLogin")
		eLogin.click()

		eMessage = self.driver.find_element_by_id("android:id/message")
		self.assertTrue(eMessage.is_displayed())

		if eMessage.is_displayed():
			eCancel = self.driver.find_element_by_id("android:id/button2")
			eCancel.click()

	def test_enter_main_page(self):
		eEmail = self.driver.find_element_by_id("idv.haojun.calculatorrecorder:id/etLoginEmail")
		eEmail.send_keys("aaa@aa.aa")

		ePassword = self.driver.find_element_by_id("idv.haojun.calculatorrecorder:id/etLoginPassword")
		ePassword.send_keys("123456789")

		eLogin = self.driver.find_element_by_id("idv.haojun.calculatorrecorder:id/tvLoginLogin")
		eLogin.click()

		self.assertTrue(self.is_main_page())

def suite():
    tests = [
		'test_is_login_page',
		'test_email_is_empty',
		'test_password_is_empty',
		'test_email_is_valid',
		'test_password_is_valid',
		'test_enter_main_page',
    ]
    return unittest.TestSuite(map(LoginTest, tests))
