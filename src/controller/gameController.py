
import model.gamePlayModes as gamePlayModes
import model.rFIDReader as rFIDReader
import model.cardManager as cardManager
import model.cardFactory as cardFactory

import model.singleton as singleton

#===============================================================================
# Game Controller
#
# central controller for GUI - Model interaction
#===============================================================================
# Error can be ignored
class GameController(metaclass=singleton.Singleton):

    def __init__(self):
        print("GameController().__init__")
        self.gameStrategy = None
        self.mainGui = None
        self.gamePlayMode = None
        self.serial = None
        self.cardManager = None
 
#''' Register Variables '''        
    def registerGameStrategy(self, gameStrategy):
        self.gameStrategy = gameStrategy

    def registerMainGui(self, mainGui):
        self.mainGui = mainGui
        
    def registerSerial(self, serial):
        self.serial = serial   
        
    def registerCardManager(self, cardManager):
        self.cardManager = cardManager    
    
#''' get and set configuration (connection between model and view) '''
    def setSerialInterface(self, serial):
        rFIDReader.RFIDReader().setSerialInterface(serial)      
    
    def getSerialInterface(self):
        return rFIDReader.RFIDReader().getSerialInterface()    

    def setCurrentGameStrategy(self, gameStrategy):
        gamePlayModes.GamePlayManager().setGamePlayMode(gameStrategy)

    def getCurrentGameStrategy(self):
        return gamePlayModes.GamePlayManager().getGamePlayMode()
    
    def getCardManager(self):
        return cardManager.CardManager()
    
#''' update view /game features '''   
    def updateCurrentCardbyColor(self, color):
        if (self.mainGui is not None):
            self.mainGui.setCardColor(color.lower())
            self.mainGui.setCardName(color)
        
       
    def startGame(self):
        print("startGame")
        if (self.gameStrategy is not None):
            print("Not none")
            self.gameStrategy.play()
        else:
            print("None")
            
    def addNewCard(self):
        cardFactory.CardFactory.createCard(self, "Color")  
              
    def updateCard(self, card, id, desc, type):
        if isinstance(card, cardFactory.ColorCard):
            cardManager.CardManager.editCard(self, card, id, desc)
            print("Updated Color Card")
        elif isinstance(card, cardFactory.StudentCard):  
            cardManager.CardManager.editCard(self, card, id, desc)
            print("Updated Student Card")
        else : print("method for this type of card not programmed")        
            
                 