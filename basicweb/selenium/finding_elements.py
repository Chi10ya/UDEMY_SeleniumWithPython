from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Selenium webdriver - Finding elements
"""
Sec-15

  1: By ID
  html as  <input id="name" name="enter-name" class="inputs" placeholder="Enter Your Name" type="text">
    driver.find_element_by_id("name")  (or) driver.find_element(By.ID, "name")
  
  2: By NAME
  html as  <input id="displayed-text" name="show-hide" class="inputs displayed-class" placeholder="Hide/Show Example" type="text">
    driver.find_element_by_name("show-hide") (or) driver.find_element(By.NAME, "show-hide")
    
  3: By XPATH
  html as <input id="name" name="enter-name" class="inputs" placeholder="Enter Your Name" type="text">
    driver.find_element_by_xpath("//input[@id='name']")  (or) driver.find_element(By.XPATH, "//input[@id='name']")
    
  4: By CSS SELECTOR
  html as <input id="displayed-text" name="show-hide" class="inputs displayed-class" placeholder="Hide/Show Example" type="text">
    driver.find_element_by_css_selector("#displayed-text") (or) driver.find_element(By.CSS_SELECTOR, "#displayed-text")

  5: By LINK TEXT
  html as <a class="navbar-link fedora-navbar-link" href="/sign_in"> Login </a>
    driver.find_element_by_link_text("login") (or) driver.find_element(By.LINK_TEXT, "Login")
    
  6: By PARTIAL LINK TEXT
  html as <a class="fedora-navbar-link navbar-link" href="/pages/practice" target> Practice </a>
    driver.find_element_by_partial_link_text("Prac") (or) driver.find_element(By.PARTIAL_LINK_TEXT, "Prac")
    
  7: By CLASS NAME
  html as  <input id="displayed-text" name="show-hide" class="inputs displayed-class" placeholder="Hide/Show Example" type="text">
    driver.find_element_by_class_name("displayed-class") (or) driver.find_element(By.CLASS_NAME, "displayed-class")
    
  8: By TAG NAME
  html as  <h1>Practice Page</h1> Note: Here tag is h1. Any first word or letter after < (for ex: <h1, <a, <input, <div) or tag names
    driver.find_element_tag_name("h1") (or) driver.find_element(By.TAG_NAME, "h1")

Sec 16: CSS Selectors - Advanced Locators
    
    1: Using IDs with CSS selectors to find elements. 
    Syntax: tag[attribute = 'value'] ("#" is for ID, "." is for Class)
    
    html as  <input id="displayed-text" name="show-hide" class="inputs displayed-class" placeholder="Hide/Show Example" type="text">
        input[id='displayed-text'] (or) #displayed-text (or) input#displayed-text  
    
  
    2: Using classes with CSS selectors to find elements. 
    Syntax: tag[attribute = 'value'] ("#" is for ID, "." is for Class)
    
    html as  <input id="displayed-text" name="show-hide" class="inputs displayed-class" placeholder="Hide/Show Example" type="text">
        input[class='inputs displayed-class'] (or) .displayed-class (or) input.displayed-class (or) input.inputs.displayed-class
    
    Appending classes: .class1.class2.class3  
    html as <a id="opentab" class="btn-style class1 class2" href="https://letskodeit.teachable.com/courses" target="_blank" css="1">Open Tab</a>
        a[class='btn-style class1 class2'] (or) .btn-style.class1.class2 (or) a.class2 (or) a.btn-style.class1.class2
          
  
"""
class findingElements():


    def chrome_driver(self):
        chromeDriverPath = "C:\\Users\\chaitanya.mohammad\\PycharmProjects\\Python_Selenium_BrowserDrivers\\chromedriver.exe"
        driver= webdriver.Chrome(executable_path= chromeDriverPath)
        driver.get("https://letskodeit.teachable.com/p/practice")
        driver.maximize_window()
        time.sleep(5)

    # By ID
        elementById = driver.find_element_by_id("name")
        if elementById is not None:
            print("Element by id is found")
            elementById.send_keys("ChaitanyaAmbicaYashDhiya")
            time.sleep(5)
            elementById.clear()

        elementByIdByClass = driver.find_element(By.ID, "name")
        if elementByIdByClass is not None:
            print("Element by ID by using By Class is found")
            elementByIdByClass.send_keys("AmmuYashDhiyaChintu")
            time.sleep(5)
            elementByIdByClass.clear()

    # By NAME
        elementByName = driver.find_element_by_name("show-hide")
        if elementByName is not None:
            print("Element by NAME is found")

    # By XPATH
        elementByXPathByClass = driver.find_element(By.XPATH, "//input[@id='name']")
        if elementByXPathByClass is not None:
            print("Element by XPATH by using By Class is found")
            elementByXPathByClass.send_keys("AmmuDhiyaYashChintu")
            time.sleep(5)

    # By CSS SELECTOR
        elementByCSSSelectorByClass = driver.find_element(By.CSS_SELECTOR, "#displayed-text")
        if elementByCSSSelectorByClass is not None:
            print("Element by CSS Selector by using By Class is found")
            elementByCSSSelectorByClass.clear()
            elementByCSSSelectorByClass.send_keys("DhiyaAmmuYashChintu")
            time.sleep(5)

    # By LINK TEXT
        elementByLinkTextByClass = driver.find_element(By.LINK_TEXT, "Login")
        if elementByLinkTextByClass is not None:
            print("Element by Link text by using By Class is found")
            elementByLinkTextByClass.click()
            print("Page title is : " + driver.title)

    # By PARTIAL LINK TEXT
        elementByPartialLinkText = driver.find_element(By.PARTIAL_LINK_TEXT, "Pract")
        if elementByPartialLinkText is not None:
            print("Element by partial link text by using By Class is found")
            elementByPartialLinkText.click()
            print("Page title is : "+driver.title)

    # By CLASS NAME
        elementByClassName = driver.find_element_by_class_name("displayed-class")
        elementByClassName.send_keys("AmmuYashDhiyaChintu")
        if elementByClassName is not None:
            print("Element by class name is found")

    # By TAG NAME
        elementByTagNameByClass = driver.find_element(By.TAG_NAME, "h1")
        elementText = elementByTagNameByClass.text
        if elementByTagNameByClass is not None:
            print("Element by tag name is found and the element tag's text is : "+elementText)

