#importing required library
from selenium import webdriver

#opening a webpage
browser = webdriver.Chrome(r"C:\Users\piotr\Selenium\chromedriver_win32\chromedriver.exe")
# Simply just open a new Edge browser and go to lambdatest.com
# browser.maximize_window()
# browser.get('https://www.puralsight.com/')

#closing the current window
# browser.quit()

#opening web page with options
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)

browser.get("https://www.puralsight.com/")

