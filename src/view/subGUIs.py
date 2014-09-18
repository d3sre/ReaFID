#! /usr/bin/python


import tkinter as tk
import model.cardFactory as cardFactory
import controller.gameController as controller

#===============================================================================
# Card Configuration Dialog Box
#
# Dialog for configuring the RFID Cards for the game
#===============================================================================
class CardConfigDialog():
    def __init__(self, parent):
#        self.myCardManager = cardManager.CardManager()
        self.top = tk.Toplevel(parent)

        self.createWidgets()
        self.initializeWidgets()
        
""" create graphical elements """
    def createWidgets(self): 
        self.top.wm_title("Card Configuration Menu")  
        
        self.frame1 = tk.Frame(self.top, borderwidth=1)
        labelTitel = tk.Label(self.frame1, text="Configure playable Cards")
        labelTitel.pack(side="top", fill="both")
        labelID = tk.Label(self.frame1, text="ID")
        labelID.pack(side="left", fill="both")
        labelDesc = tk.Label(self.frame1, text="Description")
        labelDesc.pack(side="left", fill="both")
        labelType = tk.Label(self.frame1, text="Type")
        labelType.pack(side="left", fill="both") 
        self.frame1.pack(fill="both", expand=1)
        
        self.frame2 = tk.Frame(self.top, borderwidth=1, width=200)
        self.listboxCards = tk.Listbox(self.top)
        self.listboxCards.bind('<<ListboxSelect>>', self.cardSelected)
        self.listboxCards.pack(fill="x")    
        self.frame2.pack(fill="both", expand=1)
        
        
        self.frame3 = tk.Frame(self.top, borderwidth=1, width=200)
        self.entryID = tk.Entry(self.frame3)
        self.entryID.pack(side="left")
#        self.entryID.bind(sequence, func, add)
        self.entryDesc = tk.Entry(self.frame3)
        self.entryDesc.pack(side="left")

        self.entryType = tk.OptionMenu(self.frame3, "Color", "Student")  
        self.entryType.pack(side="left") 
        self.frame3.pack(fill="both", expand=1)
         
        buttonNew = tk.Button(self.top, text="New", command=self.new)
        buttonNew.pack(side="left", padx=5, pady=5)
        buttonDelete = tk.Button(self.top, text="Delete", command=self.delete)
        buttonDelete.pack(side="left", padx=5, pady=5)
        buttonSave = tk.Button(self.top, text="Save", command=self.save)
        buttonSave.pack(side="right", padx=5, pady=5)
        buttonCancel = tk.Button(self.top, text="Cancel", command=self.cancel)
        buttonCancel.pack(side="right", padx=5, pady=5)
        
""" get cards from Card Manager to display """       
    def initializeWidgets(self):
#        self.myCardManager.loadConfiguration()
#        cardManager.CardManager.loadConfiguration(self)
        
        # numberCards = cardManager.CardManager.getSizeCardArray(self)
        self.myCardManager = controller.GameController().getCardManager()
        numberCards = self.myCardManager.getSizeCardArray()
        cardIndex = 0
        while (cardIndex < numberCards):
            currentCard = self.myCardManager.getCardByNumber(cardIndex)
#            currentIDString = currentCard.getID().decode("utf-8")
            if (isinstance(currentCard, cardFactory.ColorCard)):
                entry = str(currentCard.getID()) + "   " + currentCard.getColor() + "   Color"
                self.listboxCards.insert("end", entry)
            elif (isinstance(currentCard, cardFactory.StudentCard)):
                entry = str(currentCard.getID()) + "   " + currentCard.getName() + "   Student ID"
                self.listboxCards.insert("end", entry)
            else:
                print("Unknown card type")
            cardIndex += 1
        
        self.listboxCards.pack() 

""" insert selected card info into change card boxes """        
    def cardSelected(self, event):
        selectEvent = event.widget
        self.curIndex = int(selectEvent.curselection()[0]) 
        
#        displayUid = event.widget
        
        # print self.curIndex
        value = selectEvent.get(self.curIndex)
        print(value)
        self.selectedUid = value[:11]
        
        activeCard = self.myCardManager.getCardByID(self.selectedUid)
        self.entryID.delete(0, "end")
        self.entryID.insert(0, self.selectedUid)
        
        if isinstance(activeCard, cardFactory.ColorCard):
            self.entryType.setvar("Color", 1)
            self.entryDesc.delete(0, "end")
            self.entryDesc.insert(0, activeCard.getColor())
            print("Type: Color, Description: ", activeCard.getColor())
        elif isinstance(activeCard, cardFactory.StudentCard):  
            self.entryType.setvar("Student", 2)
            self.entryDesc.delete(0, "end")
            self.entryDesc.insert(0, activeCard.getName())
            print("Type: Student, Description: ", activeCard.getName())
        else : print("method for this type of card not programmed")  
        
        # UID aus value auslesen
        # passende card per uid suchen
        # card element in edit felder schreiben

