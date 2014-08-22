#! /usr/bin/python

class RFIDReaderClass:

    def __init__(self):
        import serial
        self.__serialUid = ""
        self.__srl = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
#        print(self.__srl.readline())

    def readUID(self, uid):
        print("ok")
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
