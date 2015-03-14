#!/usr/bin/env python

from vars import *
import requests as req
from urllib import urlencode
import uuid

def listinst():
	Action = "list-instances"
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

	# Pull data
	data = req.get(r).json()
	# print data
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


listinst()
