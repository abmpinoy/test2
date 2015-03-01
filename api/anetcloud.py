#!/usr/bin/env python

import json
import requests as req
import random
import hashlib
import string
import time
import hmac
import base64

def id_generator(size=20, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

urlbase = "https://cloudapi.atlantic.net/api.php/?Action=list-instances"
Version = "2010-12-30"
ACSAccessKeyId = "ATL981de504cb0f5c4528d959abe0fd465b"
Format = "json"
Timestamp= int(float(time.time()))
Rndguid = id_generator()
string_to_sign = str(Timestamp) + Rndguid
priv_key = "5408e3d4de33c7adfdbf72ed648bddc80609890a"
message = bytes(string_to_sign).encode('utf-8')
secret = bytes(priv_key).encode('utf-8')
signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())
