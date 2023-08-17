import deesStuff
import random

# TODO add logic to aces

class Card:
    def __init__(self, cardValue:int, suit:str) -> None:
        self.value = cardValue
        self.suit = suit
        self.name = str(cardValue) + " of " + suit

class Hand:
    def __init__(self, user = False) -> None:
        def newCards():
            global deck
            cards = []

            for _ in range(2):
                cards.append(random.choice(deck))
                deck.remove(cards[-1])

                if cards[-1].value == 1:
                    self.ace = True
            
            return cards
        
        self.ace = False

        self.dealer = False
        
        if user == False:
            self.dealer = True
        
        self.cards = newCards()

        while user == True and self.total() >= 21:
            self.cards = newCards()

    def total(self) -> int:
        if self.ace == False:
            total = 0
            for i in self.cards:
                total+=i.value

            return total
        
        if self.ace == True:
            total1 = 0
            total2 = 0
            for i in self.cards:
                total1+=i.value

                if i.value == 1:
                    total2 += 11
                
                else:
                    total2 += i.value
            
            if total2 > 21:
                return total1
            
            return total2
    
    def __str__(self) -> str:
        string = "\n"
        for i in self.cards:
            string += i.name + "\n"
        return string
    
    def displayhand(self, displayAll = False) -> str:
        if self.dealer == False or displayAll == True:
            string = ""
            for i in self.cards:
                string += str(i.value) + " "
            
            return string
        
        else:
            return str(self.cards[0].value) + " ?"
    
    def addCard(self):
        self.cards.append(random.choice(deck))
        deck.remove(self.cards[-1])

def displayHands(dealerDraw = False):
    global userCards
    global dealerCards
    print("Your Hand\tDealers Hand")

    print(userCards.displayhand() + "\t\t" + dealerCards.displayhand(dealerDraw))
    

deck = [
    Card(1, "Spades"), Card(2, "Spades"), Card(3, "Spades"), Card(4, "Spades"), Card(5, "Spades"), 
    Card(6, "Spades"), Card(7, "Spades"), Card(8, "Spades"), Card(9, "Spades"), Card(10, "Spades"), Card(11, "Spades"), 
    Card(12, "Spades"), Card(13, "Spades"),
    Card(1, "Clubs"), Card(2, "Clubs"), Card(3, "Clubs"), Card(4, "Clubs"), Card(5, "Clubs"), 
    Card(6, "Clubs"), Card(7, "Clubs"), Card(8, "Clubs"), Card(9, "Clubs"), Card(10, "Clubs"), Card(11, "Clubs"), 
    Card(12, "Clubs"), Card(13, "Clubs"),
    Card(1, "Hearts"), Card(2, "Hearts"), Card(3, "Hearts"), Card(4, "Hearts"), Card(5, "Hearts"), 
    Card(6, "Hearts"), Card(7, "Hearts"), Card(8, "Hearts"), Card(9, "Hearts"), Card(10, "Hearts"), Card(11, "Hearts"), 
    Card(12, "Hearts"), Card(13, "Hearts"),
    Card(1, "Diamonds"), Card(2, "Diamonds"), Card(3, "Diamonds"), Card(4, "Diamonds"), Card(5, "Diamonds"), 
    Card(6, "Diamonds"), Card(7, "Diamonds"), Card(8, "Diamonds"), Card(9, "Diamonds"), Card(10, "Diamonds"), Card(11, "Diamonds"), 
    Card(12, "Diamonds"), Card(13, "Diamonds")
]

userCards = Hand(True)

dealerCards = Hand()

preWin = False

displayHands()

print()

whatDo = deesStuff.getUserInput("Would you like to (h)it or (s)tay?")

while whatDo != "x":

    if whatDo == "h":
        userCards.addCard()
        displayHands()
    
    elif whatDo == "s":
        displayHands(True)
        while dealerCards.total()<18:
            dealerCards.addCard()
            displayHands(True)
        
        whatDo = "x"
    
    if userCards.total() == 21:
        print("You Win!")
        whatDo = "x"
        preWin = True

    elif userCards.total() > 21:
        print("Bust!")
        whatDo = "x"
        preWin = True

    if whatDo != "x":
        print()
        whatDo = deesStuff.getUserInput("Would you like to (h)it or (s)tay?")

if dealerCards.total() > 21 and preWin == False:
    print("Dealer Busts You Win!")

elif dealerCards == 21 and preWin == False:
    print("Dealer Wins")

elif 21 - dealerCards.total() < 21 - userCards.total() and preWin == False:
    print("Dealer Closer You Lose")

elif 21 - dealerCards.total() > 21 - userCards.total() and preWin == False:
    print("Closer to 21 You Win!")