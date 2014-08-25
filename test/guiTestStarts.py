#! /usr/bin/python

# Test code
import unittest
import sys

sys.path.append('/home/des/git/ReaFID/src/view/')
import tkinter as tk
import mainGUI
import subGUIs

class TestGUI(unittest.TestCase):
    
    #Create Test Object
    def setUp(self):
        self.root = tk.Tk() 
        
    def tearDown(self):
        if (self.root) :
            self.root.destroy()
        else : print("test ended")    
            

    
    # Run Tests
    def test_openMainGUI(self):
         
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

    

