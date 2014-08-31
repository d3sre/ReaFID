#! /usr/bin/python

import controller
import singleton
class RFIDReaderClass(metaclass=singleton.Singleton):

    def __init__(self):
        import serial
        self.__serialUid = ""
        self.serialInterface = '/dev/ttyACM0'
        controller.GameController().registerSerial(self.serialInterface)
        self.__srl = serial.Serial(self.serialInterface, 115200, timeout=1)
#        print(self.__srl.readline())

    def setSerialInterface(self, serial):
        self.serialInterface = serial
        controller.GameController().registerSerial(self.serialInterface)
        print("New Serial connection is: ", self.serialInterface )
        
    def getSerialInterface(self):
        print("Active Serial connection is: ", self.serialInterface ) 
        return self.serialInterface   


    def readUID(self):
        if (self.checkSerialLineOpen() == False):  
            print("serial line had to be opened")
            self.__srl.open()
        print("ok")
        uid = bytes(0)
        i = 0
        self.__uid = uid
        while(self.__uid == b''):
#            print(self.__srl.readline())
            srlin = self.__srl.readline()
            self.srlInput = srlin + srlin
#            print(i)
            i = i + 1
            pointer = self.srlInput.find(b'***')            
            if (pointer != -1):
#                print("pointer: ", pointer)
                self.__uid = srlin.split(b'***')[1]
#                print(self.__uid.strip())  
        self.__srl.close()   
        return self.__uid.strip()
    
    def stopReading(self):    
        self.__srl.close()
        
    def checkSerialLineOpen(self):
        return self.__srl.isOpen()    
        
    

        
