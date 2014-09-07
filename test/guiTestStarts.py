#! /usr/bin/python

# Test code
import unittest

# import view
# import controller
# import model

# import sys
# 
# sys.path.append('/home/des/git/ReaFID/src/view/')
# sys.path.append('git/ReaFID/src/controller')
import tkinter as tk
import view.mainGUI as mainGUI
import view.subGUIs as subGUI
import controller.gameController as controller
import model.gamePlayModes as gamePlayModes
import model.cardManager as cardManager
import model.rFIDReader as rFIDReader
import model.cardFactory as cardFactory

class TestGUI(unittest.TestCase):
    
    #Create Test Object
    def setUp(self):
        
        self.myController = controller.GameController()
        
#     def tearDown(self):
#         if (self.root) :
#             self.root.destroy()
#         else : print("test ended")    
            

    
    # Run Tests
    def test_openMainGUI(self):
#        self.myController 
        
        rFIDReader.RFIDReader()
        gamePlayModes.GamePlayManager().setGamePlayMode(0)
        cardFactory.CardFactory() 
        myCardManager = cardManager.CardManager()
        myCardManager.loadConfiguration()
        
        app = mainGUI.MainGui()
        app.pack()
        app.master.title("ReaFID")
        app.mainloop()
        

#     def test_openConfigGUI(self): 
#         
#         app = subGUIs.ConfigCardsGui.configGUI()
#         app.pack()
#         self.root.mainloop()
        
     
  

if __name__ == '__main__':
    unittest.main()

    

