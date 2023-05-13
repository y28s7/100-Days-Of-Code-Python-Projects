import time
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\Users\shahn\OneDrive\Documents\Development\chromedriver.exe"
# Following code makes sure that browser doesn't automatically close and makes it start maximized #
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
# ----------------------------------------------------------------------------------------------- #
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
# Waits for website to load
time.sleep(2.5)

# Following code automatically accepts cookies #
try:
    accept_cookies_link = driver.find_element(By.LINK_TEXT, "Got it!")
    accept_cookies_link.click()
    print("Successfully accepted cookies.")
except NoSuchElementException:
    print("Website not loaded yet, could not accept cookies. Waiting for website to load...")
    time.sleep(2.5)
# -------------------------------------------- #

cookie = driver.find_element(By.ID, "cookie")

timeout = time.time() + 5 * 60  # 5 minutes from now
short_timeout = time.time() + 5  # short_timeout = five seconds from now
while True:
    if time.time() > short_timeout:
        affordable_items = []
        store = driver.find_elements(By.CSS_SELECTOR, "#store div")
        store.reverse()
        for item in store:
            if item.get_attribute("class") != "grayed":
                affordable_items.append(item)
        affordable_items[0].click()
        short_timeout = time.time() + 5
    if time.time() > timeout:
        print("Ending bot...")
        cps_raw = driver.find_element(By.ID, "cps")
        cps = cps_raw.text.split(":")[1].strip()
        break
    try:
        cookie.click()
    except NoSuchElementException:
        print("Element not found. Try again")
        time.sleep(1)
    except NoSuchWindowException:
        print("Window has been closed.")
        break
print(cps)
