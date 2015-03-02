#!/usr/bin/env python

from vars import *
import requests as req
import subprocess as sub

Action = "run-instance" 
Action_img = "describe-image"

planname =  raw_input("Select VPS size(S,M,L,XL,XXL: ")
servername = raw_input("Server Name: ")

'''
# List images
l = urlbase +  "Action=" + Action_img + "&Version=" + Version + "&ACSAccessKeyId=" + ACSAccessKeyId + "&Format=" + Format \
+ "&Timestamp=" + str(Timestamp) + "&Rndguid=" + Rndguid + "&Signature=" + Signature
print "\nQuery:"
print l + "\n"

ldata = req.get(l).json()
#print data
litems =  ldata['describe-imageresponse']['imagesset']

for litem in litems:
    img = litems[litem]
    print "imageid: " + img['imageid']
'''

for line in sub.Popen(['/home/python/api/get_images.py'], stdout=sub.PIPE).stdout.read().split('\n'):
    print line


imageid = raw_input("\nSelect an image: ")

# Create request
r = urlbase + "Action=" + Action + "&Version=" + Version + "&ACSAccessKeyId=" + ACSAccessKeyId + "&Format=" + Format \
+ "&Timestamp=" + str(Timestamp) + "&Rndguid=" + Rndguid + "&Signature=" + Signature + "&servername=" + servername \
+ "&imageid=" + imageid + "&planname=" + planname.upper()
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
#items =  data['describe-imageresponse']['imagesset']

