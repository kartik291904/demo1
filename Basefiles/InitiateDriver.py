from selenium.webdriver import Chrome
from Basefiles.ConfigReader import readData

def startBrowser():
    global driver
    driver = Chrome()
    driver.get(readData('Section1','url'))
    driver.maximize_window()
    return driver

def closeBrowser():
    driver.close()