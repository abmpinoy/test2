#!/usr/bin/env python

from vars import *
import requests as req
import uuid
from urllib import urlencode

Action = "describe-image"
Timestamp = int(float(time.time()))
Rndguid = str(uuid.uuid4())
string_to_sign = str(Timestamp) + Rndguid
message = bytes(string_to_sign).encode('utf-8')
secret = bytes(priv_key).encode('utf-8')
Signature = urlencode({'Signature':base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())})

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

# Pull data
'''
displayname: FreeBSD 10.1 Server 64-Bit
imageid: FreeBSD-10.1_64bit
ostype: linux
platform: linux
architecture: amd64
owner: atlantic
'''

data = req.get(r).json()
#print data
items =  data['describe-imageresponse']['imagesset']

for item in items:
    img = items[item]
    print "imageid: " + img['imageid']
print
