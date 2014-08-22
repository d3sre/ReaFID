#! /usr/bin/python

class safeRFIDCards:

    def __init__(self):
        import pickle
        self.card1 =""
        self.card2 =""
        self.card3 =""

    def assignCards(self, uid):
        self.card1 = uid
        return self.card1

    def saveConfig(self):
        print("done")
