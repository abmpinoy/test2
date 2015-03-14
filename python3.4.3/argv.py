#! /home/virtualenvs/python3/bin/python

import requests

from sys import argv

x = input('this is a print test: ')
print('this is your output ' + x)

for i in argv:
    print(i)
