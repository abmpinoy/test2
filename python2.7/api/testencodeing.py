#!/usr/bin/env python

import sys
from urllib import urlencode
artist = "Kruder & Dorfmeister"
artist = urlencode({'ArtistSearch':artist})
print artist
