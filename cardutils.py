cardMap = {1:"Ace", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Jack", 12:"Queen", 13:"King"}

class Hand:
    def __init__(self,cards:list,bet:int,split:bool):
        self.c = cards
        self.b = bet
        self.s = split
        self.has_ace = False
        self.value = getHandValue(cards)[0]

    def printPlayerHand(self): 
        """
        Print player's hand in human-readable format.
        """
        print("Player hand: ",end="  ")
        for card in self.c:
            print(cardMap[card], end ="  ")
        print(f"  ({getHandValue(self.c)[0]})")

    def dealCard(self,deck:list):
        """
        Deal a card to this hand.
        """
        self.c.append((deck.pop(0) % 13)+1)
        self.value = getHandValue(self.c)[0]
        if self.c.count(1):
            self.has_ace = True

def printPlayerHand(hand): # print player's hand cards
    print("Player hand: ",end="  ")
    for card in hand:
        print(cardMap[card], end ="  ")
    print("")

def printDealerHand(hand): # print dealer's hand cards
    print("Dealer hand: ",end="  ")
    for card in hand:
        print(cardMap[card], end ="  ")
    print(f"  ({getHandValue(hand)[0]})")

def convertNonAceCard(card): # card will be [2,13]
    if card > 10:
        return 10
    else:
        return card 

def getHandValue(hand): # returns numeric hand val and whether it is soft
    hardTotal = 0
    aceCount = 0
    for card in hand: # hand could be a set instead of list since order does not matter
        if card > 1: # NOT an ace
            hardTotal += convertNonAceCard(card)
        else:       # is an ace
            aceCount += 1
    if aceCount > 0: # could be soft 
        if (hardTotal + 10 + aceCount) > 21: return (hardTotal + aceCount), False
        else: return (hardTotal + 10 + aceCount), True 
    else:               # can't be soft 
        return hardTotal, False

def dealCard(deck):
    return (deck.pop(0) % 13)+1
