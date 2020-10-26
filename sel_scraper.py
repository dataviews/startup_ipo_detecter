from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from datetime import *
import requests
import re
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# path to chromedriver.exe
path = '/Users/dominiklambersy/PycharmProjects/startup_ipo_detecter/ext/chromedriver'

# create instance of webdriver
# driver = webdriver.Chrome(path)

# Use the headless option to avoid opening a new browser window
options = webdriver.ChromeOptions()
#options.add_argument("headless")
desired_capabilities = options.to_capabilities()
driver = webdriver.Chrome(path, desired_capabilities=desired_capabilities)
# google url
url = 'https://www.nasdaq.com/market-activity/ipos'

# Code to open a specific url
driver.get(url)

# we find the search bar using it's name attribute value


table = driver.find_elements_by_class_name("market-calendar-table__row")

companies = []

for i, items in enumerate(table):
    print(i)
    ipo = items.text
    companies.append(ipo)


    if i == 3: ## computational limiter for now
        print(companies)
        break

clean= []

for ipo in companies:
    ipo = ipo.replace(' ', '/xex/') ## placeholder to later use strip() appropriately
    ipo = ipo.replace('\n', ' ')

    item_list = ipo.split()
    item_list_clean = []
    for row in item_list:
        temp = row.replace('/xex/', ' ')
        item_list_clean.append(temp)


    clean.append(item_list_clean)

cols = ['symbol', 'name', 'market', 'price', 'shares', 'date', 'nr_shares', 'actions']

df = pd.DataFrame(clean, columns=cols)
print(df)

