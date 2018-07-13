import unittest
import appium_config

class EZCalculatorTest(unittest.TestCase):
	"""
	TestCase: Test calculator
	Description: test +, -, x, /
	"""
	
	@classmethod
	def setUpClass(self):
		self.driver = appium_config.appium_start()
	
	###  common function [START]
	def setText(self, eid, text):
		e1 = self.driver.find_element_by_id(eid)
		e1.send_keys(text)
	
	def performClick(self, eid):
		self.driver.find_element_by_id(eid).click()

	def getText(self, eid):
		return self.driver.find_element_by_id(eid).text
	###  common function [END]

	def test_addition(self):

		value1 = 3
		value2 = 2
		result = value1 + value2

		# set value1
		self.setText('idv.haojun.appiumtest:id/etValue1', str(value1))

		# set value2
		self.setText('idv.haojun.appiumtest:id/etValue2', str(value2))

		# click add button
		self.performClick('idv.haojun.appiumtest:id/btAdd')

		# get text
		text = self.getText('idv.haojun.appiumtest:id/tvResult')

		# assert
		self.assertEqual(text, str(result))

	def test_subtraction(self):
		
		value1 = 3
		value2 = 2
		result = value1 - value2

		# set value1
		self.setText('idv.haojun.appiumtest:id/etValue1', str(value1))

		# set value2
		self.setText('idv.haojun.appiumtest:id/etValue2', str(value2))

		# click add button
		self.performClick('idv.haojun.appiumtest:id/btSub')

		# get text
		text = self.getText('idv.haojun.appiumtest:id/tvResult')

		# assert
		self.assertEqual(text, str(result))
	
	def test_multiplication(self):
		
		value1 = 5
		value2 = 12
		result = value1 * value2

		# set value1
		self.setText('idv.haojun.appiumtest:id/etValue1', str(value1))

		# set value2
		self.setText('idv.haojun.appiumtest:id/etValue2', str(value2))

		# click add button
		self.performClick('idv.haojun.appiumtest:id/btMul')

		# get text
		text = self.getText('idv.haojun.appiumtest:id/tvResult')

		# assert
		self.assertEqual(text, str(result))

	def test_division(self):
		
		value1 = 10
		value2 = 2
		result = value1 / value2

		# set value1
		self.setText('idv.haojun.appiumtest:id/etValue1', str(value1))

		# set value2
		self.setText('idv.haojun.appiumtest:id/etValue2', str(value2))

		# click add button
		self.performClick('idv.haojun.appiumtest:id/btDiv')

		# get text
		text = self.getText('idv.haojun.appiumtest:id/tvResult')

		# assert
		self.assertEqual(text, str(int(result)))

	@classmethod
	def tearDownClass(self):
		self.driver.quit()
		
# texture Testcase
def suite():
    tests = [
        'test_addition',
		'test_subtraction',
		'test_multiplication',
		'test_division'
    ]
    return unittest.TestSuite(map(EZCalculatorTest, tests))

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())