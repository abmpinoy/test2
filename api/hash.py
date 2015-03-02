#!/usr/bin/env python

import string, random, time, hashlib, hmac, base64

def id_generator(size=20, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

priv_key = "5408e3d4de33c7adfdbf72ed648bddc80609890a"
Timestamp= int(float(time.time()))
Rndguid = id_generator()

# Prepare signature
string_to_sign = str(Timestamp) + Rndguid
message = bytes(string_to_sign).encode('utf-8')
secret = bytes(priv_key).encode('utf-8')

# Hash signature
Signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())


print "Timestamp: " + str(Timestamp)
print "Rndguid: " + Rndguid
print "string_to_sign: " + string_to_sign
print "message: " + message
print "secret: " + secret
print "Signature: " + Signature + "\n"
