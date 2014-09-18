#! /usr/bin/python

# Test code
import unittest
import sys

sys.path.append('/home/des/git/ReaFID/src/model/')
import cardManager
import cardFactory
import gameLogics

#===============================================================================
# Test game logics (tests of random) 
#===============================================================================
class TestManagerCreation(unittest.TestCase):
    
    """ Create Test Object """
    def setUp(self):
        self.myCardFactory = cardFactory.CardFactory()   
        self.card1 = self.myCardFactory.createCard("Color")
        self.card2 = self.myCardFactory.createCard("Color")
        self.card3 = self.myCardFactory.createCard("Student")
        self.card1.setColor("Card1")
        self.card2.setColor("Card2")
        self.card3.setName("Card3")
        self.card1.setID("AD B8 57 94")
        self.card2.setID("B2 FB 30 E9")
        self.card3.setID("8D F4 61 94")
        self.myCardManager = cardManager.CardManager()

        self.myCardManager.addCard(self.card1)
        self.myCardManager.addCard(self.card2)
        self.myCardManager.addCard(self.card3)


    def tearDown(self):
        cardManager.CardManager().getEmptyManager(self.myCardManager)   
    
    """ Run Tests """
    def test_checkRandomValue(self):        
        self.assertEqual(self.myCardManager.getSizeCardArray(), 3)
        self.size = self.myCardManager.getSizeCardArray()
        print ("-1- size: " ,self.size)
        self.assertLessEqual(gameLogics.GameLogic().getRandomNumber(), self.size)
        print ("-2- random: " ,gameLogics.GameLogic().getRandomNumber())


    def test_getRandomColor(self):
        print("color: ", gameLogics.GameLogic().getRandomDescription())
         
  

if __name__ == '__main__':
    unittest.main()

    

