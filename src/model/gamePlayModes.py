#! /usr/bin/python
'''
Created on Aug 24, 2014

@author: des
'''

# import random
# import cardManager
# import cardFactory

import singleton
# Error can be ignored
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
        self.gameStrategyEasy()
        
        def gameStrategyEasy():
            print ("Started Easy Mode")
            
            
            
class GameStrategyAdvanced(GamePlayStrategy):
    '''
    this class holds the game logics for the GUI
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.gameStrategyAdvanced()
        
        def gameStrategyAdvanced():
            print ("Started Advanced Mode")          
          