#! /usr/bin/python

# Test code
import unittest

import model.rFIDReader as rFIDReader
import time

class TestCardCreation(unittest.TestCase):
    
    #Create Test Object
    def setUp(self):
        self.myRfidReader = rFIDReader.RFIDReader()
        self.uid = bytes(0)
        

    
    # Run Tests
    def test_readRFIDTag(self):               
        time.sleep(2)
        print("start")
        while (True):
            receivedUid = self.myRfidReader.readUID()
            print("received UID is: " , receivedUid)
        
#        print("type: " ,type(receivedUid))
        
#        self.assertEqual(type(receivedUid), "<class 'bytes'>")
        assert isinstance(receivedUid, bytes)


  

if __name__ == '__main__':
    unittest.main()

    

