from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(r'C:\Users\piotr\Selenium\chromedriver_win32\chromedriver.exe')
driver.get("https://www.python.org")

print(driver.title)