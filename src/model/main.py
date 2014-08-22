#! /usr/bin/python

import rFIDReader
import cardFactory
import cardManager


rfidReader = rFIDReader.RFIDReaderClass()
#receivedTime = timeMeasure.timeMeasureClass()


#def main():
    #uid = bytes(0)
    #elapsedTime = 0
    #time.sleep(2)
    #print("start")
    #receivedTime.startTimer()
    #receivedUid = rfidReader.readUID(uid)
    #print("received UID is: " , receivedUid)
    #gotTime = receivedTime.getTime(elapsedTime)
    #print("used time is: " , gotTime)
    #savedCard = strategieCards.StrategieCardBlue(receivedUid)
    #print("saved Card: " , savedCard)
    

def registerCard():
    uid = bytes(0)
    receivedName = input("Enter Description: ")
    cardTyp = "Color"
    receivedUid = rfidReader.readUID(uid)
    
    myCardFactory = cardFactory.CardFactory()   
    myCard = myCardFactory.createCard(cardTyp)
    myCard.setID(receivedUid)
    
    if (cardTyp == "Color"):
        myCard.setColor(receivedName)
    elif (cardTyp == "Student"):
        myCard.setName(receivedName)
    else : print("Error with Card Typ")    
    
    myCardManager = cardManager.CardManager()
    myCardManager.addCard(myCard)
    myCardManager.outputCards()

    myCardManager.saveConfiguration()


def testLoadConfig():
    myCardManager = cardManager.CardManager()
    myCardManager.loadConfiguration()
    myCardManager.outputCards()


def testSaveConfig():
    myCardFactory = cardFactory.CardFactory()   
    card1 = myCardFactory.createCard("Color")
    card2 = myCardFactory.createCard("Color")
    card3 = myCardFactory.createCard("Student")
    card1.setColor("Card1")
    card2.setColor("Card2")
    card3.setName("Card3")
    card1.setID("AD B8 57 94")
    card2.setID("B2 FB 30 E9")
    card3.setID("8D F4 61 94")
    
    myCardManager = cardManager.CardManager()
    myCardManager.addCard(card1)
    myCardManager.addCard(card2)
    myCardManager.addCard(card3)
    myCardManager.outputCards()

    myCardManager.saveConfiguration()
    

#testSaveConfig()
#registerCard()
testLoadConfig()
