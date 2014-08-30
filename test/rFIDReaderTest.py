#! /usr/bin/python

# Test code
import unittest
import sys

sys.path.append('/home/des/git/ReaFID/src/model/')
import rFIDReader
import time

class TestCardCreation(unittest.TestCase):
    
    #Create Test Object
    def setUp(self):
        self.myRfidReader = rFIDReader.RFIDReaderClass()
        self.uid = bytes(0)
        

    
    # Run Tests
    def test_readRFIDTag(self):               
        time.sleep(2)
        print("start")
        receivedUid = self.myRfidReader.readUID()
        print("received UID is: " , receivedUid)
        print("type: " ,type(receivedUid))
        
#        self.assertEqual(type(receivedUid), "<class 'bytes'>")
        assert isinstance(receivedUid, bytes)


  

if __name__ == '__main__':
    unittest.main()

    

