from demo1.Basefiles import InitiateDriver
import pytest



def test_valid():
    driver = InitiateDriver.startBrowser()
    driver.find_element("xpath", "//input[@id='username']").send_keys('student2')
    driver.find_element("xpath", "//input[@id='password']").send_keys('Password123')
    driver.find_element('xpath', "//button[@id='submit']").click()
