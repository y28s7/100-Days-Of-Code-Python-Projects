# NOTE: This program is still very buggy, and sometimes does not work for reasons I don't know. Also, it doesn't get
# save all the jobs in the list for some reason, and I can't get it to scroll, so I'm just going to leave this
# program's functionality at here.
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
from dotenv import load_dotenv

load_dotenv(dotenv_path=r"C:\Users\shahn\Python Code\Pycharm Env Vars\linkedin-sign-in.env")

username = os.environ["LINKEDIN_USERNAME"]
password = os.environ["LINKEDIN_PASSWORD"]
chrome_driver_path = r"C:\Users\shahn\OneDrive\Documents\Development\chromedriver.exe"
# Following code makes sure that browser doesn't automatically close and makes it start maximized #
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
# ----------------------------------------------------------------------------------------------- #
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
driver.get("https://www.linkedin.com/jobs/search?keywords=Python%2BDeveloper&location=Bergen%2BCounty%2C%2BNew"
           "%2BJersey%2C%2BUnited%2BStates&geoId=101975700&trk=public_jobs_jobs-search-bar_search-submit&currentJobId"
           "=3571257415&position=1&pageNum=0")
login_page_redirect = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
login_page_redirect.click()

email_input = driver.find_element(By.ID, "username")
email_input.send_keys(username)

password_input = driver.find_element(By.ID, "password")
password_input.send_keys(password)
time.sleep(1)  # give the linkedin website a breather
password_input.send_keys(Keys.ENTER)

time.sleep(2.5)  # let website load

job_offerings_on_screen = driver.find_elements(By.CLASS_NAME, "job-card-list__title")
for job in job_offerings_on_screen:
    try:
        job.click()
    except ElementClickInterceptedException:
        while True:
            try:
                x_button = driver.find_element(By.CLASS_NAME, "artdeco-toast-item__dismiss")
                x_button.click()
            except NoSuchElementException:
                break

    time.sleep(1)

    save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    print(save_button.text)
    save_status = save_button.text.split()[0]
    if save_status == "Save":
        save_button.click()
