__author__ = 'JACKIE CHAN'


class athing():

    def __init__(self):
        self.thing = "a thing"


    def get_thing(self):
        print self.thing



class bthing():


    def __init__(self):
        self.thing = "bs thing"


    def get_thing(self):
        print "FUCK PYTHON"


abthing = bthing()
aathing = athing()

blah = [aathing, abthing]
for x in blah:
    x.get_thing()