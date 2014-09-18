#! /usr/bin/python

#=============================================================================== 
# Card Factory interface for creating of card objects
#
# check for what type shall be created and run that specific method
#===============================================================================
class CardFactory:

    def createCard(self, type):
        if type == "Color": return ColorCard()
        if type == "Student": return StudentCard()
        assert 0, "No card type: " + type
    factory = staticmethod(createCard)
    
#===============================================================================
# creating of the actual card object - head of factory
#
# class with shared methods, accessible from all factory types
#===============================================================================
class Card(object):
    def __init__(self):
        self.cardID = "EmptyID"
        
    def setID(self, uid):
        self.cardID = uid
        
    def getID(self):
        return self.cardID
    
#===============================================================================
# factory type of card: Color Card
#
# special methods only needed for color cards
#===============================================================================
class ColorCard(Card):
    def __init__(self):
        self.color = "EmptyColor"
    
    def setColor(self, definedColorName): 
        self.color = definedColorName
    
    def getColor(self):
        return self.color
    
#==============================================================================
# factory type of card: Student Card 
#
# special methods only needed for student cards
#==============================================================================
class StudentCard(Card):
    def __init__(self):
        self.name = "EmptyStudent"
    
    def setName(self, definedStudentName):
        self.name = definedStudentName
        
    def getName(self):
        return self.name
    
    

    