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
        randomColor = (GameLogic.getRandomNumber(self) -1)
        print ("random Color Number" , randomColor)
        checkType = type(cardManager.CardManager().getCardByNumber(randomColor))
        print ("typ: " ,checkType)
        if (isinstance(cardManager.CardManager().getCard(randomColor), cardFactory.ColorCard)):
            receivedCard = cardManager.CardManager().getCard(randomColor).getColor()           
        else :
            receivedCard = cardManager.CardManager().getCard(randomColor).getName()    
        return receivedCard
     
        
        
#GameLogic()        