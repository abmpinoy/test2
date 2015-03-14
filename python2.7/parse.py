import re

fl = "/var/log/syslog.1"
f = open(fl)

for line in f:
    if re.search(r"cron",line):
        print line.rstrip()

f.close()
