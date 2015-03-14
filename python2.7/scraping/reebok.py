#!/usr/bin/env python

# http://www.reebok.com/us/reebok-crossfit-nano-4.0/M40521.html?pr=CUSTOMIZE_IMG_Reebok%2520CrossFit%2520Nano%25204.0

from bs4 import BeautifulSoup as bs
import requests

req = requests.get('http://www.reebok.com/us/reebok-crossfit-nano-4.0/M40521.html?pr=CUSTOMIZE_IMG_Reebok%2520CrossFit%2520Nano%25204.0')
data = req.text

soup = bs(data)

for link in soup.find_all('span'):
    p = link.get('data-sale-price')
    if p is not None:
        print int(float(p))
