# importing required package of webdriver
from ast import Return
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.opera.options import Options
from selenium.webdriver.support.wait import WebDriverWait

if __name__ == '__main__':
    # Instantiate the webdriver with the executable location of MS Edge
    browser = webdriver.Chrome(r'C:\Users\piotr\Selenium\chromedriver_win32\chromedriver.exe')
    # Simply just open a new Chrome browser and go to pluralsight.com
    browser.maximize_window()
    browser.get('https://www.pluralsight.com/')
    try:
        # Get the search filed
        myElem_1 = browser.find_element_by_class_name('ps-nav--search')
        myElem_1.click()
        myElem_2 = browser.find_element_by_name('q')
        myElem_2.send_keys("Python")
        myElem_2.send_keys(Return)
        sleep(25)
        
        
    except TimeoutException:
        print("No element found")
    sleep(10)
    browser.close()

    