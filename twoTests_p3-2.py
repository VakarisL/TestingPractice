from selenium import webdriver
import unittest
firstLink = "http://suninjuly.github.io/registration1.html"
secondLinK = "http://suninjuly.github.io/registration2.html"
registerFields=["potato","potato","potato@field.com","123","field"]

def make_registration_test_case(link):
    class RegistrationTestCase(unittest.TestCase):
        def registration_test(self):
            browser = webdriver.Chrome()
            browser.get(link)
            inputs = browser.find_elements_by_class_name("form-control")
            self.assertEqual(len(inputs), 5, "Expected 5 inputs")
            for index, x in enumerate(inputs):
                x.send_keys(registerFields[index])
            button = browser.find_element_by_class_name("btn-default")
            button.click()

    return RegistrationTestCase

suite = unittest.TestSuite()
suite.addTest(make_registration_test_case(firstLink)("registration_test"))
suite.addTest(make_registration_test_case(secondLinK)("registration_test"))
unittest.TextTestRunner().run(suite)
