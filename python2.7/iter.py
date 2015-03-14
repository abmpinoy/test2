#!/usr/bin/env python
import sys

argv_iter = iter(sys.argv[1:])
def get_next_arg(prompt):
    try:
        return argv_iter.next()
    except StopIteration:
        return raw_input(prompt)


USERNAME = get_next_arg('user login name: ')
REALNAME = get_next_arg('user full name: ')
argv_iter.next()