from selenium.webdriver import Chrome
from demo1.Basefiles import InitiateDriver
from demo1.Basefiles import ConfigReader
import pytest



def test_valid():
    driver = InitiateDriver.startBrowser()
    driver.find_element("xpath", ConfigReader.elementsData('valid','username_xpath')).send_keys('student')
    driver.find_element("xpath", ConfigReader.elementsData('valid','password_xpath')).send_keys('Password123')
    driver.find_element('xpath', ConfigReader.elementsData('valid','click_xpath')).click()
