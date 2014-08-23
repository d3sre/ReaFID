#! /usr/bin/python

import rFIDReader
import cardFactory
import pickle


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class CardManager(metaclass=Singleton):
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
  
    def getCard(self, id):
        for card in self.activeCards:
            if card.getID() == id:
                print("Found card: ", card.getID())
                return card
            
    def removeCard(self, card):
        self.activeCards.remove(card)
        
        
    def saveConfiguration(self):
        with open('data.pickle', 'wb') as f:
            pickle.dump(self.activeCards, f, pickle.HIGHEST_PROTOCOL)

    def loadConfiguration(self):
        with open('data.pickle', 'rb') as f:
            self.activeCards = pickle.load(f)
