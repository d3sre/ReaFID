#! /usr/bin/python

# Test code
import unittest
import sys

sys.path.append('/home/des/git/RFIDuino/src/model/')
import cardFactory

class TestCardCreation(unittest.TestCase):
    
    #Create Test Object
    def setUp(self):
        self.classInstance = cardFactory.CardFactory()
        self.card =  self.classInstance.createCard("Color")
        self.card.setColor("Blue")
        self.card.setID("ColorIDTest")
        self.card2 =  self.classInstance.createCard("Student")
        self.card2.setName("sachedes")
        self.card2.setID("StudentIDTest")
    
    # Run Tests
    def test_createColorCard(self):
        self.assertEqual(self.card.getColor(), "Blue")
        self.assertEqual(self.card.getID(), "ColorIDTest")

    def test_createStudentCard(self):
        self.assertEqual(self.card2.getName(), "sachedes")
        self.assertEqual(self.card2.getID(), "StudentIDTest")
  

if __name__ == '__main__':
    unittest.main()

    

