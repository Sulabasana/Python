from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#adding option on chrome
# chromeOptions = Options()
# chromeOptions.add_argument("--kiosk")

driver = webdriver.Chrome(r'C:\Users\piotr\Selenium\chromedriver_win32\chromedriver.exe')
driver.get("https://www.premierleague.com")

players_ele = driver.find_element_by_link_text("players").click()
#searching for Timo Werner
element = WebDriverWait(driver ,10).until(
    EC.element_to_be_clickable((By.ID, "search-input")))

search_ele = driver.find_element_by_id("search-input")
search_ele.send_keys("Timo Wener")
search_ele.send_keys(Keys.RETURN)

driver.implicitly_wait(2)
driver.quit()

