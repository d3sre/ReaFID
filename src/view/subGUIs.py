#! /usr/bin/python

import sys
sys.path.append('/home/des/git/ReaFID/src/model/')
import tkinter as tk
import gameLogics
import rFIDReader
import cardManager
import cardFactory


class CardConfigDialog():
    def __init__(self, parent):
        top = self.top = tk.Toplevel(parent)

        self.createWidgets()
        self.initializeWidgets()
        
        
    def createWidgets(self): 
        self.top.wm_title("Card Configuration Menu")  
        
        self.frame1 = tk.Frame(self.top, relief="raised", borderwidth=1)
        labelTitel = tk.Label(self.frame1, text= "Configure playable Cards")
        labelTitel.pack(side="top", fill="both")
        labelID = tk.Label(self.frame1, text="ID")
        labelID.pack(side="left", fill="both")
        labelDesc = tk.Label(self.frame1, text="Description")
        labelDesc.pack(side="left", fill="both")
        labelType = tk.Label(self.frame1, text="Type")
        labelType.pack(side="left", fill="both") 
        self.frame1.pack(fill="both", expand=1)
        
        self.frame2 = tk.Frame(self.top, relief="raised", borderwidth=1)
        self.listboxCards = tk.Listbox(self.top)
        self.listboxCards.bind('<<ListboxSelect>>', self.cardSelected)
        self.listboxCards.pack()    
        self.frame2.pack(fill="both", expand=1)
         
        #self.pack(fill="both", expand=1)
         
        buttonNew = tk.Button(self.top, text="New", command=self.new)
        buttonNew.pack(side="left", padx=5, pady=5)
        buttonDelete = tk.Button(self.top, text="Delete", command=self.delete)
        buttonDelete.pack(side="left", padx=5, pady=5)
        buttonSave = tk.Button(self.top, text="Save", command=self.save)
        buttonSave.pack(side="right", padx=5, pady=5)
        buttonCancel = tk.Button(self.top, text="Cancel", command=self.cancel)
        buttonCancel.pack(side="right", padx=5, pady=5)
        
    def initializeWidgets(self):
        myCardManager = cardManager.CardManager()
        myCardManager.loadConfiguration()
        
        numberCards = myCardManager.getSizeCardArray()
        cardIndex = 0
        while (cardIndex < numberCards):
            currentCard = myCardManager.getCardByNumber(cardIndex)
            if (isinstance(currentCard, cardFactory.ColorCard)):
                entry = currentCard.getID() + "   " + currentCard.getColor() + "   Color"
                self.listboxCards.insert("end", entry)
            elif (isinstance(currentCard, cardFactory.StudentCard)):
                entry = currentCard.getID() + "   " + currentCard.getName() + "   Student ID"
                self.listboxCards.insert("end", entry)
            else:
                print("Unknown card type")
            cardIndex += 1
        
        self.listboxCards.pack() 
        
    def cardSelected(self, event):
        w = event.widget
        self.curIndex = int(w.curselection()[0]) 
        #print self.curIndex
        value = w.get(self.curIndex)
        print(value)
        #UID aus value auslesen
        #passende card per uid suchen
        #card element in edit felder schreiben

    def new(self):
        self.top.destroy()
        
    def delete(self):
        self.top.destroy()

    def save(self):
        #aus edit felder texte holen
        #über self.curINdex passende card suchen
        #card mit neuen texten aktualisieren
        #listbox eintrag aktualisieren
        #card manager configuration speichern
        
        self.top.destroy()

    def cancel(self):
        self.top.destroy()




class ConfigCardsDialog(tk.Toplevel):
    def __init__(self, parent):
        self.ok_button = tk.Button(parent, "OK", command=self.on_ok)
#         tk.Frame.__init__(self, parent)
#         
#         self.parent = parent
#  #      self.grid()
#         self.configGUI()
#         
#         parent.geometry("300x200+300+300")

    def on_ok(self):
        print("OK")
        # send the data to the parent
#         self.app.new_data(... data from this dialog ...)
#         
        
    def configGUI(self): 
        ###test begin
#        self.parent = tk.Frame.__init__(self)
            
#        self.parent.pack(expand=True, padx=300, pady=200)
        ###test end
        
        self.t = tk.Toplevel(self)
        self.t.wm_title("Configuration Menu")  
#        self.style = tk.ttk.Style()
#        self.style.theme_use("default")

        self.frame1 = tk.Frame(self.t, relief="raised", borderwidth=1)
        tk.Label(self.frame1, text= "Configure playable Cards").pack(side="top", fill="both")
        m = tk.Label(self.frame1, text="ID")
        m.pack(side="left", fill="both")
        m = tk.Label(self.frame1, text="Description")
        m.pack(side="left", fill="both")
        m = tk.Label(self.frame1, text="Type")
        m.pack(side="left", fill="both") 
        self.frame1.pack(fill="both", expand=1)
        self.frame2 = tk.Frame(self.t, relief="raised", borderwidth=1)
        
        self.getCardList()
        
        self.frame2.pack(fill="both", expand=1)
        
        self.pack(fill="both", expand=1)
        
        closeButton = tk.Button(self.t, text="Load from Config")
        closeButton.pack(side="left", padx=5, pady=5)
        closeButton = tk.Button(self.t, text="Save")
        closeButton.pack(side="right", padx=5, pady=5)
        cancelButton = tk.Button(self.t, text="Cancel")
        cancelButton.pack(side="right", padx=5, pady=5)

    def getCardList(self):
        # listbox
        textbox = tk.Listbox(self.frame2)
        m = tk.Label(textbox, text="TEST")
        textbox.insert(1, m)
        textbox.pack(fill="both")
        
#         m = tk.Label(self.frame2, text="ID")
#         m.pack(side="left", fill="both")
#         m = tk.Label(self.frame2, text="Description")
#         m.pack(side="left", fill="both")
#         m = tk.Label(self.frame2, text="Type")
#         m.pack(side="left", fill="both")    
#         
        
    def configSerialConnection(self):
        
#        self.currentserial = rFIDReader.RFIDReaderClass.getSerial(self)
        self.currentserial = "/dev/ttyACM0"
        
        self.t = tk.Toplevel(self)
        self.t.wm_title("Configure Serial Connection") 
        
        self.frame1 = tk.Frame(self.t)
        tk.Label(self.frame1, text= "Current configured Serial Connection:").pack(side="top")
        serial = tk.Entry(self.frame1, textvariable=self.currentserial)
        serial.pack()
        self.frame1.pack(expand=True, padx=50, pady=20)
        closeButton = tk.Button(self.t, text="Save")
        closeButton.pack(side="right", padx=5, pady=5)
        cancelButton = tk.Button(self.t, text="Cancel")
        cancelButton.pack(side="right", padx=5, pady=5)
        
            
        
def main():
    window = tk.Tk()
    app = ConfigCardsGui(window)
    app.mainloop()
    
    
#main()    