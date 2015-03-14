
#!/usr/bin/env python

class vehicle(object):
    def __init__(self, color,make,model):
        self.color = color
        self.make = make
        self.model = model
    def blah(self):
        print "test test test"

class car(vehicle):
    def test(self):
	print self.color
        print self.make
        print self.model

c = car('red','honda','accord')
c.blah('self')
