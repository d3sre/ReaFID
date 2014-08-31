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
import time
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
        self.myCardManager = controller.GameController().getCardManager()
        self.numberOfRounds = 10
        
        print("gameStrategyEasy register")
        controller.GameController().registerGameStrategy(self)
        
    def play(self):
        print ("Started Easy Mode")
        # Nur zum Test
        #controller.GameController().updateCurrentCardbyColor("red")
        activeRound = 0
        while (activeRound < self.numberOfRounds):
            print("-------------next round")
            self.showNeededCard()
            self.readSignal()
            ### game round
            #startTime = self.myTimeMeasure.startTimer()
            #print("Start Counter at ", startTime)
            #readUid = self.myRFIDReaderConnection.readUID()
            #print("Read UID is ", str(readUid()) )
            timeNeeded = self.myTimeMeasure.getTime()
            print("Time needed was: ", timeNeeded)
            print("total time in gamePlayModes: ", self.myTimeMeasure.totalTime())

            ###
            time.sleep(2)
            activeRound +=1
        self.myRFIDReaderConnection.stopReading()
        print("end time in gamePlayModes: ", self.myTimeMeasure.totalTime())
        print("stopped reading rfid signal")   
            
    def showNeededCard(self):
        self.activeDescription = gameLogics.GameLogic.getRandomDescription(self)
        self.activeColorParsing = self.activeDescription.islower()
        print("Current Card: ", self.activeDescription)
#        print("ActiveColorParsing: ", self.activeColorParsing)
        
        rFIDReader.RFIDReaderClass().flushSerialInput()    
        controller.GameController().updateCurrentCardbyColor(self.activeDescription)    
                
    def readSignal(self):
        startTime = self.myTimeMeasure.startTimer()
        print("Start Counter at ", startTime)  
        readUid = self.myRFIDReaderConnection.readUID()  
         
        stringUid = readUid.decode(encoding='UTF-8')
        print("read UID: ", readUid)
        print("string UID: ", stringUid)
        readCard = self.myCardManager.getCardByID(stringUid)
        readDescription = readCard.getColor()
        print("read Description: ", readDescription )
            
            
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
