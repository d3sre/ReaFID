#! /usr/bin/python

import controller
import time
import model.singleton as singleton
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


    def readUID(self):
#         if (self.checkSerialLineOpen() == False):  
#             print("serial line had to be opened")
#             self.__srl.open()
        print("ok")
        uid = bytes(0)
        i = 0
        self.__uid = uid



#TEST
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
                found = line.find(b' ***\n', start)   
#            print("Current line: ", line, " Length: ", length, " Start: ", start, " End: ", end, " Found: ", found)
            if (found != -1):
                endFound = True
        
        self.__srl.flushInput()
        
        start = found - 11
        self.__uid = line[start:found]
        
        #print("Found UID: ", self.__uid) 
        return self.__uid
        
        
        
#TEST
        
        
        
        
#         while(self.__uid == b''):
# #            print(self.__srl.readline())
#             srlin = self.__srl.readline()
#             self.srlInput = srlin + srlin
# #            print(i)
#             i = i + 1
#             pointer = self.srlInput.find(b'***')            
#             if (pointer != -1):
# #                print("pointer: ", pointer)
#                 self.__uid = srlin.split(b'***')[1]
# #                print(self.__uid.strip())  
# #         self.__srl.close()   
#  
#         self.__uid.strip()
#          
# #         temp = self.__srl.readline()
# #         while(temp != b''):
# #             temp = self.__srl.readline()
#          
#         return self.__uid
    
    def stopReading(self):    
        self.__srl.close()
        
    def checkSerialLineOpen(self):
        return self.__srl.isOpen()    
        
    def flushSerialInput(self):
        self.__srl.flushInput()    
    

        
