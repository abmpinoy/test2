#!/ur/bin/env python
import time

t = int(float(time.time()))
print t
import hashlib
hash_object = hashlib.sha256(str(t)).hexdigest().encode("base64")
print hash_object

#hex_dig = hash_object.hexdigest()
#print(hex_dig)

