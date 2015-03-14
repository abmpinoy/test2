#!/usr/bin/env python

import itertools

def is_even(x):
    print 'is_even called for %d' % (x,)
    return x % 2 == 0

def even():
    return filter(is_even, xrange(20))


print even()[:10]
