#!/usr/bin/env python

import json, random, hashlib, string, time, hmac, base64
import requests as req

def id_generator(size=20, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

urlbase = "https://cloudapi.atlantic.net/api.php/?Action=list-instances&Version=2010-12-30"
ACSAccessKeyId = "ATL981de504cb0f5c4528d959abe0fd465b"
priv_key = "5408e3d4de33c7adfdbf72ed648bddc80609890a"
Format = "json"
Timestamp= int(float(time.time()))
Rndguid = id_generator()
string_to_sign = str(Timestamp) + Rndguid
message = bytes(string_to_sign).encode('utf-8')
secret = bytes(priv_key).encode('utf-8')
Signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())
#Signature = hashlib.sha256(message + secret).digest().encode("base64")

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
items =  data['list-instancesresponse']['instancesSet']

# Count VMs and output their data
count = 0
for item in items:
    vmdata = items[item]
    print "Name: " + vmdata['vm_description']
    print "OS: " + vmdata['vm_image']
    print "Instance ID: " + vmdata['InstanceId']
    print "IP: " + vmdata['vm_ip_address']
    print "RAM: " + vmdata['vm_ram_req']
    print "CPU Cores: " + vmdata['vm_cpu_req']
    print "Disk Size: " + vmdata['vm_disk_req']
    print "Created on: " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(vmdata['vm_created_date']))) + "\n"
    count+=1
print str(count) + " Virtual Machines detected"
