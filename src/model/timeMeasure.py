#! /usr/bin/python
import datetime

#===============================================================================
#  time measurement functions
#
#  used by the game play modes to measure times
#===============================================================================
class TimeMeasure:   

    def __init__(self):      
        self.initTime = datetime.datetime.now()
        self.totalTimeCounter = datetime.timedelta(0)
        print("time now: " , self.initTime)
        #print("1")
        
    def startTimer(self):
        #print("2")
        self.tstart = datetime.datetime.now()
        return self.tstart
#        return self.t
        
    def getTime(self):
        #print("3")
        self.tstop = datetime.datetime.now()
        self.elapsed_time = self.tstop - self.tstart
        print("elapsed time: ", self.elapsed_time)
        return self.elapsed_time
    
    def totalTime(self):
  #      counter = datetime.timedelta()
        self.totalTimeCounter = self.totalTimeCounter  + self.elapsed_time   
        print("total Time in TimeMeasure class: ", self.totalTimeCounter)
        return self.totalTimeCounter