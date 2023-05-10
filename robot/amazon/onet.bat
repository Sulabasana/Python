@echo off
cd c:\Users\frydrysz\TestRobot
call python -m robot Tests/Onet.robot
#Change logs directory
call python -m robot -d results/LogsfromChrome Tests/Onet.robot
#Select browser
call python -m robot -d results/LogsfromChrome -v BROWSER:chrome Tests/Onet.robot
