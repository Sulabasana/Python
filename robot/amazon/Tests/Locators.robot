*** Settings ***
Library    Selenium2Library
#pybot -d results Tests/Locators.robot
*** Variables ***

*** Test Cases ***
Should be able to search for product
    Open Browser  http://www.amazon.com  chrome
    Sleep  3s
    Input Text  id=twotabserachtextbox  Ferrari 458
    Sleep  3s
    #CSS
    #Click Button  css=#nav-search > form > div.nav-right > div > input
    #Xpath
    Click Button  xpath=//*[@id="nav-search"]/form/div[2]/div/input
    Sleep  3s
#    Click Link TU daj link

*** Keywords ***
