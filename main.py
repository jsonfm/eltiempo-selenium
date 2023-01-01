import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome Beta.app/Contents/MacOS/Google Chrome Beta"
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")


browser = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), 
    options=options
)

browser.get("https://eltiempo.es")


button_class = " didomi-components-button didomi-button didomi-dismiss-button didomi-components-button--color didomi-button-highlight highlight-button".replace(" ", ".")
WebDriverWait(browser, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_class)))\
    .click()


search_input_class = "input#term.text-roboto-condensed"
WebDriverWait(browser, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, search_input_class)))\
    .send_keys("Madrid")


search_icon_class = "i.icon.icon-sm.icon-search"
WebDriverWait(browser, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, search_icon_class)))\
    .click()


item_li_class = ".icon_weather_s.icon.icon-sm.icon-city"
WebDriverWait(browser, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, item_li_class)))\
    .click()


xpath_link = '/html/body/div[5]/div[1]/div[4]/div/main/section[3]/section/div/article/section/ul[1]/li[2]/h2/a'
WebDriverWait(browser, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, xpath_link)))\
    .click()


xpath_ul ='//*[@id="cityTable"]/div[1]/ul/li[1]/ul'
WebDriverWait(browser, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, xpath_ul)))\


cols = browser.find_element("xpath", xpath_ul)
cols = cols.text
today = cols.split("\n")
today = today[1:]
# print("today: ", today)

data = {
    "hours": [],
    "temperature": [],
    "wind_speed": [] 
}

for i in range(0, len(today), 7):
    data["hours"].append(today[i])
    data["temperature"].append(today[i + 2])
    data["wind_speed"].append(today[i + 5])


df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)


browser.quit()