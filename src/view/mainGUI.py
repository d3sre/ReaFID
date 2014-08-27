#! /usr/bin/python

import sys
sys.path.append('/home/des/git/ReaFID/src/model/')
import tkinter as tk
import gameLogics
import cardManager
import subGUIs


class MainGui(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.topMenuBar()     

        try:
            self.master.config(menu=self.menubar)
        except AttributeError:
            self.master.tk.call(master, "config", "-menu", self.menubar)
       
#        self.Label(master, text="Color")  
        self.canvas = tk.Canvas(self, bg="white", width=400, height=400, bd=0, highlightthickness=0)
        self.gameColor = "blue"
        self.canvas.create_rectangle(25,25,375,375, fill=self.gameColor)
        self.canvas.pack() 
        self.descriptionLabel = tk.Label(self.canvas, text="Color", anchor="center",width=400, height=400, background=self.gameColor)
        self.descriptionLabel.pack()

   

    def topMenuBar(self):
        self.menubar = tk.Menu(self)
        menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=menu)
#        menu.add_command(label="Configure Cards", command=self.configCardsWindow)
        menu.add_command(label="Configure Cards", command=self.showConfigCardsDialog)
        menu.add_command(label="Select Game Mode", command=self.showGamePlayDialog)
        menu.add_command(label="Configure Console Connection", command=self.configSerialConnection)
        
        menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Topscore", menu=menu)
        menu.add_command(label="Show Topscore")
        
        menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="About", menu=menu)
        
        menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_separator()
        self.menubar.add_cascade(label="State")
        
              
        
    def showConfigCardsDialog(self):
        d = subGUIs.CardConfigDialog(self)
        self.wait_window(d.top)
        
    def showGamePlayDialog(self):
        d = subGUIs.GamePlayDialog(self)
        self.wait_window(d.top)   
        
    def configSerialConnection(self):
        d = subGUIs.SerialConfigDialog(self)
        self.wait_window(d.top)  

        
