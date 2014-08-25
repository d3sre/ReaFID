#! /usr/bin/python

# Test code
import unittest
import sys

sys.path.append('/home/des/git/ReaFID/src/model/')
import cardManager
import cardFactory
import rFIDReader


class TestManagerCreation(unittest.TestCase):
    
    #Create Test Object
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
        
    
    # Run Tests
    def test_getArraySize(self):
        self.assertEqual(self.myCardManager.getSizeCardArray(), 3)
        
        
    def test_singletonImplementation(self):
        self.myCardManager.addCard(self.card1)
        self.myCardManager.addCard(self.card2)
        self.myCardManager.addCard(self.card3)
        self.assertEqual(self.myCardManager.getSizeCardArray(), 6)  
 
   
    def test_storeConfiguration(self):
        self.size = self.myCardManager.getSizeCardArray()
        self.assertEqual(self.myCardManager.saveConfiguration(), None)
      

    def test_loadStoredConfiguration(self):
        self.myCardManager = cardManager.CardManager()
        self.myCardManager.loadConfiguration()
        self.myCardManager.outputCards()

        self.assertEqual(self.myCardManager.getSizeCardArray(), 3)

    def test_getCard(self):
        self.myCardManager = cardManager.CardManager()
        self.foundCard = self.myCardManager.getCard("AD B8 57 94")
        self.assertTrue(type(self.foundCard))
#        print("testCard: ", type(self.foundCard))

        
#     def test_registerCards(self):
#         rfidReader = rFIDReader.RFIDReaderClass()
#         uid = bytes(0)
#         receivedName = "Testname"
#         cardTyp = "Color"
#         receivedUid = rfidReader.readUID(uid)
#             
#         myCardFactory = cardFactory.CardFactory()   
#         myCard = myCardFactory.createCard(cardTyp)
#         myCard.setID(receivedUid)
#             
#         if (cardTyp == "Color"):
#                 myCard.setColor(receivedName)
#         elif (cardTyp == "Student"):
#                 myCard.setName(receivedName)
#         else : print("Error with Card Typ")    
#             
#         myCardManager = cardManager.CardManager()
#         
#         
#         self.assertTrue(myCardManager.addCard(myCard))
        

        
         
  

if __name__ == '__main__':
    unittest.main()

    

