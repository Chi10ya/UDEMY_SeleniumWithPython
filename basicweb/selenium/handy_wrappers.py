from selenium.webdriver.common.by import By

# 114: Generic method to find elements & 115: How to check if element is present
# Refer handy_wrappers.py and using_wrappers.py

class HandyWrappers():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        else:
            print("Locator type is not supported")
        return False

    def getElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locatorValue)
            print("Element Found :"+element)
        except:
            print("Element not found")
        return element

