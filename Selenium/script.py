# https://www.thepythoncode.com/article/automated-browser-testing-with-edge-and-selenium-in-python?utm_source=newsletter&utm_medium=email&utm_campaign=newsletter
# While performing automated browser testing, it is important for the test scripts to communicate with the browser. Without having a WebDriver, this might not be possible. The Selenium Edge WebDriver works as the mediator between your code and the browser, which helps to provide the programmable remote control of the browser.

# You can download the latest version of Selenium Edge WebDriver using this link.


# Performing Browser Automation With Edge And Selenium In Python
# Let us see what are the prerequisites to use Edge with Selenium and Python for browser automation:

# Download the latest version of Python, if not already installed, from here.
# Next, we need the Microsoft Edge browser. You can use this link to download it. Please note the version that you are downloading, for WebDriver purpose. If you have Edge already installed, you can find out its version by typing the below command in Edge’s address bar:
# edge://version/
# You can also find out the version of your Edge browser, using the below steps:
# Open the Microsoft Edge browser.
# Select Settings and more at the top right of the browser and go to Settings.
# You can see a section About Microsoft Edge at the bottom of the settings tab, that contains the information about your Edge’s version.

# pip3 install selenium
# pip install msedge-selenium-tools selenium==3.141

# importing required package of webdriver
from selenium import webdriver

if __name__ == '__main__':
    # Instantiate the webdriver with the executable location of MS Edge web driver
    browser = webdriver.Edge(r"C:\Users\Piotrek\Desktop\LearnPython\edgedriver_win32r86\msedgedriver.exe")
    # Simply just open a new Edge browser and go to lambdatest.com
    browser.get('https://www.lambdatest.com')