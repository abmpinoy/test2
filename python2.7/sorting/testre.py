
#!/usr/bin/env python
import re

x = [ "test", "one","two" ]

test = re.compile(r"test").search
for i in x:
    print i
