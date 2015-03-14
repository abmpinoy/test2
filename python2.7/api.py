#!/usr/bin/env python

import requests

response = requests.get("https://atlantic.net/")
print response.headers
print response.status_code
print response.body
