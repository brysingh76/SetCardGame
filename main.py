import random
#Set Card Game

#create the deck to play set
class setDeck():

    # Each card is unique and shows up only once
    shapeTypes = [" diamond ", " squiggle ", " oval "]
    shapeShadings = [" solid ", " striped ", " open "]
    shapeColors = [" green ", " red ", " purple "]
    shapeNums = [" 1 ", " 2 ", " 3 "]

    def createTheDeck(self):
        # 1, 2, 3, open, shaded, filled, purple, green, red, diamond, squiggle, oval
        return ['{}{}{}{}'.format(n, f, c, s)
                for n in self.shapeNums
                    for f in self.shapeShadings
                        for c in self.shapeColors
                            for s in self.shapeTypes]
    #Shuffles entire deck of cards in CardTemplate
    def shuffleDeck(self):
        random.shuffle(cardTemplate.cardDeck)


class cardTemplate(setDeck):
    cardTable = []

    cardDeck = []
    index = 0

    shapeType = ""
    shapeShading = ""
    shapeColor = ""
    numShape = ""

    threeCardList = []

    ###########################
    # Getters for Card Template#
    ###########################
    def getShapeType(self):
        return self.shapeType

    def getShapeShading(self):
        return self.shapeShading

    def getShapeColor(self):
        return self.shapeColor

    def getNumShape(self):
        return self.numShape

    def createCard(self, sNum, sShading, sColor, sType):
        s = cardTemplate()
        s.shapeType = sType
        s.shapeShading = sShading
        s.shapeColor = sColor
        s.shapeNum = sNum
        return s

    def oopCreateTheDeck(self):
        for n in self.shapeNums:
            for f in self.shapeShadings:
                for c in self.shapeColors:
                    for s in self.shapeTypes:
                        self.cardDeck.append(self.createCard(n, f, c, s))

    def printCard(self, oneCard):
        print(oneCard.shapeType)
        print(oneCard.shapeShading)
        print(oneCard.shapeColor)
        print(oneCard.shapeNum, ("\n"))

    #Calls shuffle deck function and adds 12 cards to cardTable and removes them from cardDeck
    def createCardTable(self):
        #shuffle deck before pulling 12 random cards
        self.shuffleDeck()
        cardTemplate.cardTable = cardTemplate.cardDeck[:12]
        del cardTemplate.cardDeck[:12]


    def compareTwoCards(self, cardOne, cardTwo):
        print("two new lines")
        print(cardOne.getShapeType())
        print(cardTwo.getShapeType())

    def findSets(self):
        counter = 0
        print("How do you want to implement? plan it")
        found = []
        for card in self.cardTable:
            print("Two cards: ")
            cardTemplate.compareTwoCards(card, card)













print("Starting now")
game = cardTemplate()
game.oopCreateTheDeck()
game.createCardTable()


count = 0
for card in game.cardDeck:
    game.printCard(card)
    count = count +1
print ("Total Cards in Deck: ", count)

count = 0
for card in game.cardTable:
    game.printCard(card)
    count = count +1
print ("Total Cards on Table: ", count)

newCounter = 0
print(cardTemplate.getShapeType(game.cardTable[0]))

game.findSets()










