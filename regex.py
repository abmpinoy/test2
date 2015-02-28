#!/usr/bin/env python
import re

for line in open('/var/log/auth.log'):
    test = re.search(r".* from (.*): 11", line)
    if test:
        print test.group(1)
