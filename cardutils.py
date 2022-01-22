cardMap = {1:"Ace", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Jack", 12:"Queen", 13:"King"}

class Hand:
    def __init__(self,cards:list,bet:int,split:bool):
        self.l = None
        self.r = None
        self.c = cards
        self.b = bet
        self.s = split
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

def getHandValue(hand): # easiest to determine value of cards in hand context because of aces
    hardTotal = 0
    aceCount = 0
    # if there is one ace it could be 11 or 1
    # if non-ace total is >=11, all aces are 1
    # run through hard hards first and keep a total, then run thru aces
    for card in hand: # hand should be a set instead of list since order does not matter
        if card > 1: # NOT an ace
            hardTotal += convertNonAceCard(card)
        else:       # is an ace
            aceCount += 1
    if hardTotal >= 11: # can't be soft 17
        return hardTotal + aceCount, False
    elif aceCount > 0: # could be soft 17
        if (hardTotal + 10 + aceCount) > 21: return (hardTotal + aceCount), False
        else: return (hardTotal + 10 + aceCount), (17==(hardTotal + 10 + aceCount)) 
    else:               # can't be soft 17
        return hardTotal, False

def dealCard(deck):
    return (deck.pop(0) % 13)+1
