from selenium import webdriver
import pytest
firstLink = "http://suninjuly.github.io/registration1.html"
secondLinK = "http://suninjuly.github.io/registration2.html"
registerFields=["potato","potato","potato@field.com","123","field"]

class TestRegistration():
    @pytest.fixture(scope="function")
    def browser(self):
        print("\nstart browser for test..")
        browser = webdriver.Chrome()
        yield browser
        print("\nquit browser..")
        browser.quit()

    @pytest.mark.parametrize("link", [firstLink, secondLinK])
    def test_registration(self, browser, link):
        browser.get(link)
        inputs = browser.find_elements_by_class_name("form-control")
        assert len(inputs) == 5, "Expected 5 inputs"
        for index, x in enumerate(inputs):
            x.send_keys(registerFields[index])
        button = browser.find_element_by_class_name("btn-default")
        button.click()