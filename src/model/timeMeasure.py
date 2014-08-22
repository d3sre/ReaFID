#! /usr/bin/python
import datetime

class timeMeasureClass:   

    def __init__(self):      
        self.initTime = datetime.datetime.now()
        print("time now: " , self.initTime)
        print("1")
        
    def startTimer(self):
        print("2")
        self.tstart = datetime.datetime.now()
#        return self.t
        
    def getTime(self, elapsedTime):
        print("3")
        self.tstop = datetime.datetime.now()
        self.elapsed_time = self.tstop - self.tstart
        return self.elapsed_time
    
        