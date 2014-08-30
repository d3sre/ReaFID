'''
Created on Aug 24, 2014

@author: des
'''
import sys
sys.path.append('git/ReaFID/src/model/')
sys.path.append('git/ReaFID/src/view/')

import gamePlayModes
import singleton
import tkinter as tk
import mainGUI
import cardManager
import cardFactory

# Error can be ignored
class GameController(metaclass=singleton.Singleton):
    '''
    controller for interaction with GUI
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.myGameStrategy = gamePlayModes.GamePlayStrategy()
        self.myCardManager = cardManager.CardManager()
        
        
    def registerGameStrategy(self, newMode):
        self.myGameStrategy.setGamePlayMode(newMode)
        
    def activeGameStrategy(self):
        return self.myGameStrategy.getGamePlayMode()
            
        
        
    def registerGUI(self):
        # find start params for GUI
        print ("register GUI")

        

    def setVariableCanvas(self):
        print ("variable canvas")
        
    def getCardInformation(self):
        self.currentCard = self.myCardManager.getCardByNumber(self,0)
        
        if (isinstance(self.currentCard, cardFactory.ColorCard)):
            self.gameColor = self.currentCard.getColor()
            return self.gameColor
        elif (isinstance(self.currentCard, cardFactory.StudentCard)):
            self.gameName = self.currentCard.getName()
            return self.gameName
        else:
            print("Unknown card type")
     
        
            

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