from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = r"C:\Users\shahn\OneDrive\Documents\Development\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
price = driver.find_element(by=By.CLASS_NAME, value="a-price-whole").text
xpath_price = driver.find_element(by=By.XPATH,
                                  value='//*[@id="corePriceDisplay_desktop_feature_div"]'
                                        '/div[1]/span[1]/span[2]/span[2]').text
print(
    f"Price: {price}\n"
    f"Price (found with xpath): {xpath_price}"
)

driver.quit()
