#! /usr/bin/python

import sys
sys.path.append('/home/des/git/RFIDuino/src/model/')
import tkinter as tk
import gameLogics


class MainGui(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
 #      self.grid()
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
        menu.add_command(label="Configure Cards")
        menu.add_command(label="Select Game Mode")
        
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
#    def downStatusBar(self):
            
        
        
root = tk.Tk()  
        
app = MainGui()
app.pack()
app.master.title("ReaFID")
root.mainloop()


