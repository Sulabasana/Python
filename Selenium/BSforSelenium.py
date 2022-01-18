from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.options import Options
import time

#adding option on chrome
# chromeOptions = Options()
# chromeOptions.add_argument("--kiosk")

driver = webdriver.Chrome(r'C:\Users\piotr\Selenium\chromedriver_win32\chromedriver.exe')
driver.get("https://www.pluralsight.com")

ele = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div/div/nav/div/div[2]/ul[2]/li[1]/a")
time.sleep(1)
ele.click
ele.clear()
ele.send_keys("lists")
ele.send_keys(Keys.RETURN)


print(driver.title)

driver.quit()

