#! /usr/bin/python
'''
Created on Aug 24, 2014

@author: des
'''

# import random
# import cardManager
# import cardFactory
import controller
import gameLogics
import timeMeasure
import rFIDReader

import singleton


class GamePlayManager(metaclass=singleton.Singleton):
    
    def __init__(self):
        '''
        Constructor
        '''
        self.activeGamePlayStrategy = 0
        print("gamePlayStrategy init")
        self.gameStrategies = []
        self.gameStrategies.append(GameStrategyEasy())
        self.gameStrategies.append(GameStrategyAdvanced())
        #self.gameStrategyEasy = GameStrategyEasy()
        #self.gameStrategyAdvanced = GameStrategyAdvanced()
           
           
            
    def getGamePlayMode(self):
        print("Mode is currently: ", self.activeGamePlayStrategy) 
        return self.activeGamePlayStrategy
        
    def setGamePlayMode(self, newMode):
        self.activeGamePlayStrategy = newMode
        controller.GameController().registerGameStrategy(self.gameStrategies[self.activeGamePlayStrategy])
          
        print("Mode has been set to: ", self.activeGamePlayStrategy) 


class GamePlayStrategy(object):
    '''
    this class holds the game logics for the GUI
    '''

    def __init__(self):
        '''
        Constructor
        '''           
           
            
    def play(self):
        # explicitly set it up so this can't be called directly
        raise NotImplementedError('Exception raised, GameStrategy is supposed to be an interface / abstract class!')


        
        
        
    
  
  
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
        
        print("gameStrategyEasy register")
        controller.GameController().registerGameStrategy(self)
        
    def play(self):
        print ("Started Easy Mode")
        # Nur zum Test
        controller.GameController().updateCurrentCardbyColor("red")

        
        self.activeDescription = gameLogics.GameLogic.getRandomDescription(self)
        self.activeColorParsing = self.activeDescription.islower()
        print("Current Card: ", self.activeDescription)
        
        controller.GameController().updateCurrentCardbyColor(self.activeColorParsing)
        
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
        print("gameStrategyAdvanced register")
        controller.GameController().registerGameStrategy(self)    
        
    def play(self):
        print ("Started Advanced Mode")          
