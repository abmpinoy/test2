#!/usr/bin/env python

from vars import *
import requests as req
from urllib import urlencode
import uuid

# Set method
Action = "describe-plan"
Timestamp = int(float(time.time()))
Rndguid = str(uuid.uuid4())
string_to_sign = str(Timestamp) + Rndguid
message = bytes(string_to_sign).encode('utf-8')
secret = bytes(priv_key).encode('utf-8')
Signature = urlencode({'Signature':base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())})

# Assemble query
r = urlbase + "Action=" + Action + Version + ACSAccessKeyId + Format + "&Timestamp=" + str(Timestamp) + "&Rndguid=" + Rndguid + "&" + Signature

print "\nQuery:"
print r + "\n"

print "Debug information: "
print "Timestamp: " + str(Timestamp)
print "Rndguid: " + Rndguid
print "string_to_sign: " + string_to_sign
print "message: " + message
print "secret: " + secret
print "Signature: " + Signature + "\n"

#Pull data
data = req.get(r).json()
#print data

items =  data['describe-planresponse']['plans']

for item in items:
    img = items[item]
    for attrib in img:
        print attrib + ": " + str(img[attrib])
    print
