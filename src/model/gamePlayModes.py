#! /usr/bin/python
'''
Created on Aug 24, 2014

@author: des
'''

# import random
# import cardManager
# import cardFactory
import gameLogics
import timeMeasure
import rFIDReader

import singleton

class GamePlayStrategy(metaclass=singleton.Singleton):
    '''
    this class holds the game logics for the GUI
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.activeGamePlayStrategy = 1
        
            
    def getGamePlayMode(self):
        print("Mode is currently: ", self.activeGamePlayStrategy) 
        return self.activeGamePlayStrategy
        
    def setGamePlayMode(self, newMode):
        self.activeGamePlayStrategy = newMode  
        print("Mode has been set to: ", self.activeGamePlayStrategy)     

    

        
        
        
    
  
  
class GameStrategyEasy(GamePlayStrategy):
    '''
    this class holds the game logics for the GUI
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.myTimeMeasure = timeMeasure.timeMeasureClass()
        self.myRFIDReaderConnection = rFIDReader.RFIDReaderClass()
        self.numberOfRounds = 10
        
        self.gameStrategyEasy()
        
    def gameStrategyEasy(self):
        print ("Started Easy Mode")
        self.activeDescription = gameLogics.GameLogic.getRandomDescription(self)
        self.activeColorParsing = self.activeDescription.islower()
        
        ### game round
        startTime = self.myTimeMeasure.startTimer()
        print("Start Counter at ", startTime)
        readUid = self.myRFIDReaderConnection.readUID()
        print("Read UID is ", readUid() )
        endTime = self.myTimeMeasure.getTime()
        print("End Counter at ", endTime)
        ###
            
            
            
class GameStrategyAdvanced(GamePlayStrategy):
    '''
    this class holds the game logics for the GUI
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.gameStrategyAdvanced()
        
    def gameStrategyAdvanced(self):
        print ("Started Advanced Mode")          
          