""" new button to add new cards to Card Manager """
    def new(self):
        cardFactory.CardFactory.createCard(self, self.entryType)
        print ("New card was added to card Factory")
#        self.top.destroy()
 
""" delete button to delete card from Card Manager """       
    def delete(self):
        self.myCardManager.removeCard(self.selectedUid)
#        self.top.destroy()

""" save button to save configuration to Card Manager """
    def save(self):
        # aus edit felder texte holen
        # über self.curINdex passende card suchen
        # card mit neuen texten aktualisieren
        # listbox eintrag aktualisieren
        # card manager configuration speichern
        
        self.top.destroy()

""" cancel button to dismiss all changes """
    def cancel(self):
        self.top.destroy()


#===============================================================================
# Serial Configuration Dialog Box
#
# Dialog for configuring the Serial Interfaces for the game
#===============================================================================            
class SerialConfigDialog():
    def __init__(self, parent):
        # self.activeSerialInterface = rFIDReader.RFIDReader()
 #       self.activeSerialInterface = controller.GameController()
        self.top = tk.Toplevel(parent)
        
        self.configSerialConnection()

""" create dialog elements """                
    def configSerialConnection(self):

               
        self.top.wm_title("Configure Serial Connection") 
        
        self.frame1 = tk.Frame(self.top)
        tk.Label(self.frame1, text="Current configured Serial Connection:")
        self.serial = tk.Entry(self.frame1)
        self.serial.insert(0, controller.GameController().getSerialInterface())
        self.serial.pack()
        self.frame1.pack(expand=True, padx=70, pady=20)
        closeButton = tk.Button(self.top, text="Save", command=self.save)
        closeButton.pack(side="right", padx=5, pady=5)
        cancelButton = tk.Button(self.top, text="Cancel", command=self.cancel)
        cancelButton.pack(side="right", padx=5, pady=5)

""" update serial configuration over controller """        
    def updateSerialConnection(self):
        controller.GameController().setSerialInterface(self.serial.get())

""" save button to save changes """        
    def save(self):
        self.updateSerialConnection()     
        self.top.destroy()

""" cancel button to dismiss changes """
    def cancel(self):
        self.top.destroy()
        
#===============================================================================
# Game Play Configuration Dialog Box
#
# Dialog for configuring the game play mode
#===============================================================================           
class GamePlayDialog():
    def __init__(self, parent):
#        self.myGameController = controller.GameController()
        self.top = tk.Toplevel(parent)
        
        self.configGamePlayMode()

""" create dialg elements """                
    def configGamePlayMode(self):             
        self.top.wm_title("Configure Game Play Mode") 
        
        self.frame1 = tk.Frame(self.top)
        tk.Label(self.frame1, text="Active Game Play Mode").pack(side="top")        
        self.mode = tk.IntVar()
        self.mode.set(controller.GameController().getCurrentGameStrategy())
        tk.Radiobutton(self.frame1, text="Easy Mode", variable=self.mode, value=0, command=self.selectGameMode()).pack(anchor="w")
        tk.Radiobutton(self.frame1, text="Advanced Mode", variable=self.mode, value=1, command=self.selectGameMode()).pack(anchor="w")        
        self.frame1.pack(expand=True, padx=50, pady=20)
        
        closeButton = tk.Button(self.top, text="Save", command=self.save)
        closeButton.pack(side="right", padx=5, pady=5)
        cancelButton = tk.Button(self.top, text="Cancel", command=self.cancel)
        cancelButton.pack(side="right", padx=5, pady=5)
        
""" select active game mode """
    def selectGameMode(self):
        controller.GameController().setCurrentGameStrategy(self.mode.get())     
#        print("Active Game Play Mode: ", self.myGamePlayStrategy.getGamePlayMode())


""" save button to save changes to game play modes """
    def save(self):
        self.selectGameMode()      
        self.top.destroy()

""" cancel button to dismiss changes """
    def cancel(self):
        self.top.destroy()

               
