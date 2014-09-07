#! /usr/bin/python

import model.cardFactory as cardFactory
import pickle
import model.singleton as singleton


# class Singleton(type):
#     _instances = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]

class CardManager(metaclass=singleton.Singleton):
    def __init__(self):
        self.activeCards = []
                 

    # add card object to array
    def addCard(self, card):
        self.activeCards.append(card)

    def outputCards(self):
        if self.activeCards:
            for card in self.activeCards:
                if isinstance(card, cardFactory.ColorCard):
                    print("Uid: " , card.getID(), "Typ: Color , Name: ", card.getColor())
                elif isinstance(card, cardFactory.StudentCard):
                    print("Uid: " , card.getID(), "Typ: Student , Name: ", card.getName())
                else : print("Unknown card type")
        else : print("No cards found")
  
    def getCardByID(self, uid):
        for card in self.activeCards:
            if card.getID() == uid:
                print("Found card: ", card.getID())
                return card

            
    def getCardByNumber(self, number):
        return self.activeCards[number]
             
            
    def removeCard(self, card):
        self.activeCards.remove(card)
        
        
    def saveConfiguration(self):
        with open('cardPickle.pickle', 'wb') as f:
            pickle.dump(self.activeCards, f, pickle.HIGHEST_PROTOCOL)

    def loadConfiguration(self):
        with open('cardPickle.pickle', 'rb') as f:
            self.activeCards = pickle.load(f)

    def getSizeCardArray(self):
        return len(self.activeCards)
    
    def getEmptyManager(self, list):
        return self.activeCards.clear()