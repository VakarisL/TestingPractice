from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import math
link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_id("book")
    WebDriverWait(browser, 30).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()

    x = browser.find_element_by_id('input_value').get_attribute("innerHTML")
    answer = math.log(abs(12 * math.sin(float(x))))
    answerElement = browser.find_element_by_id("answer")
    answerElement.send_keys(str(answer))

    button = browser.find_element_by_id("solve")
    button.click()

finally:
    time.sleep(30)