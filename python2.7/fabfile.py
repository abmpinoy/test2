#!/usr/bin/env python

from fabric.api import *

env.hosts=["209.208.108.246"]

env.user="root"
def hostname_check():
    run("cat /var/log/syslog | grep cron --color")
