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
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# article_count.click()  # clicks on the article_count link

all_portals_link = driver.find_element(By.LINK_TEXT, "English")
# all_portals_link.click()

search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)
