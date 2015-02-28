#!/usr/bin/env python

from bs4 import BeautifulSoup as bs
import requests

req = requests.get('https://www.atlantic.net')
data = req.text

out = bs(data)

def links():
    r = []
    for i in out.find_all('a'):
        x = i.get('href')
        if 'http' in x:
            r.append(x)
    return r

for line in links():
    print line
