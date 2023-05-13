from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\Users\shahn\OneDrive\Documents\Development\chromedriver.exe"
# Following code makes sure that browser doesn't automatically close #
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# ------------------------------------------------------------------ #
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
driver.get("https://web.archive.org/web/20211121100453/https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

first_name.send_keys("Yugm")
last_name.send_keys("Shah")
email.send_keys("yugsha28@gmail.com" + Keys.ENTER)
