# 114: Generic method to find elements
# Refer handy_wrappers.py and using_wrappers.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from basicweb.selenium.handy_wrappers import HandyWrappers

class UsingWrappers():

    def chrome_driver(self):

        practicePageURL = "https://letskodeit.teachable.com/p/practice"
        loginPageURL = "https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1"
        chromeDriverPath = "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"
        driver = webdriver.Chrome(executable_path= chromeDriverPath)
        driver.maximize_window()
        driver.implicitly_wait(10)
        # 114 & 115
        hw = HandyWrappers(driver)
        driver.get(practicePageURL)


        textField1 = hw.getElement("name") # here in the parameters list, the locator type as ID is not passing as parameter. Because already default argument ID is given in the method definition.
        textField1.send_keys("Test")
        time.sleep(2)
        textField2 = hw.getElement("//input[@id='name']", locatorType="xpath") # here in the parameters list, the locator type is passing as parameter XPath.
        textField2.clear()

objUWrap = UsingWrappers()
objUWrap.chrome_driver()


