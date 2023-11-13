import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random

print(" Welcome to Roblox Automated Account Creator \n [1] Create Account \n [2] Quit")
input = int(input())

User = random.randint(21442, 531298393)
Username = "f" + str(User)
print(Username)
    
# Inputs and Creating account
if input == 1:
    print(" Loading.. This may  take up to a minute.")
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), 
                              options=options)

    driver.get("https://roblox.com/")
    print(" Loaded up website")
    driver.maximize_window()
    # Month
    driver.find_element(By.ID, "MonthDropdown").click()
    driver.find_element(By.ID, "MonthDropdown").send_keys("m")
    driver.find_element(By.ID, "MonthDropdown").send_keys(Keys.ENTER)

    # Day
    driver.find_element(By.ID, "DayDropdown").click()
    driver.find_element(By.ID, "DayDropdown").send_keys("1") # Does day 10
    driver.find_element(By.ID, "DayDropdown").send_keys(Keys.ENTER)

    # Year
    driver.find_element(By.ID, "YearDropdown").click()
    driver.find_element(By.ID, "YearDropdown").send_keys("1") # Puts year 1999
    driver.find_element(By.ID, "YearDropdown").send_keys(Keys.ENTER)

    # Enter user and pass
    driver.find_element(By.ID, "signup-username").send_keys(Username)
    driver.find_element(By.ID, "signup-password").send_keys("ImSoCool12@")

    # Gender
    driver.find_element(By.ID, "MaleButton").click()

    # Confirm
    time.sleep(0.8)
    driver.find_element(By.ID, "signup-button").click()
    # long loop so gui does not close
    time.sleep(9999999)
elif input == 2:
    print("Quitting.")
    sys.exit()

