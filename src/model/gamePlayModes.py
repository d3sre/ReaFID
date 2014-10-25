#! /usr/bin/python

import controller
import model.gameLogics as gameLogics
import model.timeMeasure as timeMeasure
import model.rFIDReader as rFIDReader
import time
import model.singleton as singleton

#===============================================================================
# Game Play Manager Class
#
# singleton to always access the same manager - controls the access to the game 
# strategies
#===============================================================================
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
        controller.gameController.GameController().registerGameStrategy(self.gameStrategies[self.activeGamePlayStrategy])       # registers new game strategy (id) in the controller
          
        print("Mode has been set to: ", self.activeGamePlayStrategy) 


#===============================================================================
# Game Play Strategy 
#
# Strategy class for game strategy, behaves like an interface
#===============================================================================
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

   
#=============================================================================
# Game Strategy Easy
#
# easy strategy with color cards only and simple mode
#=============================================================================
class GameStrategyEasy(GamePlayStrategy):
    '''
    this class holds the game logics for the GUI
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.myTimeMeasure = timeMeasure.TimeMeasure()
        self.myRFIDReaderConnection = rFIDReader.RFIDReader()
        self.myCardManager = controller.gameController.GameController().getCardManager()
        self.numberOfRounds = 10
        
        print("gameStrategyEasy register")

        controller.gameController.GameController().registerGameStrategy(self)
 
       
    def play(self):
        ''' play - implements strategy method '''
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
        ''' find card for next round '''
        self.activeDescription = gameLogics.GameLogic.getRandomDescription(self)
        self.activeColorParsing = self.activeDescription.islower()      # lower case color name is parsed correctly to color 
        print("Current Card: ", self.activeDescription)
#        print("ActiveColorParsing: ", self.activeColorParsing)
        
        rFIDReader.RFIDReader().flushSerialInput()                      # clear buffer first
        controller.gameController.GameController().updateCurrentCardbyColor(self.activeDescription)     # update displayed gard in GUI 

                
    def readSignal(self):
        ''' read until UID is found - needed for verify showed card'''
        startTime = self.myTimeMeasure.startTimer()
        print("Start Counter at ", startTime)  
        readUid = self.myRFIDReaderConnection.readUID()  
         
        stringUid = readUid.decode(encoding='UTF-8')                    # parse read UID to search for the card in the card manager
        print("read UID: ", readUid)
        print("string UID: ", stringUid)
        readCard = self.myCardManager.getCardByID(stringUid)
        readDescription = readCard.getColor()
        print("read Description: ", readDescription )
            
#===================================================================
# Game Strategy Advanced 
#
# not implemented yet, just here to show the manager works
#===================================================================
class GameStrategyAdvanced(GamePlayStrategy):
    '''
    this class holds the game logics for the GUI
    '''

    def __init__(self):
        '''
        Constructor
        '''
        print("gameStrategyAdvanced register")
        controller.gameController.GameController().registerGameStrategy(self)    
        
    def play(self):
        print ("Started Advanced Mode")          
