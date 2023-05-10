*** Settings ***
Library    Selenium2Library
#pybot -d results Tests/Locators.robot
*** Variables ***

*** Test Cases ***
Should be able to search for product
    Open Browser  http://www.onet.pl  chrome
    Sleep  3s
    Click Button  class=Logo_logoLink__LpkW5
    Sleep  3s
    Close Browser