'''
Created on Aug 24, 2014

@author: des
'''

import model.gamePlayModes as gamePlayModes
import model.rFIDReader as rFIDReader
import model.cardManager as cardManager

import model.singleton as singleton

# Error can be ignored
class GameController(metaclass=singleton.Singleton):
    '''
    controller for interaction with GUI
    '''


    def __init__(self):
        print("GameController().__init__")
        self.gameStrategy = None
        self.mainGui = None
        self.gamePlayMode = None
        self.serial = None
        self.cardManager = None

         
#         '''
#         Constructor
#         '''
#         self.myGameStrategy = gamePlayModes.GamePlayStrategy()
#         self.myCardManager = cardManager.CardManager()
#         
#         
#     def registerGameStrategy(self, newMode):
#         self.myGameStrategy.setGamePlayMode(newMode)
#         
#     def activeGameStrategy(self):
#         return self.myGameStrategy.getGamePlayMode()
 
 
    ### Register Variables        
    def registerGameStrategy(self, gameStrategy):
        self.gameStrategy = gameStrategy

    def registerMainGui(self, mainGui):
        self.mainGui = mainGui
        
    def registerSerial(self, serial):
        self.serial = serial   
        
    def registerCardManager(self, cardManager):
        self.cardManager = cardManager    
    
    ### get and set configuration (connection between model and view)    
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
    
    ### update view /game features    
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
            
            
            
#         
# 
#     def setVariableCanvas(self):
#         print ("variable canvas")
#         
#     def initializeVariables(self, self.app):
#         self.currentCard = self.myCardManager.getCardByNumber(self,0)
#         
#         if (isinstance(self.currentCard, cardFactory.ColorCard)):
#             self.gameColor = self.currentCard.getColor()
#             
#         elif (isinstance(self.currentCard, cardFactory.StudentCard)):
#             self.gameName = self.currentCard.getName()
#             return self.gameName
#         else:
#             print("Unknown card type")
     
        
            

# root = Tk()
# canvas = Canvas(root)
# canvas.pack()
    
#     def tick():
#         time = 60
#         # You have to clear the canvas each time the clock updates 
#         # (otherwise it writes on top of the old time).  Since the
#         # time is the only thing in the canvas, delete(ALL) works
#         # perfectly (if it wasn't however, you can delete the id
#         # that goes with the clock).
#         canvas.delete(ALL)
#         # I have to declare time as a global because I'm not using
#         # a class (otherwise, I could do something like self.time -= 1)
#         global time
#         time -= 1
#         # You can place the time wherever in the canvas
#         # (I chose 10,10 for the example)
#         canvas.create_text(10, 10, text=time)
#         if time == 0:
#             do_something()
#         else:
#             canvas.after(1000, tick)
# canvas.after(1, tick)
# root.mainloop()      