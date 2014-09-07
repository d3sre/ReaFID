#! /usr/bin/python
'''
Created on Aug 25, 2014

@author: des
'''
#import sys
#sys.path.append('/home/des/git/ReaFID/src/model/')
#sys.path.append('/home/des/git/ReaFID/src/view/')


# Eclipse Error is wrong, it finds the mainGUI
#@UnresolvedImport
import view.mainGUI as mainGUI
import model.rFIDReader as rFIDReader
import model.gamePlayModes as gamePlayModes
import model.cardManager as cardManager
import model.cardFactory as cardFactory
#import controller
import controller.gameController as gameController
    
def main():

        
        
        # Initialize all singeltons
        gameController.GameController()
        rFIDReader.RFIDReader()
        cardFactory.CardFactory() 
        cardManager.CardManager()

        
        gamePlayModes.GamePlayManager().setGamePlayMode(0)
        cardManager.CardManager().loadConfiguration()
        
        app = mainGUI.MainGui()
        app.pack()
        app.master.title("ReaFID")
        app.mainloop()
        
    
main()    