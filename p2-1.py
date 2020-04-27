from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import math
link = "http://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("btn-primary")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    WebDriverWait(browser, 30).until(lambda browser: browser.current_url != link)

    x = browser.find_element_by_id('input_value').get_attribute("innerHTML")
    answer = math.log(abs(12 * math.sin(float(x))))
    answerElement = browser.find_element_by_id("answer")
    answerElement.send_keys(str(answer))

    button = browser.find_element_by_class_name("btn-primary")
    button.click()
finally:
    time.sleep(30)