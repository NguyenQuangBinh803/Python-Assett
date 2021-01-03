import unittest
from appium import webdriver

class SimpleCalculatorTests(unittest.TestCase):

    def setUp(self):
        #set up appium
        desired_caps = {}
        desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities= desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_initialize(self):
        self.driver.find_element_by_accessibility_id("clearButton").click()
        self.driver.find_element_by_accessibility_id("num7Button").click()

        result = self.driver.find_element_by_accessibility_id("CalculatorResults")
        self.assertIn(" 7 ", str(result.text))

    def test_addition(self):
        self.driver.find_element_by_accessibility_id("num1Button").click()
        self.driver.find_element_by_accessibility_id("plusButton").click()
        self.driver.find_element_by_accessibility_id("num7Button").click()
        self.driver.find_element_by_accessibility_id("equalButton").click()

        result = self.driver.find_element_by_accessibility_id("CalculatorResults")
        self.assertIn( " 8 ", str(result.text))

    def test_combination(self):
        self.driver.find_element_by_accessibility_id("num7Button").click()
        self.driver.find_element_by_accessibility_id("multiplyButton").click()
        self.driver.find_element_by_accessibility_id("num9Button").click()
        self.driver.find_element_by_accessibility_id("plusButton").click()
        self.driver.find_element_by_accessibility_id("num1Button").click()
        self.driver.find_element_by_accessibility_id("equalButton").click()
        self.driver.find_element_by_accessibility_id("divideButton").click()
        self.driver.find_element_by_accessibility_id("num8Button").click()
        self.driver.find_element_by_accessibility_id("equalButton").click()

        result = self.driver.find_element_by_accessibility_id("CalculatorResults")
        self.assertIn( " 8 ", str(result.text))

    def test_division(self):
        self.driver.find_element_by_accessibility_id("num8Button").click()
        self.driver.find_element_by_accessibility_id("num8Button").click()
        self.driver.find_element_by_accessibility_id("divideButton").click()
        self.driver.find_element_by_accessibility_id("num1Button").click()
        self.driver.find_element_by_accessibility_id("num1Button").click()
        self.driver.find_element_by_accessibility_id("equalButton").click()

        result = self.driver.find_element_by_accessibility_id("CalculatorResults")
        self.assertIn( " 8 ", str(result.text))

    def test_multiplication(self):
        self.driver.find_element_by_accessibility_id("num9Button").click()
        self.driver.find_element_by_accessibility_id("multiplyButton").click()
        self.driver.find_element_by_accessibility_id("num9Button").click()
        self.driver.find_element_by_accessibility_id("equalButton").click()

        result = self.driver.find_element_by_accessibility_id("CalculatorResults")
        self.assertIn( " 81 ", str(result.text))

    def test_subtraction(self):
        self.driver.find_element_by_accessibility_id("num9Button").click()
        self.driver.find_element_by_accessibility_id("minusButton").click()
        self.driver.find_element_by_accessibility_id("num1Button").click()
        self.driver.find_element_by_accessibility_id("equalButton").click()

        result = self.driver.find_element_by_accessibility_id("CalculatorResults")
        self.assertIn( " 8 ", str(result.text))



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleCalculatorTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
