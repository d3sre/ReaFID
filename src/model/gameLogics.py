'''
Created on Aug 24, 2014

@author: des
'''

import random
import cardManager

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
        validRandomNumber = random.randint(0,cardArraySize)
        print ("validRandomNumber:", validRandomNumber)
        return validRandomNumber
    
    def getRandomDescription(self):
        randomColor = (GameLogic.getRandomNumber(self))
        print ("random Color Number" , randomColor)
 #       checkType = type(cardManager.CardManager().getCardByNumber(randomColor))
 #       print ("typ: " ,checkType)
#         if (isinstance(cardManager.CardManager().getCard(randomColor, "Color"))):
#             receivedCard = cardManager.CardManager().getCard(randomColor).getColor()           
#         else :
#             receivedCard = cardManager.CardManager().getCard(randomColor).getName()    
#        return receivedCard
     
        
        
GameLogic()        