# #importing required library
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# #opening a webpage
browser = webdriver.Chrome(r"C:\Users\piotr\Selenium\chromedriver_win32\chromedriver.exe")
browser.get('https://python.org')

search = browser.find_element_by_name('q')
search.clear()
search.send_keys("pycon")
search.send_keys(Keys.RETURN)
time.sleep(4)

browser.close()
# element_id = browser.find_element_by_id('gsc-iw-id1')
# print(element_id)
# element_name = browser.find_element_by_name('submit')
# print(element_name)

# element_xpath = browser.find_element_by_xpath("//section[@class='hero homepage']/h1[1]")
# print(element_xpath)

# element_classname = browser.find_element_by_class_name('selenium-backers')
# print(element_classname)
# # heading_xpath = browser.find_element_by_xpath("//*[@id='mainContent']/h2[1]")
# # print(heading_xpath)

# # element_classname = browser.find_element_by_class_name('selenium-sponsors')
# # print(element_classname)

# browser.close()
# # driver.close()

# # Simply just open a new Edge browser and go to lambdatest.com
# # browser.maximize_window()
# # browser.get('https://www.puralsight.com/')

# #closing the current window
# # browser.quit()

# #opening web page with options
# # options = webdriver.ChromeOptions()
# # options.add_argument("--ignore-certificate-errors")
# # options.add_argument("--incognito")
# # options.add_argument("--headless")
# # browser = webdriver.Chrome(options=options)

# # browser.get("https://www.puralsight.com/")

