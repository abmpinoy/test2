#!/usr/bin/env python

import subprocess as sub

x = range(33,63)
for num in x:
    ip = '69.28.20.' + str(num)
    print sub.Popen(('host',ip), stdout=sub.PIPE).stdout.read(),
