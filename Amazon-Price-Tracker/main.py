import os

import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=r"C:\Users\shahn\Python Code\Pycharm Env Vars\email-stuff.env")

TARGET_PRICE = 100

EMAIL = os.environ["EMAIL"]
EMAIL_APP_PASSWORD = os.environ["EMAIL_APP_PASSWORD"]

url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

html_code = requests.get(url=url,
                         headers={
                             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                           "(KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
                             "Accept-Language": "en-US,en;q=0.9",
                             "Cookie": "PHPSESSID=47e2398401cd9cffc1f90fab80454909"
                         }).text

soup = BeautifulSoup(html_code, "lxml")
price_whole = str(soup.select_one("span.a-price-whole")).split(">")[1].split("<")[0]
price_fraction = str(soup.select_one("span.a-price-fraction")).split(">")[1].split("<")[0]
price = float(f"{price_whole}.{price_fraction}")

product_title = soup.select_one(selector="span#productTitle").getText().strip().replace("é", "e")
print(product_title)

if price <= TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=EMAIL_APP_PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject:Sale for {product_title}\n\n{product_title},"
                                                                 f" Now only {price}!\nBuy Now at: {url}")
