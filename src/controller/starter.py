#! /usr/bin/python
'''
Created on Aug 25, 2014

@author: des
'''
import sys
#sys.path.append('/home/des/git/ReaFID/src/model/')
sys.path.append('/home/des/git/ReaFID/src/view/')

import tkinter as tk
# Eclipse Error is wrong, it finds the mainGUI
#@UnresolvedImport
import mainGUI

    
def main():
        root = tk.Tk()  
        
        app = mainGUI.MainGui()
        app.pack()
        app.master.title("ReaFID")
        root.mainloop()
        
    
main()    