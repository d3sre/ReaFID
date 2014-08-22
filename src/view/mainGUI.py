#! /usr/bin/python


import tkinter as tk


class MainGui(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        
    def createWidgets(self):
        self.quitButton = tk.Button(self, text="Quit", command=self.quit)
        self.quitButton.grid()
        
    def menu(self):
        self.subMenu = tk.Menu(self.menuRoot)
        self.menuRoot.add_cascade(label="Menu", menu=self.subMenu)
        self.subMenu.add_command(label="Card Configurationq", command=self.__aboutHandler)
        
    def topscore(self):
        print "topscore"
        
    def about(self):
        print "about"       
        
    def menuRoot(self):
        menubar = tk.Menu() 
        menubar.add_command(label="Menu", command=self.menu())
        menubar.add_command(label="Topscore", command=self.topscore())
        menubar.add_command(label="About", command=self.about())  
        
         
        
app = MainGui()
app.master.title("ReaFID")
app.mainloop()


