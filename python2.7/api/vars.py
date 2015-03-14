import json, random, hashlib, string, time, hmac, base64
import requests as req

urlbase = "https://cloudapi.atlantic.net/api.php/?"
Version = "&Version=2010-12-30"
ACSAccessKeyId = "&ACSAccessKeyId=ATL981de504cb0f5c4528d959abe0fd465b"
priv_key = "5408e3d4de33c7adfdbf72ed648bddc80609890a"
Format = "&Format=json"
#Timestamp= int(float(time.time()))
#Rndguid = id_generator()
#string_to_sign = str(Timestamp) + Rndguid
#message = bytes(string_to_sign).encode('utf-8')
#secret = bytes(priv_key).encode('utf-8')
#Signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())
