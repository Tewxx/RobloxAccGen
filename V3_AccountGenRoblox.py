import sys
import time
import customtkinter
import tkinter
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random

# Plain GUI
app = customtkinter.CTk() # create CTk window like you do with the Tk window
app.geometry("650x325") # Tk Window Size
app.title("RBX Account Creator X v0.1")

# Apperance
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")
app.resizable(False,False) # Makes the window size unable to change

def CreateAccount_function():
    accnum_str = CodeInput.get("1.0", tkinter.END)
    print(accnum_str)
    accnum = int(accnum_str)
    if accnum > 0:
        for i in range (accnum):
            options = Options()
            options.add_experimental_option("detach", True)
            options.add_argument("--headless")
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            User = random.randint(21442, 53129835593)
            Username = "f" + str(User)
            OutputBox.configure(state="normal")
            OutputBox.insert(tkinter.END, "Username: " + Username + " Password: ImSoCool12@\n")
            print(" Loading.. This may  take up to a minute.")
            options = Options()
            options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), 
                                    options=options)

            driver.get("https://roblox.com/")
            print(" Loaded up website")
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
            # time before gui auto close
            time.sleep(8)
            driver.close()

# Create Account Button
Createbutton = customtkinter.CTkButton(master=app, fg_color="#5A5A5A")
Createbutton = customtkinter.CTkButton(master=app, text="Create account(s)", command=CreateAccount_function, width=140, height=40)
Createbutton.place(x=565, y=295, anchor=customtkinter.CENTER)

# Display usernames and pass
OutputBox = customtkinter.CTkTextbox(master=app, width=300, height=175)
OutputBox.place(x=160, y=150, anchor=tkinter.CENTER)
ScrollBar = customtkinter.CTkScrollbar(master=app, height=175, bg_color="transparent") 
ScrollBar.place(x=302, y=150, anchor=tkinter.CENTER)
OutputBox.configure(yscrollcommand=ScrollBar.set, state="disabled")
ScrollBar.configure(command=OutputBox.yview)
OutputBox.configure(font=("Arial", 10, ))

# Top Footer
TopBar = customtkinter.CTkFrame(master=app, width=800, height =65, )
TopBar.place(x=330, y=15, anchor=tkinter.CENTER)

# Top Main Label
MainLabel = customtkinter.CTkLabel(master=app, text="Welcome to Roblox Account Creator X v0.1", width=240, height=50, corner_radius=8, bg_color="#212121")
MainLabel.place(x=325, y=20, anchor=tkinter.CENTER)
MainLabel.configure(font=("Arial", 25, ))

# Bottom Label
BottomLabel = customtkinter.CTkLabel(master=app, text="Amount of accounts:", width=240, height=50, corner_radius=8, bg_color="#242424")
BottomLabel.place(x=120, y=295, anchor=tkinter.CENTER)
BottomLabel.configure(font=("Arial", 25, ))

# Warning Label
WarningLabel = customtkinter.CTkLabel(master=app, text="WARNING! The program may show not \n responding while creating the \n accounts, wait for it to stop \n generating and it will go away \n \n Please do not spam the create \n account button, wait for it to \n display in the output box.", width=120, height=50, corner_radius=8, bg_color="#242424")
WarningLabel.place(x=455, y=135, anchor=tkinter.CENTER, )
WarningLabel.configure(font=("Arial", 15, ))

# Text Input
CodeInput = customtkinter.CTkTextbox(master=app, width=250, height=40)
CodeInput.place(x=360, y=295, anchor=tkinter.CENTER)
CodeInput.configure(font=("Arial", 15))

app.mainloop()
