from selenium import webdriver
import time
link = "https://www.seleniumeasy.com/test/input-form-demo.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Potato")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Fries")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("potato.fries@gmail.com")
    input4 = browser.find_element_by_name("phone")
    input4.send_keys("112")
    input5 = browser.find_element_by_name("address")
    input5.send_keys("somewhere in the fields")
    input6 = browser.find_element_by_name("city")
    input6.send_keys("Detroit")
    input7 = browser.find_element_by_class_name("selectpicker")
    input7.send_keys("Texas")
    input8 = browser.find_element_by_name("zip")
    input8.send_keys("zippity")
    input9 = browser.find_element_by_name("website")
    input9.send_keys("www.potato.com")
    input10 = browser.find_element_by_name("hosting")
    input10.click()
    input11 = browser.find_element_by_name("comment")
    input11.send_keys("Potatoes do not write comments")

    button = browser.find_element_by_class_name("btn-default")
    time.sleep(2)
    button.click()

finally:
    time.sleep(30)