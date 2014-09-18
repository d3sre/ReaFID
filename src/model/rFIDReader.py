#! /usr/bin/python

import controller
import time
import model.singleton as singleton

#===============================================================================
#  RFID Reader Class
#
# all reads from the serial interface are performed here
#===============================================================================
class RFIDReader(metaclass=singleton.Singleton):

    def __init__(self):
        import serial
        self.__serialUid = ""
        self.serialInterface = '/dev/ttyACM0'
        controller.gameController.GameController().registerSerial(self.serialInterface)
        self.__srl = serial.Serial(self.serialInterface, 115200, timeout=0)
        
        time.sleep(2)
        
        while (self.__srl.inWaiting() != 0):
            self.__srl.flushInput()
            
#        print(self.__srl.readline())

    def setSerialInterface(self, serial):
        self.serialInterface = serial
        controller.gameController.GameController().registerSerial(self.serialInterface)
        print("New Serial connection is: ", self.serialInterface )
        
    def getSerialInterface(self):
        print("Active Serial connection is: ", self.serialInterface ) 
        return self.serialInterface   

""" main method to read only UIDs """
    def readUID(self):
        print("ok")
        uid = bytes(0)
        i = 0
        self.__uid = uid

        while(self.__srl.inWaiting() == 0):
            pass

        byte = bytes(0)
        line = bytes(0)
        endFound = False
        found = -1 
        while(endFound == False):
            byte = self.__srl.read()
            line = line + byte
            length = len(line)
            start = length - 5
            if (start >= 0):
                found = line.find(b' ***\n', start)     # Found end when pattern '***\n' is found
#            print("Current line: ", line, " Length: ", length, " Start: ", start, " End: ", end, " Found: ", found)
            if (found != -1):
                endFound = True
        
        self.__srl.flushInput()                         # flush Input so no noise is kept in the buffer
        
        start = found - 11                              # find the start of the UID
        self.__uid = line[start:found]                  # store the UID
        
        #print("Found UID: ", self.__uid) 
        return self.__uid
        
""" close the serial interface at the end of the reads """    
    def stopReading(self):    
        self.__srl.close()

""" check if line is open for display in MainGUI """        
    def checkSerialLineOpen(self):
        return self.__srl.isOpen()    

""" flush function to clear the buffer """        
    def flushSerialInput(self):
        self.__srl.flushInput()    
    

        
