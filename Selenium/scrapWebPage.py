#Selenium
# #importing library
# from selenium import webdriver

# driver= webdriver.Chrome(r"C:\Users\piotr\Github\Python\Python\Selenium\driver\chromedriver")
# # driver = webdriver.Chrome(r"C:\bin")
# driver.get("https://pluralsight.com/")

# driver.quit()

# Selenium + Python + BS4

# importing required packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


# variable
playerName = "Wayne Rooney"

# adding options on chrome
chromeOptions = Options()
# chromeOptions.add_argument("--kiosk")


# navigating to the premier league site

driver = webdriver.Chrome(options=chromeOptions)
# driver.get("https://www.premierleague.com/")
driver.get("https://www.premierleague.com/players/")

# clicking on the players tab
# players_ele = driver.find_element_by_link_text("Players").click()

# searching for player
# web driver wait
element = WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable((By.ID, "search-input")))

search_ele = driver.find_element(By.ID, "search-input")
search_ele.send_keys(playerName)
time.sleep(2)
search_ele.send_keys(Keys.RETURN)


# clicking on player
# driver.implicitly_wait(3)
playerLink = f'"Photo for {playerName}"'
# print("Player link is " + playerLink)
print(playerLink)
# click_player = driver.find_element_by_xpath("//img[@alt='" + playerLink + "']").click()
# click_player = driver.find_element(By.ID, "text")
# click_player = driver.find_element_by_xpath("//img[@alt=%s]"%str(playerLink)).click()
# click_player = driver.find_element_by_xpath("//img[@alt='Photo for Wayne Rooney')]".click()
                                            
click_player = driver.find_element(By.XPATH, "//*[@alt='Photo for Wayne Rooney']").click()




 

# Assign to variable
page_source_overview = driver.page_source
# Beautiful Soup
from bs4 import BeautifulSoup

# loading page source info
soup = BeautifulSoup(page_source_overview, 'lxml')

# locating the titles
title_finder = soup.find_all("span", class_="title")

print(10*"-" + "These are the latest news headlines about " + playerName + 10*"-" + "\n")
for title in title_finder:
    print(title.string)

# stats button element
time.sleep(2)
wayne_stats = driver.find_element_by_xpath("//a[@href='stats']").click()

page_source_stats = driver.page_source

soup = BeautifulSoup(page_source_stats, "lxml")

# locating all the stats
stat_finder = soup.find_all("span", class_="allStatContainer")

print(stat_finder)

print(10*"-" + playerName + " Stats" + 10*"-" + "\n")
for stat in stat_finder:
    print(stat["data-stat"] +  " - " + stat.string)

driver.close()