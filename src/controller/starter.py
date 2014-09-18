#! /usr/bin/python

# Eclipse Error is wrong, it finds the mainGUI
#@UnresolvedImport
import view.mainGUI as mainGUI
import model.rFIDReader as rFIDReader
import model.gamePlayModes as gamePlayModes
import model.cardManager as cardManager
import model.cardFactory as cardFactory
#import controller
import controller.gameController as gameController


#===========================================================================
# Main class - starter class for the game 
#
# initial control class 
#===========================================================================
def main():

        
        
        # Initialize all singeltons
        gameController.GameController()                             # initialize Game Controller
        rFIDReader.RFIDReader()                                     # open serial interface manager
        cardFactory.CardFactory()                                   # initialize card factory manager
        cardManager.CardManager()                                   # initialize card manager

        
        gamePlayModes.GamePlayManager().setGamePlayMode(0)          # activate game play mode "simple"
        cardManager.CardManager().loadConfiguration()               # load config from pickle to card manager
        
        app = mainGUI.MainGui()                                     # start gui
        app.pack()
        app.master.title("ReaFID")
        app.mainloop()
        
    
main()    