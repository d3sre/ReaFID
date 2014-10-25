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
                 


    def addCard(self, card):
        ''' add card object to array '''
        self.activeCards.append(card)


    def outputCards(self):
        ''' print out all cards in manager '''
        if self.activeCards:
            for card in self.activeCards:
                if isinstance(card, cardFactory.ColorCard):                 # check what type of card object it is
                    print("Uid: " , card.getID(), "Typ: Color , Name: ", card.getColor())
                elif isinstance(card, cardFactory.StudentCard):
                    print("Uid: " , card.getID(), "Typ: Student , Name: ", card.getName())
                else : print("Unknown card type")
        else : print("No cards found")

  
    def getCardByID(self, uid):
        ''' get card by uid '''
        for card in self.activeCards:
            if card.getID() == uid:
                print("Found card: ", card.getID())
                return card

            
    def getCardByNumber(self, number):
        ''' get card by the number it has in the array '''
        return self.activeCards[number]
             
           
    def removeCard(self, card):
        ''' remove card from activeCards array ''' 
        self.activeCards.remove(card)
        
       
    def saveConfiguration(self):
        ''' pickle the configuration - store array ''' 
        with open('cardPickle.pickle', 'wb') as f:
            pickle.dump(self.activeCards, f, pickle.HIGHEST_PROTOCOL)


    def loadConfiguration(self):
        ''' load pickle configuration '''
        with open('cardPickle.pickle', 'rb') as f:
            self.activeCards = pickle.load(f)


    def getSizeCardArray(self):
        ''' get size of array - for only get right random value '''
        return len(self.activeCards)
    
    
    def getEmptyManager(self, list):
        ''' get empty manager - clear array '''
        return self.activeCards.clear()
    
    def editCard(self, card, uid, name):
        if isinstance(card, cardFactory.ColorCard):
            card.setID(uid)
            card.setColor(name)
        elif isinstance(card, cardFactory.StudentCard):
            card.setID(uid)
            card.setName(name)
        else: print ("Error with card occured")