#!/usr/bin/env python

import json, random, hashlib, string, time, hmac, base64
import requests as req

def id_generator(size=20, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

urlbase = "https://cloudapi.atlantic.net/api.php/?Action=describe-plan&Version=2010-12-30"
ACSAccessKeyId = "ATL981de504cb0f5c4528d959abe0fd465b"
priv_key = "5408e3d4de33c7adfdbf72ed648bddc80609890a"
Format = "json"
Timestamp= int(float(time.time()))
Rndguid = id_generator()
string_to_sign = str(Timestamp) + Rndguid
message = bytes(string_to_sign).encode('utf-8')
secret = bytes(priv_key).encode('utf-8')
Signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())


# Assemble query
r = urlbase + "&ACSAccessKeyId=" + ACSAccessKeyId + "&Format=" + Format \
+ "&Timestamp=" + str(Timestamp) + "&Rndguid=" + Rndguid + "&Signature=" + Signature
print "\nQuery:"
print r + "\n"

print "Debug information: "
print "Timestamp: " + str(Timestamp)
print "Rndguid: " + Rndguid
print "string_to_sign: " + string_to_sign
print "message: " + message
print "secret: " + secret
print "Signature: " + Signature + "\n"

# Pull data
data = req.get(r).json()
print data
items =  data['describe-planresponse']['plans']

for item in items:
    img = items[item]
    for attrib in img:
        print attrib + ": " + str(img[attrib])
    print