# find_elements

        elementListByClassName = driver.find_elements_by_class_name("inputs")
        length1 = len(elementListByClassName)
        if elementListByClassName is not None:
            print("Size of the list is : "+str(length1))

        elementListByTagNameByClass = driver.find_elements(By.TAG_NAME, "h1")
        length2 = len(elementListByTagNameByClass)
        if elementListByClassName is not None:
            print("Size of the list is : "+str(length2))

    # By CSS Selector - ID

# 1: Using IDs with CSS selectors to find elements.
#   Syntax: tag[attribute = 'value'] ("#" is for ID, "." is for Class)
#   html as  <input id="displayed-text" name="show-hide" class="inputs displayed-class" placeholder="Hide/Show Example" type="text">
#   input[id='displayed-text'] (or) #displayed-text (or) input#displayed-text

        elementByCSSSelectorID = driver.find_element_by_css_selector("input#displayed-text")
        if elementByCSSSelectorID is not None:
            print("Element by CSS Selector - ID is found")

    # By CSS Selector - Classes

# 2: Using classes with CSS selectors to find elements.
#   Syntax: tag[attribute = 'value'] ("#" is for ID, "." is for Class)
#   html as <input id = "displayed-text" name = "show-hide" class ="inputs displayed-class" placeholder="Hide/Show Example" type="text" >
#   input[class ='inputs displayed-class'] ( or ).displayed-class(or ) input.displayed- class ( or ) input.inputs.displayed- class
#
#   Appending classes:.class1.class2.class3
#   html as <a id = "opentab"class ="btn-style class1 class2" href="https://letskodeit.teachable.com/courses" target="_blank" css="1" > Open Tab < / a >
#   a[class ='btn-style class1 class2'] ( or ).btn-style.class1.class2 ( or ) a.class2 ( or ) a.btn-style.class1.class2


        elementByCSSSelectorClasses = driver.find_element_by_css_selector("a.btn-style.class1.class2")
        if elementByCSSSelectorClasses is not None:
            print("Element by CSS Selector - Classes is found")

# 3: Using wild card characters with CSS selector
#   Wild card characters are "^", "$", "*"
#   <input id = "displayed-text" name = "show-hide" class ="inputs displayed-class" placeholder="Hide/Show Example" type="text" style css="1" >
        # driver.find_element_by_css_selector(input[placeholder='Hide/Show Example']) (or) input[placeholder*='Show'] (or) input[placeholder^='Hide']
        # (or) input[placeholder$='Example']

# 4: How to find child nodes using CSS selectors - Travesing to the child nodes

        # <table id="product" name="courses" class="table-display" border="1" style="" css="1"></table> --> which is inside the fieldset

        # fieldset>table (or) fieldset>#product (or) fieldset>.table-display

# 17: Difference between Absolute and Relative path


        driver.quit()


fdriver = findingElements()
fdriver.chrome_driver()