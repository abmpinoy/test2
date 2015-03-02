#!/usr/bin/env python

from vars import *
import requests as req

Action = "describe-image"

# Assemble query
r = urlbase + "Action=" + Action + "&Version=" + Version + "&ACSAccessKeyId=" + ACSAccessKeyId + "&Format=" + Format \
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
