#!/usr/bin/env python

# 03-Mar-2015 14:17:02.585 client 69.252.66.221#46581: query: orldfl-ns-1.atlantic.net IN A -

import timeit
import subprocess as sub, re
from collections import Counter

def test1():
        start = timeit.default_timer()
	# original, slowest
	list = []	
	for line in open('queries.log'):
	    test = re.search(r": query: (.*atlantic.net) IN", line, re.I)
	    if test:
	        list.append(test.group(1))
	cnt = Counter(list)
	
	list2 = [ (cnt[list],list) for list in cnt ]
	
	for entry in sorted(list2, key=lambda asdf: int(asdf[0]), reverse=False):
	    #print entry
	    pass
        stop = timeit.default_timer()
        print stop - start

def test2():
	# improved, a bit faster
        start = timeit.default_timer()
	x = open('queries.log')
	test = re.compile(r": query: (.*atlantic.net) IN",re.I).search	
	list = [ test(line).group(1) for line in x if test(line) ]
	cnt = Counter(list)
	list2 = [ (cnt[list],list) for list in cnt ]
	
	for entry in sorted(list2, key=lambda asdf: int(asdf[0]), reverse=False):
	    #print entry
	    pass
        stop = timeit.default_timer()
        print stop - start


# best speed
def test3():
	start = timeit.default_timer()
        x = open('queries.log').read()
	list = re.findall(r": query: (.*atlantic.net) IN", x, re.I)
	cnt = Counter(list)
        list2 = [ (cnt[i],i) for i in cnt ]
        for entry in sorted(list2, key=lambda asdf: int(asdf[0]), reverse=False):
            #print entry
	    pass
	stop = timeit.default_timer()
	print stop - start


test1()
test2()
test3()
