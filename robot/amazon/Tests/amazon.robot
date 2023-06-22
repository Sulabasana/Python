****** Settings ***
Documentation   This is some basic info about the whole suite
Library  Selenium2Library

# Copy/paste the line below into Terminal to execute:
# robot -d results tests/amazon.robot


*** Variables ***


*** Test Cases ***
User must sign it to check out
    [Documentation]  This is some basic information about the test
    [Tags]  Smoke

    Begin Web Test
    Search for Products
    Select Product from Search Results
    Add Product to Cart
    Begin Checkout
    End Web Test


*** Keywords ***

Begin Web Test
    Open Browser  about:blank chrome

Search for Products
    Go To  http://www.amazon.com
    Wait Until Page Contains  Today's Deals
    Input Text  id=twotabsearchtextbox  Ferrari 458
    Click Button  xpath=//*[@id="nav-search"]/form/div[2]/div/input
    Wait Until Page Contains  results for "Ferrari 458"

Select Product from Search Results
    Click Link  css=#result_0 > div > div > div > div.a-fixed-left-grid-col.a-col-right > div.a-row.a-spacing-small > div:nth-child(1) > a
    Wait Until Page Contains  Back to search results

Add Product to Cart
    Click Button  id=add-to-cart-button
    Wait Until Page Contains  Added to Cart

Begin Checkout
    Click Link  Proceed to Checkout
    Page Should Contain Element  continue

End Web Test
    Close Browser
