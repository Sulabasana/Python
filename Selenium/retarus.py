# importing required package of webdriver
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
    browser = webdriver.Edge(r"C:\Users\Piotrek\Desktop\LearnPython\edgedriver_win32r86\msedgedriver.exe")
    # Simply just open a new Edge browser and go to lambdatest.com
    browser.maximize_window()
    browser.get('https://eas.retarus.com/PicoPortal/')
    try:
        # Get the text box to insert Email using selector ID
        myElem_1 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'j_username')))
        # Entering the email address
        myElem_1.send_keys("piotr.frydryszak@pl.mahle.com")
        myElem_1.click()
        #Get the text box to insert Password using selector ID 
        myElem_2 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'j_password')))
        #Entering passwrod
        myElem_2.send_keys("T!a1x1i1")
        myElem_2.click()
        # Get the Submit button to click and start free testing using selector CSS_SELECTOR
        myElem_3= WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login")))
        # Starting free testing on LambdaTest
        myElem_3.click()
        sleep(2)

        #Click Administration
        myElem_4= WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#navlist > li:nth-child(5) > div")))
        myElem_4.click()
        sleep(1)
        #Click E-mail Services
        myElem_5 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#navlist9 > li:nth-child(1)")))
        myElem_5.click()
        sleep(1)
        #Click User Configuration
        myElem_6 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#navlist14 > li:nth-child(6)")))
        myElem_6.click()
        sleep(25)
        
        
    except TimeoutException:
        print("No element found")
    sleep(10)
    browser.close()

    