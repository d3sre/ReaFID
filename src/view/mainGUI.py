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
        self.gameRectangle()
        self.canvas.pack() 

   

    def topMenuBar(self):
        self.menubar = tk.Menu(self)
        menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=menu)
#        menu.add_command(label="Configure Cards", command=self.configCardsWindow)
        menu.add_command(label="Configure Cards", command=self.showConfigCardsDialog)
        menu.add_command(label="Select Game Mode")
        menu.add_command(label="Configure Console Connection", command=self.configSerialConnection)
        
        menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Topscore", menu=menu)
        menu.add_command(label="Show Topscore")
        
        menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="About", menu=menu)
        
        menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_separator()
        self.menubar.add_cascade(label="State")
        
        

    def gameRectangle(self):
        self.gameColor = "blue"
        self.canvas.create_rectangle(25,25,375,375, fill=self.gameColor)
        
        
    def showConfigCardsDialog(self):
        d = subGUIs.CardConfigDialog(self)
        self.wait_window(d.top)
        
#         myConfigDialog = subGUIs.ConfigCardsDialog(self)
#         myConfigDialog.show()
        #myConfigGUI.configGUI(self)
        
    def configSerialConnection(self):
        d = subGUIs.SerialConfigDialog(self)
        self.wait_window(d.top)  

        
        
    def listConfiguredCards(self):
#        textbox = tk.Listbox(self)
#        textbox.pack(fill="both")
        
        self.activeCards = (cardManager.CardManager.getSizeCardArray(self)- 1)
        card = 0
        while (card <= self.activeCards):
            currentCard = cardManager.CardManager.getCardByNumber(self, card)
            tk.Text()
            tk.INSERT(0, currentCard.getID())
            card += 1

        
        
#         self.middleLabel = tk.Label(self.t, text="middlelabel")   
#         return self.middleLabel  
#    def downStatusBar(self):
            
        
        
# root = tk.Tk()  
#          
# app = MainGui()
# app.pack()
# app.master.title("ReaFID")
# root.mainloop()


