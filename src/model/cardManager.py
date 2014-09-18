#! /usr/bin/python

import model.cardFactory as cardFactory
import pickle
import model.singleton as singleton



#===============================================================================
# Card Manager Class
#
# manages the cards, controls that there's only one manager, handles all the 
# interaction and access to card objects
#===============================================================================
class CardManager(metaclass=singleton.Singleton):
    def __init__(self):
        self.activeCards = []
                 

""" add card object to array """
    def addCard(self, card):
        self.activeCards.append(card)

""" print out all cards in manager """
    def outputCards(self):
        if self.activeCards:
            for card in self.activeCards:
                if isinstance(card, cardFactory.ColorCard):                 # check what type of card object it is
                    print("Uid: " , card.getID(), "Typ: Color , Name: ", card.getColor())
                elif isinstance(card, cardFactory.StudentCard):
                    print("Uid: " , card.getID(), "Typ: Student , Name: ", card.getName())
                else : print("Unknown card type")
        else : print("No cards found")

""" get card by uid """  
    def getCardByID(self, uid):
        for card in self.activeCards:
            if card.getID() == uid:
                print("Found card: ", card.getID())
                return card

""" get card by the number it has in the array """            
    def getCardByNumber(self, number):
        return self.activeCards[number]
             
""" remove card from activeCards array """            
    def removeCard(self, card):
        self.activeCards.remove(card)
        
""" pickle the configuration - store array """        
    def saveConfiguration(self):
        with open('cardPickle.pickle', 'wb') as f:
            pickle.dump(self.activeCards, f, pickle.HIGHEST_PROTOCOL)

""" load pickle configuration """
    def loadConfiguration(self):
        with open('cardPickle.pickle', 'rb') as f:
            self.activeCards = pickle.load(f)

""" get size of array - for only get right random value """
    def getSizeCardArray(self):
        return len(self.activeCards)
    
""" get empty manager - clear array """    
    def getEmptyManager(self, list):
        return self.activeCards.clear()