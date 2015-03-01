#!/usr/bin/env python

import hashlib
import hmac
import base64

message = bytes("Message").encode('utf-8')
secret = bytes("secret").encode('utf-8')

signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())
print(signature)
