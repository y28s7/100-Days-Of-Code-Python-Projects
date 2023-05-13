import pprint

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = r"C:\Users\shahn\OneDrive\Documents\Development\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get("https://www.python.org")

dates = driver.find_elements(By.CSS_SELECTOR, "div.event-widget > div.shrubbery > ul.menu > li > time")
titles = driver.find_elements(By.CSS_SELECTOR, "div.event-widget > div.shrubbery > ul.menu > li > a")
dates = [date.text for date in dates]
titles = [title.text for title in titles]

result = {}
for i in range(len(dates)):
    result[i] = {"date": dates[i], "title": titles[i]}

print(result)

driver.quit()
