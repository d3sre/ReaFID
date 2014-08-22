#! /usr/bin/python

class StrategieCards(object):

    def __init__(self, strategy=None):
        self.action = None
        self.count = 0
        if strategy: 
            self.action = strategy()

    def assignCards(self, uid):
        self.cardName = "Test"
        self.cardUid = uid
        print("Test UID: " , self.cardUid)
        
        
class StrategieCardBlue(StrategieCards):
    def __init__(self):
        StrategieCards.__init__(self, assignCard)
        self.cardName = "Blue"
        print("Blue UID: " , self.cardUid)
        
class StrategieCardRed(StrategieCards):
    def assignCards(self, uid):
        self.cardName = "Red"
        self.cardUid = uid   
        print("Red UID: " , self.cardUid)
        
class StrategieCardGreen(StrategieCards):
    def assignCards(self, uid):
        self.cardName = "Green"
        self.cardUid = uid
        print("Green UID: " , self.cardUid)
        
        
def assignCard(self,uid):
    self.cardUid = uid
    return self.cardUid
        
        
if __name__ == "__main__":      
    
    blueCard = StrategieCards(StrategieCardBlue("B2 FB 30 E9"))
    blueCard.assignCards()