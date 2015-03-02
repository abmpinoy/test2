#!/usr/bin/env python

from vars import *
import requests as req

# Set method
Action = "describe-plan"

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
data = req.get(r).json()
print data
items =  data['describe-planresponse']['plans']

for item in items:
    img = items[item]
    for attrib in img:
        print attrib + ": " + str(img[attrib])
    print
