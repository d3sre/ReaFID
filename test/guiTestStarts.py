#! /usr/bin/python

# Test code
import unittest
import sys

sys.path.append('/home/des/git/ReaFID/src/view/')
sys.path.append('git/ReaFID/src/controller')
import tkinter as tk
import mainGUI
import subGUIs
import controller

class TestGUI(unittest.TestCase):
    
    #Create Test Object
    def setUp(self):
        self.root = tk.Tk() 
        self.myController = controller.GameController()
        
    def tearDown(self):
        if (self.root) :
            self.root.destroy()
        else : print("test ended")    
            

    
    # Run Tests
    def test_openMainGUI(self):
#        self.myController 
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

    

