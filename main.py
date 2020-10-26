# This is a sample Python script.
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from datetime import *
import requests
import re

def create_soup_object(url):
    response = requests.get(url)
    print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser')

    return soup


if __name__ == '__main__':
    url = 'https://www.marketwatch.com/tools/ipo-calendar' #'https://www.nasdaq.com/market-activity/ipos'
    print(url)

    print('soupin')
    soup = create_soup_object(url)

    ipos = soup.find_all('tr', {'class': 'table__row'})

    companies = []
    #print(ipos[0])
    for ipo in ipos:
        row = ipo.find_all('td', {'class': 'table__cell'})
        data = []

        for point in row:
            data.append(point.text)

        companies.append(data)

    print('original scraped companies: ', len(companies))


    cleaned = []
    for company in companies:
        if len(company) <= 5:
            cleaned.append(company)

    print('cleaned companies: ', len(cleaned))

    df = pd.DataFrame(cleaned, columns=['name', 'ticker','se', 'price', 'available_shares'])
    df['name'] = df.name.str.replace('\n' , '')
    df.to_csv('test.csv', index=False)

    #for i, ipo in enumerate(ipos):
    #    print(i)
    #    print(ipo.text)
