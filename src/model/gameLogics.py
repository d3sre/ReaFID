#! /usr/bin/python
'''
Created on Aug 24, 2014

@author: des
'''

import random
import cardManager
import cardFactory

class GameLogic(object):
    '''
    this class holds the game logics for the GUI
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.getRandomDescription()
    
    def getRandomNumber(self):
        cardArraySize = cardManager.CardManager().getSizeCardArray()
#        print ("cardArraySize:", cardArraySize)
        if (cardArraySize != 0):
            validRandomNumber = random.randint(1,cardArraySize)
#            print ("validRandomNumber:", validRandomNumber)
            return validRandomNumber
        else : print("Card Manager is still empty")
    
    def getRandomDescription(self):
        randomNumber = (GameLogic.getRandomNumber(self) -1)
        print ("random Color Number" , randomNumber)
        
        card = cardManager.CardManager().getCardByNumber(randomNumber)
        checkType = type(cardManager.CardManager().getCardByNumber(randomNumber))
        print ("typ: " ,checkType)
        if (isinstance(card, cardFactory.ColorCard)):
            print("getRandomDescription: Color true")
            receivedCard = card.getColor()           
        else :
            print("getRandomDescription: Color false")
            receivedCard = card.getName()    
        return receivedCard
     
        
        
#GameLogic()        