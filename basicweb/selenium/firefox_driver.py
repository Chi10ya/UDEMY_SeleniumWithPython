from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.common.exceptions import *
import logging
import time


class RunChromeTests():

    def chrome_driver(self):

        practicePageURL = "https://letskodeit.teachable.com/p/practice"
        loginPageURL = "https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1"
        chromeDriverPath = "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"

        driver = webdriver.Chrome(executable_path= chromeDriverPath)
        driver.get(practicePageURL)
        # 102
        driver.maximize_window()
        time.sleep(5)
        pageTitle = driver.title
        print("Title of the webpage is : " +pageTitle)
        currentURL = driver.current_url
        print("Current URL of the page is : "+currentURL)
        driver.refresh()  # Page refresh
        driver.get(driver.current_url) # Page refresh
        driver.get(loginPageURL)
        print(driver.title)
        driver.back()
        print(driver.get(driver.current_url))
        driver.forward()
        print(driver.get(driver.current_url))
        # 103:
        driver.implicitly_wait(10)
        lnkLogin = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        lnkLogin.click()
        txtUserName= driver.find_element(By.ID, "user_email")
        txtUserName.send_keys("test")
        txtPassword = driver.find_element(By.ID, "user_password")
        txtPassword.send_keys("test")
        time.sleep(3)
        # 104:

        if txtUserName.is_enabled():
            print("Username edit box is enabled")
        else:
            print("Username edit box is not enabled")

        driver.get(practicePageURL)

        rdbtnBMW = driver.find_element(By.ID, "bmwradio")
        print("Radio button status : "+ rdbtnBMW.is_selected())
        rdbtnBMW.click()
        print("Radio button status : " + rdbtnBMW.is_selected())

        chkbxBenz = driver.find_element(By.ID, "benzcheck")
        print("Check box status : "+chkbxBenz.is_selected())
        chkbxBenz.click()
        print("Check box status : " +chkbxBenz.is_selected())

        # 106:
        radioBtnsList = driver.find_elements(By.XPATH, "//input[contains(@type, 'radio') and contains(@name, 'cars')]")
        size = len(radioBtnsList)
        print("Size of the list", +str(size))
        for radioButton in radioBtnsList:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(5)

        # 107: Understanding drop down elements & 108: Working with a dropdown element *** Practical example ***
        element = driver.find_element_by_id("carselect")
        sel = Select(element)
        sel.select_by_index("2")
        time.sleep(3)
        sel.select_by_value("benz")
        time.sleep(3)
        sel.select_by_visible_text("BMW")

        # 109 : How to work with hidden elements & 110 : Working with hidden elements - Practical Example

        txtBoxElement = driver.find_element_by_id("show-textbox").click()
        txtBoxState = txtBoxElement.is_displayed()
        print("Text is visible ?"+str(txtBoxState))

        # 112: How to get the text on element
        openTabElementText = driver.find_element_by_id("opentab").text
        print("Text of openTab Element is : "+openTabElementText)

        # 113: How to get value of element attribute
        element = driver.find_element_by_id("name")
        result= element.get_attribute("type")
        print("Value of attribute is : "+result)
        time.sleep(1)


        # 114: Generic method to find elements & 115: How to check if element is present
        # Refer handy_wrappers.py and using_wrappers.py

        # 119: Implicitly Wait

        # 120: Explicit wait
        driver.get("http://www.expedia.com")
        driver.maximize_window()
        driver.implicitly_wait(.5) # Wait for .5 seconds
        driver.find_element_by_id("tab-flight-tab").click()
        driver.find_element_by_id("flight-origin").send_keys("SFO")
        driver.find_element_by_id("flight-destination").send_keys("NYC")
        driver.find_element_by_id("flight-departing").send_keys("12/24/2020")
        returnDate = driver.find_element_by_id("flight-returning")
        returnDate.clear()
        returnDate.send_keys("12/26/2020")
        driver.find_element_by_id("search-button").click()

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                ElementNotVisibleException,
                                                ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.ID, "stopFilter_stops-0")))
        element.click()

        # 121: Generic method to work with explicit wait

        # 123: Calendar selection Introduction

        # 124:

        # 125: Calendar Selection *** Real Time Example ***
        driver.get("http://www.expedia.com")
        driver.maximize_window()
        driver.implicitly_wait(3)
        # click flights tab
        driver.find_element_by_id("tab-flight-tab").click()
        # click departing field
        driver.find_element_by_id("flight-departing").click()
        calMonth = driver.find_element(By.XPATH, "//section[@class='cal-month'][position()=1]")
        allValidDates = calMonth.find_elements(By.TAG_NAME, "a")
        time.sleep(2)

        for date in allValidDates:
            if date.text == "31":
                date.click()
                break


        # 126: AutoComplete Introduction
        # 127: AutoComplete *** Practical Example ***
        # 128: How to take screenshots
        # 129: Generic method to take screenshots

        # 130: Executing JavaScript commands
        driver.execute_script("window.location = 'https://letskodeit.teachable.com/p/practice';")
        driver.implicitly_wait(2)
        element = driver.execute_script("return document.getElementById('name');")


        # 131: How to find size of the window
        driver.get(practicePageURL)
        driver.implicitly_wait(3)
        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print("Height :"+str(height))
        print("Width :"+str(width))

        # 132: How to scroll enrollment into view
        driver.get(practicePageURL)
        driver.implicitly_wait(3)

        # Scroll Down
        driver.execute_script("window.scrollBy(0, 1000);")

        # Scroll Up
        driver.execute_script("window.scrollBy(0, -1000);")

        # Scroll Element into View
        element = driver.find_element(By.ID, "mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, -150);")

        # Native way to scroll element into View
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, -1000);")
        location = element.location_once_scrolled_into_view
        print("Location : "+str(location))
        driver.execute_script("window.scrollBy(0, -150);")


        # 133: Interview Questions.

        # 134: How to switch window focus & Switch to window *** Practical Example ***
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.maximize_window()
        parentHandle = driver.current_window_handle
        print("Parent Handle : "+parentHandle)
        time.sleep(3)
        driver.find_element(By.ID, "openwindow").click()
            # Switch to window and search course
        handles= driver.window_handles
            # Switch to window and search course
        for handle in handles:
            print("Handle :"+handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switched to window :: "+handle)
                searchBox = driver.find_element(By.ID, "search-courses")
                searchBox.send_keys("python")
                time.sleep(2)
                driver.close()
                break
            # Switch back to the parent handle
        driver.switch_to.window(parentHandle)
        driver.find_element(By.ID, "name").send_keys("Test Successful")

        # 136: How to work with iFrames & 137: Switch to iFrame Practical example ***
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.maximize_window()
        driver.execute_script("window.scrollBy(0, 1000);")
            # Switch to frame using ID
        driver.switch_to.frame("courses-iframe")
            # Switch to frame ususing name
        #driver.switch_to.frame("iframe-name")
            # Switch to frame using numbers
        #driver.switch_to.frame("0")

        time.sleep(3)
            # Search course
        searchBox = driver.find_element(By.ID, "serach-courses")
        searchBox.send_keys("python")
        time.sleep(2)

            # Switch back to the parent frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("Test Successful")

        # 138: Handling Javascript ppopup
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.maximize_window()
        driver.find_element(By.ID, "name").send_keys("Test")
        driver.find_element(By.ID, "alertbtn").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        driver.find_element(By.ID, "name").send_keys("Test")
        driver.find_element(By.ID, "confirmbtn").click()
        time.sleep(2)
        driver.switch_to.alert.dismiss()

        # 139: Mouse Hover actions
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.maximize_window()
        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(2)
        element = driver.find_element(By.ID, "mousehover")
        itemToClickLocator = ".//div[@class='mouse-hover-content']//a[text()='Top']"
        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse hovered on element")
            time.sleep(2)
            topLink = driver.find_element(By.XPATH, itemToClickLocator)
            actions.move_to_element(topLink).click().perform()
            print("Item clicked")
        except:
            print("Mouse Hover failed on element")

        # 140: How to drag and drop element on a webpage
        driver.get("https://jqueryui.com/droppable")
        driver.maximize_window()
        driver.switch_to.frame(0)

        sourceElement = driver.find_element(By.ID, "draggable")
        destinationElememt = driver.find_element(By.ID, "droppable")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            actions.click_and_hold(sourceElement).move_to_element(destinationElememt).release().perform()
            time.sleep(2)
        except:
            print("Drag and Drop failed on element")

        # 141: Working with sliders actions
        driver.get("https://jqueryui.com/droppable")
        driver.maximize_window()
        driver.switch_to.frame(0)

        element = driver.find_element(By.XPATH, "//div[@id='slider']//span")
        time.sleep(2)
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(element, 100, 0).perform()
            time.sleep(2)
        except:
            print("Sliding failed on element")

        # 142:
        logging.basicConfig(filename="test.log", level=logging.DEBUG)
        logging.warning("Warning message")
        logging.info("Info message")
        logging.error("Error message")

        # 143: Changing the format of logs
        # Refer the website : https://docs.python.org/3/library/logging.html#logrecord-attributes
        # Refer the website : https://docs.python.org/3/library/time.html#time.strftime

        logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:S', level=logging.DEBUG)
        logging.warning("Warning message")
        logging.info("Info message")
        logging.error("Error message")

        # 144: Logger - Console example
        # Refer LoggerDemoConsole.py file for Logger - Console

        # 145: Logger - Configuration file example

        # 146: How to write a generic custom logger utility  --> ** This is the one to be used for logging.
        # Refer custom_logger.py and custom_logger_demo.py



        # -----------------------------------------------------------------------
        # Exercise 1: Find the price of the course "Python Programming Language"

        pythonCoursePriceXPath = "//*[@id='product']//td[text()='Python Programming Language']//following-sibling::td"
        coursePrice = driver.find_element_by_xpath(pythonCoursePriceXPath).text
        print("Python Programming course price is : "+str(coursePrice))
        if int(coursePrice) == 30:
            print("Test case passed")
        else:
            print("Test case failed")

        driver.quit()


fdriver = RunChromeTests()
fdriver.chrome_driver()