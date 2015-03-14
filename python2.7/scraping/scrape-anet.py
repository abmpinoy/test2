#!/usr/bin/env python

from bs4 import BeautifulSoup as bs
import requests

req = requests.get('https://www.atlantic.net/hosting-services/')
soup = bs(req.content)
#print soup.prettify()

links = soup.find_all('form')
print links
