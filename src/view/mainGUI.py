#! /usr/bin/python


import tkinter as tk
import controller.gameController as controller
import view.subGUIs as subGUIs

#===============================================================================
# Main GUI
#
# 
#===============================================================================
class MainGui(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.topMenuBar()     
        self.cardName = "Let's play a game"
        self.gameColor = "white"
        try:
            self.master.config(menu=self.menubar)
        except AttributeError:
            self.master.tk.call(master, "config", "-menu", self.menubar)
       
#        fontText = tk.Font("Arial", 14,"bold")
#        self.Label(master, text="Color")  
        self.frameCanvas = tk.Frame(self, borderwidth=1)
 
         
        self.canvas = tk.Canvas(self.frameCanvas, bg="white", width=400, height=400, bd=0, highlightthickness=0)
         
        self.canvas.pack() 
        self.canvas.create_rectangle(25,25,375,375, fill=self.gameColor)
        self.canvas.create_text(200,200,text=self.cardName)
         
        self.frameCanvas.pack()
         
        self.frameGameControl = tk.Frame(self, borderwidth=1)
        self.frameGameControl.pack()
        
        controller.GameController().registerMainGui(self)

   
""" menu bar wih all controls """
    def topMenuBar(self):
        self.menubar = tk.Menu(self)
        menuFile = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=menuFile)
#        menu.add_command(label="Configure Cards", command=self.configCardsWindow)
        menuFile.add_command(label="Configure Cards", command=self.showConfigCardsDialog)
        menuFile.add_command(label="Select Game Mode", command=self.showGamePlayDialog)
        menuFile.add_command(label="Configure Console Connection", command=self.configSerialConnection)
        
        menuTopScore = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Topscore", menu=menuTopScore)
        menuTopScore.add_command(label="Show Topscore")
        
        menuAbout = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="About", menu=menuAbout)
        
        menuState = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_separator()
        self.menubar.add_cascade(label="State")
        
        #menuGame = tk.Menu(self.menubar, tearoff=0)
        #self.menubar.add_cascade(label="Game", menu=menuGame)
        self.menubar.add_command(label="Play", command=self.play)
        
  
""" GUI commands """
        
    def showConfigCardsDialog(self):
        d = subGUIs.CardConfigDialog(self)
        self.wait_window(d.top)
        
    def showGamePlayDialog(self):
        d = subGUIs.GamePlayDialog(self)
        self.wait_window(d.top)   
        
    def configSerialConnection(self):
        d = subGUIs.SerialConfigDialog(self)
        self.wait_window(d.top)  

    def play(self):
        controller.GameController().startGame() 
        
""" Game controls """     
    
    def setCardColor(self, color):
        self.canvas.delete("all")
        self.gameColor = color
        self.canvas.create_rectangle(25,25,375,375, fill=self.gameColor)
        self.canvas.update_idletasks()
        
    def setCardName(self, cardName):       
        self.cardName = cardName
        self.canvas.create_text(200,200,text=self.cardName)
        self.canvas.update_idletasks()
        
    def setTimer(self):        
        self.timerLabel = "now"
        
    def refreshCanvas(self):
        self.setCardName("Timer")
        
   
            
