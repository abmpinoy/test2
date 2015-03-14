#!/usr/bin/env python

import re
from sys import argv

for line in open(argv[1]):
    try:
        x = re.search(r'PTR     (.*\.[a-zA-Z]{0,3}$)',line).group(1)
        print x
    except:
        pass
'''
    if x:
        y = x.group(1)
        test = re.search(r'(.*\.[a-zA-Z]{0,3}\.)',y)
        if not test:
            print y
'''
