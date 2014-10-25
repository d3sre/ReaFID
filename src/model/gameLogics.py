#! /usr/bin/python


import random
import model.cardManager as cardManager
import model.cardFactory as cardFactory

#===============================================================================
# Game Logic class 
#
# methods for use during the game strategy
#===============================================================================
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
        ''' select a random number - but only  valid in the range of available cards '''  
        cardArraySize = cardManager.CardManager().getSizeCardArray()
#        print ("cardArraySize:", cardArraySize)
        if (cardArraySize != 0):
            validRandomNumber = random.randint(1,cardArraySize)
#            print ("validRandomNumber:", validRandomNumber)
            return validRandomNumber
        else : print("Card Manager is still empty")

   
    def getRandomDescription(self):
        ''' get description of the matching card to update the MainGUI ''' 
        randomNumber = (GameLogic.getRandomNumber(self) -1)
        print ("random Color Number" , randomNumber)
        
        card = cardManager.CardManager().getCardByNumber(randomNumber)
        checkType = type(cardManager.CardManager().getCardByNumber(randomNumber))
#        print ("typ: " ,checkType)
        if (isinstance(card, cardFactory.ColorCard)):
#            print("getRandomDescription: Color true")
            receivedCard = card.getColor()           
        else :
#            print("getRandomDescription: Color false")
            receivedCard = card.getName()    
        return receivedCard
     
        
        
#GameLogic()        